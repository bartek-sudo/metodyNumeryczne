def horner_scheme(coefficients, x):

    n = len(coefficients) - 1
    result = coefficients[n]
    for i in range(n - 1, -1, -1):
        result = result * x + coefficients[i]
    return result


# Przykład użycia
coefficients = [2, -3, 1]  # wielomian: 2x^2 - 3x + 1
x = 3
print("Wartość wielomianu dla x =", x, ":", horner_scheme(coefficients, x))
