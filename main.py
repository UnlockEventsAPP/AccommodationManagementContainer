from fastapi import FastAPI
from database import create_tables
from routers import accommodations, access

app = FastAPI()

# Crear tablas en la base de datos en el inicio de la aplicación
@app.on_event("startup")
def on_startup():
    create_tables()

# Incluir las rutas para gestionar alojamientos y accesos
app.include_router(accommodations.router, prefix="/api/accommodations", tags=["Accommodations"])
app.include_router(access.router, prefix="/api/access", tags=["Access"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Accommodation Service"}
