import math


def f(x):
    """
    Definicja funkcji równania nieliniowego: sin(x) - x.
    """
    return math.sin(x) - x


def f_prime(x):
    """
    Pochodna funkcji równania nieliniowego: sin(x) - x.
    """
    return math.cos(x) - 1


def newton_raphson_method(f, f_prime, initial_guess, tolerance):
    """
    Metoda Newtona-Raphsona do znajdowania pierwiastka funkcji f.

    :param f: funkcja równania nieliniowego
    :param f_prime: pochodna funkcji równania nieliniowego
    :param initial_guess: przybliżone miejsce początkowe
    :param tolerance: dokładność poszukiwań
    :return: przybliżona wartość pierwiastka
    """
    x = initial_guess
    while abs(f(x)) > tolerance:
        x = x - f(x) / f_prime(x)
    return x


# Przedział startowy i dokładność
initial_guess = 1  # Początkowe przybliżenie pierwiastka
tolerance = 0.01  # Dokładność

# Znalezienie pierwiastka
root = newton_raphson_method(f, f_prime, initial_guess, tolerance)
print("Dodatni pierwiastek równania sin(x) - x = 0 z dokładnością E =", tolerance, "to:", root)
