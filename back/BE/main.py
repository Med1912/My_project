from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_routes
from routes.association_router import association_router
from routes import demande
from routes import status as status_routes
from routes import tache
from models import user_models
from db.database import Base, engine
import logging
from fastapi.responses import JSONResponse
from routes import sinistre_routes
from routes import volontaire_routes

user_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )

# origins = [
#     "http://localhost:5174",  
#     "http://127.0.0.1:5174",  
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)
app.include_router(demande.router)
app.include_router(status_routes.router)
app.include_router(tache.router)
app.include_router(association_router)
app.include_router(sinistre_routes.router)
app.include_router(volontaire_routes.router)

logging.basicConfig(level=logging.DEBUG)
