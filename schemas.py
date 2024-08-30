from pydantic import BaseModel
from datetime import datetime

# Esquema base para Alojamiento
class AlojamientoBase(BaseModel):
    nombre: str
    direccion: str
    ciudad: str
    aforo: int
    convenio: str

# Esquema utilizado para crear un nuevo Alojamiento
class AlojamientoCreate(AlojamientoBase):
    pass

# Esquema utilizado para devolver un Alojamiento
class Alojamiento(AlojamientoBase):
    id: int

    class Config:
        from_attributes = True

# Esquema base para Acceso
class AccesoBase(BaseModel):
    id_usuario: int
    id_alojamiento: int
    id_evento: int
    tipo_acceso: str
    fecha_hora_acceso: datetime

# Esquema utilizado para crear un nuevo Acceso
class AccesoCreate(AccesoBase):
    pass

# Esquema utilizado para devolver un Acceso
class Acceso(AccesoBase):
    id: int

    class Config:
        from_attributes = True
