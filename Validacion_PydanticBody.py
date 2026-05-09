from fastapi import FastAPI, Query 
from typing import Annotated 
from pydantic import BaseModel, Field 

app=FastAPI()

class User (BaseModel):
    username:str
    email:str
    age: Annotated [int, Field (gt=0)]
    
@app.post ("/users")
def validacion(Usuario:User):
    return{"validacion_exitosa": Usuario}
