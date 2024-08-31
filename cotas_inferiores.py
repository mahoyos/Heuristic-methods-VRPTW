import networkx as nx
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 3)

def process_file(file_path):
    with open(file_path, 'r') as file:
        n, Q = map(int, file.readline().strip().split())
        nodes = []
        for _ in range(n + 1):
            node_data = list(map(float, file.readline().strip().split()))
            nodes.append(node_data)
        
        nodes_dict = {}
        for i, node in enumerate(nodes):
            xi, yi = node[1], node[2]
            nodes_dict[i] = {'x': xi, 'y': yi}
        
        return n, nodes_dict

def create_complete_graph(n, nodes_dict):
    G = nx.complete_graph(n + 1)  # Crear un grafo completo con n+1 nodos (incluyendo el depósito)
    
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            distance = calculate_euclidean_distance(nodes_dict[i]['x'], nodes_dict[i]['y'], nodes_dict[j]['x'], nodes_dict[j]['y'])
            G[i][j]['weight'] = distance
            G[j][i]['weight'] = distance  # El grafo es no dirigido
    
    return G

def calculate_lower_bound(G):
    tsp_route = nx.approximation.traveling_salesman_problem(G, cycle=False, weight='weight')
    total_distance = 0
    for i in range(len(tsp_route) - 1):
        total_distance += G[tsp_route[i]][tsp_route[i + 1]]['weight']
    
    return total_distance

def calculate_gap(current_solution, lower_bound):
    """
    Calcula el gap entre la solución actual y la cota inferior.

    Parámetros:
    current_solution (float): El valor de la solución actual obtenida.
    lower_bound (float): El valor de la cota inferior.

    Retorna:
    float: El porcentaje del gap entre la solución actual y la cota inferior.
    """
    if current_solution == 0:
        raise ValueError("La solución actual no puede ser 0.")
    
    gap = ((current_solution - lower_bound) / current_solution) * 100
    return gap

def main():    
    for i in range(1, 19):
        file_name = f"VRPTW{i}.txt"
        n, nodes_dict = process_file(file_name)
        G = create_complete_graph(n, nodes_dict)
        lower_bound = calculate_lower_bound(G)
        print(f"La cota inferior en distancia para la instancia {i} es: {lower_bound}")

if __name__ == "__main__":
    main()
    print(calculate_gap(374.785, 121.55800000000002))

