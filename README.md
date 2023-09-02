# Furniest: a furniture assistance solution
-----------------------------------------------

##### Authors:
##### Muhammad Asghar masghar@andrew.cmu.edu 
##### Edvin Handoko ehandoko@andrew.cmu.edu 
##### Sahithya Senthilkumar sahithys@andrew.cmu.edu 
##### Saba Zaheer szaheer@andrew.cmu.edu
<br/>

We provided scrapped data from the following websites AptDeco, Craigslist, RealSimple, Etsy, and YellowPages with recommendations based on location and price. You can also provide a zipcode to get the nearest UHaul locations.
<br/>

Users can view both new and second hand furniture and compare. Links will be provided if you choose to purchase. 
<br/>

Pre-scraped CSV results are provided. You will be prompted if you want to use that or compile new data. 
<br/>

## HOW TO RUN: 
<br/>

You will have to pip install the following packages: `folium`, `geopy`, `apify`, `apify-client`, `seaborn`.

Download or clone the marketplace repo. In terminal or command line, navigate to the root directory of marketplace folder.
<br/>

Run `python3 __main__.py`.
<br/>

Everything is interfaced via the command line with simple prompts.
<br/>

If you are using a Mac the visualizations do not open automatically for some reason, but the .html file should be generated in your directory. On Windows, this is not an issue.
<br/>

You can now enter a product you are interested in purchasing (e.g. couches, tables, chairs, etc.) and results will be displayed. 
