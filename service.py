from database import get_db
from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Conta
from schemas import ContaInput

class Conta_Service():
    def __init__(self, db: Session):
        self.db = db

    def criar_conta(self, input: ContaInput):
        novo_usuario = Conta(nome_titular=input.nome, saldo=input.saldo)
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        return novo_usuario

    def deletar_conta(self, id: int):
        conta_deletada = self.db.scalars(select(Conta).where(id == Conta.id)).first()
        if conta_deletada.conta_ativa == False:
            return {"message": "essa conta já esta desativada!"}
        elif conta_deletada.conta_ativa == True:
            conta_deletada.conta_ativa == False
            return {"message": "conta desativada com sucesso!"}
        else:
            raise HTTPException(status_code=404, detail="Conta não encontrada")

    def buscar_conta(self, id: int):
        conta_buscar = self.db.scalars(select(Conta).where(id == Conta.id))
        if conta_buscar:
            return conta_buscar
        else:
            raise HTTPException(status_code=404, detail="Conta não encontrada!")

class Transacao_Service():
    def __init__(self, db: Session):
        self.db = db
