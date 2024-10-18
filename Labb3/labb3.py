import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("unlabelled_data.csv")
data.columns = data.columns.str.replace("-1.885907518189583", "x_values").str.replace("-1.997407599218205","y_values")
x = np.array([-4, 4])
y = np.array ([-4, 4])
plt.plot(x, y)


data["noll_ett"] = data["x_values"]
for x in data.index:
    if data.loc[x, "y_values"] > data.loc[x, "x_values"]:
        data["noll_ett"] = data["noll_ett"].replace(data.loc[x, "noll_ett"], 0)
    else: 
        data["noll_ett"] = data["noll_ett"].replace(data.loc[x, "noll_ett"], 1)

data.to_csv("labelled_data.csv", index = False)

noll = data[data["noll_ett"] == 1]
ett = data[data["noll_ett"] == 0]   

plt.scatter(noll["x_values"], noll["y_values"], color = "blue")
plt.scatter(ett["x_values"], ett["y_values"], color = "orange")
plt.title("Unlabelled data")
plt.xlabel("Column 1")
plt.ylabel("column 2")
plt.grid(True)
plt.show()
plt.show()





