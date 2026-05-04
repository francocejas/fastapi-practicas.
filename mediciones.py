from fastapi import FastAPI
from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator

app= FastAPI()


class Medicion (BaseModel):  #validacion de valores modelo
    valor:float
    unidad:Annotated[str, Field (pattern="^(C|F)$")]  #validacion específica con annotated
    
    @field_validator("valor") #validamos el valor numerico float
    @classmethod
    def validar_unidad(cls, v:float,info):
        if info.data.get ("unidad") == "C" and v < -273.15:
            raise ValueError ("La temp. no puede ser menor al cero absoluto")
        return v
@app.post("/mediciones")
async def registrar_medicion(datos: Medicion):
    return {
        "mensaje": "Medición recibida correctamente",
        "temperatura": datos.valor,
        "unidad": datos.unidad}



