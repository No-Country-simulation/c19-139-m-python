from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.models.user import UsersLoginRequest
from app.config.db_conexion import data_conexion
from app.utils.utils import create_access_token, settings

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
    raise HTTPException(status_code=401, detail="Incorrect credentials")
