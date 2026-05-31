# ClinicalCopilot — Person 1 Task Sheet
## Role: ML Agent Engineer
### Your 4 agent files are already scaffolded. Your job is to tune the prompts and validate the output.

---

## ⚡ FIRST: Clone and set up

```bash
git clone https://github.com/SIDEYS/clinical-copilot
cd clinical-copilot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
# LLM_MODEL is already set to anthropic/claude-sonnet-4-20250514 by default
```

---

## What's Already Done For You

All 4 of your agent files exist in the repo with working implementations:

```
agents/ingestion.py    ✅ complete
agents/medication.py   ✅ complete
agents/timeline.py     ✅ complete
agents/risk.py         ✅ complete
```

**The key change from the original spec:** agents no longer import `anthropic` directly.
They call `shared/llm.py` instead:

```python
from shared.llm import chat  # this is all you need

result = chat("your prompt here", max_tokens=1000)
# returns a plain string — strip JSON from it and parse
```

To switch LLM providers, change `LLM_MODEL` in `.env`. No agent code changes needed.

---

## Your Files

```
agents/ingestion.py     — no LLM, pure Python (already done — just verify it works)
agents/medication.py    — Claude + OpenFDA API (tune prompt if needed)
agents/timeline.py      — LLM only (tune prompt if needed)
agents/risk.py          — LLM with medical thresholds (MOST IMPORTANT — tune hard)
```

**Do NOT touch:** `orchestrator/`, `api/`, `ui/`, `weave_integration/`, `shared/models.py`, `shared/llm.py`

---

## The One Rule

Every agent `run()` must return an `AgentMessage`. It already does. Don't break the signature.

```python
from shared.models import AgentMessage

def run(...) -> AgentMessage:
    return AgentMessage(
        agent="YOUR_AGENT_NAME",
        status="ok",       # never raise — catch and return status="error"
        payload={...},
        trace_id=trace_id,
        timestamp=datetime.utcnow().isoformat()
    )
```

---

## Task 1 — Verify IngestionAgent

No changes needed. Just confirm it works on the sample chart.

```bash
python -c "
from agents.ingestion import run
import json
r = run(open('tests/sample_chart.txt').read())
print(json.dumps(r['payload']['chunks'], indent=2))
"
```

✅ Done when: you see 6–10 clean section chunks.

---

## Task 2 — Verify + Tune MedicationAgent

```bash
python -c "
from agents.ingestion import run as ing
from agents.medication import run as med
import json
i = ing(open('tests/sample_chart.txt').read())
m = med(i, 'test-001')
print(json.dumps(m['payload'], indent=2))
"
```

✅ Done when: medications list includes furosemide, carvedilol, lisinopril, spironolactone, metformin, aspirin — and at least one interaction warning.

**If the LLM returns malformed JSON**, edit the prompt in `agents/medication.py`:
- Add `Return ONLY raw JSON. No prose. No markdown.` at the top
- Truncate input: change `text[:3000]` to `text[:2000]`

---

## Task 3 — Verify + Tune TimelineAgent

```bash
python -c "
from agents.ingestion import run as ing
from agents.timeline import run as tl
import json
i = ing(open('tests/sample_chart.txt').read())
t = tl(i, 'test-001')
print(json.dumps(t['payload']['events'], indent=2))
"
```

✅ Done when: events include CHF 2021, T2DM 2015, HTN 2012, NSTEMI 2019, CKD 2023 — sorted oldest first.

---

## Task 4 — Verify + Tune RiskAgent (MOST IMPORTANT)

```bash
python -c "
from agents.ingestion import run as ing
from agents.medication import run as med
from agents.risk import run as risk
import json
i = ing(open('tests/sample_chart.txt').read())
m = med(i, 'test-001')
r = risk(i, m, 'test-001')
print(json.dumps(r['payload']['flags'], indent=2))
"
```

✅ Done when: you see HIGH severity flags for:
- K+ 6.1 (hyperkalemia)
- SpO2 91% on RA
- BNP 1840 (critically elevated)
- Lisinopril + spironolactone combo (hyperkalemia risk)
- HR 102 (tachycardia)

**If flags are missing**, strengthen the PROMPT in `agents/risk.py` — be more explicit about each threshold. The demo lives or dies on this output.

---

## Sync Checkpoints

| Time | What you do |
|---|---|
| +20 min | Pull repo. Confirm all 4 agent files exist. Run ingestion test. |
| +45 min | All 4 agents passing locally. Push any prompt tweaks. |
| +1h30 | **Integration checkpoint** — Person 3 runs full pipeline. Be on Slack. |
| +3h10 | Full end-to-end test with Person 3. Fix anything broken. |
| +4h00 | Join Person 3 for screen recording. |

---

## Push Your Prompt Tweaks

```bash
git add agents/
git commit -m "feat: tune [agent_name] prompt for better output"
git push
```

---

## If You Get Stuck

| Problem | Fix |
|---|---|
| JSON parse error | Add `.replace("```json","").replace("```","").strip()` before `json.loads()` |
| OpenFDA 404 | Already handled — it skips gracefully |
| Agent slow (>10s) | Truncate input to `text[:2000]` |
| Any exception | Catch it, return `status="error"` with error in payload, never raise |
| Wrong model | Change `LLM_MODEL` in `.env` — try `groq/llama-3.1-70b-versatile` for speed |
