import pandas as panda
import matplotlib.pyplot as plt

Hyades = panda.read_csv("Hyadesx2xPxG.csv")

Hyades = Hyades.dropna(axis=0, subset=['rmag'])

plt.plot(Hyades[["r-K"]], Hyades[["Kmag"]], marker = "v", markersize = 1, color = "red", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")
plt.ylim(20, 0)
plt.show()

