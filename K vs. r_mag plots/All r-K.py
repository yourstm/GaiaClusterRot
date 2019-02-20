import pandas as panda
import matplotlib.pyplot as plt


#Add new column to CSV file to calculate Absolute Kmag. The graph is of Absolute Kmag vs. r-K. equation here:
# def magnitude(par, g_mag, listOfMag):
#     if (par < 0): 
#         par = par * (-1)
#     if par == 0:
#         listOfMag.append(0)
#     Mv = float(g_mag) - ((5*(math.log10(float(1/par)))) + 5)
#     listOfMag.append(Mv)


Hyades = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/Hyades/Hyadesx2xPxG.csv")
Praesepe = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/Praesepe/Praesepex2xPxG.csv")
Pleiades = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/Pleiades/Pleiadesx2xPxG.csv")
NGC2682 = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/NGC2682/NGC2682x2xPxG.csv")
NGC752 = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/NGC752/NGC752x2xPxG.csv")
NGC188 = panda.read_csv("/Users/mitchy/Desktop/School/Astro 316 Covey/GaiaClusterRot/K vs. r_mag plots/NGC188/NGC188x2xPxG.csv")

Pleiades = Pleiades.dropna(axis=0, subset=['rmag'])
Hyades = Hyades.dropna(axis=0, subset=['rmag'])
Praesepe = Praesepe.dropna(axis=0, subset=['rmag'])
NGC2682 = NGC2682.dropna(axis=0, subset=['rmag'])
NGC752 = NGC752.dropna(axis=0, subset=['rmag'])
NGC188 = NGC188.dropna(axis=0, subset=['rmag'])


plt.plot(NGC188[["r-K"]], NGC188[["Kmag"]], marker = "v", markersize = 1, color = "blue", linestyle = "none")
plt.plot(NGC752[["r-K"]], NGC752[["Kmag"]], marker = "v", markersize = 1, color = "green", linestyle = "none")
plt.plot(NGC2682[["r-K"]], NGC2682[["Kmag"]], marker = "v", markersize = 1, color = "purple", linestyle = "none")
plt.plot(Praesepe[["r-K"]], Praesepe[["Kmag"]], marker = "v", markersize = 1, color = "orange", linestyle = "none")
plt.plot(Pleiades[["r-K"]], Pleiades[["Kmag"]], marker = "v", markersize = 1, color = "black", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(20, 5)
plt.show()
