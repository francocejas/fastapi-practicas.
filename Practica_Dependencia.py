from fastapi import FastAPI,Depends
from typing import Annotated 

app= FastAPI()


def calcule_tax(price:float):
    return price*1.21


@app.get("/checkout")
def controlar_precio (total:Annotated[float,Depends(calcule_tax)]):
    return {
        "mensaje": "precio final calculado",
        "valor": total
    }