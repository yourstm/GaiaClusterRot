
import pandas as panda
import matplotlib.pyplot as plt

NGC752 = panda.read_csv("NGC752x2xPxG.csv")

NGC752 = NGC752.dropna(axis=0, subset=['rmag'])

plt.plot(NGC752[["r-K"]], NGC752[["Kmag"]], marker = "v", markersize = 1, color = "green", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(20, 5)
plt.show()
