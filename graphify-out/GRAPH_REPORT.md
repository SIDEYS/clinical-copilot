# Graph Report - clinicalcopilot  (2026-05-31)

## Corpus Check
- 34 files · ~11,613 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 214 nodes · 263 edges · 21 communities (18 shown, 3 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9d1d6850`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

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
- [[_COMMUNITY_Shared Module|Shared Module]]

## God Nodes (most connected - your core abstractions)
1. `ClinicalCopilot — Person 3 Task Sheet` - 21 edges
2. `run()` - 18 edges
3. `ClinicalCopilot 🏥` - 14 edges
4. `run_pipeline()` - 8 edges
5. `extract_medications()` - 7 edges
6. `chat()` - 6 edges
7. `code:bash (python -c ")` - 6 edges
8. `AgentMessage` - 6 edges
9. `_deterministic_flags()` - 6 edges
10. `analyze()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Drug combo: Lisinopril + Spironolactone (ACE + K-sparing diuretic)` --conceptually_related_to--> `ACE inhibitor + potassium-sparing diuretic hyperkalemia rule`  [INFERRED]
  tests/sample_chart.txt → agents/medication.py
- `trace_agent()` --conceptually_related_to--> `IngestionAgent`  [INFERRED]
  weave_integration/tracer.py → README.md
- `run_pipeline()` --calls--> `IngestionAgent`  [EXTRACTED]
  orchestrator/pipeline.py → README.md
- `Parallel asyncio Agent Fan-out Pattern` --rationale_for--> `run_pipeline()`  [EXTRACTED]
  README.md → orchestrator/pipeline.py
- `ClinicalCopilot — multi-agent clinical chart analysis system` --references--> `_async_pipeline()`  [EXTRACTED]
  README.md → orchestrator/pipeline.py

## Hyperedges (group relationships)
- **All LLM-calling agents share the chat() interface via shared/llm.py** — agents_timeline_run, agents_medication_extract_medications, agents_risk_run, agents_synthesis_run, shared_llm_chat [EXTRACTED 1.00]
- **Pipeline execution order: ingestion -> [medication || timeline] -> risk -> synthesis** — agents_ingestion_run, agents_medication_run, agents_timeline_run, agents_risk_run, agents_synthesis_run [EXTRACTED 1.00]
- **Five test cases covering five different acute emergencies for full pipeline validation** — tests_sample_chart_jane_doe, tests_case_02_sepsis_john_smith, tests_case_03_stemi_robert_chen, tests_case_04_dka_maria_gonzalez, tests_case_05_stroke_dorothy_williams [EXTRACTED 1.00]

## Communities (21 total, 3 thin omitted)

### Community 0 - "Task Documentation"
Cohesion: 0.06
Nodes (34): code:bash (git add agents/), code:block2 (agents/ingestion.py    ✅ complete), code:python (from shared.llm import chat  # this is all you need), code:block4 (agents/ingestion.py     — no LLM, pure Python (already done ), code:python (from shared.models import AgentMessage), Push Your Prompt Tweaks, Role: ML Agent Engineer, Task 1 — Verify IngestionAgent (+26 more)

### Community 1 - "Agent Implementations"
Cohesion: 0.13
Nodes (18): ACE inhibitor + potassium-sparing diuretic hyperkalemia rule, check_interactions(), extract_medications(), _fallback_extract_medications() — regex-only medication parser, _fallback_extract_medications(), _med_key(), _merge_medications(), OpenFDA Drug Label API — drug interaction lookup (+10 more)

### Community 2 - "FastAPI + Contract Layer"
Cohesion: 0.17
Nodes (11): AgentMessage, _async_pipeline(), Parallel asyncio fan-out: medication and timeline run concurrently, Temporary stub for testing the API.     Person 3 replaces this entire file with, run_pipeline(), Pipeline Stub Design, AgentMessage TypedDict — shared message contract across all agents, AgentMessage Shared Contract (+3 more)

### Community 3 - "README Architecture"
Cohesion: 0.08
Nodes (24): ⚡ FIRST: Clone and set up, API, Architecture, ClinicalCopilot 🏥, code:block1 ([Raw Clinical Text]), code:bash (# Default), code:block3 (clinical-copilot/), code:python (# shared/models.py) (+16 more)

### Community 4 - "Multi-Agent Pipeline Docs"
Cohesion: 0.19
Nodes (14): IngestionAgent, MedicationAgent, RiskAgent, SynthesisAgent, TimelineAgent, Anthropic Claude API (claude-sonnet-4-20250514), ClinicalCopilot System, OpenFDA Drug Label API (+6 more)

### Community 5 - "Clinical Test Cases"
Cohesion: 0.16
Nodes (14): _add_flag(), Clinical threshold constants (K>6.0 HIGH, BNP>1000 HIGH, SpO2<94, etc.), _deterministic_flags(), _max_number_after(), _merge_flags(), _numbers_after(), Diagnosis: DKA severe — pH 7.08, bicarb 8, glucose 512, Critical lab: Glucose 512 mg/dL, bicarb 8, anion gap 28 (+6 more)

### Community 6 - "LiteLLM Config"
Cohesion: 0.09
Nodes (19): ACCEPTED_TYPES, FileUploadProps, UploadState, FlagBadgeProps, SEVERITY_DOT, SEVERITY_STYLES, ReportPanelProps, ResultsDashboardProps (+11 more)

### Community 7 - "Environment Setup"
Cohesion: 0.19
Nodes (11): analyze(), AnalyzeRequest, AnalyzeResponse, normalize(), NormalizeRequest, NormalizeResponse, Run InputAgent to normalize raw text into structured clinical chart format., BaseModel (+3 more)

### Community 8 - "Task Scaffolding"
Cohesion: 0.29
Nodes (9): Extract text from an uploaded PDF, DOCX, MD, or TXT file., upload_file(), _extract_docx(), _extract_pdf(), _extract_pdf_fallback(), extract_text(), File text extraction. Pure Python, no LLM. Uses pdfplumber for PDFs — extracts t, Uses pdfplumber for spatial-aware extraction — captures text that sits     besid (+1 more)

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
- **79 isolated node(s):** `InputAgent: normalizes raw, messy clinical text into structured chart format. Th`, `Extract text from an uploaded PDF, DOCX, MD, or TXT file.`, `Run InputAgent to normalize raw text into structured clinical chart format.`, `File text extraction. Pure Python, no LLM. Uses pdfplumber for PDFs — extracts t`, `Uses pdfplumber for spatial-aware extraction — captures text that sits     besid` (+74 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run()` connect `Agent Implementations` to `FastAPI + Contract Layer`, `Shared Models`, `Clinical Test Cases`?**
  _High betweenness centrality (0.385) - this node is a cross-community bridge._
- **Why does `ClinicalCopilot 🏥` connect `README Architecture` to `Task Documentation`, `Agent Implementations`?**
  _High betweenness centrality (0.318) - this node is a cross-community bridge._
- **Why does `ClinicalCopilot — Person 3 Task Sheet` connect `Task Documentation` to `Demo + Submission`, `README Architecture`?**
  _High betweenness centrality (0.203) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `run_pipeline()` (e.g. with `analyze()` and `AgentMessage`) actually correct?**
  _`run_pipeline()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `InputAgent: normalizes raw, messy clinical text into structured chart format. Th`, `Extract text from an uploaded PDF, DOCX, MD, or TXT file.`, `Run InputAgent to normalize raw text into structured clinical chart format.` to the rest of the system?**
  _79 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Task Documentation` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Agent Implementations` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._