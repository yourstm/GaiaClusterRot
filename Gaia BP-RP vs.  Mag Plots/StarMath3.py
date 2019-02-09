    
import matplotlib as py
import matplotlib.pyplot as plt
import math
import numpy as np

NGC188 = open("NGC188 Complete.txt")
NGC752 = open("NGC752 Complete.txt")
NGC2682 = open("NGC2682 Complete.txt")
Hyades = open("Hyades Complete.txt")
Pleiades = open("Pleiades Complete.txt")
Praesepe = open("Praesepe Complete.txt")

# making empty lists for each cluster for their respective magnitudes and BP_RP difference

NGC752_Mag = []
NGC752_BP_RP = []

NGC188_Mag = []
NGC188_BP_RP = []

NGC2682_Mag = []
NGC2682_BP_RP = []

Hyades_Mag = []
Hyades_BP_RP = []

Pleiades_Mag = []
Pleiades_BP_RP = []

Praesepe_Mag = []
Praesepe_BP_RP = []

# This for statement checks if the line entry actually has all the required values of parallax, BP_RP, and g_mag. If it is missing
# at least one of them, it skips the value and leaves it out of the graphed data

def main():

    for aLine in NGC752:
        entries = aLine.split("|")
        if len(entries) < 4:
            continue
        else:
            parallax_ = entries[0]
            g_mag = entries[1]
            NGC752_BP_RP.append(float(entries[4]))
            magnitude(parallax(parallax_), g_mag, NGC752_Mag)


    for aLine in NGC188:
        entries = aLine.split("|")
        if len(entries) < 4:
            continue
        else:
            parallax_ = entries[0]
            g_mag = entries[1]
            NGC188_BP_RP.append(float(entries[4]))
            magnitude(parallax(float(parallax_)), float(g_mag), NGC188_Mag)

    for aLine in NGC2682:
        entries = aLine.split("|")
        if len(entries) < 4:
            continue
        else:
            parallax_ = entries[0]
            g_mag = entries[1]
            NGC2682_BP_RP.append(float(entries[4]))
            magnitude(parallax(parallax_), g_mag, NGC2682_Mag)

    for aLine in Hyades:
        entries = aLine.split("|")
        if len(entries) < 4:
            continue
        else:
            parallax_ = entries[0]
            g_mag = entries[1]
            Hyades_BP_RP.append(float(entries[4]))
            magnitude(parallax(float(parallax_)), float(g_mag), Hyades_Mag)

    for aLine in Pleiades:
        entries = aLine.split("|")
        if len(entries) < 4:
            continue
        else:
            parallax_ = entries[0]
            g_mag = entries[1]
            Pleiades_BP_RP.append(float(entries[4]))
            magnitude(parallax(parallax_), g_mag, Pleiades_Mag)

    for aLine in Praesepe:
        entries = aLine.split("|")
        if len(entries) < 4:
            continue
        else:
            parallax_ = entries[0]
            g_mag = entries[1]
            Praesepe_BP_RP.append(float(entries[4]))
            magnitude(parallax(parallax_), g_mag, Praesepe_Mag)


def parallax(x):
    par = float(x)*float(10**(-3))
    return float(par)

# if parallax returned negative, i just took the positive of it.
def magnitude(par, g_mag, listOfMag):
    if (par < 0): 
        par = par * (-1)
    if par == 0:
        listOfMag.append(0)
    Mv = float(g_mag) - ((5*(math.log10(float(1/par)))) + 5)
    listOfMag.append(Mv)
    
main()



plt.plot(Hyades_BP_RP, Hyades_Mag, marker = "v", markersize = 2, color = "red", linestyle = "none")
plt.plot(NGC752_BP_RP, NGC752_Mag, marker = "o", markersize = 2, color = "green", linestyle = "none")
plt.plot(NGC2682_BP_RP, NGC2682_Mag, marker = "+", markersize = 2, color = "y", linestyle = "none")
plt.plot(NGC188_BP_RP, NGC188_Mag, marker = "x", markersize = 2, color = "blue", linestyle = "none")
plt.plot(Pleiades_BP_RP, Pleiades_Mag, marker = "v", markersize = 2, color = "k", linestyle = "none")
plt.plot(Praesepe_BP_RP, Praesepe_Mag, marker = "o", markersize = 2, color = "c", linestyle = "none")
plt.xlabel("BP-RP")
plt.xlim([-1, 4.5])


plt.ylabel("Mag")
plt.ylim([15, -20])

plt.show()

