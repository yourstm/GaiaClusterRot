import pandas as panda
import matplotlib.pyplot as plt

NGC2682 = panda.read_csv("NGC2682x2xPxG.csv")

NGC2682 = NGC2682.dropna(axis=0, subset=['rmag'])

plt.plot(NGC2682[["r-K"]], NGC2682[["Kmag"]], marker = "v", markersize = 1, color = "purple", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(20, 5)
plt.show()
