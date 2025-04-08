from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all route modules
from routes.analyze import router as analyze_router
from routes.tagged_analyze import router as tagged_router
from routes.prompt_gen import router as prompt_gen_router  # ✅ New Route

app = FastAPI(title="AI RFP Analyzer")

# CORS setup — allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # during dev. Replace with frontend origin in prod.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register endpoints
app.include_router(analyze_router, prefix="/analyze")
app.include_router(tagged_router, prefix="/tagged-analyze")
app.include_router(prompt_gen_router, prefix="/generate-prompts")  # ✅ New Prompt Generator

@app.get("/")
def read_root():
    return {"message": "RFP Analyzer Backend is running 🚀"}
