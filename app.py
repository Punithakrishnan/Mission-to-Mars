from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping  # the self created python file

# To remove an encountered error
app = Flask(__name__, template_folder='Templates')

# config MongoDB URI with flask app
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app' #mars_app is DataBase name (=db)
# set up mongodb connection
mongo = PyMongo(app)

# --------------------------------------------------------
# set up flask app route of homepage(root)
@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars)

# ---------------------------------------------------------
# set up scraping route
# step_1: access the database, 
# step_2: scrape newly scraped data using  'scrape_mars.py' script, 
# step_3: update the database, and return a message when successful
@app.route('/scrape')
def scrape():
    mars = mongo.db.mars 
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert = True)
    return render_template('index2.html', mars = mars)

# run flask app using terminal
if __name__ == '__main__':
    app.run()   # run on local development server