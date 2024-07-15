from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.models.user import UsersLoginRequest
from app.config.db_conexion import data_conexion
from app.utils.utils import create_access_token, settings
from app.routes import manager
from jose import jwt


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
        user_request.password_hash
    ]
    users = data_conexion.execute_procedure('sp_user_login')
    
    user = None
    if users is not None and 'result' in users and users['result']:
        user = users['result'][0][0]
    
    if user is not None:
        access_token = create_access_token(data={"sub": user["email"], "role": user["role"]})
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            max_age=3600
        )

        return {"access_token": access_token, "token_type": "bearer"}
    # CORS response should come after returning token
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# Middleware to validate the token in the routes
async def user_token_validation(request: Request, call_next):
    if request.url.path.startswith("/login") == False:
        token = request.headers.get("Authorization", "").replace("Bearer ", "").strip()
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        role: str = payload.get("support", "manager", "member")

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

# Routes
app.include_router(manager.router, prefix="/manager", tags=["Manager"])

# Running the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
