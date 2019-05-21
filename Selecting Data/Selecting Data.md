# 							Selecting Data

## 1. Go to VO > Table Access Protocol (TAP) Query

## ![Screen Shot 2019-05-21 at 4.10.15 PM](Step 1.png)

## 2. Search for Gaia Data. Select ARI-Gaia (48/59), use whichever .gaia_source you need.

![Screen Shot 2019-05-21 at 4.15.38 PM](Step 2.png)

## 3. Keep Mode on Synchronous (unless it yells at you, then use asynchronous). Go to Examples > Basic > Cone Selection.

![Screen Shot 2019-05-21 at 4.20.03 PM](Step 3.png)

## 4. This is the "code" that selects data. TOP ___ designates max number of rows used, Circle() method takes parameters 'ICRS', ra, dec, angle around those coordinates. This will now generate a table with stars that fit those parameters.

 ![Screen Shot 2019-05-21 at 4.21.15 PM](Step 4.png)