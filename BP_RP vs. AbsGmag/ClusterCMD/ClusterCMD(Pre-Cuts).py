import pandas as panda
import matplotlib.pyplot as plt

# Loading each CSV into a dataframe to read from
Hyades = panda.read_csv("../Hyades/Hyadesx2xPxG.csv")
Praesepe = panda.read_csv("../Praesepe/Praesepex2xPxG.csv")
Pleiades = panda.read_csv("../Pleiades/Pleiadesx2xPxG.csv")
NGC2682 = panda.read_csv("../NGC2682/NGC2682x2xPxG.csv")
NGC752 = panda.read_csv("../NGC752/NGC752x2xPxG.csv")
NGC188 = panda.read_csv("../NGC188/NGC188x2xPxG.csv")



# Plotting
plt.plot(Hyades[["bp_rp"]], Hyades[["AbsGmag"]], marker = "v", markersize = 0.5, color = "red", linestyle = "none", label = "Hyades")
plt.plot(NGC188[["bp_rp"]], NGC188[["AbsGmag"]], marker = "v", markersize = 0.5, color = "blue", linestyle = "none", label = "NGC188")
plt.plot(NGC752[["bp_rp"]], NGC752[["AbsGmag"]], marker = "v", markersize = 0.5, color = "green", linestyle = "none", label = "NGC752")
plt.plot(NGC2682[["bp_rp"]], NGC2682[["AbsGmag"]], marker = "v", markersize = 0.5, color = "purple", linestyle = "none", label = "NGC2682")
plt.plot(Praesepe[["bp_rp"]], Praesepe[["AbsGmag"]], marker = "v", markersize = 0.5, color = "orange", linestyle = "none", label = "Praesepe")
plt.plot(Pleiades[["bp_rp"]], Pleiades[["AbsGmag"]], marker = "v", markersize = 0.5, color = "black", linestyle = "none", label = "Pleiades")

plt.ylabel("AbsGmag")
plt.xlabel("bp_rp")
plt.legend(markerscale = 8)
plt.ylim(27, 5)
plt.show()
