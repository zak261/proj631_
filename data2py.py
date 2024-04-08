#!/usr/bin/python3
#-*-coding:utf-8-*-

def charger_fichier(data_file_name):
    """
    Charge le contenu d'un fichier de données spécifié.

    Args:
        data_file_name (str): Le chemin vers le fichier de données.

    Returns:
        str: Le contenu du fichier.
    """
    try:
        with open(data_file_name, 'r') as f:
            return f.read()
    except OSError:
        print(f"Le fichier {data_file_name} n'a pas été trouvé.")
        return ""

def dates2dic(dates):
    """
    Convertit les dates fournies en un dictionnaire.

    Args:
        dates (str): Les dates à convertir, séparées par des retours à la ligne.

    Returns:
        dict: Un dictionnaire où chaque clé est le nom d'une station et la valeur est une liste d'horaires.
    """
    dic = {}
    splitted_dates = dates.split("\n")
    for stop_dates in splitted_dates:
        if stop_dates:  # Assure que la ligne n'est pas vide
            tmp = stop_dates.split(" ")
            dic[tmp[0]] = tmp[1:]
    return dic

def charger_horaires(data_file_name):
    """
    Charge les horaires à partir d'un fichier spécifié et les convertit en dictionnaires.

    Args:
        data_file_name (str): Le chemin vers le fichier de données.

    Returns:
        dict: Un dictionnaire contenant les itinéraires et horaires réguliers et de week-ends/jours fériés.
    """
    content = charger_fichier(data_file_name)
    if not content:
        return {}

    slited_content = content.split("\n\n")
    horaires = {
        'regular_path': slited_content[0],
        'regular_date_go': dates2dic(slited_content[1]),
        'regular_date_back': dates2dic(slited_content[2]),
        'we_holidays_path': slited_content[3],
        'we_holidays_date_go': dates2dic(slited_content[4]),
        'we_holidays_date_back': dates2dic(slited_content[5])
    }
    return horaires

# Exemple d'utilisation
if __name__ == "__main__":
    data_file_name = 'data/1_Poisy-ParcDesGlaisins.txt'
    # Ou data_file_name = 'data/2_Piscine-Patinoire_Campus.txt'
    horaires = charger_horaires(data_file_name)
    print("Horaires chargés :", horaires)
