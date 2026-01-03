usuario = {
    "id": 1,
    "nombre": "Juan",
    "edad": 20,
    "direccion": {
        "calle": "Avenida los girasoles",
        "numero": 123,
        "piso": 1,
        "coordenadas": (1.23, 4.56),
    },
    "telefono": "123456789",
}

"""RECUPERAR ELEMENTOS DEL DICCIONARIO"""
print(usuario["nombre"])
print(usuario["direccion"]["coordenadas"])

""" Agregar elementos a un diccionario """
usuario["correo"] = "juan@gmail.com"

"""eliminar elementos del diccionario"""
usuario.pop("edad")
del usuario["direccion"]

"""RECORRER ELEMENTOS DEL DICCIONARIO"""
for key, value in usuario.items():
    print(f"{key}: {value}") #esto es util si queremos tanto llaves como valores

for key in usuario:
    print(key, usuario[key])  #otra forma de obtener los valores a partir de las llaves

for key in usuario.keys():
    print(key,usuario[key]) #otra forma de obtener los valores a partir de las llaves

for value in usuario.values():
    print(value) #esto es util si solo nos interesan los valores


