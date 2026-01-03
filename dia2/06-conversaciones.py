# programa para convertir diversas de pesosmexicanos a dolares y viceversa
import os
#impor os es para limpiar la pantalla
import time #importar time es para hacer una pausa
condicion = True #variable de control para el while
while condicion: #bucle principal
    print("""
        =====================================
              CONVERSIONES DE DIVISAS
        =====================================
          [1] Convertir de pesos a dolares
          [2] Convertir de dolares a pesos
          [3] Salir
        =====================================
    """) #menu de opciones
    opcion = input("Elija una operación:")
    os.system("cls" if os.name == "nt" else "clear") #limpiar pantalla
    if opcion == "1":
        print("""
              =====================================
                CONVERSION DE PESOS A DOLARES
              =====================================
         """)
        pesos= float(input("Ingresa el monto en pesos mexicanos:"))
        dolares= pesos / 18.5
        print(F"El monto en dolares es: {dolares}")

    elif opcion == "2":
        print("""
              =====================================
                CONVERSION DE DOLARES A PESOS
              =====================================
          """)
        dolares = float(input("Ingresa el monto en dolares:"))
        pesos= dolares * 18.5
        print(F"El monto en pesos mexicanos es: {pesos:.2f}")

    elif opcion == "3":
        print("""
              =====================================
                    saliendo del programa...
              =====================================
        """)
        condicion= False
    else:
        print("opcion invalida, intente de nuevo")
    import time
    time.sleep(2) #pausa de 2 segundos antes de limpiar pantalla
    os.system("cls" if os.name == "nt" else "clear") #limpiar pantalla


#round  es para redondear cifras decimales