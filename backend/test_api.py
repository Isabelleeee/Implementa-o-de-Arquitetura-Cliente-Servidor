import requests

# URL do backend no Azure
BASE_URL = "https://deploydearquiteturacliente-servidor-djfyh4axbwddh9cg.brazilsouth-01.azurewebsites.net"

def testar_listar_livros():
    """Função de teste para o endpoint GET /livros"""
    print("--- Testando GET /livros ---")
    response = requests.get(f"{BASE_URL}/livros")
    
    if response.status_code == 200:
        print("✅ Sucesso! O servidor retornou a lista.")
        print(f"Livros encontrados: {len(response.json())}")
    else:
        print(f"❌ Falha! Código de status: {response.status_code}")

def testar_adicionar_livro():
    """Função de teste para o endpoint POST /livros"""
    print("\n--- Testando POST /livros ---")
    novo_livro = {
        "id": 3,
        "titulo": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "preco": 45.0
    }
    response = requests.post(f"{BASE_URL}/livros", json=novo_livro)
    
    if response.status_code == 200:
        print("✅ Sucesso! Livro adicionado via script.")
    else:
        print(f"❌ Falha ao adicionar livro: {response.status_code}")

if __name__ == "__main__":
    testar_listar_livros()
    testar_adicionar_livro()