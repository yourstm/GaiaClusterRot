import pandas as panda
import matplotlib.pyplot as plt
#find a way to make if statements for each cluster, iteraing over .csv "Cluster Names" to calculate Absolute magnitude 
# using parallax through pandas
# MAKE NEW EMPTY ARRAYS FOR EACH ABS MAG 
df1 = panda.read_csv("Hyadesx2xPxG.csv")


plt.plot(df1[["rmag"]], df1[["Kmag"]], marker = "v", markersize = 1, color = "red", linestyle = "none")

plt.ylabel("Kmag")
plt.xlabel("rmag")

plt.ylim(22.5, 5)
plt.show()

