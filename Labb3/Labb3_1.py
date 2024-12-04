import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Läs in filen och sätt kolumnnamn
data = pd.read_csv("unlabelled_data.csv", names=["x_values", "y_values"], header=None)

# Förbereda data för att hitta linjär regression
X = data["x_values"].values
y = data["y_values"].values

# Beräkna linjens lutning och intercept med minstakvadratsmetoden
n = len(X)
sum_x = np.sum(X)
sum_y = np.sum(y)
sum_xy = np.sum(X * y)
sum_x2 = np.sum(X**2)

# Beräkna lutning och intercept
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

# Skapa linjen för att separera klustren
x_line = np.array([-4, 4]) 
y_line = m * x_line + b     

# Plotta linjen
plt.plot(x_line, y_line, color="green", label="Separationslinje")

# Lägg till den etiketterade kolumnen "noll_ett"
data["noll_ett"] = np.where(data["y_values"] > data["x_values"], 0, 1)

# Spara den etiketterade filen
data.to_csv("labelled_data.csv", index=False)

# Dela upp data i de två klustren baserat på "noll_ett" kolumnen
noll = data[data["noll_ett"] == 1]
ett = data[data["noll_ett"] == 0]

# Plotta data
plt.scatter(noll["x_values"], noll["y_values"], color="blue", label="Cluster 1")
plt.scatter(ett["x_values"], ett["y_values"], color="orange", label="Cluster 2")
plt.title("Unlabelled data with separation line")
plt.xlabel("Column 1")
plt.ylabel("Column 2")
plt.grid(True)
plt.legend()
plt.show()
