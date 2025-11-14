#!/usr/bin/python3
"""
Module pour générer des invitations personnalisées à partir d'un template.
"""


def generate_invitations(template, attendees):
    """
    Génère des fichiers d'invitation personnalisés à partir d'un template
    et d'une liste de participants.

    Args:
        template (str): Le template contenant les placeholders
        attendees (list): Liste de dictionnaires avec les données des participants

    Returns:
        None
    """
    # Vérifier le type du template
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return

    # Vérifier le type de la liste des participants
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return

    # Vérifier que tous les éléments de la liste sont des dictionnaires
    if attendees and not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return

    # Vérifier si le template est vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Vérifier si la liste des participants est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Créer une copie du template pour chaque participant
        output = template

        # Remplacer les placeholders
        placeholders = ['name', 'event_title', 'event_date', 'event_location']

        for placeholder in placeholders:
            key = f"{{{placeholder}}}"
            value = attendee.get(placeholder)

            # Si la valeur est None ou vide, utiliser "N/A"
            if value is None or (isinstance(value, str) and not value.strip()):
                value = "N/A"

            output = output.replace(key, str(value))

        # Écrire dans le fichier de sortie
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")


if __name__ == "__main__":
    # Lire le template depuis le fichier
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

    # Appeler la fonction
    generate_invitations(template_content, attendees)
