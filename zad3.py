def bisection_method(f, a, b, tolerance):
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja nie spełnia warunków metody bisekcji na danym przedziale.")

    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2


# Funkcja równania x^3 + x - 1
def equation(x):
    return x ** 3 + x - 1


# Przedział [0, 1] z dokładnością E = 0.01
a = 0
b = 1
tolerance = 0.01

# Znalezienie pierwiastka
root = bisection_method(equation, a, b, tolerance)
print("Pierwiastek równania x^3 + x - 1 = 0 w przedziale [0, 1] z dokładnością E =", tolerance, "to:", root)
