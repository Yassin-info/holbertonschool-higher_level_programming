# Python - Serialization

Ce projet explore les concepts de marshaling et de sérialisation en Python.

## Description

La sérialisation est le processus de conversion de structures de données ou d'états d'objets en un format qui peut être facilement sauvegardé dans un fichier ou envoyé sur un réseau. Ce projet implémente différentes méthodes de sérialisation en Python.

## Structure du projet

```
python-serialization/
├── task_00_basic_serialization.py   # Sérialisation JSON de base
├── task_01_pickle.py                # Sérialisation avec pickle
├── task_02_csv.py                   # Conversion CSV vers JSON
├── task_03_xml.py                   # Sérialisation XML
├── main_00.py                       # Test task 0
├── main_01.py                       # Test task 1
├── main_02_csv.py                   # Test task 2
├── main_03.py                       # Test task 3
├── data.csv                         # Données CSV exemple
└── README.md
```

## Tâches

### Task 0: Basic Serialization
Sérialisation et désérialisation de base avec JSON.

**Fonctions:**
- `serialize_and_save_to_file(data, filename)` - Sérialise un dictionnaire Python en JSON
- `load_and_deserialize(filename)` - Désérialise un fichier JSON en dictionnaire Python

**Test:**
```bash
python3 main_00.py
```

### Task 1: Pickling Custom Classes
Sérialisation d'objets personnalisés avec le module pickle.

**Classe CustomObject:**
- Attributs: `name`, `age`, `is_student`
- Méthodes:
  - `display()` - Affiche les attributs
  - `serialize(filename)` - Sérialise l'objet
  - `deserialize(filename)` - Désérialise l'objet (classmethod)

**Test:**
```bash
python3 main_01.py
```

### Task 2: Converting CSV Data to JSON Format
Conversion de données CSV en format JSON.

**Fonction:**
- `convert_csv_to_json(csv_filename)` - Convertit CSV en JSON

**Test:**
```bash
python3 main_02_csv.py
```

### Task 3: Serializing and Deserializing with XML
Sérialisation et désérialisation avec XML.

**Fonctions:**
- `serialize_to_xml(dictionary, filename)` - Sérialise un dictionnaire en XML
- `deserialize_from_xml(filename)` - Désérialise XML en dictionnaire

**Test:**
```bash
python3 main_03.py
```

## Utilisation

1. **Sérialisation JSON:**
```python
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data = {"name": "John", "age": 30}
serialize_and_save_to_file(data, 'output.json')
loaded_data = load_and_deserialize('output.json')
```

2. **Pickle:**
```python
from task_01_pickle import CustomObject

obj = CustomObject(name="Alice", age=25, is_student=True)
obj.serialize("data.pkl")
new_obj = CustomObject.deserialize("data.pkl")
```

3. **CSV to JSON:**
```python
from task_02_csv import convert_csv_to_json

convert_csv_to_json("input.csv")
```

4. **XML:**
```python
from task_03_xml import serialize_to_xml, deserialize_from_xml

data = {'name': 'John', 'age': '28', 'city': 'New York'}
serialize_to_xml(data, "output.xml")
loaded = deserialize_from_xml("output.xml")
```

## Formats de sérialisation

- **JSON**: Format léger et lisible, idéal pour les API web
- **Pickle**: Format binaire Python, pour objets Python complexes
- **CSV**: Format tabulaire simple, compatible avec Excel
- **XML**: Format structuré, utilisé dans de nombreux systèmes

## Auteur

Projet Holberton School
