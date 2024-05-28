def f(x):
    """
    Definicja funkcji równania nieliniowego: x^3 + x^2 - 3x - 3.
    """
    return x ** 3 + x ** 2 - 3 * x - 3


def secant_method(f, a, b, tolerance):
    """
    Metoda siecznych do znajdowania pierwiastka funkcji f w przedziale [a, b] z dokładnością tolerance.

    :param f: funkcja równania nieliniowego
    :param a: lewa granica przedziału
    :param b: prawa granica przedziału
    :param tolerance: dokładność poszukiwań
    :return: przybliżona wartość pierwiastka
    """
    while True:
        c = b - f(b) * (b - a) / (f(b) - f(a))
        if abs(c - b) < tolerance:
            return c
        a, b = b, c


# Przedział [1, 2] i dokładność E = 0.0001
a = 1
b = 2
tolerance = 0.0001

# Znalezienie pierwiastka
root = secant_method(f, a, b, tolerance)
print("Pierwiastek równania x^3 + x^2 - 3x - 3 = 0 w przedziale [1, 2] z dokładnością E =", tolerance, "to:", root)
