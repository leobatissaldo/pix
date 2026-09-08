from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
from schemas import ContaInput, ContaResponse
from models import Conta
from service import Conta_Service
import models

app = FastAPI(title="Transações Pix")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"message": "ok", "status": 200}

@app.post("/contas")
def adicionar_conta(dados:ContaInput, db: Session = Depends(get_db)):
    service = Conta_Service(db)
    return service.criar_conta(dados)