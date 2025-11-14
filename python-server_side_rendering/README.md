# Python - Server-Side Rendering

Ce projet explore le rendu côté serveur (SSR) en utilisant Python et Flask avec le moteur de templates Jinja.

## Description

Le projet couvre les concepts suivants :
- Templating avec Python
- Création d'applications Flask
- Utilisation de Jinja pour générer du HTML dynamique
- Lecture de données depuis JSON, CSV et SQLite
- Gestion de contenu dynamique

## Structure du projet

```
python-server_side_rendering/
├── task_00_intro.py          # Génération d'invitations personnalisées
├── task_01_jinja.py          # Application Flask de base
├── task_02_logic.py          # Templates avec boucles et conditions
├── task_03_files.py          # Lecture de données JSON/CSV
├── task_04_db.py             # Lecture de données SQLite
├── create_database.py        # Script pour créer la base de données
├── template.txt              # Template pour les invitations
├── items.json                # Données pour task_02
├── products.json             # Données JSON pour task_03/04
├── products.csv              # Données CSV pour task_03/04
└── templates/                # Dossier des templates HTML
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
```

## Installation

1. Installer Flask :
```bash
pip install Flask
```

2. Créer la base de données (pour task_04) :
```bash
python3 create_database.py
```

## Utilisation

### Task 0 - Templating simple
```bash
python3 task_00_intro.py
```

### Task 1 - Application Flask de base
```bash
python3 task_01_jinja.py
```
Puis visiter : http://localhost:5000, http://localhost:5000/about, http://localhost:5000/contact

### Task 2 - Templates dynamiques
```bash
python3 task_02_logic.py
```
Puis visiter : http://localhost:5000/items

### Task 3 - Données JSON/CSV
```bash
python3 task_03_files.py
```
Puis visiter :
- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=json&id=1

### Task 4 - Base de données SQLite
```bash
python3 task_04_db.py
```
Puis visiter :
- http://localhost:5000/products?source=sql
- http://localhost:5000/products?source=sql&id=1

## Auteur

Projet Holberton School
