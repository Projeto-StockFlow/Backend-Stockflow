# Arquivo para criar o código de conexão com o banco de dados
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CheckConstraint, text, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///.stockflow.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    db.execute(text("PRAGMA Foreign_keys = ON"))

    try:
        yield db
    finally:
        db.close()


class VendedorDB(Base):
    __tablename__ = "vendedor"

    id_vendedor = Column(Integer, primary_key=True)
    nome_loja = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

class ProdutoDB(Base):
    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    quantidade = Column(String, nullable=False)
    estoque_minimo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    id_vendedor = Column(Integer, ForeignKey("vendedor.id_vendedor"), nullable=False)

class MovimentacaoDB(Base):
    __tablename__ = "movimentacao"

    id_movimentacao = Column(Integer, primary_key=True)
    quantidade = Column(Integer, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    observacao = Column(String, nullable=True)
    id_produto = Column(Integer, ForeignKey("produto.id_produto"))