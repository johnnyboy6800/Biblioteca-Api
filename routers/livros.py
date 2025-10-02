from fastapi import  status, Depends, Response, APIRouter
from database.database import SessionLocal, get_db
from models import schemas
from sqlalchemy.orm import Session
from typing import List
from repository.livros_functions import buscar_livro_porNome ,deletar_livro, exibir_livro_porID, get_all, edit, postar_novo_livro, edit_titulo
from repository.oaoth2 import get_current_user



router = APIRouter(
    prefix='/livros',
    tags=['livros']
)



@router.put('/titulo/{id}')
async def modificar_livro_titulo(id, request: schemas.showTitulo, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return edit_titulo(id, request, db)

@router.put('/{id}')
async def modificar_livro(id, request: schemas.Livro ,db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return edit(id, request, db)


@router.get("/", response_model=List[schemas.Show])
def exibir_livros(db: Session = Depends(get_db)):
    return get_all(db)

@router.delete('/{id}',  status_code=status.HTTP_200_OK)
def livros_del_getID(id,response: Response ,db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return deletar_livro(id, response, db)
    
    

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.Show)
def livros_getID(id,response: Response,db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return exibir_livro_porID(id, response, db)
    

@router.post('/', status_code=status.HTTP_201_CREATED)
def Postar_livro(request: schemas.Livro, db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
   return  postar_novo_livro(request, db)

@router.get('/Search/', response_model= schemas.Livro)
def buscar_livro(request, db: Session = Depends(get_db) ,current_user: schemas.User = Depends(get_current_user)):
    return buscar_livro_porNome(request, db)
