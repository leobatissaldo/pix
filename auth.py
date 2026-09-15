from passlib.context import CryptContext
from fastapi.security import OAuth2AuthorizationCodeBearer
from models import Conta
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

oauth_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="login")
pwd_context = CryptContext(["sha256_crypt"])

# def get_usuario_atual(db: Session = Depends(get_db)):
#     usuario_atual = db.scalars(select(Conta).where())

def gerar_hash(senha):
    senha_hash = pwd_context.hash(senha)
    return senha_hash 
    

