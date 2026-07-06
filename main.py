from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from RAG Project!"}

@app.get("/test")
async def test():
    return {"message": "Test endpoint working!"}

# Vercel expects 'app' to be the FastAPI instance
# If you have if __name__ == "__main__", keep it but Vercel ignores it
    

