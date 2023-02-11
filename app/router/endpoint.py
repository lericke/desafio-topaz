from fastapi.responses import JSONResponse
from fastapi import APIRouter

from utils.github import Github 
from utils.relatorio import Relatorio

router = APIRouter(prefix="/router", tags=["Router"])

@router.post("/gera_relatorio/{nome_usuario}")
def detalha_usuario(nome_usuario):
    
    usuario = Github().get_data(nome_usuario)

    repos = Github().get_repos(nome_usuario)

    relatorio = Relatorio().criar_relatorio(nome_usuario, usuario, repos)

    return {"message": "Relatório gerado com sucesso!"}

