from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI application
app = FastAPI(
    title="Personal Finance Chatbot API",
    description="Intelligent Guidance for Savings, Taxes, and Investments using IBM Watson AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Personal Finance Chatbot API",
        "description": "Intelligent Guidance for Savings, Taxes, and Investments",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

# Example API endpoint for testing
@app.get("/health")
async def health():
    return {"status": "ok"}

# Demo Budget Summary endpoint
@app.post("/api/v1/budget-summary")
async def budget_summary_endpoint(request: Request):
    data = await request.json()
    # Return a sample budget summary
    return JSONResponse({
        "success": True,
        "data": {
            "summary": (
                "Your budget is healthy! You are saving more than you spend each month, which puts you on a strong path toward your financial goals. "
                "Keep tracking your expenses and maintaining this positive habit. Consider increasing your savings or investing the surplus to accelerate your progress even further."
            )
        }
    })

# Demo NLU endpoint
@app.post("/api/v1/nlu")
async def nlu_endpoint(request: Request):
    data = await request.json()
    # Return a sample NLU analysis
    return JSONResponse({
        "success": True,
        "data": {
            "sentiment": {"document": {"label": "positive", "score": 0.85}},
            "keywords": ["savings", "budget", "investment"],
            "entities": ["student", "professional"]
        }
    })

# Demo Q&A endpoint
@app.post("/api/v1/generate")
async def generate_endpoint(request: Request):
    data = await request.json()
    # Return a sample answer
    return JSONResponse({
        "success": True,
        "data": {
            "response": (
                "To improve your financial health, start by tracking your monthly income and expenses to identify areas where you can cut unnecessary spending. "
                "Set clear savings goals and automate transfers to a dedicated savings account each month. Consider creating a realistic budget that prioritizes essentials, savings, and debt repayment before discretionary spending. "
                "If you have high-interest debt, focus on paying it down as quickly as possible. Explore investment options that match your risk tolerance and time horizon, such as index funds or retirement accounts. "
                "Regularly review your financial plan and adjust as your circumstances change. Remember, consistency and discipline are key to achieving long-term financial stability and growth."
            ),
            "nlu_analysis": {
                "sentiment": {"document": {"label": "positive", "score": 0.7}},
                "keywords": ["budget", "savings", "debt repayment", "investment", "financial plan"]
            }
        }
    })


# Demo Spending Insights endpoint (correct placement)
@app.post("/api/v1/spending-insights")
async def spending_insights_endpoint(request: Request):
    data = await request.json()
    # Return a sample spending insights analysis
    return JSONResponse({
        "success": True,
        "data": {
            "insights": [
                "Your spending is well balanced.",
                "Track your expenses regularly to identify patterns.",
                "Reduce discretionary expenses to reach your savings goals faster.",
                "Review your goals and adjust your budget as needed.",
                "Consider setting aside a fixed amount each month for investments or emergencies."
            ]
        }
    })

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("FASTAPI_HOST", "0.0.0.0")
    port = int(os.getenv("FASTAPI_PORT", 8000))
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
