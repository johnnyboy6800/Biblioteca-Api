# API - Guia de Execução

Este projeto utiliza **FastAPI** para construção da API.  
Siga os passos abaixo para rodar localmente:

---

## 1. Criar e ativar o ambiente virtual

Antes de rodar a aplicação, é necessário criar um ambiente virtual para isolar as dependências do projeto.

### Linux / MacOS
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows(Prompt de comando)
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```
### Windows(PowerShell)
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
### Instale as Dependências
```bash
pip install -r requirements.txt
```
### Para executar a aplicação
```bash
fastapi dev
```
### Para acessar a documentação (Swagger)
```bash
http://127.0.0.1:8000/docs
```




