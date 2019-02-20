import pandas as panda
import matplotlib.pyplot as plt

Pleiades = panda.read_csv("Pleiadesx2xPxG.csv")

Pleiades = Pleiades.dropna(axis=0, subset=['rmag'])

plt.plot(Pleiades[["r-K"]], Pleiades[["Kmag"]], marker = "v", markersize = 1, color = "black", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(20, 5)
plt.show()
