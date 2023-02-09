from fastapi.responses import JSONResponse
from fastapi import APIRouter

router = APIRouter(prefix="/router", tags=["Router"])

@router.get("/")
async def root():
    return {"message": "Hello WOrld"}

@router.get("/detalha_usuario")
def detalha_usuario(nome_usuario,):
    pass
