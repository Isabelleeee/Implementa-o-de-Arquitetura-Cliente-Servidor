# Livraria Mackenzie - Exercício 8.3

Este projeto consiste na implementação de uma aplicação de livraria baseada na **Arquitetura Cliente-Servidor**, conforme o modelo definido no Exercício 8.1. A solução demonstra a separação clara entre a interface do usuário (Client) e a lógica de processamento e regras de negócio (Server).

## 🏗️ Arquitetura da Solução
A aplicação segue o padrão de camadas para garantir modularidade e facilidade de manutenção:
*   **Camada de Cliente (Front-end)**: Interface desenvolvida em HTML5 e JavaScript puro (ES6+), utilizando a **Fetch API** para realizar chamadas assíncronas ao servidor.
*   **Camada de Servidor (Back-end)**: API desenvolvida em **Python** com o framework **FastAPI**, responsável pelo processamento das requisições e gerenciamento do catálogo de livros.

---

## 📂 Estrutura do Repositório
```text
/
├── backend/
│   ├── main.py            # Servidor e rotas da API desenvolvidos em FastAPI
│   └── requirements.txt   # Dependências do projeto (FastAPI, Uvicorn, Pydantic)
├── frontend/
│   └── index.html         # Interface web da livraria (Cliente)
└── README.md              # Documentação do projeto
```

---

## 🚀 Como Executar

### 1. Preparação do Ambiente
Certifique-se de ter o Python 3.x instalado em sua máquina. Recomenda-se a criação de um ambiente virtual para isolar as dependências:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2. Instalação das Dependências
Navegue até a pasta do back-end e instale os pacotes necessários listados no arquivo de requerimentos:
```bash
cd backend
pip install -r requirements.txt
```

### 3. Execução do Servidor
Inicie a API utilizando o servidor Uvicorn:
```bash
uvicorn main:app --reload
```
O servidor estará ativo e pronto para receber requisições em: `http://127.0.0.1:8000`

### 4. Acessando a Aplicação
Abra o arquivo `frontend/index.html` em seu navegador de preferência. A página realizará o consumo automático dos dados do servidor local e exibirá o catálogo.

### 5. Testes do Back-end
Para validar o funcionamento da API de forma independente do front-end, foi desenvolvida uma função de teste automatizada em Python.

**Como rodar o teste:**
1. Instale a biblioteca requests: `pip install requests`
2. Execute o script: `python backend/test_api.py`
3. O script validará os endpoints de listagem (GET) e inserção (POST) diretamente no Azure.

---

## 🛠️ Tecnologias Utilizadas
*   **Linguagem**: Python.
*   **Framework**: FastAPI.
*   **Servidor ASGI**: Uvicorn.
*   **Validação de Dados**: Pydantic.
*   **Comunicação**: JSON / Protocolo HTTP via Fetch API.
*   **Front-end**: HTML/JavaScript (Client-side rendering).

---

**Desenvolvido por:** Isabelle da Costa Lopes
**Instituição:** Universidade Presbiteriana Mackenzie
**Curso:** Engenharia de Computação
