#!/usr/bin/python3
"""
Application Flask pour afficher des données depuis JSON, CSV ou SQLite.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(filename='products.json'):
    """Lit les données depuis un fichier JSON."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def read_csv(filename='products.csv'):
    """Lit les données depuis un fichier CSV."""
    products = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertir l'id en int et le price en float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        return []
    except (ValueError, KeyError):
        return []
    return products


def read_sql(database='products.db'):
    """Lit les données depuis une base SQLite."""
    products = []
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })

        conn.close()
    except sqlite3.Error:
        return []
    return products


@app.route('/products')
def products():
    """Route pour afficher les produits depuis JSON, CSV ou SQL."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Vérifier la source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               error="Wrong source")

    # Lire les données selon la source
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:  # sql
        products_list = read_sql()

    # Filtrer par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)
            products_list = [p for p in products_list if p['id'] == product_id]
            if not products_list:
                return render_template('product_display.html',
                                       error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html',
                           products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
