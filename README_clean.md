# RFP Analyzer – Meta-Prompt Driven Compliance & Risk Intelligence

## Overview

RFP Analyzer is an AI-powered tool designed to automate the evaluation of Government RFPs by providing fast, accurate insights into eligibility, compliance, risk, and checklist requirements.

Built for use in fast-paced environments like hackathons or enterprise procurement, this system uses cutting-edge language model capabilities combined with a unique **meta-prompting strategy** to generate highly relevant, context-aware insights from long legal documents.

---

## Key Features

- **Meta-Prompting Architecture**: Instead of hardcoding static prompts for each section, the analyzer first interprets the content of each chunk and dynamically generates optimized prompts tailored to that context and the company profile. This greatly enhances the relevance and accuracy of AI responses.
- **LLM Agents for Each Task**: Dedicated agents for:
  - Compliance Analysis
  - Eligibility Verification
  - Risk Identification
  - Submission Checklist Extraction
- **Summarized Outputs Only**: End users are shown clean, per-category summaries (one block each for Compliance, Eligibility, Risk, Checklist). The internal chunking and multi-step RAG process is completely abstracted away from the user interface.
- **PDF File Support**: Accepts two files — the RFP document and the company profile — and performs side-by-side analysis.
- **Gemini 1.5 Pro Backend**: Utilizes the most advanced Gemini models available with support for 2M token context and multi-agent workflows.
- **Dark Mode UI**: Professional, minimal, and clean ReactJS frontend with custom CSS.

---

## Unique Technical Approach

### Meta-Prompting at its Core

Unlike typical LLM apps that reuse a generic prompt across inputs, RFP Analyzer **generates prompts dynamically** for each section of the RFP based on the content and the company’s profile. These meta-prompts are crafted using a separate prompt-engineering LLM agent.

This approach ensures that each agent (compliance, eligibility, risk, checklist) receives context-specific instructions optimized for every individual chunk of the document.

### Agentic Pipeline

The backend operates in the following order:

1. **PDF Parsing and Chunking**
2. **Meta-Prompt Generation** per chunk and agent
3. **Agent Execution** (with Gemini) for each category
4. **Final Summary Generation** per category using another LLM pass

---

## Tech Stack

### Backend

- **FastAPI** for RESTful endpoints
- **Gemini 1.5 Pro** via Google Generative AI API
- **FAISS** (optional for vector search)
- **PyMuPDF / PDFMiner** for document parsing
- **Multi-agent architecture** with prompt routing

### Frontend

- **ReactJS** with Vite
- Custom **Dark Mode CSS**
- Axios for file upload & API communication

---

## How to Run

### 1. Clone the Repo

```
git clone https://github.com/your-username/rfp-analyzer.git
cd rfp-analyzer
```

### 2. Setup Backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Setup Frontend

```
cd frontend
npm install
npm run dev
```

### 4. Access the App

Visit `http://localhost:5173` in your browser.

---

## Sample Use Case

Upload:

- An RFP PDF (e.g., "Hazelwood IT Audit RFP")
- A company profile PDF (e.g., "FirstStaff Inc.")

Get instant output like:

- Eligibility Verdict: Ineligible (missing audit experience)
- Compliance Issues: Missing W-9 and bank letter
- Risks: Scope creep, underqualified staff, missing certifications
- Checklist: Required forms and exact submission format

---


