import pandas as panda
import matplotlib.pyplot as plt

Kepler = panda.read_csv("../McQuillan/keplerMcQuillan.csv")

Kepler = Kepler[(Kepler.phot_g_mean_flux_over_error >= 50) & (Kepler.phot_rp_mean_flux_over_error >= 20) & (Kepler.phot_bp_mean_flux_over_error >= 20)]

plt.plot(Kepler[["bp_rp"]], Kepler[["abs_gmag"]], marker = "v", markersize = 0.5, color = "green", linestyle = "none", label = "Kepler")
plt.ylabel("absolute gmag")
plt.xlabel("bp_rp")
plt.ylim(17, 6)
plt.show()
