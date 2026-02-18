# LLM-Assisted Workflow I/O Bottleneck Diagnosis

## Overview
This project explores whether **large language models (LLMs)** can accurately diagnose **HPC workflow I/O bottlenecks** from structured execution data.

Goal: evaluate LLM reasoning quality, classification accuracy, and explanation quality using offline workflow traces (no live system integration).

---

## Core Research Questions
- Can LLMs correctly classify I/O bottleneck types?
- Do their explanations align with expert reasoning?
- How do different prompting strategies impact results?

---

## Bottleneck Categories
- Storage contention  
- Small-file overhead  
- Producer–consumer mismatch  
- Storage tier mismatch  
- Serialization bottleneck  

---

## Project Deliverables
- Bottleneck dataset (expert-labeled workflow snapshots)
- Prompt library (zero-shot, few-shot, CoT, structured)
- Evaluation framework (LLM vs ground truth)
- Accuracy analysis

Optional:
- Multi-model comparison
- Explanation scoring
- Failure analysis

---

## Methodology
1. **Dataset Curation**  
   Build 30–50 labeled workflow execution snapshots.

2. **Prompt Engineering**  
   Test and iterate on prompting strategies.

3. **Evaluation**  
   Measure accuracy, precision/recall, and explanation quality.

4. **Analysis**  
   Study strengths, weaknesses, and failure modes.

---
