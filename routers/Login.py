from datetime import timedelta
from database.database import get_db
from sqlalchemy.orm import Session
from models import models, schemas
from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from repository.hash import Hash
from repository import token_c

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)



@router.post('/')
def user_login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Credenciais inválidas')
    if not  Hash.verify(request.password, user.password):
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Credenciais inválidas')
    access_token_expires = timedelta(minutes=token_c.ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = token_c.create_access_token(
    data={"sub": user.email}, expires_delta = access_token_expires
    )
    return{"access_token": access_token, "token_type": "bearer"}
    

