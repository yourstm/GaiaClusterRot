import matplotlib.pyplot as plt
Total = open("AllClustersX-Match")
Total_K_Mag = []
Total_r_Mag = []
firstLine = True

for aLine in Total:
	entries = aLine.split(",")
	if (firstLine):
		firstLine = False
		continue
	else:
		print(Total_r_Mag)
		print(Total_K_Mag)
		Total_K_Mag.append(entries[37])
		Total_r_Mag.append(entries[35])
		


plt.plot(Total_K_Mag, Total_r_Mag, marker = "o", markersize = "1", color = "red", linestyle = "none")


# use pandas data frame to load in the tables using data frames for arguments
# astro pi to read in tables
#