from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import create_tables
from routers import accommodations, access

app = FastAPI()

origins = [
    "https://front-unlock-patrones.vercel.app",  # Dominio de tu frontend
    "http://localhost:4200",  # Si estás probando en Angular localmente
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Crear tablas en la base de datos en el inicio de la aplicación
@app.on_event("startup")
def on_startup():
    create_tables()

# Incluir las rutas para gestionar alojamientos y accesos
app.include_router(accommodations.router, prefix="/accommodations", tags=["Accommodations"])
app.include_router(access.router, prefix="/accommodations", tags=["Access"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Accommodation Service"}
