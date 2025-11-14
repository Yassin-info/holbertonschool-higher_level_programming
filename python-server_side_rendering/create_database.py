#!/usr/bin/python3
"""
Script pour créer et peupler la base de données SQLite.
"""
import sqlite3


def create_database():
    """Crée et peuple la base de données products.db."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Supprimer la table si elle existe déjà
    cursor.execute('DROP TABLE IF EXISTS Products')

    # Créer la table Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insérer les données
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully!")


if __name__ == '__main__':
    create_database()
