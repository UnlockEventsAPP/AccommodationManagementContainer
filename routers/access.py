from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Acceso
from schemas import AccesoCreate, Acceso as AccesoSchema
from crud import create_acceso, get_acceso, get_accesos, update_acceso, delete_acceso
from database import get_db

router = APIRouter()

# Endpoint para crear un nuevo acceso
@router.post("/accesos/", response_model=AccesoSchema)
def create_access(access: AccesoCreate, db: Session = Depends(get_db)):
    return create_acceso(db=db, acceso=access)

# Endpoint para obtener un acceso por ID
@router.get("/accesos/{access_id}", response_model=AccesoSchema)
def read_access(access_id: int, db: Session = Depends(get_db)):
    db_access = get_acceso(db=db, acceso_id=access_id)
    if db_access is None:
        raise HTTPException(status_code=404, detail="Access not found")
    return db_access

# Endpoint para obtener una lista de accesos
@router.get("/accesos/", response_model=List[AccesoSchema])
def read_accesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_accesos(db=db, skip=skip, limit=limit)

# Endpoint para actualizar un acceso por ID
@router.put("/accesos/{access_id}", response_model=AccesoSchema)
def update_access(access_id: int, access: AccesoCreate, db: Session = Depends(get_db)):
    db_access = get_acceso(db=db, acceso_id=access_id)
    if db_access is None:
        raise HTTPException(status_code=404, detail="Access not found")
    return update_acceso(db=db, acceso_id=access_id, acceso=access)

# Endpoint para eliminar un acceso por ID
@router.delete("/accesos/{access_id}", response_model=AccesoSchema)
def delete_access(access_id: int, db: Session = Depends(get_db)):
    db_access = get_acceso(db=db, acceso_id=access_id)
    if db_access is None:
        raise HTTPException(status_code=404, detail="Access not found")
    return delete_acceso(db=db, acceso_id=access_id)
