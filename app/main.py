from fastapi import FastAPI
from app.auth import register_user, login_user
from app.crud import get_taxonomy, add_taxonomy

app = FastAPI()


@app.post("/register")
def register(user: dict):
    return register_user(user)


@app.post("/login")
def login(form_data: dict):
    return login_user(form_data)


@app.get("/taxonomy/{taxonomy_id}")
async def read_taxonomy(taxonomy_id: int):
    return await get_taxonomy(taxonomy_id)


@app.post("/taxonomy")
async def create_taxonomy(taxonomy: dict):
    return await add_taxonomy(taxonomy)
