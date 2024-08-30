from sqlalchemy.orm import Session
from models import Alojamiento, Acceso
from schemas import AlojamientoCreate, AccesoCreate

# Funciones CRUD para Alojamiento

def create_alojamiento(db: Session, alojamiento: AlojamientoCreate):
    db_alojamiento = Alojamiento(**alojamiento.dict())
    db.add(db_alojamiento)
    db.commit()
    db.refresh(db_alojamiento)
    return db_alojamiento

def get_alojamiento(db: Session, alojamiento_id: int):
    return db.query(Alojamiento).filter(Alojamiento.id == alojamiento_id).first()

def get_alojamientos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Alojamiento).offset(skip).limit(limit).all()

def update_alojamiento(db: Session, alojamiento_id: int, alojamiento: AlojamientoCreate):
    db_alojamiento = db.query(Alojamiento).filter(Alojamiento.id == alojamiento_id).first()
    if db_alojamiento:
        for key, value in alojamiento.dict().items():
            setattr(db_alojamiento, key, value)
        db.commit()
        db.refresh(db_alojamiento)
    return db_alojamiento

def delete_alojamiento(db: Session, alojamiento_id: int):
    db_alojamiento = db.query(Alojamiento).filter(Alojamiento.id == alojamiento_id).first()
    if db_alojamiento:
        db.delete(db_alojamiento)
        db.commit()
    return db_alojamiento

# Funciones CRUD para Acceso

def create_acceso(db: Session, acceso: AccesoCreate):
    db_acceso = Acceso(**acceso.dict())
    db.add(db_acceso)
    db.commit()
    db.refresh(db_acceso)
    return db_acceso

def get_acceso(db: Session, acceso_id: int):
    return db.query(Acceso).filter(Acceso.id == acceso_id).first()

def get_accesos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Acceso).offset(skip).limit(limit).all()

def update_acceso(db: Session, acceso_id: int, acceso: AccesoCreate):
    db_acceso = db.query(Acceso).filter(Acceso.id == acceso_id).first()
    if db_acceso:
        for key, value in acceso.dict().items():
            setattr(db_acceso, key, value)
        db.commit()
        db.refresh(db_acceso)
    return db_acceso

def delete_acceso(db: Session, acceso_id: int):
    db_acceso = db.query(Acceso).filter(Acceso.id == acceso_id).first()
    if db_acceso:
        db.delete(db_acceso)
        db.commit()
    return db_acceso
