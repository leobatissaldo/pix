from passlib.context import CryptContext
from fastapi.security import OAuth2AuthorizationCodeBearer

oauth_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="login")


