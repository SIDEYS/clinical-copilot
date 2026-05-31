# ClinicalCopilot — Person 3 Task Sheet
## Role: Pipeline Lead + Demo Owner
### Most of the pipeline is already built. Your job: sample data, validation, demo, submission.

---

## ⚡ FIRST: Clone and set up

```bash
git clone https://github.com/SIDEYS/clinical-copilot
cd clinical-copilot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY and WANDB_API_KEY to .env
```

---

## What's Already Done For You

```
agents/synthesis.py         ✅ complete
orchestrator/pipeline.py    ✅ complete — full asyncio fan-out, NOT a stub
shared/llm.py               ✅ LiteLLM wrapper — all agents use this
```

The pipeline runs: `Ingestion → [Medication ‖ Timeline] → Risk → Synthesis`

**The key change from the original spec:** No agent imports `anthropic` directly.
All LLM calls go through `shared/llm.py`. The model is set by `LLM_MODEL` in `.env`.

---

## Your Files

```
tests/sample_chart.txt      ← Task 0  PUSH THIS FIRST — Person 1 is blocked without it
README.md                   ← Task 1  Fill in submission section + Weave URL
```

**Do NOT touch:** any `agents/*.py`, `api/`, `weave_integration/`, `shared/`

---

## Task 0 — Sample Data `tests/sample_chart.txt`
### Do this IMMEDIATELY. Person 1 needs it to test agents.

Create `tests/sample_chart.txt` with this content:

```
PATIENT: Jane Doe  |  DOB: 1958-03-14  |  MRN: 00291847
DATE: 2026-05-31  |  PROVIDER: Dr. A. Patel, MD

CHIEF COMPLAINT:
Shortness of breath and leg swelling x 4 days.

HISTORY OF PRESENT ILLNESS:
68F with PMH of CHF (EF 35%, dx 2021), T2DM, HTN, CKD stage 3.
Presents with progressive dyspnea on exertion, bilateral ankle edema,
and orthopnea x2 pillows. Denies chest pain. 6 lbs weight gain in 5 days.
No recent medication changes. Last BMP 3 weeks ago: K 5.2, Cr 1.8, Na 139.

MEDICATIONS:
1. Furosemide 40mg PO daily
2. Carvedilol 12.5mg PO BID
3. Lisinopril 10mg PO daily
4. Metformin 500mg PO BID (held today given contrast CT)
5. Spironolactone 25mg PO daily (started 2026-03-01)
6. Aspirin 81mg PO daily

VITALS:
BP 164/98, HR 102, RR 22, SpO2 91% on RA, Temp 37.1C, Wt 89kg

LABS (TODAY):
Na 137, K 6.1 (CRITICALLY HIGH), BUN 42, Cr 2.3 (elevated from baseline 1.8)
Hgb 9.8, WBC 8.2, Plt 210
BNP 1840 pg/mL (CRITICALLY HIGH — severe heart failure)

PAST MEDICAL HISTORY:
- Congestive heart failure (EF 35%) diagnosed January 2021
- Type 2 Diabetes Mellitus diagnosed 2015
- Hypertension diagnosed 2012
- CKD Stage 3 diagnosed 2023
- NSTEMI (heart attack) 2019, managed medically, no intervention

REVIEW OF SYSTEMS:
Positive: dyspnea, orthopnea, bilateral leg swelling, fatigue, decreased urine output
Negative: chest pain, syncope, fever, cough, hemoptysis

PHYSICAL EXAM:
General: Mild respiratory distress, speaking in short sentences
Cardiovascular: S3 gallop, JVD present, 2+ pitting edema bilateral LE to knees
Respiratory: Bilateral basilar crackles
Abdomen: Mild hepatomegaly

ASSESSMENT & PLAN:
1. Acute decompensated CHF exacerbation — admit for IV Lasix diuresis, strict I&Os, daily weights
2. Hyperkalemia K 6.1 — HOLD lisinopril and spironolactone immediately, cardiology notified, repeat BMP in 4 hours, cardiac monitoring
3. AKI on CKD — Cr 2.3 from baseline 1.8, likely cardiorenal. Hold metformin. Nephrology consult placed.
4. Poorly controlled HTN — uptitrate antihypertensives once K normalized
Cardiology consult placed. Repeat BMP in 4 hours. Echo pending.
```

Push immediately:
```bash
git add tests/sample_chart.txt
git commit -m "test: add realistic synthetic patient chart"
git push
```

**Message Person 1: "sample_chart.txt pushed — you can test agents now"**

---

## Task 1 — Validate the Full Pipeline

Once Person 1 confirms their agents are passing, run end-to-end:

```bash
python -c "
from orchestrator.pipeline import run_pipeline
import json
result = run_pipeline(open('tests/sample_chart.txt').read())
print(json.dumps(result, indent=2))
"
```

✅ Done when: you see a complete dict with `soap_note`, `red_flags`, `medications`, `timeline_events`, `risk_flags` all populated with real data (not stubs).

**Expected red flags in output:**
- K+ 6.1 — HIGH
- SpO2 91% — HIGH
- BNP 1840 — HIGH
- Lisinopril + Spironolactone interaction — HIGH

If any are missing, tell Person 1 to tune the risk agent prompt.

---

## Task 2 — Test the Full API + UI

```bash
# Terminal 1
source .venv/bin/activate
uvicorn api.main:app --reload --port 8000

# Terminal 2 — smoke test
curl -s -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$(cat tests/sample_chart.txt)\", \"patient_id\": \"DEMO-001\"}" | python3 -m json.tool
```

Then open `ui/index.html` in your browser, paste the sample chart, click Analyze, and confirm:
- Red flag badges appear (red = HIGH, amber = MEDIUM, green = LOW)
- SOAP note 4 sections are populated
- Medication table shows all 6 drugs
- Timeline shows 5+ events

---

## Task 3 — Fill in README Submission Section

Edit `README.md` — find the `[INSERT URL after setup]` and `[INSERT URL]` placeholders and replace with your actual W&B Weave URL once Person 2 shares it.

Also update the repo URL from `YOUR_ORG` to `SIDEYS`:
```
git clone https://github.com/SIDEYS/clinical-copilot
```

---

## Task 4 — Demo Prep (start at 3:30pm)

### Submission description (pre-written, paste into AGI House):

```
TEAM NAME: ClinicalCopilot

SUMMARY:
ClinicalCopilot is a multi-agent AI system that transforms unstructured medical charts
into structured SOAP notes with automated red flag detection. Five specialized agents —
ingestion, medication, timeline, risk, and synthesis — execute in a parallel asyncio
orchestration harness with full W&B Weave traceability for every agent decision.

WHAT IT DOES:
Physicians spend 2+ hours per day on clinical documentation. ClinicalCopilot accepts
raw patient notes and returns: a structured SOAP note, prioritized red flags
(hyperkalemia, low SpO2, elevated BNP), drug interaction alerts via OpenFDA, and a
reconstructed medical timeline. Every agent's reasoning is auditable via Weave.

HOW IT'S BUILT:
Orchestration: custom asyncio pipeline with parallel fan-out using a typed AgentMessage
contract. LLM layer: LiteLLM (provider-agnostic) — swap models via a single env var.
Default model: Claude Sonnet. Tracing: W&B Weave @weave.op on every agent.
External API: OpenFDA drug label API. Backend: FastAPI. No agent framework dependencies.

SPONSOR TOOLS USED:
W&B Weave — every agent call is wrapped with @weave.op, making inputs, outputs, latency,
and token usage visible in the Weave dashboard. The trace graph proves multi-agent
orchestration visually.
Weave Dashboard: [INSERT WANDB URL]
```

### Screen recording script (2 min, practice once):

| Time | Action |
|---|---|
| 0:00–0:15 | Open UI. Say: "ClinicalCopilot uses 5 parallel agents to summarize clinical charts and flag risks in real time." |
| 0:15–0:25 | Paste sample_chart.txt. Show the messy unstructured text. |
| 0:25–0:45 | Click Analyze. Switch to W&B Weave. Watch 5 agent spans appear. |
| 0:45–1:10 | Back to UI. Walk through RED FLAGS: "K+ 6.1 critical, SpO2 91%, BNP 1840." Show colors. |
| 1:10–1:30 | Show SOAP note sections. Show medication table + drug interaction alert. |
| 1:30–1:50 | Back to Weave. Zoom into synthesis agent — show it received inputs from 4 agents. |
| 1:50–2:00 | "Full audit trail in Weave. GitHub: https://github.com/SIDEYS/clinical-copilot" |

---

## Sync Checkpoints

| Time | What you do |
|---|---|
| +20 min | Push sample_chart.txt. Message Person 1. |
| +1h30 | Run full pipeline locally. Paste JSON output in team chat. |
| +2h30 | Full API + UI working. Share screenshots with team. |
| +3h10 | All 5 agents end-to-end. Fix anything broken with Person 1. |
| +3h30 | Start rehearsing demo. Time yourself — under 2 minutes. |
| +4h00 | Record demo. Max 2 takes. |
| +4h20 | Submit on AGI House platform. |

---

## Submission Checklist

- [ ] `tests/sample_chart.txt` pushed (minute 20)
- [ ] Full pipeline runs end-to-end locally
- [ ] API returns real SOAP note + red flags (not stubs)
- [ ] UI shows red flags, SOAP, meds, timeline
- [ ] Weave dashboard shows 5 agent traces — grab URL
- [ ] README updated with Weave URL and correct repo link
- [ ] Screen recording under 2 minutes
- [ ] AGI House form filled (team name, emails, GitHub, Weave URL, description)
- [ ] Draft submitted by 7:00 PM
- [ ] Final submitted by 8:00 PM

---

## If You Get Stuck

| Problem | Fix |
|---|---|
| Pipeline timeout | Reduce `max_tokens` to 800 in `shared/llm.py`, truncate input to 2000 chars |
| Weave decorator failing | Already wrapped in try/except — it degrades gracefully |
| Synthesis JSON malformed | Add stronger JSON-only instruction to `SYNTHESIS_PROMPT` in `agents/synthesis.py` |
| asyncio event loop error | Replace `asyncio.run()` in pipeline with a sequential sync version for the demo |
| Slow LLM | Change `LLM_MODEL=groq/llama-3.1-70b-versatile` in `.env` for faster responses |
