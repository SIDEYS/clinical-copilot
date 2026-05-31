import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from weave_integration.tracer import init_weave
init_weave()

from orchestrator.pipeline import run_pipeline

app = FastAPI(title="ClinicalCopilot", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    text: str
    patient_id: str = "DEMO-001"


class AnalyzeResponse(BaseModel):
    trace_id: str
    soap_note: dict
    red_flags: list
    summary: str
    medications: list
    interactions: list
    timeline_events: list
    risk_flags: list
    weave_url: str


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    if not req.text or len(req.text.strip()) < 50:
        raise HTTPException(status_code=400, detail="Text too short. Paste a real clinical chart.")
    try:
        result = run_pipeline(req.text.strip(), req.patient_id)
        entity = os.environ.get("WANDB_ENTITY", "")
        project = os.environ.get("WANDB_PROJECT", "clinical-copilot")
        weave_url = f"https://wandb.ai/{entity}/{project}/weave" if entity else f"https://wandb.ai/{project}/weave"
        return AnalyzeResponse(
            trace_id=result["trace_id"],
            soap_note=result["soap_note"],
            red_flags=result["red_flags"],
            summary=result.get("summary", ""),
            medications=result["medications"],
            interactions=result["interactions"],
            timeline_events=result["timeline_events"],
            risk_flags=result["risk_flags"],
            weave_url=weave_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")


@app.get("/health")
def health():
    return {"status": "ok", "service": "ClinicalCopilot"}


@app.get("/")
def serve_ui():
    return FileResponse("ui/index.html")
