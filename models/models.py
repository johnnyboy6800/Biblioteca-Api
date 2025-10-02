from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Livro(Base):
    __tablename__ = "livros"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)
    lançamento = Column(String)
    #dono = Column(String, ForeignKey(Usuarios.))
    userid = Column(Integer, ForeignKey("Usuarios.id"))
    user = relationship("User", back_populates="livros")
class User(Base):
    __tablename__ = "Usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    idade = Column(Integer)
    email = Column(String)
    password = Column(String)
    livros = relationship('Livro', back_populates='user')