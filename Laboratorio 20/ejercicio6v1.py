def normalizar(lista, modo):
    if modo not in ("minmax", "zscore", "unit"):
        raise ValueError("Modo inválido. Usa: 'minmax', 'zscore' o 'unit'.")

    valores = lista[:] 

    if modo == "minmax":
        minimo = min(valores)
        maximo = max(valores)
        rango = maximo - minimo

        if rango == 0:
            return [0 for _ in valores] 

        return [(x - minimo) / rango for x in valores]

    elif modo == "zscore":
        n = len(valores)
        media = sum(valores) / n
        var = sum((x - media) ** 2 for x in valores) / n
        desviacion = var ** 0.5

        if desviacion == 0:
            return [0 for _ in valores]

        return [(x - media) / desviacion for x in valores]

    elif modo == "unit":
        norma = sum(x**2 for x in valores) ** 0.5

        if norma == 0:
            return [0 for _ in valores]

        return [x / norma for x in valores]


valores = [10, 20, 30]

print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print("Original:", valores)