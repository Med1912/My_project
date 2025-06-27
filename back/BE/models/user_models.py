from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship
from db.database import Base
from models.demande import Demande 


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    prenom = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    role = Column(String(255))  
    latitude = Column(Float)
    longitude = Column(Float)
    association_nom = Column(String(100))
   

    association = relationship("Association", back_populates="user", uselist=False)
    volontaire = relationship("Volontaire", back_populates="user", uselist=False)
    sinistre = relationship("Sinistre", back_populates="user", uselist=False)

class Association(Base):
    __tablename__ = "associations"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    location = Column(String((255)))
    user_id = Column(Integer, ForeignKey("users.id"))

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship("User", back_populates="association")
    demandes = relationship("Demande", back_populates="association")

    @property
    def email(self):
        return self.user.email if self.user else None

class Volontaire(Base):
    __tablename__ = "volontaires"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="volontaire")
    taches = relationship("Tache", back_populates="volontaire", cascade="all, delete")


class Sinistre(Base):
    __tablename__ = "sinistres"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    latitude = Column(Float, nullable=True)  
    longitude = Column(Float, nullable=True)
    user = relationship("User", back_populates="sinistre")

    demandes = relationship("Demande", back_populates="sinistre", cascade="all, delete-orphan")


