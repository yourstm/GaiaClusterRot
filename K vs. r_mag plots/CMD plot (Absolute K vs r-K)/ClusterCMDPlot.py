import pandas as panda
import matplotlib.pyplot as plt

# Loading each CSV into a dataframe to read from
Hyades = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/Hyades/Hyadesx2xPxG.csv")
Praesepe = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/Praesepe/Praesepex2xPxG.csv")
Pleiades = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/Pleiades/Pleiadesx2xPxG.csv")
NGC2682 = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/NGC2682/NGC2682x2xPxG.csv")
NGC752 = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/NGC752/NGC752x2xPxG.csv")
NGC188 = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/NGC188/NGC188x2xPxG.csv")

# Dropping rows that depend on rmag whose rmag values dont exist
Pleiades = Pleiades.dropna(axis=0, subset=['rmag'])
Hyades = Hyades.dropna(axis=0, subset=['rmag'])
Praesepe = Praesepe.dropna(axis=0, subset=['rmag'])
NGC2682 = NGC2682.dropna(axis=0, subset=['rmag'])
NGC752 = NGC752.dropna(axis=0, subset=['rmag'])
NGC188 = NGC188.dropna(axis=0, subset=['rmag'])

# Plotting
plt.plot(Hyades[["r-K"]], Hyades[["AbsKmag"]], marker = "v", markersize = 0.5, color = "red", linestyle = "none", label = "Hyades")
plt.plot(NGC188[["r-K"]], NGC188[["AbsKmag"]], marker = "v", markersize = 0.5, color = "blue", linestyle = "none", label = "NGC188")
plt.plot(NGC752[["r-K"]], NGC752[["AbsKmag"]], marker = "v", markersize = 0.5, color = "green", linestyle = "none", label = "NGC752")
plt.plot(NGC2682[["r-K"]], NGC2682[["AbsKmag"]], marker = "v", markersize = 0.5, color = "purple", linestyle = "none", label = "NGC2682")
plt.plot(Praesepe[["r-K"]], Praesepe[["AbsKmag"]], marker = "v", markersize = 0.5, color = "orange", linestyle = "none", label = "Praesepe")
plt.plot(Pleiades[["r-K"]], Pleiades[["AbsKmag"]], marker = "v", markersize = 0.5, color = "black", linestyle = "none", label = "Pleiades")

plt.ylabel("Absolute Kmag")
plt.xlabel("r-K")
plt.legend(markerscale = 8)
plt.ylim(20, 0)
plt.show()
