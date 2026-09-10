import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Conta
from service import Transacao_Service
from schemas import TransacaoInput
from conftest import get_test_db

def test_transacao_teste_valor(get_test_db):
    transacao_service = Transacao_Service(get_test_db)
    conta_origem_teste = Conta(
        nome_titular="teste1", 
        saldo=1000
    )
    conta_destino_teste = Conta(
        nome_titular="teste2",
        saldo=1000
    )

    get_test_db.add(conta_origem_teste)
    get_test_db.add(conta_destino_teste)
    get_test_db.commit()
    get_test_db.refresh(conta_origem_teste)
    get_test_db.refresh(conta_destino_teste)

    transacao_input = TransacaoInput(
        conta_origem_id=conta_origem_teste.id,
        conta_destino_id=conta_destino_teste.id,
        valor=100
    )
    

    transacao_service.realizar_transacao(transacao_input)

    get_test_db.refresh(conta_origem_teste)
    get_test_db.refresh(conta_destino_teste)

    assert conta_origem_teste.saldo == 900
    assert conta_destino_teste.saldo == 1100