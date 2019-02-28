import pandas as panda
import matplotlib.pyplot as plt

# Loading each CSV into a dataframe to read from
Hyades = panda.read_csv("../Hyades/Hyadesx2xPxG.csv")
Praesepe = panda.read_csv("../Praesepe/Praesepex2xPxG.csv")
Pleiades = panda.read_csv("../Pleiades/Pleiadesx2xPxG.csv")
NGC2682 = panda.read_csv("../NGC2682/NGC2682x2xPxG.csv")
NGC752 = panda.read_csv("../NGC752/NGC752x2xPxG.csv")
NGC188 = panda.read_csv("../NGC188/NGC188x2xPxG.csv")

# Dropping rows that depend on rmag whose rmag values dont exist
Pleiades = Pleiades.dropna(axis=0, subset=['rmag'])
Hyades = Hyades.dropna(axis=0, subset=['rmag'])
Praesepe = Praesepe.dropna(axis=0, subset=['rmag'])
NGC2682 = NGC2682.dropna(axis=0, subset=['rmag'])
NGC752 = NGC752.dropna(axis=0, subset=['rmag'])
NGC188 = NGC188.dropna(axis=0, subset=['rmag'])

#Removing points with error in parallax, rmag, and Gmag thats more than 0.1
Hyades = Hyades[(Hyades.parallax_error <= 0.1) & (Hyades.e_rmag <= 0.1) & (Hyades.e_gmag <= 0.1)]
NGC188 = NGC188[(NGC188.parallax_error <= 0.1) & (NGC188.e_rmag <= 0.1) & (NGC188.e_gmag <= 0.1)]
NGC752 = NGC752[(NGC752.parallax_error <= 0.1) & (NGC752.e_rmag <= 0.1) & (NGC752.e_gmag <= 0.1)]
NGC2682 = NGC2682[(NGC2682.parallax_error <= 0.1) & (NGC2682.e_rmag <= 0.1) & (NGC2682.e_gmag <= 0.1)]
Pleiades = Pleiades[(Pleiades.parallax_error <= 0.1) & (Pleiades.e_rmag <= 0.1) & (Pleiades.e_gmag <= 0.1)]
Praesepe = Praesepe[(Praesepe.parallax_error <= 0.1) & (Praesepe.e_rmag <= 0.1) & (Praesepe.e_gmag <= 0.1)]


# Plotting
plt.plot(Hyades[["bp_rp"]], Hyades[["AbsGmag"]], marker = "v", markersize = 0.5, color = "red", linestyle = "none", label = "Hyades")
plt.plot(NGC188[["bp_rp"]], NGC188[["AbsGmag"]], marker = "v", markersize = 0.5, color = "blue", linestyle = "none", label = "NGC188")
plt.plot(NGC752[["bp_rp"]], NGC752[["AbsGmag"]], marker = "v", markersize = 0.5, color = "green", linestyle = "none", label = "NGC752")
plt.plot(NGC2682[["bp_rp"]], NGC2682[["AbsGmag"]], marker = "v", markersize = 0.5, color = "purple", linestyle = "none", label = "NGC2682")
plt.plot(Praesepe[["bp_rp"]], Praesepe[["AbsGmag"]], marker = "v", markersize = 0.5, color = "orange", linestyle = "none", label = "Praesepe")
plt.plot(Pleiades[["bp_rp"]], Pleiades[["AbsGmag"]], marker = "v", markersize = 0.5, color = "black", linestyle = "none", label = "Pleiades")

plt.ylabel("Absolute Gmag")
plt.xlabel("bp_rp")
plt.legend(markerscale = 8)
plt.ylim(25, 5)
plt.show()
