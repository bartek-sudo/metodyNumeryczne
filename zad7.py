import math

def func(x):
    return math.sqrt(1 + x)

def trapezoidal_rule(func, a, b, h):
    n = int((b - a) / h)  # liczba podprzedziałów
    integral = 0.5 * (func(a) + func(b))  # obszar pierwszego i ostatniego trapezu
    for i in range(1, n):
        x_i = a + i * h
        integral += func(x_i)  # dodawanie obszarów trapezów wewnątrz przedziału
    integral *= h
    return integral

a = 0  # początek przedziału
b = 1  # koniec przedziału
h = 1/3  # krok
result = trapezoidal_rule(func, a, b, h)
print("Przybliżona wartość całki:", result)
