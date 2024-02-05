import numpy as np
import pulp as pl


model = pl.LpProblem("Drinks_Optimization", pl.LpMaximize)

A = pl.LpVariable("Lemonade", lowBound=0, cat="Integer")
B = pl.LpVariable("Fruit_Juice", 0, cat="Integer")

model += A + B

model += 2 * A + B <= 100  # Обмеження води
model += A <= 50  # Обмеження цукру
model += A <= 30  # Обмеження лимонного соку
model += 2 * B <= 40  # Обмеження фруктового пюре

model.solve()

print("Lemonade:", pl.value(A))
print("Fruit_Juice:", pl.value(B))
print("State:", pl.LpStatus[model.status])
