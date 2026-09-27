# 📊 GenAI-Adoption-Ops: Enterprise Program Analytics & Custom Skill Toolkit

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![UI](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Discipline](https://img.shields.io/badge/Discipline-GenAI_Adoption_%26_Evals-blue)

> An open-source framework for measuring enterprise GenAI program success through **A/B cohort experimentation**, **developer adoption funnels**, and **custom AI workflow skills** for game and interactive media engines.

---

## 📌 The Problem: Measuring GenAI Impact Beyond "Hype"

Organizations deploying AI tools across engineering and creative studios face three major governance challenges:
1. **Unmeasured ROI:** Teams lack quantitative data comparing AI-assisted delivery against traditional baselines.
2. **Workflow Disconnect:** Generic chatbot tools fail to address domain-specific engine budgets (VRAM, draw calls, polygon limits).
3. **Change Saturation:** Rolling out tools without structured adoption funnels leads to low long-term active creator retention.

---

## 💡 The Solution: Quantitative Adoption & Custom Skills

**GenAI-Adoption-Ops** provides the operational toolkit to measure, govern, and accelerate AI adoption:

```mermaid
flowchart TD
    A[Studio Feature Request] --> B[Custom AI Skill: Game Asset Governor]
    B --> C{Engine Budget Check}
    C -->|Pass| D[Approved Engine Contract]
    C -->|Fail| E[Automated Remediation Advisory]
    
    subgraph Program Analytics Engine
        D & E --> F[Cohort Telemetry Ingestion]
        F --> G[A/B Cohort Performance Matrix]
        F --> H[Studio Adoption Funnel]
        F --> I[Quarterly Net ROI Model]
    end
