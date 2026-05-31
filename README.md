# ClinicalCopilot 🏥

> Multi-agent AI system that transforms unstructured medical charts into structured SOAP notes with automated red flag detection.
> Built at AGI House × W&B Multi-Agent Orchestration Build Day — May 31, 2026

---

## What It Does

Paste a raw, messy clinical chart → ClinicalCopilot runs **5 specialized AI agents in parallel** and returns:

- ✅ A structured **SOAP note** (Subjective / Objective / Assessment / Plan)
- 🚨 Prioritized **red flags** (critical vitals, dangerous lab values, acute diagnoses)
- 💊 **Medication list** with drug interaction alerts via OpenFDA
- 📅 **Chronological medical timeline** reconstructed from notes
- 🔍 Full **W&B Weave audit trail** of every agent decision

---

## Architecture

```
[Raw Clinical Text]
        │
        ▼
  IngestionAgent          ← cleans + chunks input (no LLM)
        │
        ├──────────────────────────────┐
        ▼                              ▼
  MedicationAgent              TimelineAgent
  (Claude + OpenFDA)           (Claude)
        │
        ▼
    RiskAgent                  ← needs medication output
  (Claude, clinical thresholds)
        │
        ▼ (all 4 results collected)
  SynthesisAgent               ← merges everything into SOAP note
  (Claude)
        │
        ▼
  [FastAPI /analyze endpoint]
        │
        ▼
  [UI: index.html]   +   [W&B Weave Dashboard]
```

**Medication + Timeline run in parallel (asyncio). Risk waits for Medication. Synthesis waits for all 4.**

---

## Repo Structure

```
clinical-copilot/
├── shared/
│   ├── __init__.py
│   └── models.py              ← AgentMessage contract — DO NOT CHANGE without team agreement
├── agents/
│   ├── __init__.py
│   ├── ingestion.py           ← Person 1
│   ├── medication.py          ← Person 1
│   ├── timeline.py            ← Person 1
│   ├── risk.py                ← Person 1
│   └── synthesis.py           ← Person 3
├── orchestrator/
│   ├── __init__.py
│   └── pipeline.py            ← Person 3
├── api/
│   ├── __init__.py
│   └── main.py                ← Person 2
├── ui/
│   └── index.html             ← Person 2
├── weave_integration/
│   ├── __init__.py
│   └── tracer.py              ← Person 2
├── tests/
│   └── sample_chart.txt       ← Person 3 (realistic synthetic patient note)
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Shared Message Contract

**Every agent input and output uses this exact TypedDict. Do not deviate.**

```python
# shared/models.py
from typing import TypedDict

class AgentMessage(TypedDict):
    agent: str        # "ingestion" | "medication" | "timeline" | "risk" | "synthesis"
    status: str       # "ok" | "error"
    payload: dict     # agent-specific (see schemas below)
    trace_id: str     # UUID4 — same value for entire pipeline run
    timestamp: str    # ISO 8601 UTC
```

### Payload Schemas

| Agent | Payload Keys |
|---|---|
| ingestion | `chunks: List[str]`, `raw_text: str`, `patient_id: str` |
| medication | `medications: List[{name, dose, frequency}]`, `interactions: List[{drug, warnings}]` |
| timeline | `events: List[{date, event, category}]` |
| risk | `flags: List[{flag, severity: HIGH\|MEDIUM\|LOW, evidence}]` |
| synthesis | `soap_note: {subjective, objective, assessment, plan}`, `summary: str`, `red_flags: List[str]` |

---

## API

| Method | Endpoint | Description |
|---|---|---|
| POST | `/analyze` | Main pipeline. Body: `{text: str, patient_id: str}` |
| GET | `/health` | Health check |

### Response shape

```json
{
  "trace_id": "uuid",
  "soap_note": { "subjective": "", "objective": "", "assessment": "", "plan": "" },
  "red_flags": ["K+ 6.1 CRITICAL", "SpO2 91% on RA"],
  "summary": "One-sentence executive summary",
  "medications": [{ "name": "", "dose": "", "frequency": "" }],
  "interactions": [{ "drug": "", "warnings": "" }],
  "timeline_events": [{ "date": "", "event": "", "category": "" }],
  "risk_flags": [{ "flag": "", "severity": "HIGH", "evidence": "" }],
  "weave_url": "https://wandb.ai/..."
}
```

---

## External APIs Used

| API | Purpose | Auth |
|---|---|---|
| Anthropic Claude API (`claude-sonnet-4-20250514`) | All 4 LLM agents | `ANTHROPIC_API_KEY` |
| OpenFDA Drug Label API | Drug interaction detection | None (free, no key) |
| W&B Weave | Agent call tracing + audit trail | `WANDB_API_KEY` |

OpenFDA endpoint: `https://api.fda.gov/drug/label.json?search=openfda.generic_name:{drug}&limit=1`

---

## Environment Setup

```bash
git clone https://github.com/YOUR_ORG/clinical-copilot
cd clinical-copilot
pip install -r requirements.txt
cp .env.example .env
# Fill in ANTHROPIC_API_KEY and WANDB_API_KEY in .env
uvicorn api.main:app --reload --port 8000
# Open ui/index.html in browser
```

### .env.example

```
ANTHROPIC_API_KEY=your_anthropic_key_here
WANDB_API_KEY=your_wandb_key_here
WANDB_PROJECT=clinical-copilot
WANDB_ENTITY=your_wandb_username
```

---

## Running the Pipeline Directly

```bash
# Quick test without the API
python -c "
from orchestrator.pipeline import run_pipeline
result = run_pipeline(open('tests/sample_chart.txt').read())
import json; print(json.dumps(result, indent=2))
"
```

---

## W&B Weave

Every agent call is wrapped with a `@weave.op` decorator. The Weave dashboard shows:
- Input/output for each of the 5 agents
- Latency per agent
- Token usage per Claude call
- Full trace graph showing the parallel fan-out

**Weave Dashboard:** [INSERT URL after setup]

---

## Hackathon Submission

- **Event:** AGI House × W&B Multi-Agent Orchestration Build Day
- **Submission URL:** app.agihouse.org/events/multi-agent-orchestration-build-day
- **Draft due:** 7:00 PM
- **Final due:** 8:00 PM
- **Demo:** 3-minute live presentation + Q&A

### Judging Criteria Coverage

| Criterion | How We Satisfy It |
|---|---|
| Agent Orchestration | 5 agents, parallel asyncio fan-out, typed message contract |
| Utility | Real clinical pain point — 2+ hrs/day saved on documentation |
| Technical Execution | FastAPI, typed contracts, OpenFDA, error handling |
| Creativity | Parallel specialist agents + full auditability for clinical AI |
| Sponsor Tool Usage | W&B Weave traces every agent call — also targeting Best Use of Weave ($1k) |

---

## Team

| Role | Responsibility |
|---|---|
| Person 1 — ML Engineer | IngestionAgent, MedicationAgent, TimelineAgent, RiskAgent |
| Person 2 — Infra Engineer | shared/models.py, FastAPI, Weave integration, UI |
| Person 3 — Pipeline Lead | SynthesisAgent, Orchestrator, sample data, demo + submission |

---

## Timeline

| Time | Milestone |
|---|---|
| 0:00–0:20 | Person 2 creates repo + shared/models.py + pushes. Unblocks everyone. |
| 0:20–1:30 | All 3 build in parallel |
| 1:30–1:45 | Integration checkpoint 1 — wire ingestion → medication |
| 1:45–3:00 | Full pipeline working end-to-end |
| 3:00–3:30 | Weave integration + UI polish |
| 3:30–4:00 | Demo prep + rehearsal |
| 4:00–4:20 | Record 2-min screen demo |
| 4:20–4:30 | Submit on AGI House platform |
