from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.database import supabase

# Define el esquema para extraer el token del header Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Valida el token JWT usando Supabase Auth y retorna los datos del usuario actual.
    """
    try:
        # Llamamos a Supabase para validar el token y obtener el usuario
        response = supabase.auth.get_user(token)

        if not response or not response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales de autenticación inválidas",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user = response.user

        # Retornamos un diccionario con el ID (coincide con current_user.get("id"))
        return {
            "id": user.id,
            "email": user.email
        }

    except Exception as e:
        print(">>> ERROR DE AUTENTICACIÓN:", str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudo validar el token de acceso",
            headers={"WWW-Authenticate": "Bearer"},
        )