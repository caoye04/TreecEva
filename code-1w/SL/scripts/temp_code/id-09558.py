from collections import defaultdict

def calculate_network_load(edges, flow):
    graph = defaultdict(int)
    capacity = 0

    for u, v in edges:
        graph[u] += 1
        graph[v] += 1

    for node in graph:
        if graph[node] > 2:
            capacity += flow * 2
        else:
            capacity += flow

    # Irrelevant intermediate variable (minimal distraction)
    temp_debug = [graph[n] for n in graph if graph[n] > 1]
    
    total_load = capacity // 2
    return total_load

# Define network connections and flow rate
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (2, 5)]
flow = 7

# Compute final load
total_load = calculate_network_load(edges, flow)
print(f"Result: {total_load}")