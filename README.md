# WorkoutAPI

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.127.0-009688.svg)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-11-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Uma API REST moderna e assíncrona para gerenciamento de atletas, categorias e centros de treinamento de CrossFit, desenvolvida com FastAPI.

## 📋 Índice

- [Características](#-características)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração do Banco de Dados](#-configuração-do-banco-de-dados)
- [Uso](#-uso)
- [Endpoints da API](#-endpoints-da-api)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Modelagem de Dados](#-modelagem-de-dados)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

## ✨ Características

- **API Assíncrona**: Performance otimizada com operações assíncronas usando `async/await`
- **Validação de Dados**: Validação automática com Pydantic
- **Documentação Automática**: Swagger UI e ReDoc integrados
- **Paginação**: Suporte a paginação com `fastapi-pagination`
- **Filtros**: Query parameters para busca por nome e CPF
- **Tratamento de Erros**: Exceções customizadas e tratamento de integridade de dados
- **Migrações**: Controle de versão do banco de dados com Alembic
- **Docker**: Ambiente de desenvolvimento com Docker Compose

## 🚀 Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e de alta performance
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM Python
- **[Alembic](https://alembic.sqlalchemy.org/)** - Ferramenta de migração de banco de dados
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados
- **[PostgreSQL](https://www.postgresql.org/)** - Banco de dados relacional
- **[Docker](https://www.docker.com/)** - Containerização
- **[fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/)** - Paginação automática

## 📦 Pré-requisitos

- Python 3.11+
- Poetry ou pip
- Docker e Docker Compose
- Make (opcional, mas recomendado)

## 🔧 Instalação

### Opção 1: Usando Poetry (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/digitalinnovationone/workout_api.git
cd workout_api

# Instale as dependências com Poetry
poetry install

# Ative o ambiente virtual
poetry shell
```

### Opção 2: Usando pip

```bash
# Clone o repositório
git clone https://github.com/digitalinnovationone/workout_api.git
cd workout_api

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Opção 3: Usando pyenv

```bash
# Instale a versão do Python
pyenv install 3.11.4

# Crie o ambiente virtual
pyenv virtualenv 3.11.4 workoutapi

# Ative o ambiente
pyenv activate workoutapi

# Instale as dependências
pip install -r requirements.txt
```

## 🗄️ Configuração do Banco de Dados

### 1. Inicie o PostgreSQL com Docker

```bash
# Inicie o container do PostgreSQL
docker-compose up -d

# Ou usando Make
make run-docker
```

### 2. Execute as Migrações

```bash
# Aplique as migrações existentes
alembic upgrade head

# Ou usando Make
make run-migrations
```

### 3. Criar uma Nova Migração (se necessário)

```bash
# Crie uma nova migração
alembic revision --autogenerate -m "descrição_da_migração"

# Ou usando Make
make create-migrations d="descrição_da_migração"
```

### 4. Popular o Banco de Dados (Opcional)

```bash
# Execute o script de população
python populate_db.py
```

## 🎯 Uso

### Iniciar o Servidor

```bash
# Inicie o servidor de desenvolvimento
uvicorn workout_api.main:app --reload

# Ou usando Make
make run

# Ou com Poetry
poetry run uvicorn workout_api.main:app --reload
```

## 📚 Endpoints da API

### Atletas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/atletas/` | Criar novo atleta |
| `GET` | `/atletas/` | Listar todos os atletas (com paginação) |
| `GET` | `/atletas/{id}` | Buscar atleta por ID |
| `PATCH` | `/atletas/{id}` | Atualizar atleta |
| `DELETE` | `/atletas/{id}` | Deletar atleta |

**Query Parameters para GET /atletas/**:
- `nome`: Filtrar por nome (busca parcial, case-insensitive)
- `page`: Número da página (padrão: 1)
- `size`: Tamanho da página (padrão: 50)

### Categorias

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/categorias/` | Criar nova categoria |
| `GET` | `/categorias/` | Listar todas as categorias (com paginação) |
| `GET` | `/categorias/{id}` | Buscar categoria por ID |

### Centros de Treinamento

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/centros_treinamento/` | Criar novo centro de treinamento |
| `GET` | `/centros_treinamento/` | Listar todos os centros (com paginação) |
| `GET` | `/centros_treinamento/{id}` | Buscar centro por ID |

## 💡 Exemplos de Uso

### Criar uma Categoria

```bash
curl -X POST "<local_host_to_api_url>" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Scale"
  }'
```

**Resposta:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "nome": "Scale"
}
```

### Criar um Centro de Treinamento

```bash
curl -X POST "<local_host_to_api_url>" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "CT King",
    "endereco": "Rua X, 10",
    "proprietario": "Marcos"
  }'
```

**Resposta:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "nome": "CT King",
  "endereco": "Rua X, 10",
  "proprietario": "Marcos"
}
```

### Criar um Atleta

```bash
curl -X POST "<local_host_to_api_url>" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "cpf": "12345678900",
    "idade": 25,
    "peso": 75.5,
    "altura": 1.75,
    "sexo": "M",
    "categoria": {
      "nome": "Scale"
    },
    "centro_treinamento": {
      "nome": "CT King"
    }
  }'
```

**Resposta:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "created_at": "2025-12-28T10:30:00",
  "nome": "João Silva",
  "cpf": "12345678900",
  "idade": 25,
  "peso": 75.5,
  "altura": 1.75,
  "sexo": "M",
  "categoria": {
    "nome": "Scale"
  },
  "centro_treinamento": {
    "nome": "CT King"
  }
}
```

### Listar Atletas com Paginação

```bash
# Primeira página (50 itens por página)
curl "<local_host_to_api_url>/atletas/?page=1&size=50"

# Filtrar por nome
curl "<local_host_to_api_url>/atletas/?nome=João"
```

**Resposta:**
```json
{
  "items": [
    {
      "nome": "João Silva",
      "categoria": {
        "nome": "Scale"
      },
      "centro_treinamento": {
        "nome": "CT King"
      }
    }
  ],
  "total": 1,
  "page": 1,
  "size": 50,
  "pages": 1
}
```

### Buscar Atleta por ID

```bash
curl "<local_host_to_api_url>/atletas/3fa85f64-5717-4562-b3fc-2c963f66afa6"
```

### Atualizar um Atleta

```bash
curl -X PATCH "<local_host_to_api_url>/atletas/3fa85f64-5717-4562-b3fc-2c963f66afa6" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Pedro Silva",
    "idade": 26
  }'
```

### Deletar um Atleta

```bash
curl -X DELETE "<local_host_to_api_url>/atletas/3fa85f64-5717-4562-b3fc-2c963f66afa6"
```

### Usando Python com httpx

```python
import httpx
import asyncio

async def criar_atleta():
    async with httpx.AsyncClient() as client:
        # Criar categoria
        categoria = await client.post(
            "<local_host_to_api_url>/categorias/",
            json={"nome": "Scale"}
        )
        
        # Criar centro de treinamento
        centro = await client.post(
            "<local_host_to_api_url>/centros_treinamento/",
            json={
                "nome": "CT King",
                "endereco": "Rua X, 10",
                "proprietario": "Marcos"
            }
        )
        
        # Criar atleta
        atleta = await client.post(
            "<local_host_to_api_url>/atletas/",
            json={
                "nome": "João Silva",
                "cpf": "12345678900",
                "idade": 25,
                "peso": 75.5,
                "altura": 1.75,
                "sexo": "M",
                "categoria": {"nome": "Scale"},
                "centro_treinamento": {"nome": "CT King"}
            }
        )
        
        print(atleta.json())

asyncio.run(criar_atleta())
```

## 📁 Estrutura do Projeto

```
workout_api/
├── alembic/                    # Migrações do banco de dados
│   ├── versions/              # Versões das migrações
│   └── env.py                 # Configuração do Alembic
├── workout_api/               # Pacote principal
│   ├── __init__.py
│   ├── main.py               # Aplicação FastAPI
│   ├── routers.py            # Roteadores da API
│   ├── services.py           # Serviços da aplicação
│   ├── atleta/               # Módulo de atletas
│   │   ├── controller.py     # Endpoints
│   │   ├── models.py         # Modelos SQLAlchemy
│   │   └── schemas.py        # Schemas Pydantic
│   ├── categorias/           # Módulo de categorias
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── centro_treinamento/   # Módulo de centros de treinamento
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── configs/              # Configurações
│   │   ├── database.py       # Configuração do banco
│   │   └── settings.py       # Settings da aplicação
│   └── contrib/              # Utilitários compartilhados
│       ├── dependencies.py   # Dependências do FastAPI
│       ├── models.py         # Modelos base
│       └── schemas.py        # Schemas base
├── alembic.ini               # Configuração do Alembic
├── docker-compose.yml        # Compose do PostgreSQL
├── Makefile                  # Comandos úteis
├── populate_db.py           # Script para popular o banco
├── pyproject.toml           # Configuração do Poetry
├── requirements.txt         # Dependências pip
└── README.md               # Este arquivo
```

## 🗂️ Modelagem de Dados

### Entidade-Relacionamento

```
┌─────────────────┐
│   Categoria     │
├─────────────────┤
│ id (UUID)       │
│ nome (str)      │
└────────┬────────┘
         │
         │ 1
         │
         │ N
    ┌────┴────────────────────┐
    │       Atleta            │
    ├─────────────────────────┤
    │ id (UUID)               │
    │ nome (str)              │
    │ cpf (str) [UNIQUE]      │
    │ idade (int)             │
    │ peso (float)            │
    │ altura (float)          │
    │ sexo (str)              │
    │ created_at (datetime)   │
    │ categoria_id (FK)       │
    │ centro_treinamento_id   │
    └────────┬────────────────┘
             │
             │ N
             │
             │ 1
    ┌────────┴──────────────────┐
    │  Centro de Treinamento    │
    ├───────────────────────────┤
    │ id (UUID)                 │
    │ nome (str)                │
    │ endereco (str)            │
    │ proprietario (str)        │
    └───────────────────────────┘
```

### Schemas

#### AtletaIn
```python
{
  "nome": "string",
  "cpf": "string",
  "idade": 0,
  "peso": 0.0,
  "altura": 0.0,
  "sexo": "string",
  "categoria": {
    "nome": "string"
  },
  "centro_treinamento": {
    "nome": "string"
  }
}
```

## 🛡️ Tratamento de Erros

A API implementa tratamento robusto de erros:

- **400 Bad Request**: Categoria ou centro de treinamento não encontrado
- **303 See Other**: Tentativa de criar entidade com dados duplicados (CPF, nome)
- **404 Not Found**: Recurso não encontrado
- **500 Internal Server Error**: Erros internos do servidor

### Exemplo de Erro de Integridade

```bash
# Tentar criar atleta com CPF duplicado
curl -X POST "http://127.0.0.1:8000/atletas/" \
  -H "Content-Type: application/json" \
  -d '{"cpf": "12345678900", ...}'
```

**Resposta (303):**
```json
{
  "detail": "Já existe um atleta com o CPF informado: 12345678900"
}
```

## 🔨 Comandos Make Disponíveis

```bash
make run              # Inicia a aplicação
make run-docker       # Inicia o PostgreSQL
make create-migrations d="msg"  # Cria nova migração
make run-migrations   # Aplica migrações
```

## 🧪 Testes

```bash
# Execute os testes (quando implementados)
pytest

# Com cobertura
pytest --cov=workout_api
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fork o projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

- **Repository**: [digitalinnovationone/workout_api](https://github.com/digitalinnovationone/workout_api)


## 🔗 Referências

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/)
- [PostgreSQL](https://www.postgresql.org/docs/)

---

Desenvolvido com ❤️ para a comunidade Python
