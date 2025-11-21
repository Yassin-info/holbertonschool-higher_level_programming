#!/usr/bin/python3
"""Script de test complet pour tous les exercices."""

print("=" * 60)
print("TEST COMPLET - Python Serialization")
print("=" * 60)

# Test Task 0
print("\n[Task 0] Basic Serialization")
print("-" * 60)
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data = {"name": "John Doe", "age": 30, "city": "New York"}
serialize_and_save_to_file(data, 'test_data.json')
loaded = load_and_deserialize('test_data.json')
print(f"Original: {data}")
print(f"Loaded:   {loaded}")
print(f"✓ Task 0: {'PASS' if data == loaded else 'FAIL'}")

# Test Task 1
print("\n[Task 1] Pickling Custom Classes")
print("-" * 60)
from task_01_pickle import CustomObject

obj = CustomObject(name="Alice", age=25, is_student=True)
print("Original Object:")
obj.display()

obj.serialize("test_object.pkl")
new_obj = CustomObject.deserialize("test_object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
    test_pass = (obj.name == new_obj.name and 
                 obj.age == new_obj.age and 
                 obj.is_student == new_obj.is_student)
    print(f"✓ Task 1: {'PASS' if test_pass else 'FAIL'}")
else:
    print("✗ Task 1: FAIL - deserialize returned None")

# Test Task 1 - Error handling
print("\nTest gestion d'erreurs:")
result = CustomObject.deserialize("nonexistent.pkl")
print(f"Fichier inexistant: {result} (devrait être None)")
print(f"✓ Error handling: {'PASS' if result is None else 'FAIL'}")

# Test Task 2
print("\n[Task 2] Converting CSV to JSON")
print("-" * 60)
from task_02_csv import convert_csv_to_json
import json

result = convert_csv_to_json("data.csv")
print(f"Conversion réussie: {result}")

if result:
    with open('data.json', 'r') as f:
        json_data = json.load(f)
    print(f"Nombre d'entrées: {len(json_data)}")
    print(f"Première entrée: {json_data[0]}")
    print(f"✓ Task 2: PASS")
else:
    print("✗ Task 2: FAIL")

# Test Task 2 - Error handling
result = convert_csv_to_json("nonexistent.csv")
print(f"CSV inexistant: {result} (devrait être False)")
print(f"✓ Error handling: {'PASS' if result is False else 'FAIL'}")

# Test Task 3
print("\n[Task 3] XML Serialization")
print("-" * 60)
from task_03_xml import serialize_to_xml, deserialize_from_xml

test_dict = {'name': 'Bob', 'age': '30', 'city': 'Paris'}
serialize_to_xml(test_dict, "test_data.xml")
loaded_dict = deserialize_from_xml("test_data.xml")

print(f"Original: {test_dict}")
print(f"Loaded:   {loaded_dict}")
print(f"✓ Task 3: {'PASS' if test_dict == loaded_dict else 'FAIL'}")

# Nettoyage
print("\n" + "=" * 60)
print("Nettoyage des fichiers de test...")
import os
for f in ['test_data.json', 'test_object.pkl', 'test_data.xml']:
    if os.path.exists(f):
        os.remove(f)
        print(f"✓ Supprimé: {f}")

print("\n" + "=" * 60)
print("TESTS TERMINÉS")
print("=" * 60)
