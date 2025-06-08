#!/usr/bin/python3
# Module permettant la sérialisation et la désérialisation de données en JSON

import json

def serialize_and_save_to_file(data, filename):
    """
    Sérialise des données en format JSON et les enregistre dans un fichier.
    
    Args:
        data (dict): Les données à sérialiser (doit être un dictionnaire)
        filename (str): Le nom du fichier où enregistrer les données
        
    Raises:
        TypeError: Si data n'est pas un dictionnaire
    """
    if not isinstance(data, dict):
        raise TypeError(f"serialize_and_save_to_file not dict {type(data)}")

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Charge et désérialise des données JSON depuis un fichier.
    
    Args:
        filename (str): Le nom du fichier contenant les données JSON
        
    Returns:
        dict: Les données désérialisées
        
    Raises:
        ValueError: Si les données chargées ne sont pas un dictionnaire
    """
    with open(filename, 'r', encoding="utf-8") as fp:
        data = json.load(fp)
        
    if not isinstance(data, dict):
        raise ValueError(f"serialize_and_save_to_file Not a dict{type(data)}")
    return data
