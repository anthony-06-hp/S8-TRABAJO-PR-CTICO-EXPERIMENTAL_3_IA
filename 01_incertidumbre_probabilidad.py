import random

# Simular 10 tiradas de un dado
tiradas = [random.randint(1, 6) for _ in range(10)]

print("Tiradas del dado:")
print(tiradas)


# Calcular probabilidad de obtener un número mayor a 4

exitos = sum(1 for t in tiradas if t > 4)

probabilidad = exitos / len(tiradas)


print("\nCantidad de veces que salió un número mayor a 4:")
print(exitos)


print("\nProbabilidad estimada:")
print(f"{probabilidad:.2f}")
