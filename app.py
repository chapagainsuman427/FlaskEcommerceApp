from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# MongoDB URI from environment variable
MONGODB_URI = os.getenv("MONGODB_URI")

# MongoDB connection
client = MongoClient(MONGODB_URI)
db = client['shop_db']
products_collection = db['products']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
