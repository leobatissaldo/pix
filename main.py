from fastapi import FastAPI
import models

app = FastAPI(title="Transações Pix")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"message": "ok", "status": 200}