import uvicorn
from fastapi import FastAPI

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
    

