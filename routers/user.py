from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import schemas, models
from database.database import SessionLocal, get_db
from typing import List
from repository import user_functions


router = APIRouter(
    prefix='/usuarios',
    tags=['usuarios']
)


@router.post('/')
def add_user(user: schemas.User, db: Session = Depends(get_db)):
   return user_functions.add_user_func(user, db)


@router.get('/{id}',response_model= schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_functions.get_user_byId(id, db)


@router.get('/', response_model=List[schemas.ShowUser], )
def exibir_usuarios(db: Session = Depends(get_db)):
    return user_functions.show_all_users(db)


@router.delete('/{id}' )
def delete_usuario(id, db: Session = Depends(get_db)):
   return user_functions.delete_User(id, db)
    
    
@router.put('/{id}' )
def edit_user(id, request: schemas.User, db: Session = Depends(get_db)):
   return user_functions.edit_user_byId
