# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
import pandas as pd
import numpy as np
df = pd.read_csv("plantillas/registro_experimento.csv")
print(df.head())

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
print(df.groupby("ubicacion")["ventas_producto"].mean())

# TODO 3: imprime el número de registros por grupo (value_counts)
print(df["ubicacion"].value_counts())
# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis


#Diseño del Experimento
tiendas = {"Quito Norte","Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
            "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja", "Machala"}

semanas = {1, 2, 3, 4}
rng = np.random.default_rng(1234597)
primera = rng.choise(["pasillo_principal","habitual"], size = len(tiendas))
filas = []

for tiendas, cond in zip(tiendas, primera)
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    