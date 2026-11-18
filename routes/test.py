from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/")
def test():
    return {"message": "Hola, esto es un test para las nuevas rutas"}