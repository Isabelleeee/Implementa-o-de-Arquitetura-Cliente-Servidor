from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# 1º: Cria a instância do app
app = FastAPI()

# 2º: Configura o CORS (LOGO ABAIXO DO APP)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    preco: float

# Banco de dados em memória
db_livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "preco": 35.50},
    {"id": 2, "titulo": "O Alquimista", "autor": "Paulo Coelho", "preco": 42.00}
]

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    return db_livros

@app.get("/")
def read_root():
    return {"message": "API da Livraria Mackenzie Rodando!"}

@app.post("/livros")
def adicionar_livro(livro: Livro):
    db_livros.append(livro.dict())
    return {"status": "Livro adicionado com sucesso!"}