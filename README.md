# 💳 Transaction Verification

API REST para gerenciamento de transações financeiras entre usuários e lojistas, construída com **FastAPI** e **Clean Architecture**.

## 🚀 Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green?logo=fastapi)
![SQLModel](https://img.shields.io/badge/SQLModel-ORM-red)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-orange)

**Backend:** Python, FastAPI, SQLModel, Pydantic  
**Database:** SQL Server  
**Architecture:** Clean Architecture, Repository Pattern, Dependency Injection

## 📋 Funcionalidades

- ✅ Cadastro de usuários (Comum e Lojista)
- ✅ Validações robustas (CPF/CNPJ único, email válido, senha forte)
- ✅ Documentação automática (Swagger/OpenAPI)
- 🚧 Sistema de transferências (em desenvolvimento)

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/DigaLugas/transaction-verification.git
cd transaction-verification

# Ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Dependências
pip install -r requirements.txt

# Configure .env
echo "USER=seu_usuario" > .env
echo "SENHA=sua_senha" >> .env

# Execute
uvicorn app.main:app --reload

# Acesse a documentação
# http://localhost:8000/docs
```

## 📁 Arquitetura

```
app/
├── domain/
│   ├── models/      # Entidades (User, Transaction)
│   ├── dto/         # Validação de entrada (Pydantic)
│   ├── repository/  # Acesso a dados
│   └── service/     # Lógica de negócio
├── routers/         # Endpoints da API
├── dependencies/    # Dependency Injection
└── database/        # Configuração do banco
```

**Padrões aplicados:** Repository Pattern, Service Layer, DTO, Dependency Injection

## 📚 Documentação

A API possui **documentação interativa automática** (Swagger/OpenAPI):
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

*Todos os endpoints, schemas e validações estão documentados automaticamente.*

## 🛠️ Características Técnicas

- **Type hints** em todo o código
- **Validações customizadas** (Pydantic validators)
- **Separação de camadas** (Domain, Application, Infrastructure)
- **Dependency Injection** (FastAPI Depends)
- **SQL com ORM** (SQLModel)
- **Variáveis de ambiente** (.env)

## 👤 Contato

**GitHub:** [@DigaLugas](https://github.com/DigaLugas)  
**LinkedIn:** [Lucas Zan](https://linkedin.com/in/lucasgrfzan)

---

*Projeto de estudo - demonstrando boas práticas de desenvolvimento backend*
