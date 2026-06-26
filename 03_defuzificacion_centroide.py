# Valores de salida

valores = [10, 20, 30]


# Grados de pertenencia

grados = [0.2, 0.5, 0.8]


# Método del centroide

numerador = sum(
    mu * x 
    for mu, x in zip(grados, valores)
)


denominador = sum(grados)


centroide = numerador / denominador



print("Valores:")
print(valores)


print("\nGrados de pertenencia:")
print(grados)


print(
    "\nValor defuzificado (centroide):",
    f"{centroide:.2f}"
)
