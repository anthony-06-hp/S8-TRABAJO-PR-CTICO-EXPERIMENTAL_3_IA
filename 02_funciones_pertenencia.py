def triangular(x, a, b, c):

    """
    Función de pertenencia triangular.

    a = inicio de la base
    b = punto máximo (grado 1)
    c = fin de la base
    """

    if x <= a or x >= c:
        return 0

    elif a < x < b:
        return (x - a) / (b - a)

    elif b <= x < c:
        return (c - x) / (c - b)

    else:
        return 0



# Ejemplo:
# Temperatura cálida [15,25,35]

temperatura = 25


grado = triangular(
    temperatura,
    15,
    25,
    35
)


print("Temperatura:", temperatura, "°C")

print(
    "Grado de pertenencia a 'cálida':",
    f"{grado:.2f}"
)
