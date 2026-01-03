import os

usuarios = {
    '788383838': {
        'nombre': 'Juan',
        'correo': 'juan@correo.com'
    }
}

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    limpiar()
    print("""
    ===============================
        GESTIÓN DE USUARIOS
    ===============================
      [1] Agregar usuario
      [2] Mostrar usuarios
      [3] Actualizar usuario
      [4] Eliminar usuario
      [5] Salir
    """)

    try:
        opcion = int(input("Elija una opción: "))
    except ValueError:
        input("Opción inválida. ENTER para continuar...")
        continue

    # AGREGAR
    if opcion == 1:
        limpiar()
        print("=== AGREGAR USUARIO ===")
        dni = input("DNI: ")

        if dni in usuarios:
            input("El usuario ya existe. ENTER para continuar...")
            continue

        nombre = input("Nombre: ")
        correo = input("Correo: ")

        usuarios[dni] = {
            'nombre': nombre,
            'correo': correo
        }

        input("Usuario agregado exitosamente. ENTER para continuar...")

    # MOSTRAR
    elif opcion == 2:
        limpiar()
        print("=== LISTA DE USUARIOS ===\n")

        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            for dni, usuario in usuarios.items():
                print(f"DNI: {dni}")
                print(f"Nombre: {usuario['nombre']}")
                print(f"Correo: {usuario['correo']}")
                print("-" * 30)

        input("\nENTER para continuar...")

    # ACTUALIZAR
    elif opcion == 3:
        limpiar()
        print("=== ACTUALIZAR USUARIO ===")
        dni = input("DNI del usuario: ")

        if dni not in usuarios:
            input("Usuario no encontrado. ENTER para continuar...")
            continue

        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")

        usuarios[dni]['nombre'] = nombre
        usuarios[dni]['correo'] = correo

        input("Usuario actualizado exitosamente. ENTER para continuar...")

    # ELIMINAR
    elif opcion == 4:
        limpiar()
        print("=== ELIMINAR USUARIO ===")
        dni = input("DNI del usuario: ")

        if dni not in usuarios:
            input("Usuario no encontrado. ENTER para continuar...")
            continue

        usuarios.pop(dni)
        input("Usuario eliminado exitosamente. ENTER para continuar...")

    # SALIR
    elif opcion == 5:
        limpiar()
        print("Saliendo del programa...")
        break

    # OPCIÓN INVÁLIDA
    else:
        input("Opción inválida. ENTER para continuar...")
