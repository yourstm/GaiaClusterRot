import pandas as panda
import matplotlib.pyplot as 
#find a way to make if statements for each cluster, iteraing over .csv "Cluster Names" to calculate Absolute magnitude 
# using parallax through pandas
# MAKE NEW EMPTY ARRAYS FOR EACH ABS MAG 

Hyades = panda.read_csv("Hyadesx2xPxG.csv")


plt.plot(Hyades[["rmag"]], Hyades[["Kmag"]], marker = "v", markersize = 1, color = "red", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("r-K")

plt.ylim(22.5, 5)
plt.show()

