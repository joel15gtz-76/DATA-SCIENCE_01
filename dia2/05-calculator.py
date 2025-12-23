while True:
   print("MINI CALCULADORA")
   numero_1=int(input("Ingrese el primer numero:"))
   numero_2=int(input(" Ingrese el segundo numero :"))
   operacion=input("¿que operacion desea realizar?(suma, resta, multiplicacion, division):")

   if operacion=="suma":
         resultado= int(numero_1)+int(numero_2)
   elif operacion=="resta":
            resultado=int(numero_1)- int(numero_2)
   elif operacion=="multiplicacion":
            resultado=int(numero_1)*int(numero_2)
   elif operacion=="division":
            resultado=int(numero_1)/int(numero_2)
   else:
    print("operacion incorrecta")
    continue
   print(f"El resultado es: {resultado}")


   #print(f"El resultado es: {resultado}")