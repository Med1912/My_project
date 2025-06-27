from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    etat = Column(String(255), default="en attente")
    demande_id = Column(Integer, ForeignKey("demandes.id"))

    demande = relationship("Demande", back_populates="status")
