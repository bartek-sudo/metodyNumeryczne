import math

def func(x):
    return math.sin(x) * math.exp(-3*x) + x**3

def simpsons_rule(func, a, b, n):
    h = (b - a) / n  # szerokość podprzedziału
    integral = func(a) + func(b)  # wartości na krańcach przedziału
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x_i)  # wartości parzyste
        else:
            integral += 4 * func(x_i)  # wartości nieparzyste
    integral *= h / 3
    return integral

def max_error(func, a, b, n):
    h = (b - a) / n  # szerokość podprzedziału
    max_err = 0
    for i in range(n):
        x_i = a + i * h
        integral_approx = simpsons_rule(func, x_i, x_i + h, 2)
        exact_integral = simpsons_rule(func, x_i, x_i + h, 4)
        err = abs(exact_integral - integral_approx)
        if err > max_err:
            max_err = err
    return max_err

a = -3  # początek przedziału
b = 1   # koniec przedziału
n = 100 # liczba podprzedziałów

result = simpsons_rule(func, a, b, n)
max_error = max_error(func, a, b, n)

print("Przybliżona wartość całki:", result)
print("Błąd maksymalny:", max_error)
