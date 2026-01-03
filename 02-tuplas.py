"""LAS TUPLAS SON LISTAS QYUE NO PUEDEN CAMBIAR"""
dias= ("lunes", "martes", "miercoles", "jueves", "viernes")

print(type(dias))

"""AGREGAR ELEMENTOS A LA LISTA"""
dias =list(dias)
dias.append("sabado")
dias= tuple(dias)

for dia in dias:
    print(dia)
