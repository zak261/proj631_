from datetime import datetime, timedelta
import heapq
from typing import List

# Supposons que les fonctions de Shortest.py, Fastest.py, et foremost.py sont déjà importées ou intégrées ici
from Shortest import chemin_le_plus_court
from Fastest import chemin_le_plus_rapide
from Formost import trajet_le_plus_tot

import data2py

class Horaire:
    def __init__(self, heure: int, minute: int, ligne: 'Ligne'):
        self.heure = heure
        self.minute = minute
        self.ligne = ligne

    def __str__(self):
        return f"{self.heure:02d}:{self.minute:02d} ({self.ligne})"

class Ligne:
    def __init__(self, nom: str):
        self.nom = nom

    def __str__(self):
        return f"Ligne {self.nom}"

class Station:
    def __init__(self, nom: str):
        self.nom = nom
        self.horaires_semaine = {}
        self.horaires_weekend = {}
        self.horaires_feries = {}

    def ajouter_horaire_semaine(self, jour: str, horaires: List[Horaire]):
        self.horaires_semaine[jour] = horaires

    def ajouter_horaire_weekend(self, jour: str, horaires: List[Horaire]):
        self.horaires_weekend[jour] = horaires

    def ajouter_horaire_ferie(self, date: str, horaires: List[Horaire]):
        self.horaires_feries[date] = horaires

class Calendrier:
    def __init__(self):
        self.stations = {}

    def ajouter_station(self, station: Station):
        self.stations[station.nom] = station

    def afficher_horaires(self):
        for nom, station in self.stations.items():
            print(f"Station: {nom}")
            print("Horaires en semaine:")
            for jour, horaires in station.horaires_semaine.items():
                print(f" - {jour}: {[str(horaire) for horaire in horaires]}")
            print("Horaires le weekend:")
            for jour, horaires in station.horaires_weekend.items():
                print(f" - {jour}: {[str(horaire) for horaire in horaires]}")
            print("Horaires les jours fériés:")
            for date, horaires in station.horaires_feries.items():
                print(f" - {date}: {[str(horaire) for horaire in horaires]}")

def ajouter_station_avec_horaires(calendrier, nom_station, horaires):
    station = Station(nom_station)
    for jour, heures in horaires.items():
        liste_horaires = []
        for h in heures:
            if '-' not in h:  
                heure, minute = map(int, h.split(':'))
                liste_horaires.append(Horaire(heure, minute, Ligne("Nom de la Ligne")))
            else:
                print(f"Plage horaire non disponible pour {nom_station} le {jour} à {h}")
        

    calendrier.ajouter_station(station)


def main():
    horaires = data2py.charger_horaires('data/1_Poisy-ParcDesGlaisins.txt')
    calendrier = Calendrier()

    for nom_station, horaires_station in horaires.items():
        if isinstance(horaires_station, dict):  # Vérification ajoutée pour plus de clarté
            ajouter_station_avec_horaires(calendrier, nom_station, horaires_station)
        else:
            print(f"Erreur dans le format des horaires pour la station {nom_station}")

    calendrier.afficher_horaires()


    # Utilisez les fonctions de calcul d'itinéraire ici

if __name__ == "__main__":
    main()

# Création des lignes de bus
ligne1 = Ligne("4")
ligne2 = Ligne("2")

calendrier = Calendrier()

# Création des stations avec leurs horaires
ajouter_station_avec_horaires(
    calendrier,
    "SEYNOD_NEIGEOS",
    {"Lundi": [Horaire(6, 4, ligne1), Horaire(6, 24, ligne1), Horaire(6, 44, ligne1)]},
    {"Samedi": [Horaire(6, 4, ligne1), Horaire(6, 24, ligne1), Horaire(6, 44, ligne1)]},
    {}
)


ajouter_station_avec_horaires(
    calendrier,
    "Saint-Jean",
    {"Lundi": [Horaire(6, 8, ligne1), Horaire(6, 28, ligne1), Horaire(6, 48, ligne1)]},
    {"Samedi": [Horaire(6, 8, ligne1), Horaire(6, 28, ligne1), Horaire(6, 48, ligne1)]},
    {}
)


ajouter_station_avec_horaires(
    calendrier,
    "L.P._Gordini",
    {"Lundi": [Horaire(6, 10, ligne1), Horaire(6, 30, ligne1), Horaire(6, 50, ligne1)]},
    {"Samedi": [Horaire(6, 10, ligne1), Horaire(6, 30, ligne1), Horaire(6, 50, ligne1)]},
    {}
)


# Calcul des trajets
heure_depart = datetime.strptime('10:00', '%H:%M')
chemin_court = chemin_le_plus_court("SEYNOD_NEIGEOS", "L.P._Gordini", 'Court', heure_depart)
print("Chemin le plus court:", chemin_court)
chemin_rapide = chemin_le_plus_rapide("SEYNOD_NEIGEOS", "L.P._Gordini", 'Rapide', heure_depart)
print("Chemin le plus rapide:", chemin_rapide)
chemin_tot = trajet_le_plus_tot("SEYNOD_NEIGEOS", "L.P._Gordini", 'Tot', heure_depart)
print("Chemin le plus tôt:", chemin_tot)


