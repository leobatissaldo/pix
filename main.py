from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
from schemas import ContaInput, ContaResponse, TransacaoInput, TransacaoOutput
from models import Conta
from service import Conta_Service, Transacao_Service
import models

app = FastAPI(title="Transações Pix")

models.Base.metadata.create_all(bind=engine)

# @app.get("/")
# def health_check():
#     return {"message": "ok", "status": 200}

@app.post("/contas")
def adicionar_conta(dados:ContaInput, db: Session = Depends(get_db)):
    service = Conta_Service(db)
    return service.criar_conta(dados)

@app.get("/contas")
def listar_contas(db: Session = Depends(get_db)):
   service = Conta_Service(db)
   return service.listar()

@app.get("/contas/{id}")
def buscar_conta(id: int, db: Session = Depends(get_db)):
    service = Conta_Service(db)
    return service.buscar_conta(id)

@app.delete("/contas/{id}")
def desativar_conta(id: int, db: Session = Depends(get_db)):
    service = Conta_Service(db)
    return service.desativar_conta(id)


@app.post("/transacao")
def criar_transacao(dados: TransacaoInput, db: Session = Depends(get_db)):
    service = Transacao_Service(db)
    return service.realizar_transacao(dados)

@app.get("/transacao/{id}")
def buscar_transacao(id: int, db: Session = Depends(get_db)):
    service = Transacao_Service(db)
    return service.buscar_transacao(id)
