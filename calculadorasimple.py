from fastapi import FastAPI

app= FastAPI()

@app.get ("/sumar")
async def sumar_enteros (n1:int, n2:int):
    calculo=n1+n2
    return{"resultado":f"el valor de la suma es {calculo}"}
