from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.terreno import TerrenoCreate, TerrenoUpdate
from app.services.terreno_service import (
    create_terreno_in_db,
    get_all_terrenos_from_db,
    get_terreno_by_id_from_db,
    update_terreno_in_db,
    delete_terreno_from_db
)
from app.core.security import get_current_user

router = APIRouter(prefix="/terrenos", tags=["Terrenos"])

@router.post("/", summary="Crear un nuevo terreno")
def create_terreno(terreno: TerrenoCreate, current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    result = create_terreno_in_db(terreno, user_id)
    if not result:
        raise HTTPException(status_code=400, detail="No se pudo registrar el terreno en Supabase")
    return {"message": "Terreno registrado con éxito", "data": result}

@router.get("/", summary="Listar todos los terrenos del usuario")
def list_terrenos(current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    return get_all_terrenos_from_db(user_id)

@router.get("/{terreno_id}", summary="Obtener un terreno por ID")
def get_terreno(terreno_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    terreno = get_terreno_by_id_from_db(terreno_id, user_id)
    if not terreno:
        raise HTTPException(status_code=404, detail="Terreno no encontrado")
    return terreno

@router.put("/{terreno_id}", summary="Actualizar un terreno")
def update_terreno(terreno_id: str, terreno_update: TerrenoUpdate, current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    updated = update_terreno_in_db(terreno_id, terreno_update, user_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Terreno no encontrado o no se pudo actualizar")
    return {"message": "Terreno actualizado con éxito", "data": updated}

@router.delete("/{terreno_id}", summary="Eliminar un terreno")
def delete_terreno(terreno_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    return delete_terreno_from_db(terreno_id, user_id)