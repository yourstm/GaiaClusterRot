import pandas as panda
import matplotlib.pyplot as plt
#find a way to make if statements for each cluster, iteraing over .csv "Cluster Names" to calculate Absolute magnitude 
# using parallax through pandas
# MAKE NEW EMPTY ARRAYS FOR EACH ABS MAG 
main(
	df1 = panda.read_csv("AllClustersX-Match.csv")

	
	plt.plot(df1.loc[df1["Cluster Name"] == "Hyades" , "rmag"], df1.loc[df1["Cluster Name"] == "Hyades" , "Kmag"], marker = "v", markersize = 1, color = "red", linestyle = "none")
	plt.plot(df1.loc[df1["Cluster Name"] == "NGC188" , "rmag"], df1.loc[df1["Cluster Name"] == "NGC188" , "Kmag"], marker = "o", markersize = 1, color = "blue", linestyle = "none")
	plt.plot(df1.loc[df1["Cluster Name"] == "NGC752" , "rmag"], df1.loc[df1["Cluster Name"] == "NGC752" , "Kmag"], marker = "x", markersize = 1, color = "yellow", linestyle = "none")
	plt.plot(df1.loc[df1["Cluster Name"] == "NGC2682" , "rmag"], df1.loc[df1["Cluster Name"] == "NGC2682" , "Kmag"], marker = "v", markersize = 1, color = "green", linestyle = "none")
	plt.plot(df1.loc[df1["Cluster Name"] == "Pleiades" , "rmag"], df1.loc[df1["Cluster Name"] == "Pleiades" , "Kmag"], marker = "v", markersize = 1, color = "purple", linestyle = "none")
	plt.plot(df1.loc[df1["Cluster Name"] == "Praesepe" , "rmag"], df1.loc[df1["Cluster Name"] == "Praesepe" , "Kmag"], marker = "v", markersize = 1, color = "red", linestyle = "none")

	plt.ylim(22.5, 5)
	plt.show()

)

def magnitude(par, g_mag, listOfMag):
    if (par < 0): 
        par = par * (-1)
    if par == 0:
        listOfMag.append(0)
    Mv = float(g_mag) - ((5*(math.log10(float(1/par)))) + 5)
    listOfMag.append(Mv)