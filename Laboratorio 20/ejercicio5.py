def pedir_entero(minimo=3):
    print("=" * 25)
    print("GENERAR MATRIZ NXN")
    print("=" * 25)
    while True:
        try:
            n = int(input(f"Ingrese un número entero mayor o igual a {minimo}: "))
            if n >= minimo:
                return n
            else:
                print("Error: El número debe ser mayor o igual a", minimo)
        except ValueError:
            print("Error: Debe ingresar un entero válido")

def generar_espiral(n):
    matriz = [[0] * n for _ in range(n)]
    numero_actual = 1
    limite_superior = 0
    limite_inferior = n - 1
    limite_izquierdo = 0
    limite_derecho = n - 1
    
    while limite_izquierdo <= limite_derecho and limite_superior <= limite_inferior:
        for columna in range(limite_izquierdo, limite_derecho + 1):
            matriz[limite_superior][columna] = numero_actual
            numero_actual += 1
        limite_superior += 1

        for fila in range(limite_superior, limite_inferior + 1):
            matriz[fila][limite_derecho] = numero_actual
            numero_actual += 1
        limite_derecho -= 1
        
        if limite_superior <= limite_inferior:
            for columna in range(limite_derecho, limite_izquierdo - 1, -1):
                matriz[limite_inferior][columna] = numero_actual
                numero_actual += 1
            limite_inferior -= 1
        
        if limite_izquierdo <= limite_derecho:
            for fila in range(limite_inferior, limite_superior - 1, -1):
                matriz[fila][limite_izquierdo] = numero_actual
                numero_actual += 1
            limite_izquierdo += 1

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{numero:3d}" for numero in fila))

n = pedir_entero()
matriz_espiral = generar_espiral(n)
imprimir_matriz(matriz_espiral)