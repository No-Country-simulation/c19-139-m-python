from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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