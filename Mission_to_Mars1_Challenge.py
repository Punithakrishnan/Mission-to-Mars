#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[7]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[9]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[10]:


slide_elem.find('div', class_='content_title')


# In[11]:


# Use the parent element to find the first `a` tag and save it as `news_title` --(only need text)
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[12]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[13]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[14]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[15]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[16]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[17]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[18]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[19]:


df.to_html()


# In[20]:


#to end the seeion of automated browising:

#browser.quit()


# In[21]:


#D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
#Hemispheres


# In[22]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[23]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range(4):
    browser.find_by_tag('h3')[i].click()
    element = browser.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    dict = {'img_url': img_url, 'title': title}
    print(img_url, title)
    hemisphere_image_urls.append(dict)
    browser.back()


# In[24]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[25]:


# 5. Quit the browser
browser.quit()


# In[ ]:




