import numpy as np

def normalizar_np(lista, modo):
    if modo not in ("minmax", "zscore", "unit"):
        raise ValueError("Modo inválido. Usa: 'minmax', 'zscore' o 'unit'.")

    x = np.array(lista, dtype=float)

    if modo == "minmax":
        minimo = x.min()
        maximo = x.max()
        rango = maximo - minimo

        if rango == 0:
            return np.zeros_like(x)

        return (x - minimo) / rango

    elif modo == "zscore":
        media = x.mean()
        desviacion = x.std()

        if desviacion == 0:
            return np.zeros_like(x)

        return (x - media) / desviacion

    elif modo == "unit":
        norma = np.linalg.norm(x)

        if norma == 0:
            return np.zeros_like(x)

        return x / norma

valores = [10, 20, 30]

print(normalizar_np(valores, "minmax"))
print(normalizar_np(valores, "zscore"))
print(normalizar_np(valores, "unit"))
print("Original:", valores)