from fastapi import FastAPI, HTTPException  # Asegúrate de importar HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Agregar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a los orígenes que deseas permitir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OBJ_DIR = os.path.join(BASE_DIR, 'models')  # Asegúrate de que existe la carpeta 'models'

@app.get("/shapes/{shape_type}")
async def get_shape_data(shape_type: str):
    obj_file = f"{shape_type}.obj"
    obj_path = os.path.join(OBJ_DIR, obj_file)
    
    if not os.path.exists(obj_path):
        raise HTTPException(status_code=404, detail="Shape not found")
    
    return FileResponse(obj_path)
