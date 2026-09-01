from pydantic import BaseModel, model_validator
from datetime import datetime

class ContaInput(BaseModel):
    nome: str
    saldo: float

    @model_validator(mode="after")
    def validar_saldo(self):
        if self.saldo <= 0:
            raise ValueError("O valor informado é incompativel")
        return self.saldo

class ContaResponse(BaseModel):
    id: int
    nome: str
    saldo: float

class TransacaoInput(BaseModel):
    conta_origem_id: int
    conta_destino_id: int
    valor: float

    @model_validator(mode="after")
    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("O valor informado é incompativel")
        return self
    
    def verificar_contas(self):
        if self.conta_destino_id == self.conta_origem_id:
            raise ValueError("As contas sao iguais")
        return self

class TransacaoOutput(BaseModel):
    horario: datetime
    conta_destino_id: int
    valor: float

