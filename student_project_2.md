# LLM-Assisted Workflow I/O Bottleneck Diagnosis

## Student Project Presentation
**PhD Lead:** Meng Tang (mtang11@hawk.illinoistech.edu)  
**Duration:** 12 Weeks  
**Team Size:** 1 Student

---

## Introduction

Large language models have shown promise in interpreting system logs, debugging code, and reasoning about complex technical scenarios. However, **their ability to reason about HPC I/O performance remains unexplored**.

This project investigates a key question: **Can LLMs accurately diagnose I/O bottlenecks from structured workflow execution data?**

This is a **feasibility study** — no live system integration required. You will work entirely with pre-collected traces and LLM API calls to evaluate diagnostic capabilities.
```
┌─────────────────────────────────────────────────────────────────┐
│                     Project Concept                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Workflow Execution Data          LLM Diagnosis                │
│   ┌─────────────────────┐         ┌─────────────────────┐       │
│   │ - Task durations    │         │ Bottleneck: Storage │       │
│   │ - I/O volumes       │ ──────▶│ contention between  │       │
│   │ - Storage metrics   │   ???   │ Task A and Task B   │       │
│   │ - Data dependencies │         │                     │       │
│   └─────────────────────┘         └─────────────────────┘       │
│                                                                 │
│   Can LLMs reason about this accurately?                        │
│   Do their explanations match expert reasoning?                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Background

### The Diagnosis Problem
- Workflow I/O bottlenecks are difficult to identify from raw metrics
- Expert diagnosis requires understanding dataflow patterns, storage behavior, and system interactions
- Current tools provide data but limited interpretive guidance

### Common I/O Bottleneck Categories
- **Storage contention**: Multiple tasks competing for shared storage bandwidth
- **Small-file overhead**: Many small I/O operations creating metadata bottlenecks
- **Producer-consumer mismatch**: Data production rate doesn't match consumption rate
- **Storage tier mismatch**: Data placed on inappropriate storage tier for access pattern
- **Serialization bottleneck**: I/O serialized when it could be parallelized

### Why LLMs?
- LLMs excel at pattern recognition and natural language explanation
- They can potentially synthesize multiple metrics into coherent diagnosis
- If effective, could make I/O diagnosis more accessible to non-experts

---

## Problem Statement

**Core Question:** Can LLMs accurately diagnose I/O bottlenecks from structured workflow execution summaries, and do their explanations reflect sound reasoning?

### Research Questions

1. **Classification Accuracy**: How accurately can LLMs identify bottleneck categories from execution data?

2. **Explanation Quality**: Do LLM-generated explanations align with expert ground truth reasoning?

3. **Prompt Sensitivity**: How do different prompt strategies affect diagnostic accuracy?

**You are encouraged to propose additional research questions** as you explore the problem space.

---

## Project Goals

### Primary Goal
Evaluate LLM capabilities for **I/O bottleneck diagnosis** through systematic prompting experiments on a curated dataset.

### Deliverables

**Required:**
- **Bottleneck Dataset**: Curated set of workflow execution snapshots with expert-labeled bottleneck categories and reasoning
- **Prompt Library**: Collection of prompt templates for bottleneck diagnosis
- **Evaluation Framework**: Scripts to run LLM diagnosis and compare against ground truth
- **Accuracy Analysis**: Quantitative results on classification accuracy across bottleneck types

**Optional (Encouraged):**
- **Multi-Model Comparison**: Systematic comparison across different LLMs (Claude, GPT, Gemini)
- **Explanation Scoring**: Rubric-based evaluation of explanation quality beyond classification
- **Failure Analysis**: Deep dive into cases where LLMs fail and why
- **Your Own Extensions**: Propose and explore directions that interest you

---

## Methodology Overview

### Phase 1: Dataset Curation
- Define bottleneck categories and their diagnostic signatures
- Collect or synthesize workflow execution snapshots (task durations, I/O volumes, storage metrics, data dependencies)
- Label each snapshot with bottleneck category and expert reasoning
- **Baseline target**: 30-50 labeled examples; you may expand or refine based on findings

### Phase 2: Prompt Engineering
- Design and iterate on prompt templates for bottleneck diagnosis
- **Baseline approaches**: Zero-shot, few-shot, chain-of-thought prompting
- **Go beyond**: Explore additional strategies — structured output formats, role-based prompts, iterative refinement, or techniques you discover

### Phase 3: Evaluation
- Run dataset examples through LLM with different prompt strategies
- Compare LLM classification against ground truth labels
- **Baseline metrics**: Accuracy, per-category precision/recall
- **Go beyond**: Develop richer evaluation criteria — explanation quality rubrics, confidence calibration, failure mode taxonomy

### Phase 4: Analysis & Reporting
- Identify which bottleneck types LLMs diagnose well vs poorly
- Analyze what makes prompts effective or ineffective
- **Synthesize insights**: What does this tell us about LLM reasoning for systems diagnosis?

---

## Baseline Dataset Design

A starting point for execution snapshot structure:
```
Workflow Execution Snapshot Example:
─────────────────────────────────────
Workflow: Genomics Pipeline
Total Duration: 847 seconds

Task Summary:
┌────────────┬──────────┬───────────┬───────────┬─────────────┐
│ Task       │ Duration │ Read (GB) │ Write(GB) │ Concurrent  │
├────────────┼──────────┼───────────┼───────────┼─────────────┤
│ preprocess │ 45s      │ 12.3      │ 8.7       │ -           │
│ align_1    │ 312s     │ 8.7       │ 15.2      │ align_2,3,4 │
│ align_2    │ 298s     │ 8.7       │ 14.8      │ align_1,3,4 │
│ merge      │ 89s      │ 60.0      │ 22.4      │ -           │
└────────────┴──────────┴───────────┴───────────┴─────────────┘

Storage Metrics:
- Shared filesystem utilization during align_*: 94%
- Average I/O throughput: 45 MB/s (capacity: 200 MB/s)

Ground Truth Label: Storage Contention
Expert Reasoning: Four align tasks running concurrently all 
reading from and writing to shared storage, saturating bandwidth.
```

**This is a starting point** — you should refine the snapshot format based on what information LLMs need to make accurate diagnoses. Consider: What's missing? What's redundant? What representation works best?

---

## Baseline Prompt Strategies

Starting approaches to explore:

- **Zero-shot**: Direct question with execution data
- **Few-shot**: Include 2-3 labeled examples before the query
- **Chain-of-thought**: Ask LLM to reason step-by-step before concluding
- **Structured output**: Request specific format (category + evidence + explanation)

**Go beyond these baselines.** As you experiment, you may discover:
- Domain-specific prompting techniques that work better
- Ways to decompose the diagnosis task
- Effective use of LLM capabilities (e.g., asking clarifying questions, multi-turn diagnosis)
- Prompt patterns from other domains that transfer well

Document what works, what doesn't, and why.

---

## Directions for Exploration

This project has significant room for you to shape its direction. Some possibilities:

**Dataset extensions:**
- Increase complexity with multi-bottleneck scenarios
- Add ambiguous cases to test LLM uncertainty handling
- Include real traces from published workflow studies

**Evaluation depth:**
- Develop explanation quality rubrics
- Analyze LLM confidence vs actual accuracy
- Characterize failure modes systematically

**Prompt innovations:**
- Explore retrieval-augmented approaches (provide relevant documentation)
- Test iterative diagnosis (LLM asks for more data)
- Compare different output formats and their effect on accuracy

**Broader questions:**
- How does diagnosis accuracy vary with bottleneck subtlety?
- Can LLMs suggest remediation, not just diagnosis?
- What's the minimal information needed for accurate diagnosis?

**Propose your own directions** — this is a research project, not just an implementation exercise.

---

## Weekly Update Requirement

### Mandatory Weekly Presentation

**Each week, you will present at least 1 slide** during our group meeting covering:

- **What I Learned**: New concepts, tools, or techniques acquired
- **What I Did**: Concrete tasks completed this week
- **What I Found**: Interesting observations, preliminary results
- **Difficulties Encountered**: Blockers, challenges, questions needing help
- **Next Steps**: Plan for the coming week

### GitHub Repository Requirement

**All project work must be documented in a dedicated GitHub repository.**

Suggested structure (adapt as needed):
```
llm-io-diagnosis/
├── README.md                 # Project overview and setup
├── docs/                     # Design decisions and findings
├── weekly-updates/           # Weekly progress notes
├── dataset/                  # Execution snapshots and labels
├── prompts/                  # Prompt templates
├── src/                      # Evaluation code
├── results/                  # Outputs and analysis
└── presentations/
```

**Documentation expectations:**
- Commit regularly (not just at the end)
- Write clear commit messages
- Document your reasoning, not just your code

---

## Expectations

### What You Will Learn
- LLM API usage and prompt engineering techniques
- Dataset curation and labeling methodology
- Evaluation design for AI systems
- I/O performance concepts and bottleneck patterns

### What We Expect From You
- **Communication**: Weekly updates, early flag of blockers
- **Documentation**: All work tracked in GitHub with clear notes
- **Initiative**: Go beyond the baseline — propose and explore your own ideas
- **Critical thinking**: Don't just run experiments; interpret and synthesize findings

**Scope is flexible** — baselines ensure you have concrete deliverables, but the most interesting work often comes from your own explorations.

---

## Getting Started

### First Steps (Before Next Meeting)

1. **Environment Setup**
   - Set up Python environment
   - Obtain API access to at least one LLM (Claude, OpenAI, or use Cursor/Claude.ai for initial experiments)

2. **Create GitHub Repository**
   - Initialize repo and share link with me

3. **Background Reading**
   - Review common workflow I/O bottleneck patterns
   - Explore prompt engineering best practices

4. **Initial Exploration**
   - Draft 2-3 example execution snapshots
   - Try a simple prompt asking an LLM to diagnose one example
   - Observe: What works? What's confusing to the LLM? What ideas does this spark?

### First Week Checklist
- [ ] Environment and LLM API access ready
- [ ] GitHub repo created and shared
- [ ] Background reading started
- [ ] Initial LLM diagnosis experiment attempted
- [ ] First weekly update slide prepared

---

## Questions?

**Contact:** Meng Tang — mtang11@hawk.illinoistech.edu

**Next Steps:**
1. Complete first-week checklist
2. Schedule regular meeting time
3. Begin dataset design and initial experiments

---

*Welcome to the project!*