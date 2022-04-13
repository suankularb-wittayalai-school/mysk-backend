from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI()


@app.get("/")
def healthCheck():
    return {"status": True}


if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get("HOST"), port=int(os.environ.get("PORT")))
