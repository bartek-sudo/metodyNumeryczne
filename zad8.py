def func(x):
    return 0.06 * x**2 + 2

def rectangle_rule(func, a, b, n):
    h = (b - a) / n  # szerokość przedziału
    integral = 0
    for i in range(n):
        x_i = a + i * h  # lewa krawędź prostokąta
        integral += func(x_i) * h  # obszar prostokąta
    return integral

a = 0  # początek przedziału
b = 4  # koniec przedziału
n = 100  # liczba podprzedziałów
result = rectangle_rule(func, a, b, n)
print("Przybliżona wartość całki:", result)
