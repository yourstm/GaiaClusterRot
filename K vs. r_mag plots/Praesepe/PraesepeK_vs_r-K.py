import pandas as panda
import matplotlib.pyplot as plt

Praesepe = panda.read_csv("Praesepex2xPxG.csv")

Praesepe = Praesepe.dropna(axis=0, subset=['rmag'])

plt.plot(Praesepe[["r-K"]], Praesepe[["Kmag"]], marker = "v", markersize = 1, color = "orange", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(20, 5)
plt.show()
