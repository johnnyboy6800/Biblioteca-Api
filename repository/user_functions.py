from models import models
from sqlalchemy.orm import Session

def add_user_func(user, db: Session):
    HashedPassword = hash.Hash.bcrypt(user.password)   
    new_user = models.User(nome = user.nome, idade = user.idade, email = user.email, password = HashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_byId(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return 'Usuario não encontrado'
    return user

def show_all_users(db: Session):
    users = db.query(models.User).all()
    if not users:
        return {"Não existe usuário cadastrado no momento"}
    return users

def delete_User(id, db: Session):
    usuario = db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    if not usuario:
      return 'usuario não encontrado'
    return 'feito'

def edit_user_byId(id, request, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    user.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return 'done'

