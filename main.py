class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child, weight):
        self.children.append((child, weight))



root = Node("Début")
node1 = Node("Fils 1")
node2 = Node("Fils 2")
node3 = Node("Fils_fin")
node4 = Node("Fils_4")


root.add_child(node1, 10)  
node1.add_child(node2, 10)  
node2.add_child(node3, 10)  
root.add_child(node3, 50)  
root.add_child(node4, 20)  
node4.add_child(node3, 20)  


print("Relations entre les nœuds :")
for node in [root, node1, node2, node3, node4]:
    print(f"{node.name} :")
    for child, weight in node.children:
        print(f"  -> {child.name} avec un poids de {weight}")


def shortest_path(node, target, path=[]):
    path = path + [node]
    if node == target:
        return path
    if not node.children:
        return None

    shortest = None
    for child, _ in node.children:
        new_path = shortest_path(child, target, path)
        if new_path:
            if not shortest or len(new_path) < len(shortest):
                shortest = new_path
    return shortest


target_node = node3 
start_node = root  
shortest = shortest_path(start_node, target_node)

if shortest:
    print("Le plus court chemin en nombre d'arcs est :", [node.name for node in shortest])
else:
    print("Aucun chemin trouvé jusqu'au nœud cible.")


def fastest_path(node, target, path=[]):
    path = path + [node]
    if node == target:
        return path
    if not node.children:
        return None
    fastest = None
    for child, weight in node.children:
        new_path = fastest_path(child, target, path)
        if new_path:
            if not fastest or total_weight(new_path) < total_weight(fastest):
                fastest = new_path
    return fastest

def total_weight(path):
    total = 0
    for i in range(len(path)-1):
        current_node = path[i]
        next_node = path[i+1]
        for child, weight in current_node.children:
            if child == next_node:
                total += weight
                break
    return total

# Exemple d'utilisation
target_node = node3  # Noeud cible: "Fils_fin"
start_node = root  # Noeud de départ: "Début"
fastest = fastest_path(start_node, target_node)

if fastest:
    print("Le plus rapide chemin est :", [node.name for node in fastest])
    print("Le poids total du chemin est :", total_weight(fastest))
else:
    print("Aucun chemin trouvé jusqu'au nœud cible.")


def foremost_path(node, target, path=[]):
    path = path + [node]
    if node == target:
        return path
    if not node.children:
        return None
    foremost = None
    for child, _ in node.children:
        new_path = foremost_path(child, target, path)
        if new_path:
            if not foremost or len(new_path) < len(foremost):
                foremost = new_path
    return foremost

# Exemple d'utilisation
target_node = node3  # Noeud cible: "Fils_fin"
start_node = root  # Noeud de départ: "Début"
foremost = foremost_path(start_node, target_node)

if foremost:
    print("Le chemin arrivant au plus tôt est :", [node.name for node in foremost])
else:
    print("Aucun chemin trouvé jusqu'au nœud cible.")

