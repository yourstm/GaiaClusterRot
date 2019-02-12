# Crossmatch Using TopCAT

1. In TopCAT, open position file for the given Star Cluster. Make sure the Format is ASCII.

   - These opened files are just plain text files with two columns: RA (Right Ascension) and DEC (Declination)

     <!--Example file will be for the Hyades Cluster-->

!["Open"]("Open".png)

2. Now that the file we opened is in our "Tables List", we can crossmatch it. Select the table we opened, and in the menu bar of TopCAT go to Joins > CDS Upload X-Match.

   !["Crossmatch"]("Crossmatch".png)

3. This window is for selecting which catalog and parameters you'd like to crossmatch against. 

   I. Select whichever catalog you need. This example will use the 2MASS data release.

   II. Select the table you are crossmatching against. 

   III. I am using a radius of 3.0 arcseconds to get more ideal results. 

   IV. Go!

   !["Select Catalog"](SelectCatalog.png)

4. Double click on the new table and it has all the data you just crossmatched. 

   !["Full Table"](FullTable.png)









