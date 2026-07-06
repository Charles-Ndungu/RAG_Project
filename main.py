import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Make sure the path is correct
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"status": "healthy", "message": "RAG Project is running!"}

@app.get("/test")
def test_data():
    return [
        {"Name": "Charles", "Course": "Data Science"},
        {"Name": "Cheryl", "Course": "Data Engineering"}
    ]

@app.get("/home", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "message": "By Charles"}
    )

# For local development
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)