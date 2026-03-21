"""Spin up a flask server"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/items')
def items_page():
    """ Read items from JSON """
    with open('items.json', 'r', encoding="utf-8") as f:
        data = json.load(f)

    items = data.get("items", [])
    return render_template('items.html', items=items)

@app.route('/products')
def products_page():
    """The product page"""
    source = request.args.get('source')
    id_param = request.args.get('id', type=int)

    error = None
    products = []

    # Check source
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        error = "Wrong source"

    # Filter by id if provided
    if not error and id_param is not None:
        products = [p for p in products if p['id'] == id_param]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

# --- Utility functions ---

def read_json(file_path):
    """Read a json"""
    with open(file_path, 'r', encoding="utf-8") as f:
        return json.load(f)

def read_csv(file_path):
    """read the csv"""
    products = []
    with open(file_path, 'r', newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # convert types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
