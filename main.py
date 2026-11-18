from fastapi import FastAPI
from routes import test

app = FastAPI()

app.include_router(test.router)

@app.get("/")
def read_root():
    return {"message": "Hola esta es la primera ruta"}