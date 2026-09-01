from pydantic import BaseModel

class ContaInput(BaseModel):
    nome: str
    saldo: float

class ContaResponse(BaseModel):
    id: int
    nome: str
    saldo: float