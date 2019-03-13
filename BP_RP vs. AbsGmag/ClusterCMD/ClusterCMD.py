import pandas as panda
import matplotlib.pyplot as plt
import matplotlib as mp
from IPython.display import set_matplotlib_formats

# Loading each CSV into a dataframe to read from
Hyades = panda.read_csv("../Hyades/Hyadesx2xPxG.csv")
Praesepe = panda.read_csv("../Praesepe/Praesepex2xPxG.csv")
Pleiades = panda.read_csv("../Pleiades/Pleiadesx2xPxG.csv")
NGC2682 = panda.read_csv("../NGC2682/NGC2682x2xPxG.csv")
NGC752 = panda.read_csv("../NGC752/NGC752x2xPxG.csv")
NGC188 = panda.read_csv("../NGC188/NGC188x2xPxG.csv")


#Removing points with error in phot_g_mean_flux_over_error > 50, phot_rp_mean_flux_over_error>20, phot_bp_mean_flux_over_error>20
Hyades = Hyades[(Hyades.phot_g_mean_flux_over_error >= 50) & (Hyades.phot_rp_mean_flux_over_error >= 20) & (Hyades.phot_bp_mean_flux_over_error >= 20)]
NGC188 = NGC188[(NGC188.phot_g_mean_flux_over_error >= 50) & (NGC188.phot_rp_mean_flux_over_error >= 20) & (NGC188.phot_bp_mean_flux_over_error >= 20)]
NGC752 = NGC752[(NGC752.phot_g_mean_flux_over_error >= 50) & (NGC752.phot_rp_mean_flux_over_error >= 20) & (NGC752.phot_bp_mean_flux_over_error >= 20)]
NGC2682 = NGC2682[(NGC2682.phot_g_mean_flux_over_error >= 50) & (NGC2682.phot_rp_mean_flux_over_error >= 20) & (NGC2682.phot_bp_mean_flux_over_error>= 20)]
Pleiades = Pleiades[(Pleiades.phot_g_mean_flux_over_error >= 50) & (Pleiades.phot_rp_mean_flux_over_error >= 20) & (Pleiades.phot_bp_mean_flux_over_error >= 20)]
Praesepe = Praesepe[(Praesepe.phot_g_mean_flux_over_error >= 50) & (Praesepe.phot_rp_mean_flux_over_error >= 20) & (Praesepe.phot_bp_mean_flux_over_error >= 20)]

# Using Davenports image quality code:
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 200

plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = 8,6
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 14

mp.rcParams['xtick.direction'] = 'out'
mp.rcParams['ytick.direction'] = 'out'


# Plotting
plt.plot(Hyades[["bp_rp"]], Hyades[["AbsGmag"]]-6, marker = "v", markersize = 0.5, color = "red", linestyle = "none", label = "Hyades")
plt.plot(NGC188[["bp_rp"]], NGC188[["AbsGmag"]]-6, marker = "v", markersize = 0.5, color = "blue", linestyle = "none", label = "NGC188")
plt.plot(NGC752[["bp_rp"]], NGC752[["AbsGmag"]]-6, marker = "v", markersize = 0.5, color = "green", linestyle = "none", label = "NGC752")
plt.plot(NGC2682[["bp_rp"]], NGC2682[["AbsGmag"]]-6, marker = "v", markersize = 0.5, color = "purple", linestyle = "none", label = "NGC2682")
plt.plot(Praesepe[["bp_rp"]], Praesepe[["AbsGmag"]]-6, marker = "v", markersize = 0.5, color = "orange", linestyle = "none", label = "Praesepe")
plt.plot(Pleiades[["bp_rp"]], Pleiades[["AbsGmag"]]-6, marker = "v", markersize = 0.5, color = "black", linestyle = "none", label = "Pleiades")

plt.ylabel("$M_G$")
plt.xlabel("$G_{BP} - G_{RP}$")
plt.legend(markerscale = 8)
plt.xlim(-0.75, 4.25)
plt.xticks([0, 1, 2, 3, 4])
plt.ylim(16, -4)
plt.yticks([0, 5, 10])
plt.show()

