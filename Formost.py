import heapq

class Station:
    def __init__(self, nom):
        self.nom = nom

class Graphe:
    def __init__(self):
        self.stations = {}
        self.connexions = {}

    def ajouter_station(self, station):
        self.stations[station.nom] = station
        self.connexions[station.nom] = {}

    def ajouter_connexion(self, station_origine, station_destination, heure_depart):
        if not self.connexions[station_origine].get(station_destination):
            self.connexions[station_origine][station_destination] = []
        self.connexions[station_origine][station_destination].append(heure_depart)

    def trajet_le_plus_tot(self, origine, destination):
        file_priorité = [(heure, origine, [origine]) for heure in self.connexions[origine][destination]]
        heapq.heapify(file_priorité)
        visités = set()

        while file_priorité:
            heure_actuelle, station_actuelle, chemin = heapq.heappop(file_priorité)

            if station_actuelle == destination:
                return (heure_actuelle, chemin)

            visités.add(station_actuelle)

            for station_suivante, heures_depart in self.connexions[station_actuelle].items():
                if station_suivante not in visités:
                    for heure_depart in heures_depart:
                        if heure_depart > heure_actuelle:
                            heapq.heappush(file_priorité, (heure_depart, station_suivante, chemin + [station_suivante]))
                            break

        return (None, [])
if __name__ == "__main__":
    graphe = Graphe()

    # Ajout des stations
    graphe.ajouter_station(Station("Origine"))
    graphe.ajouter_station(Station("Destination"))

    # Ajout des connexions entre les stations, assurez-vous que ces étapes sont correctes
    # Par exemple, pour une connexion directe (remplacez "HeureDepart" par une valeur réelle):
    graphe.ajouter_connexion("Origine", "Destination", 7)

    # Ou, si votre système dépend de connexions intermédiaires, assurez-vous qu'elles sont toutes ajoutées

   
    résultat = graphe.trajet_le_plus_tot("Origine", "Destination")
    print("Le trajet le plus tôt:", résultat)