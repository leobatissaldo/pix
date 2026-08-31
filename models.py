from database import Base
from sqlalchemy import Column, String, Integer, Float

class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_titular = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)