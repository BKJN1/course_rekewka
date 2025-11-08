from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "check"}


@app.post("/register")
def register(req, res):
    return {"write your name"}

# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# .\venv\Scripts\Activate.ps1
# python main.py
# uvicorn main:app --reload