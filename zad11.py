def partial_pivot(A, b):
    n = len(A)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        if max_index != i:
            A[i], A[max_index] = A[max_index], A[i]
            b[i], b[max_index] = b[max_index], b[i]

def gauss_elimination(A, b):
    n = len(A)
    for i in range(n):
        partial_pivot(A, b)
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

def back_substitution(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i-1, -1, -1):
            b[j] -= A[j][i] * x[i]
    return x

# Macierz współczynników A i wektor prawych stron b
A = [[3, 0, 6], [1, 2, 8], [4, 5, -2]]
b = [-12, -12, 39]

# Eliminacja Gaussa
gauss_elimination(A, b)

# Rozwiązanie układu równań
solution = back_substitution(A, b)

print("Rozwiązanie układu równań:")
print(solution)

# Metoda eliminacji Gaussa:
# Podział na etapy: Algorytm eliminacji Gaussa można podzielić na kilka kroków. Na początku, macierz współczynników
# �
# A razem z wektorem prawych stron
# �
# b tworzą rozszerzoną macierz.
#
# Eliminacja współczynników: Następnie stosuje się szereg operacji elementarnych tak, aby uzyskać macierz trójkątną górną. Operacje te polegają na odejmowaniu odpowiednio przeskalowanych wierszy od innych wierszy, aby wyeliminować współczynniki pod diagonali.
#
# Rozwiązanie układu trójkątnego: Po sprowadzeniu macierzy do postaci trójkątnej, układ równań można łatwo rozwiązać wstecz, zaczynając od ostatniego równania i podstawiając znane wartości wstecz.
#
# Metoda rozkładu LU:
# Rozkład LU: Najpierw dokonuje się rozkładu macierzy współczynników
# �
# A na iloczyn dwóch macierzy: macierzy dolnej trójkątnej
# �
# L i macierzy górnej trójkątnej
# �
# U. W ten sposób otrzymuje się
# �
# =
# �
# �
# A=LU.
#
# Rozwiązanie układu równań: Następnie układ równań
# �
# �
# =
# �
# Ax=b jest równoważny układowi
# �
# �
# �
# =
# �
# LUx=b. Możemy to rozwiązać w dwóch krokach:
#
# Rozwiązujemy układ równań
# �
# �
# =
# �
# Ly=b dla
# �
# y.
# Rozwiązujemy układ równań
# �
# �
# =
# �
# Ux=y dla
# �
# x.
# Teraz przejdźmy do konkretnego przykładu, w którym wyznaczymy rozwiązanie układu równań
# �
# �
# =
# �
# Ax=b metodą eliminacji Gaussa z wyborem elementu podstawowego w kolumnie dla podanej macierzy
# �
# A i wektora
# �
# b:
#
# �
# =
# [
# 3
# 0
# 6
# 1
# 2
# 8
# 4
# 5
# −
# 2
# ]
# A=
# ⎣
# ⎡
# ​
#
# 3
# 1
# 4
# ​
#
# 0
# 2
# 5
# ​
#
# 6
# 8
# −2
# ​
#
# ⎦
# ⎤
# ​
#
#
# �
# =
# [
# −
# 12
# −
# 12
# 39
# ]
# b=
# ⎣
# ⎡
# ​
#
# −12
# −12
# 39
# ​
#
# ⎦
# ⎤
# ​
#
#
# Krok po kroku:
# Wybór elementu podstawowego: Dla każdej kolumny, wybierz element o największej wartości bezwzględnej w tej kolumnie jako element podstawowy. Zamień wiersze, jeśli element podstawowy nie znajduje się na przekątnej.
#
# Eliminacja współczynników: Dla każdego wiersza poniżej bieżącej, dokonaj eliminacji przez odejmowanie odpowiednio przeskalowanych wierszy.
#
# Rozwiązanie układu trójkątnego: Po sprowadzeniu macierzy do postaci trójkątnej, rozwiąż układ równań wstecz, zaczynając od ostatniego równania i podstawiając znane wartości wstecz.