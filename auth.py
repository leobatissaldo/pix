
from passlib.context import CryptContext
from fastapi.security import OAuth2AuthorizationCodeBearer
from models import Conta
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY="ipoghspaighasipgahgpiagashjpxmlç"
ALGORITHM="HS256"
ACCESS_TOKEN_TIME=30


oauth_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="login", authorizationUrl="login")
pwd_context = CryptContext(["sha256_crypt"])

# def get_usuario_atual(db: Session = Depends(get_db)):
#     usuario_atual = db.scalars(select(Conta).where())

def gerar_hash(senha):
    senha_hash = pwd_context.hash(senha)
    return senha_hash

def verificar_hash(senha_hash, senha_input):
    return pwd_context.verify(senha_hash, senha_input)

def criar_token(usuario_id: int):
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_TIME)
    payload = {"sub": str(usuario_id), "exp": expiracao}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {
        "token": token,
        "type": "bearer"
    }

