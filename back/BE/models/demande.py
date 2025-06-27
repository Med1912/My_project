from sqlalchemy import Column ,Integer,String,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship
# from models.user_models import users





class Demande(Base) :
    __tablename__= "demandes"

    id= Column(Integer ,primary_key=True,index=True)
    type_aide= Column(String(255), nullable=False)
    description =Column(String(255), nullable=False)
    # sinister_id= Column(Integer,ForeignKey("sinistres.id"))
    sinistre_id = Column(Integer, ForeignKey("sinistres.id"))
    association_id = Column(Integer, ForeignKey("associations.id"))
    association = relationship("Association", back_populates="demandes")

    sinistre= relationship("Sinistre", back_populates="demandes")
    # status = relationship("Status", back_populates="demande" , cascade="all, delete-orphan")
    status = relationship("Status", back_populates="demande",uselist=False)
    taches = relationship("Tache", back_populates="demande", cascade="all, delete")




