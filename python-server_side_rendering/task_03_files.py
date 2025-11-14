#!/usr/bin/python3
"""
Application Flask pour afficher des données depuis JSON ou CSV.
"""
from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """Route pour afficher les produits depuis JSON ou CSV."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Vérifier la source
    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               error="Wrong source")

    # Lire les données selon la source
    if source == 'json':
        products_list = read_json()
    else:  # csv
        products_list = read_csv()

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
