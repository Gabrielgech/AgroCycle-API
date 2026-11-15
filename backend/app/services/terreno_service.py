from app.core.database import supabase
from app.schemas.terreno import TerrenoCreate, TerrenoUpdate

def create_terreno_in_db(data: TerrenoCreate, id_user: str):
    try:
        payload = data.model_dump()
        payload["id_user"] = id_user

        print(">>> Enviando a Supabase:", payload)
        response = supabase.table("terreno").insert(payload).execute()
        print(">>> Respuesta de Supabase:", response)

        return response.data[0] if response.data else None
    except Exception as e:
        print(">>> ERROR AL INSERTAR:", str(e))
        raise e

def get_all_terrenos_from_db(id_user: str):
    response = supabase.table("terreno").select("*").eq("id_user", id_user).execute()
    return response.data

def get_terreno_by_id_from_db(terreno_id: str, id_user: str):
    # Validamos tanto el id del terreno como que pertenezca al usuario
    response = supabase.table("terreno").select("*").eq("id", terreno_id).eq("id_user", id_user).execute()
    return response.data[0] if response.data else None

def update_terreno_in_db(terreno_id: str, data: TerrenoUpdate, id_user: str):
    payload = {k: v for k, v in data.model_dump().items() if v is not None}
    # Actualizamos solo si el terreno pertenece al usuario
    response = supabase.table("terreno").update(payload).eq("id", terreno_id).eq("id_user", id_user).execute()
    return response.data[0] if response.data else None

def delete_terreno_from_db(terreno_id: str, id_user: str):
    # Eliminamos solo si el terreno pertenece al usuario
    response = supabase.table("terreno").delete().eq("id", terreno_id).eq("id_user", id_user).execute()
    return {"message": "Terreno eliminado correctamente"}