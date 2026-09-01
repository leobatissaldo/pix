from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from models import Conta

class Transacao_Service():
    def __init__(self, db: Session):
        self.db = db

    def criar_conta(self):
        novo_usuario = Conta(nome_titular=input.nome, saldo=input.saldo)
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        return novo_usuario