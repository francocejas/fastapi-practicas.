from fastapi import FastAPI

app= FastAPI()

@app.get("/convertir/{pesos}")  #Endpoint para convertir  #recibe el monto en el parametro de ruta
async def convertir_pesos(pesos:int):
    valor_dolar= 1400  #precio del dolar aprox.
    conversion= pesos /valor_dolar
    return{"monto en dolares": conversion,       #retorna diccionario que fastapi convierte aJSON
           "mensaje": f"tus {pesos} equivalen a {conversion} dolares"}