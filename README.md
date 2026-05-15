# 🤖 Project 1 — AI Data Analyst API

A production-grade REST API that analyzes CSV data using AI powered by Groq!

## 📋 What It Does
- Load and analyze CSV datasets using Pandas
- Ask questions about your data in plain English
- Get AI powered intelligent answers using Groq LLM
- Validate all data inputs and outputs using Pydantic

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| FastAPI | REST API framework |
| Pandas | Data analysis |
| NumPy | Mathematical operations |
| Matplotlib | Data visualization |
| Pydantic | Data validation |
| Groq | AI language model |

## 📁 Project Structure
```
ai-data-analyst/
│
├── app/
│   ├── main.py          # API entry point
│   ├── models.py        # Pydantic models
│   ├── config.py        # Settings & environment variables
│   └── services/
│       ├── data.py      # Pandas data logic
│       └── llm_call.py  # Groq AI logic
│
├── Data/
│   └── students.csv
│
├── .env
├── .gitignore
└── requirements.txt
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-data-analyst.git
cd ai-data-analyst
```

### 2. Create virtual environment
```bash
python -m venv env
env\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
language_model=llama-3.3-70b-versatile
```

### 5. Run the API
```bash
uvicorn app.main:app --reload
```

### 6. Test the API
Visit → **http://127.0.0.1:8000/docs**

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/chat` | Ask questions about your data |

## 💡 Example Request
```json
{
    "question": "Who is the highest scoring student?"
}
```

## 📊 Example Response
```json
{
    "ai_response": {
        "name": "Ahmed",
        "score": 95,
        "grade": "A"
    }
}
```
