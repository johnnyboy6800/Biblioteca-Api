from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    nome: str
    idade: str
    email: str
    password : str
   
class Username(BaseModel):
    nome: str

class ShowUser(BaseModel):
    nome:str
    email:str
    password:str
    id: int
    class Config():
        orm_mode = True


class Show(BaseModel):
    id: int
    titulo: str
    autor: str
    userid: int
    user: Optional[Username]

    class Config():
        orm_mode = True

class Livro(BaseModel):
    titulo: str
    autor: str
    userid: int
    class Config():
        orm_mode = True


class showTitulo(BaseModel):
    titulo: str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email : Optional[str] = None