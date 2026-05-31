# Graph Report - .  (2026-05-31)

## Corpus Check
- 14 files · ~8,192 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 163 nodes · 195 edges · 19 communities (15 shown, 4 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 10 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Task Documentation|Task Documentation]]
- [[_COMMUNITY_Agent Implementations|Agent Implementations]]
- [[_COMMUNITY_FastAPI + Contract Layer|FastAPI + Contract Layer]]
- [[_COMMUNITY_README Architecture|README Architecture]]
- [[_COMMUNITY_Multi-Agent Pipeline Docs|Multi-Agent Pipeline Docs]]
- [[_COMMUNITY_Clinical Test Cases|Clinical Test Cases]]
- [[_COMMUNITY_LiteLLM Config|LiteLLM Config]]
- [[_COMMUNITY_Environment Setup|Environment Setup]]
- [[_COMMUNITY_Task Scaffolding|Task Scaffolding]]
- [[_COMMUNITY_Demo + Submission|Demo + Submission]]
- [[_COMMUNITY_Weave Tracing|Weave Tracing]]
- [[_COMMUNITY_Orchestrator Pipeline|Orchestrator Pipeline]]
- [[_COMMUNITY_Shared Models|Shared Models]]
- [[_COMMUNITY_Risk Deterministic Flags|Risk Deterministic Flags]]
- [[_COMMUNITY_Test Runner|Test Runner]]
- [[_COMMUNITY_Agents Module|Agents Module]]
- [[_COMMUNITY_Orchestrator Module|Orchestrator Module]]
- [[_COMMUNITY_Shared Module|Shared Module]]

## God Nodes (most connected - your core abstractions)
1. `ClinicalCopilot — Person 3 Task Sheet` - 21 edges
2. `run()` - 18 edges
3. `ClinicalCopilot 🏥` - 14 edges
4. `run_pipeline()` - 9 edges
5. `extract_medications()` - 7 edges
6. `chat()` - 6 edges
7. `code:bash (python -c ")` - 6 edges
8. `AgentMessage` - 6 edges
9. `_deterministic_flags()` - 6 edges
10. `trace_agent()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `AnalyzeResponse` --shares_data_with--> `renderResults() JS function`  [INFERRED]
  api/main.py → ui/index.html
- `Drug combo: Lisinopril + Spironolactone (ACE + K-sparing diuretic)` --conceptually_related_to--> `ACE inhibitor + potassium-sparing diuretic hyperkalemia rule`  [INFERRED]
  tests/sample_chart.txt → agents/medication.py
- `trace_agent()` --conceptually_related_to--> `IngestionAgent`  [INFERRED]
  weave_integration/tracer.py → README.md
- `serve_ui()` --references--> `analyze() JS function`  [INFERRED]
  api/main.py → ui/index.html
- `run_pipeline()` --calls--> `IngestionAgent`  [EXTRACTED]
  orchestrator/pipeline.py → README.md

## Hyperedges (group relationships)
- **All LLM-calling agents share the chat() interface via shared/llm.py** — agents_timeline_run, agents_medication_extract_medications, agents_risk_run, agents_synthesis_run, shared_llm_chat [EXTRACTED 1.00]
- **Pipeline execution order: ingestion -> [medication || timeline] -> risk -> synthesis** — agents_ingestion_run, agents_medication_run, agents_timeline_run, agents_risk_run, agents_synthesis_run [EXTRACTED 1.00]
- **Five test cases covering five different acute emergencies for full pipeline validation** — tests_sample_chart_jane_doe, tests_case_02_sepsis_john_smith, tests_case_03_stemi_robert_chen, tests_case_04_dka_maria_gonzalez, tests_case_05_stroke_dorothy_williams [EXTRACTED 1.00]

## Communities (19 total, 4 thin omitted)

### Community 0 - "Task Documentation"
Cohesion: 0.07
Nodes (29): code:bash (git add agents/), code:block4 (agents/ingestion.py     — no LLM, pure Python (already done ), code:python (from shared.models import AgentMessage), Push Your Prompt Tweaks, Role: ML Agent Engineer, Task 1 — Verify IngestionAgent, Task 2 — Verify + Tune MedicationAgent, Task 3 — Verify + Tune TimelineAgent (+21 more)

### Community 1 - "Agent Implementations"
Cohesion: 0.15
Nodes (18): ACE inhibitor + potassium-sparing diuretic hyperkalemia rule, check_interactions(), extract_medications(), _fallback_extract_medications() — regex-only medication parser, _fallback_extract_medications(), _med_key(), _merge_medications(), OpenFDA Drug Label API — drug interaction lookup (+10 more)

### Community 2 - "FastAPI + Contract Layer"
Cohesion: 0.11
Nodes (19): AgentMessage, analyze(), analyze endpoint (POST /analyze), AnalyzeRequest, AnalyzeResponse, serve_ui(), BaseModel, _async_pipeline() (+11 more)

### Community 3 - "README Architecture"
Cohesion: 0.1
Nodes (20): API, Architecture, ClinicalCopilot 🏥, code:block1 ([Raw Clinical Text]), code:bash (# Default), code:block3 (clinical-copilot/), code:python (# shared/models.py), code:json ({) (+12 more)

### Community 4 - "Multi-Agent Pipeline Docs"
Cohesion: 0.19
Nodes (14): IngestionAgent, MedicationAgent, RiskAgent, SynthesisAgent, TimelineAgent, Anthropic Claude API (claude-sonnet-4-20250514), ClinicalCopilot System, OpenFDA Drug Label API (+6 more)

### Community 5 - "Clinical Test Cases"
Cohesion: 0.22
Nodes (9): Clinical threshold constants (K>6.0 HIGH, BNP>1000 HIGH, SpO2<94, etc.), Diagnosis: DKA severe — pH 7.08, bicarb 8, glucose 512, Critical lab: Glucose 512 mg/dL, bicarb 8, anion gap 28, Patient: Maria Gonzalez — severe DKA (T1DM, missed insulin), Critical lab: BNP 1840 pg/mL (CRITICALLY HIGH), Diagnosis: Acute decompensated CHF (EF 35%), Critical lab: K 6.1 (CRITICALLY HIGH), Patient: Jane Doe — CHF decompensation with hyperkalemia (+1 more)

### Community 6 - "LiteLLM Config"
Cohesion: 0.33
Nodes (5): chat(), Default model: anthropic/claude-sonnet-4-20250514, LiteLLM — provider-agnostic LLM abstraction layer, LLM_MODEL env var — swap LLM provider without code changes, Central LLM config. All agents import `chat` from here. Swap models by setting L

### Community 7 - "Environment Setup"
Cohesion: 0.4
Nodes (5): ⚡ FIRST: Clone and set up, code:bash (git clone https://github.com/SIDEYS/clinical-copilot), code:block7 (ANTHROPIC_API_KEY=your_anthropic_key_here), .env.example, Environment Setup

### Community 8 - "Task Scaffolding"
Cohesion: 0.5
Nodes (4): code:block2 (agents/ingestion.py    ✅ complete), code:python (from shared.llm import chat  # this is all you need), code:block2 (agents/synthesis.py         ✅ complete), What's Already Done For You

### Community 9 - "Demo + Submission"
Cohesion: 0.5
Nodes (4): code:block9 (TEAM NAME: ClinicalCopilot), Screen recording script (2 min, practice once):, Submission description (pre-written, paste into AGI House):, Task 4 — Demo Prep (start at 3:30pm)

### Community 10 - "Weave Tracing"
Cohesion: 0.5
Nodes (4): Diagnosis: Septic shock — urosepsis source, Critical vital: BP 82/54 (septic hypotension), Patient: John Smith — septic shock from urosepsis, Critical lab: Lactate 4.2 mmol/L (septic shock marker)

### Community 11 - "Orchestrator Pipeline"
Cohesion: 0.5
Nodes (4): Diagnosis: Acute ischemic stroke — right MCA occlusion, NIHSS 14, Patient: Dorothy Williams — acute ischemic stroke (right MCA), Critical finding: INR 1.4 subtherapeutic (on warfarin for AFib), Treatment: IV tPA (alteplase) 0.9mg/kg + mechanical thrombectomy

### Community 12 - "Shared Models"
Cohesion: 0.67
Nodes (3): check(), End-to-end test runner for all patient cases. Usage: python tests/run_all.py, run_case()

### Community 13 - "Risk Deterministic Flags"
Cohesion: 0.67
Nodes (3): Diagnosis: Anterior wall STEMI — cath lab activation, Patient: Robert Chen — anterior STEMI, Critical lab: Troponin I 4.8 rising to 9.2 ng/mL

## Knowledge Gaps
- **62 isolated node(s):** `Decorator factory. Wraps an agent run() function with a Weave op.     Usage: med`, `Central LLM config. All agents import `chat` from here. Swap models by setting L`, `Most of the pipeline is already built. Your job: sample data, validation, demo, submission.`, `code:block2 (agents/synthesis.py         ✅ complete)`, `code:block3 (tests/sample_chart.txt      ← Task 0  PUSH THIS FIRST — Pers)` (+57 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run()` connect `Agent Implementations` to `FastAPI + Contract Layer`, `Shared Models`, `LiteLLM Config`?**
  _High betweenness centrality (0.544) - this node is a cross-community bridge._
- **Why does `ClinicalCopilot 🏥` connect `README Architecture` to `Agent Implementations`, `Environment Setup`?**
  _High betweenness centrality (0.477) - this node is a cross-community bridge._
- **Why does `ClinicalCopilot — Person 3 Task Sheet` connect `Task Documentation` to `Task Scaffolding`, `Demo + Submission`, `Environment Setup`?**
  _High betweenness centrality (0.315) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `run_pipeline()` (e.g. with `analyze()` and `AgentMessage`) actually correct?**
  _`run_pipeline()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Decorator factory. Wraps an agent run() function with a Weave op.     Usage: med`, `Central LLM config. All agents import `chat` from here. Swap models by setting L`, `Most of the pipeline is already built. Your job: sample data, validation, demo, submission.` to the rest of the system?**
  _62 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Task Documentation` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `FastAPI + Contract Layer` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._