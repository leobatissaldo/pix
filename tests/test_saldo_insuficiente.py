import pytest
from fastapi import HTTPException
from models import Conta
from service import Transacao_Service
from conftest import get_test_db
from schemas import TransacaoInput

def test_saldo_insuficiente(get_test_db):
    transacao = Transacao_Service(get_test_db)
    conta_origem_teste = Conta(nome_titular="teste", saldo=100)
    conta_destino_teste = Conta(nome_titular="teste", saldo=1000)

    get_test_db.add(conta_origem_teste)
    get_test_db.add(conta_destino_teste)
    get_test_db.commit()
    get_test_db.refresh(conta_origem_teste)
    get_test_db.refresh(conta_destino_teste)

    input_transacao = TransacaoInput(
        conta_origem_id=conta_origem_teste.id,
        conta_destino_id=conta_destino_teste.id,
        valor=1000
    )

    with pytest.raises(HTTPException):
        transacao.realizar_transacao(input_transacao)
    
    get_test_db.refresh(conta_origem_teste)
    get_test_db.refresh(conta_destino_teste)

    transacao.realizar_transacao(input_transacao)

    assert conta_origem_teste.saldo == 100
    assert conta_destino_teste.saldo == 1000


