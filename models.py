from database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey

class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_titular = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)

class Transação(Base):
    __table__ = "transacao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    horario = Column(DateTime, nullable=False)
    valor = Column(Integer, nullable=False)
    conta_partida_id = Column(Integer, ForeignKey("conta.id"))
    conta_destino_id = Column(Integer, ForeignKey("conta.id"))
    