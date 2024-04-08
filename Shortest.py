import heapq

class Noeud:
    """Représente un noeud dans le graphe, chaque noeud étant une station."""
    def __init__(self, nom):
        self.nom = nom
        self.enfants = []  # Enfants sont des tuples (Noeud, poids)

    def ajouter_enfant(self, enfant, poids):
        self.enfants.append((enfant, poids))

class Graphe:
    """Gère le graphe complet, incluant les noeuds et les chemins entre eux."""
    def __init__(self):
        self.noeuds = {}

    def ajouter_noeud(self, noeud):
        self.noeuds[noeud.nom] = noeud

    def ajouter_arête(self, origine, destination, poids):
        if origine in self.noeuds and destination in self.noeuds:
            self.noeuds[origine].ajouter_enfant(self.noeuds[destination], poids)
        else:
            print(f"Erreur: Impossible d'ajouter l'arête de {origine} à {destination}.")

    def chemin_le_plus_court(self, départ, arrivée):
        distances = {noeud: float('inf') for noeud in self.noeuds}
        distances[départ] = 0
        file_priorité = [(0, départ, [départ])]  # (coût, noeud, chemin)
        visités = set()

        while file_priorité:
            coût, noeud, chemin = heapq.heappop(file_priorité)
            if noeud not in visités:
                visités.add(noeud)
                if noeud == arrivée:
                    return coût, chemin

                for enfant, poids in self.noeuds[noeud].enfants:
                    if enfant.nom not in visités:
                        nouveau_coût = coût + poids
                        heapq.heappush(file_priorité, (nouveau_coût, enfant.nom, chemin + [enfant.nom]))

        return float('inf'), []

def exemple_utilisation():
    graphe = Graphe()
    noeuds = [Noeud("Début"), Noeud("Fils 1"), Noeud("Fils 2"), Noeud("Fin")]

    for noeud in noeuds:
        graphe.ajouter_noeud(noeud)

    graphe.ajouter_arête("Début", "Fils 1", 10)
    graphe.ajouter_arête("Fils 1", "Fils 2", 15)
    graphe.ajouter_arête("Fils 1", "Fin", 20)
    graphe.ajouter_arête("Fils 2", "Fin", 10)

    coût, chemin = graphe.chemin_le_plus_court("Début", "Fin")
    print(f"Chemin le plus court: {chemin} avec un coût de {coût}")

if __name__ == "__main__":
    exemple_utilisation()
