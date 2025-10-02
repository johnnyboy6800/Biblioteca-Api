from sqlalchemy.orm import Session
from models import models
from fastapi import HTTPException, status

def get_all(db: Session):
    livros = db.query(models.Livro).all()
    return livros

def edit(id, request ,db: Session):
    livro = db.query(models.Livro).filter(models.Livro.id == id)
    if not livro.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'livro com id {id} não encontrado')
    livro.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return 'done'

def edit_titulo(id, request, db: Session):
    livro = db.query(models.Livro).filter(models.Livro.id == id)
    livro.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return 'done'

def deletar_livro(id, response, db):
    livros = db.query(models.Livro).filter(models.Livro.id == id).delete(synchronize_session=False)
    if  livros:
        response.status_code = status.HTTP_404_NOT_FOUND
        db.commit()
        return {f'Livro com id: {id} encontrado e deletado'}
    else:
        return {'erro'}
    
def exibir_livro_porID(id, response, db):
    livros = db.query(models.Livro).filter(models.Livro.id == id).first()
    if not livros:
        response.status_code = status.HTTP_404_NOT_FOUND   
        return {'Não encontrado'} 
    return livros

def buscar_livro_porNome(request: str, db):
    livro = db.query(models.Livro).filter(models.Livro.titulo == request).first()
    return livro

def postar_novo_livro(request, db):
    new_livro = models.Livro(titulo = request.titulo, autor = request.autor, userid =  request.userid)
    db.add(new_livro)
    db.commit()
    db.refresh(new_livro)
    return new_livro
