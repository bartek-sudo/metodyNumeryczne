def divide_polynomial_by_binomial(coefficients, a):

    n = len(coefficients) - 1
    result = [coefficients[0]]  # Inicjalizacja listy wynikowej z pierwszym współczynnikiem
    for i in range(1, n):
        result.append(coefficients[i] + a * result[i - 1])
    quotient = result[-1]
    remainder = coefficients[-1] + a * quotient
    return quotient, remainder


# Przykład użycia
coefficients = [1, -3, 2]  # wielomian: x^2 - 3x + 2
a = 1  # Dzielimy przez (x - 1)
quotient, remainder = divide_polynomial_by_binomial(coefficients, a)
print("Wynik dzielenia:", quotient, "Reszta:", remainder)
