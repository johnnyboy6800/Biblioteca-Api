from fastapi import  FastAPI
import uvicorn
from database.database import  engine
from routers import user, livros, Login
from models import models

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(livros.router)
app.include_router(Login.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)