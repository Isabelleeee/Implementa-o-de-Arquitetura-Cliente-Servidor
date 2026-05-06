from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Libera geral para o exercício
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# Modelo de dados
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    preco: float

# Banco de dados em memória (para simplificar o 8.3)
db_livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "preco": 35.50},
    {"id": 2, "titulo": "O Alquimista", "autor": "Paulo Coelho", "preco": 42.00}
]

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    return db_livros

@app.post("/livros")
def adicionar_livro(livro: Livro):
    db_livros.append(livro.dict())
    return {"status": "Livro adicionado com sucesso!"}