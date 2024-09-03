from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Alojamiento
from schemas import AlojamientoCreate, Alojamiento as AlojamientoSchema
from crud import create_alojamiento, get_alojamiento, get_alojamientos, update_alojamiento, delete_alojamiento
from database import get_db

router = APIRouter()

# Endpoint para crear un nuevo alojamiento
@router.post("/alojamientos/", response_model=AlojamientoSchema)
def create_accommodation(alojamiento: AlojamientoCreate, db: Session = Depends(get_db)):
    return create_alojamiento(db=db, alojamiento=alojamiento)

# Endpoint para obtener un alojamiento por ID
@router.get("/alojamientos/{alojamiento_id}", response_model=AlojamientoSchema)
def read_accommodation(alojamiento_id: int, db: Session = Depends(get_db)):
    db_alojamiento = get_alojamiento(db=db, alojamiento_id=alojamiento_id)
    if db_alojamiento is None:
        raise HTTPException(status_code=404, detail="Alojamiento not found")
    return db_alojamiento

# Endpoint para obtener una lista de alojamientos
@router.get("/alojamientos/", response_model=List[AlojamientoSchema])
def read_accommodations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_alojamientos(db=db, skip=skip, limit=limit)

# Endpoint para actualizar un alojamiento por ID
@router.put("/alojamientos/{alojamiento_id}", response_model=AlojamientoSchema)
def update_accommodation(alojamiento_id: int, alojamiento: AlojamientoCreate, db: Session = Depends(get_db)):
    db_alojamiento = get_alojamiento(db=db, alojamiento_id=alojamiento_id)
    if db_alojamiento is None:
        raise HTTPException(status_code=404, detail="Alojamiento not found")
    return update_alojamiento(db=db, alojamiento_id=alojamiento_id, alojamiento=alojamiento)

# Endpoint para eliminar un alojamiento por ID
@router.delete("/alojamientos/{alojamiento_id}", response_model=AlojamientoSchema)
def delete_accommodation(alojamiento_id: int, db: Session = Depends(get_db)):
    db_alojamiento = get_alojamiento(db=db, alojamiento_id=alojamiento_id)
    if db_alojamiento is None:
        raise HTTPException(status_code=404, detail="Alojamiento not found")
    return delete_alojamiento(db=db, alojamiento_id=alojamiento_id)
