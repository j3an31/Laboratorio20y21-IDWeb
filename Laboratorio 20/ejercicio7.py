def agregar_estudiante(lista):
    print("\n--- Agregar estudiante ---")
    nombre = input("Nombre: ").strip()
    edad = int(input("Edad: "))
    promedio = float(input("Promedio: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    
    lista.append(estudiante)
    print("¡Estudiante agregado con éxito!\n")

def mostrar_estudiantes(lista):
    print("\n--- Lista de estudiantes ---")
    if not lista:
        print("No hay estudiantes registrados.\n")
        return
    
    for i, est in enumerate(lista, start=1):
        print(f"{i}. {est['nombre']} - {est['edad']} años - Promedio: {est['promedio']}")
    print()

def mejor_promedio(lista):
    print("\n--- Estudiante con mejor promedio ---")
    if not lista:
        print("No hay estudiantes registrados.\n")
        return
    
    mejor = max(lista, key=lambda est: est["promedio"])
    print(f"{mejor['nombre']} - {mejor['edad']} años - Promedio: {mejor['promedio']}\n")

def buscar_por_nombre(lista):
    print("\n--- Buscar estudiante por nombre ---")
    nombre = input("Nombre a buscar: ").strip()

    encontrados = [est for est in lista if est["nombre"].lower() == nombre.lower()]

    if encontrados:
        for est in encontrados:
            print(f"{est['nombre']} - {est['edad']} años - Promedio: {est['promedio']}")
    else:
        print("No se encontró un estudiante con ese nombre.")
    print()

def eliminar_por_nombre(lista):
    print("\n--- Eliminar estudiante por nombre ---")
    nombre = input("Nombre a eliminar: ").strip()

    eliminados = 0
    for est in lista[:]:  
        if est["nombre"].lower() == nombre.lower():
            lista.remove(est)
            eliminados += 1

    if eliminados > 0:
        print(f"Se eliminaron {eliminados} estudiante(s) con ese nombre.\n")
    else:
        print("No se encontró un estudiante con ese nombre.\n")

def menu():
    estudiantes = []

    while True:
        print("=" * 25)
        print("REGISTRO DE ESTUDIANTES")
        print("=" * 25)
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar estudiante con mejor promedio")
        print("4. Buscar por nombre")
        print("5. Eliminar por nombre")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            mejor_promedio(estudiantes)
        elif opcion == "4":
            buscar_por_nombre(estudiantes)
        elif opcion == "5":
            eliminar_por_nombre(estudiantes)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("¡Opción inválida! Intente otra vez\n")

menu()