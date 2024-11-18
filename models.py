from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

# Modelo de la tabla Alojamiento
class Alojamiento(Base):
    __tablename__ = "alojamientos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    direccion = Column(String(255))
    ciudad = Column(String(100))
    aforo = Column(Integer)
    convenio = Column(String(100))
    precio = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="activo")
    # Relación con la tabla Acceso
    accesos = relationship("Acceso", back_populates="alojamiento")

# Modelo de la tabla Acceso
class Acceso(Base):
    __tablename__ = "accesos"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False)
    id_alojamiento = Column(Integer, ForeignKey("alojamientos.id"), nullable=False)
    id_evento = Column(Integer, nullable=False)
    tipo_acceso = Column(String(50))
    fecha_hora_acceso = Column(DateTime)

    # Relaciones con la tabla Alojamiento
    alojamiento = relationship("Alojamiento", back_populates="accesos")
