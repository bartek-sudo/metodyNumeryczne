def f(x):
    """
    Definicja funkcji równania nieliniowego: x^3 + x^2 - 3x - 3.
    """
    return x ** 3 + x ** 2 - 3 * x - 3


def false_position_method(f, a, b, tolerance):
    """
    Metoda falsi do znajdowania pierwiastka funkcji f w przedziale [a, b] z dokładnością tolerance.

    :param f: funkcja równania nieliniowego
    :param a: lewa granica przedziału
    :param b: prawa granica przedziału
    :param tolerance: dokładność poszukiwań
    :return: przybliżona wartość pierwiastka
    """
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0 or abs(b - a) < tolerance:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c


# Przedział [1, 2] i dokładność E = 0.0001
a = 1
b = 2
tolerance = 0.0001

# Znalezienie pierwiastka
root = false_position_method(f, a, b, tolerance)
print("Rzeczywisty pierwiastek równania x^3 + x^2 - 3x - 3 = 0 w przedziale [1, 2] z dokładnością E =", tolerance,
      "to:", root)
