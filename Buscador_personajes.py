from fastapi import FastAPI

app= FastAPI()

personajes=[{"nombre": "Harry Potter"}, {"nombre": "Albus Dumbledore"}, {"nombre":"Severus Snape"}, {"nombre": "Giny Weasley"}]

@app.get("/personaje/{id}")
def encontrar_personajes(id: int):
    if id <0 or id >=len(personajes):  #el id debe ser menor que el largo de la lista
        return{"error": "personaje no existe"} #método para no recorrer va directo a la posicion del objeto del diciconario
    else:
        return{"datos": personajes[id]}
    
