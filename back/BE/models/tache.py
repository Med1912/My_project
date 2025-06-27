from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Tache(Base):
    __tablename__ = "taches"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), default="en attente")
    volontaire_id = Column(Integer, ForeignKey("volontaires.id"))
    demande_id = Column(Integer, ForeignKey("demandes.id"))

    volontaire = relationship("Volontaire", back_populates="taches")
    demande = relationship("Demande", back_populates="taches")
