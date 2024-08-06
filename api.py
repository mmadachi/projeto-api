Instalação das Dependências
bash
pip install fastapi sqlalchemy fastapi-pagination uvicorn

Criação do Modelo de Dados
Python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

do banco de dados importar Base

class Atleta(Base):
nometabela = "atletas"

id = Column(Integer, primary_key=True, autoincrement=True)
nome = Column(String(255), nullable=False)
cpf = Column(String(11), unique=True, nullable=False)
centro_treinamento = Column(String(255))
categoria = Column(String(255))

# Relacionamento com tabela de treinos (opcional)
# treinos = relationship("Treino", backref="atleta")
Configuração do Banco de Dados:
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql://usuário:senha@host:porta/banco de dados")
Base.metadata.create_all(engine)

SessionLocal = Sessão(autocommit=Falso, autoflush=Falso, bind=mecanismo)

Implementação da API Assíncrona
Python
from fastapi import FastAPI, Depends, HTTPException
from fastapi_pagination import Page, add_pagination
from sqlalchemy.orm import Session

de modelos importar Atleta
do banco de dados importar SessionLocal

aplicativo = FastAPI()

@app.on_event("startup")
async def startup_event():
sessão global
session = SessionLocal()

@app.on_event("shutdown")
async def shutdown_event():
sessão global
session.close()

Obter o banco de dados
def get_db(session: Sessão = Depends(SessionLocal)):
retornar sessão

Endpoint para buscar todos os atletas
@app.get("/atletas", response_model=Page[Atleta])
async def get_all_atletas(db: Sessão = Depends(get_db), limite: int | Nenhum = Nenhum, deslocamento: int | Nenhum = Nenhum):
atletas = db.query(Atleta).order_by(Atleta.id).limit(limit).offset(offset).all()
return Page(atletas, len(atletas))

Endpoint para buscar atletas por nome e CPF
@app.get("/atletas", response_model=List[Atleta])
async def get_atleta_by_nome_cpf(nome: str | Nenhum = Nenhum, cpf: str | Nenhum = Nenhum, db: Sessão = Depende(get_db)):
query = db.query(Atleta)

if nome:
    query = query.filter(Atleta.nome.ilike(f"%{nome}%"))

if cpf:
    query = query.filter(Atleta.cpf == cpf)

atletas = query.all()

if not atletas:
    raise HTTPException(status_code=404, detail="Atleta não encontrado")

return atletas
Endpoint para cadastrar um novo atleta
@app.post("/atletas")
assíncrono def
