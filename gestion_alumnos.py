from fastapi import FastAPI
from pydantic import BaseModel


class Alumno (BaseModel): # Valida que el usuario envíe datos corectos
    nombre:str
    materia:str
    nota:float

alumnos_db=[]  #creacion de lista

@app.post("/alumnos")  #registro de alumno
async def crear_alumno(nuevo_alumno: Alumno):
    alumnos_db.append(nuevo_alumno.model_dump())
    return {"mensaje":"alumno registrado exitosamente",
            "datos": nuevo_alumno}

@app.get("/alumnos")  #ruta para ver alumnos registrados
async def get_alumnos():
    return{"mensaje":"Listado de alumnos",
           "datos":alumnos_db}