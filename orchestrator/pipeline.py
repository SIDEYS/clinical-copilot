# STUB — Person 3 will replace this with the real asyncio pipeline
# This stub lets Person 2's API run independently for testing

import uuid
from datetime import datetime


def run_pipeline(raw_text: str, patient_id: str = "ANON") -> dict:
    """
    Temporary stub for testing the API.
    Person 3 replaces this entire file with the real multi-agent pipeline.
    """
    trace_id = str(uuid.uuid4())

    results = {
        "trace_id": trace_id,
        "soap_note": {
            "subjective": "Patient presents with clinical symptoms described in chart.",
            "objective": "Vitals and labs as documented.",
            "assessment": "1. Primary diagnosis pending agent analysis.",
            "plan": "1. Pending full agent pipeline integration."
        },
        "red_flags": ["[STUB] Real flags will appear when Person 1 agents are integrated"],
        "summary": "[STUB] Real synthesis pending pipeline integration.",
        "medications": [],
        "interactions": [],
        "timeline_events": [],
        "risk_flags": []
    }

    try:
        from agents import ingestion
        ing = ingestion.run(raw_text, patient_id)
        ing["trace_id"] = trace_id
        results["trace_id"] = trace_id
        print(f"[pipeline stub] Ingestion succeeded: {len(ing['payload']['chunks'])} chunks")
    except ImportError:
        print("[pipeline stub] agents/ingestion.py not yet available")
    except Exception as e:
        print(f"[pipeline stub] Ingestion error: {e}")

    return results
