from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.models.user import UsersLoginRequest, User
from app.config.db_conexion import data_conexion
from app.utils.utils import create_access_token, settings
from app.routes import manager
import jwt

# Setting allowed origins for CORS
origins = [
    "http://localhost:8080",
]

app = FastAPI()

# CORS middleware to handle origin allowed requests
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Endpoint to authenticate and generate access tokens
@app.post("/login")
async def login(user_request: UsersLoginRequest, response: Response):
    params = [
        user_request.email,
        user_request.password_hash  # Asegúrate de que esto es el hash de la contraseña
    ]
    users = data_conexion.execute_procedure('sp_user_login', params)

    # La lista de resultados puede ser vacía si no hay coincidencias
    if users is not None and 'result' in users and len(users['result']) > 0:
        user = users['result'][0]

        # Crear el token de acceso
        access_token = create_access_token(data={"sub": user["user_id"], "role": user["role"]})
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            max_age=3600
        )

        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Incorrect credentials")

# Middleware to validate the token in the routes
async def user_token_validation(request: Request, call_next):
    if request.url.path.startswith("/login") == False:
        token = request.headers.get("Authorization", "").replace("Bearer ", "").strip()
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        role: str = payload.get("role", "support", "manager", "member")

        if request.url.path.startswith("support"):
            verified = (role == "support")

        elif request.url.path.startswith("manager"):
            verified = (role == "manager")

        elif request.url.path.startswith("member"):
            verified = (role == "member")

        else:
            verified = False

        if verified:
            return await call_next(request)
        else:
            raise HTTPException(status_code=403, detail="You do not have permissions to access")

    return await call_next(request)

app.include_router(manager.router, prefix="/manager", tags=["Manager"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
