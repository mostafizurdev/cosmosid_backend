from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = " "
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def hash_password(password: str):
    return pwd_context.hash(password)


async def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


async def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def register_user(user: dict):
    password_hash = await hash_password(user['password'])
    return {"message": "User registered"}


async def login_user(form_data: dict):
    return {"access_token": "example_token", "token_type": "bearer"}
