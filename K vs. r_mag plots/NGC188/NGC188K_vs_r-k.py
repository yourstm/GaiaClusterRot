import pandas as panda
import matplotlib.pyplot as plt

NGC188 = panda.read_csv("NGC188x2xPxG.csv")

NGC188 = NGC188.dropna(axis=0, subset=['rmag'])


plt.plot(NGC188[["r-K"]], NGC188[["Kmag"]], marker = "v", markersize = 1, color = "blue", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(20, 5)
plt.show()
