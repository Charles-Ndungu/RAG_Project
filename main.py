import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/test")
def index():
    return [
        {   
            "Name": "Charles",
            "Course": "Data Science"
        },
        {   
            "Name": "John",
            "Course": "Data Science"
        }
    ]

@app.get("/home", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request, "message": "By Charles"}
    )
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)


    

