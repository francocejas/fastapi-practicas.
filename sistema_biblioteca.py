from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app=FastAPI()

class Libro (BaseModel):  #creacion de clase con validacion de basemodel
    titulo: Annotated [str, Field(min_length=3)] #titulo no puede ser menor que 3 caracteres
    autor: str|None= None
    paginas:Annotated [int, Field (gt=0)] #paginas no puede ser menos que 0

Listavacia= []

@app.post("/libros")
async def crear_libro(nuevo_libro: Libro):
    Listavacia.append(nuevo_libro.model_dump())
    return {
        "mensaje": "libro registado",
           "datos": nuevo_libro }

@app.get("/libros")
async def get_libros ():
    return {"mensaje": "Lista de libros",
            "Lista": Listavacia }
