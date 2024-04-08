import heapq

class Station:
    """Représente une station dans le graphe des trajets."""
    def __init__(self, nom):
        self.nom = nom

class Graphe:
    """Représente le réseau de stations et leurs connexions."""
    def __init__(self):
        self.noeuds = {}
        self.arêtes = {}

    def ajouter_noeud(self, noeud):
        self.noeuds[noeud.nom] = noeud
        self.arêtes[noeud.nom] = {}

    def ajouter_arête(self, noeud_origine, noeud_destination, poids):
        self.arêtes[noeud_origine.nom][noeud_destination.nom] = poids

    def chemin_le_plus_rapide(self, nom_origine, nom_destination):
        distances = {nom_noeud: float('inf') for nom_noeud in self.noeuds}
        distances[nom_origine] = 0
        noeuds_précédents = {}
        file_priorité = [(0, nom_origine)]
        visités = set()

        while file_priorité:
            distance_actuelle, noeud_actuel = heapq.heappop(file_priorité)
            visités.add(noeud_actuel)

            if noeud_actuel == nom_destination:
                break

            for voisin, poids in self.arêtes[noeud_actuel].items():
                if voisin in visités:
                    continue

                nouvelle_distance = distance_actuelle + poids
                if nouvelle_distance < distances[voisin]:
                    distances[voisin] = nouvelle_distance
                    noeuds_précédents[voisin] = noeud_actuel
                    heapq.heappush(file_priorité, (nouvelle_distance, voisin))

        return self._obtenir_chemin_le_plus_court(nom_origine, nom_destination, noeuds_précédents)

    def _obtenir_chemin_le_plus_court(self, origine, destination, noeuds_précédents):
        chemin = []
        actuel = destination
        while actuel != origine:
            chemin.append(actuel)
            actuel = noeuds_précédents.get(actuel)
            if actuel is None:
                return []  # S'il n'y a pas de chemin
        chemin.append(origine)
        chemin.reverse()
        return chemin

def exemple_utilisation():
    graphe = Graphe()
    # Ajoutez vos stations ici
    graphe.ajouter_noeud(Station("Début"))
    graphe.ajouter_noeud(Station("Fin"))
    # Ajoutez vos connexions ici
    graphe.ajouter_arête(Station("Début"), Station("Fin"), 10)

    chemin = graphe.chemin_le_plus_rapide("Début", "Fin")
    print("Chemin le plus rapide :", chemin)

if __name__ == "__main__":
    exemple_utilisation()
