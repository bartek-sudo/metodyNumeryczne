import numpy as np

# Węzły aproksymacji
nodes = np.array([[0, 4], [3, 5], [6, 4], [9, 1], [12, 2]])

# Rozdzielenie węzłów na x i y
x = nodes[:, 0]
y = nodes[:, 1]

# Tworzenie macierzy Vandermonde'a
V = np.vander(x, 4)  # Stopień wielomianu + 1 = 4

# Obliczanie współczynników wielomianu aproksymacyjnego
coefficients = np.linalg.lstsq(V, y, rcond=None)[0]

# Wyświetlanie wyników
print("Współczynniki wielomianu aproksymacyjnego:")
print(coefficients)

# Funkcja aproksymująca
def polynomial_approximation(x, coefficients):
    return np.polyval(coefficients[::-1], x)

# Testowanie dla jakichś wartości x
test_x = np.linspace(0, 12, 100)
approx_y = polynomial_approximation(test_x, coefficients)

# Wykres wynikowy
import matplotlib.pyplot as plt
plt.plot(x, y, 'ro', label='Węzły aproksymacji')
plt.plot(test_x, approx_y, label='Wielomian aproksymacyjny')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja wielomianowa')
plt.legend()
plt.grid(True)
plt.show()
