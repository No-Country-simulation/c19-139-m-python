from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Setting allowed origins for CORS
origins = [
    "http://localhost:8080",
]

app = FastAPI()