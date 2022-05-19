# Mission-To-Mars

### Web Scraping 

About | Web Scraping | NASA Mars News | JPL Mars Space Featured Image | Mars Facts | Mars Hemispheres | MongoDB and Flask Application | Programming Language / Applications Used | Contributors

### Overview

This project builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### Web Scraping

----

Wrote a Jupyter notebook script using BeautifulSoup, Pandas, and Requests/Splinter to scrape the data related to Mission to Mars from various websites.

#### NASA's Mars News

Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. Assigned the text to variables that can be referenced later.

#### Mars Space Featured Image

Visited the url for Featured Space Image here.
Used splinter to navigate the site and found the image url to the full size .jpg image for the current Featured Mars Image and assigned the complete url string for the image to a variable called featured_image_url.

#### Mars Facts

Visited the Mars Facts webpage here and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Used Pandas to convert the data to a HTML table string and assigned the HTML table string to a variable that can be referenced later.

#### Mars Hemispheres

Visited the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
Clicked each of the links to the hemispheres in order to find the image url to the full resolution image.
Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.
Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

---

### MongoDB and Flask Application

---
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all the scraping code from above and return one Python dictionary containing all of the scraped data.
Next, created a route called /scrape that will import scraping.py script and call scrape function.
Stored the return value in Mongo as a Python dictionary.
Created a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.
Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
Click here to view the screenshot of the webpage created.

---

### Programming Languages and Applications Tools Used

Python

BeautifulSoup

Splinter

Pandas Web Scraping

Pandas

Pymongo

Flask Application

MongoDB

Jupyter Notebook

