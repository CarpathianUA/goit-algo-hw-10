import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

# Метод Монте-Карло
Ns = [10000, 12000, 15000]
monte_carlo_results = {}

for N in Ns:
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, max(y), N)
    below_curve = y_random < f(x_random)  # Точки під кривою

    # Обчислення інтеграла методом Монте-Карло
    monte_carlo_result = np.sum(below_curve) / N * (b - a) * max(y)

    monte_carlo_results[N] = monte_carlo_result


fig, ax = plt.subplots()

ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Додавання випадкових точок
ax.scatter(x_random, y_random, color="red", marker=".", alpha=0.1)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(
    "Графік інтегрування f(x) = x^2 від "
    + str(a)
    + " до "
    + str(b)
    + "\nМетод Монте-Карло"
)
plt.grid()
plt.show()

print(
    f"Інтеграл методом квадратур: {result}, Інтеграл методом Монте-Карло: {monte_carlo_results}"
)
