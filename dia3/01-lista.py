dias= ["lunes", "martes", "miercoles", "jueves", "viernes","sabado","domingo"]

""" Recuperar elementos de la lista """
print(dias)
print(dias[3])
print(dias[-2])
print(dias[1:3])

"""Agregar elementos a la lista """
dias.append("sabado")
dias.append("domingo")

""""" Eliminar elementos de la lista """
dias.pop(2)
del dias[0]

""" Actualizar elementos de la lista """
dias[-1]= "domingo "

""" Recorrer la lista """
for dia in dias:
    print(dia)
    