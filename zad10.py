def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Dane wejściowe - współrzędne węzłów
x = [1, 2, 3]
y = [5, 7, 6]

# Wartość w punkcie xi, dla którego chcemy znaleźć wartość interpolowaną
xi = 2.5

result_lagrange = lagrange_interpolation(x, y, xi)
print("Interpolacja Lagrange'a dla x =", xi, "to:", result_lagrange)
