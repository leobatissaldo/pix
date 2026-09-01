from pydantic import BaseModel
from datetime import datetime

class ContaInput(BaseModel):
    nome: str
    saldo: float

class ContaResponse(BaseModel):
    id: int
    nome: str
    saldo: float

class TransacaoInput(BaseModel):
    conta_destino_id: int
    valor: int

class TransacaoOutput(BaseModel):
    horario: datetime
    conta_destino_id: int
    valor: int

