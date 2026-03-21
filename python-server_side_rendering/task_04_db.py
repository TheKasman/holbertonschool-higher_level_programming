"""Spin up a flask server"""
import json
import csv
import sqlite3
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
    source = (request.args.get('source') or "").lower()
    id_param = request.args.get('id', type=int)

    error = None
    products = []

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sqlite('products.db')
        if products is None:
            error = "Database error"
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

def read_sqlite(file_path):
    """What it says on the tin"""
    products = []
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for r in rows:
            products.append({
                'id': r[0],
                'name': r[1],
                'category': r[2],
                'price': r[3]
            })
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")
        return None
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
