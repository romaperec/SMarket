from fastapi import FastAPI

app = FastAPI(title="SMarket API", version="Develop")


@app.get("/")
async def root():
    return {"API": "Working"}
