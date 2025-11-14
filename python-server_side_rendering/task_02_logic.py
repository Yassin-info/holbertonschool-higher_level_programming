#!/usr/bin/python3
"""
Application Flask avec templates dynamiques utilisant boucles et conditions.
"""
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    """Route pour afficher la liste des items depuis un fichier JSON."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    except json.JSONDecodeError:
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
