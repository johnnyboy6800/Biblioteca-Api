# API - Guia de Execução

Este projeto utiliza **FastAPI** para construção da API.  
Siga os passos abaixo para rodar localmente:

---

##  Criar e ativar o ambiente virtual

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
## Instale as Dependências
```bash
pip install -r requirements.txt
```
## Para executar a aplicação
```bash
fastapi dev
```
## Para acessar a documentação (Swagger)
```bash
http://127.0.0.1:8000/docs
```
## Swagger
<img width="1505" height="864" alt="Captura de tela de 2025-10-02 12-36-53" src="https://github.com/user-attachments/assets/1ea6b34c-2c97-4671-b45c-16c5bd450735" />



