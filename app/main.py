from fastapi import FastAPI
from app.routes import agent


app = FastAPI()

app.include_router(agent.router)
