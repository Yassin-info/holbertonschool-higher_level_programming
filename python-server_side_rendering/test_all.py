#!/usr/bin/python3
"""
Script de test pour toutes les tâches du projet.
"""
import os
import sys


def test_task_00():
    """Test de la Task 0 - Génération d'invitations."""
    print("=" * 60)
    print("TEST TASK 0 - Génération d'invitations")
    print("=" * 60)

    from task_00_intro import generate_invitations

    # Lire le template
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des participants
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]

    # Générer les invitations
    generate_invitations(template_content, attendees)

    # Vérifier que les fichiers ont été créés
    for i in range(1, 4):
        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            print(f"✓ {filename} créé avec succès")
            with open(filename, 'r') as f:
                print(f"  Contenu: {f.read()[:50]}...")
        else:
            print(f"✗ {filename} n'a pas été créé")

    print("\n")


def test_task_01():
    """Test de la Task 1 - Application Flask de base."""
    print("=" * 60)
    print("TEST TASK 1 - Application Flask de base")
    print("=" * 60)
    print("Pour tester cette tâche, lancez:")
    print("  python3 task_01_jinja.py")
    print("\nPuis visitez dans votre navigateur:")
    print("  - http://localhost:5000/")
    print("  - http://localhost:5000/about")
    print("  - http://localhost:5000/contact")
    print("\n")


def test_task_02():
    """Test de la Task 2 - Templates dynamiques."""
    print("=" * 60)
    print("TEST TASK 2 - Templates dynamiques")
    print("=" * 60)
    print("Pour tester cette tâche, lancez:")
    print("  python3 task_02_logic.py")
    print("\nPuis visitez dans votre navigateur:")
    print("  - http://localhost:5000/items")
    print("\n")


def test_task_03():
    """Test de la Task 3 - Données JSON/CSV."""
    print("=" * 60)
    print("TEST TASK 3 - Données JSON/CSV")
    print("=" * 60)
    print("Pour tester cette tâche, lancez:")
    print("  python3 task_03_files.py")
    print("\nPuis visitez dans votre navigateur:")
    print("  - http://localhost:5000/products?source=json")
    print("  - http://localhost:5000/products?source=csv")
    print("  - http://localhost:5000/products?source=json&id=1")
    print("  - http://localhost:5000/products?source=xml (test erreur)")
    print("\n")


def test_task_04():
    """Test de la Task 4 - Base de données SQLite."""
    print("=" * 60)
    print("TEST TASK 4 - Base de données SQLite")
    print("=" * 60)
    print("Pour tester cette tâche, lancez:")
    print("  python3 task_04_db.py")
    print("\nPuis visitez dans votre navigateur:")
    print("  - http://localhost:5000/products?source=sql")
    print("  - http://localhost:5000/products?source=sql&id=1")
    print("\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        task = sys.argv[1]
        if task == "0":
            test_task_00()
        elif task == "1":
            test_task_01()
        elif task == "2":
            test_task_02()
        elif task == "3":
            test_task_03()
        elif task == "4":
            test_task_04()
        else:
            print("Usage: python3 test_all.py [0|1|2|3|4]")
    else:
        # Tester toutes les tâches
        test_task_00()
        test_task_01()
        test_task_02()
        test_task_03()
        test_task_04()

        # Nettoyer les fichiers de sortie
        for i in range(1, 10):
            filename = f"output_{i}.txt"
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Nettoyé: {filename}")
