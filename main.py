from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
from schemas import ContaInput, ContaResponse
from models import Conta
import models

app = FastAPI(title="Transações Pix")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"message": "ok", "status": 200}

@app.post("/contas")
def adicionar_conta(input:ContaInput, db: Session = Depends(get_db)):
    novo_usuario = Conta(nome_titular=input.nome, saldo=input.saldo)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario