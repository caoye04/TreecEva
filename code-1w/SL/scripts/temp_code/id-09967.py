from collections import defaultdict

# Simulate a network topology with node dependencies
def build_network():
    network = defaultdict(set)
    network[1].add(2)
    network[1].add(3)
    network[2].add(4)
    network[3].add(4)
    network[4].add(5)
    return network

# Calculate resilience based on redundant paths
def has_redundant_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return len(path) > 1
    if start not in graph:
        return False
    
    multiple_paths = 0
    for node in graph[start]:
        if node not in path:
            if has_redundant_path(graph, node, end, path):
                multiple_paths += 1
    return multiple_paths > 1

def calculate_resilience(nodes_graph):
    resilient_nodes = 0
    for node in nodes_graph:
        if has_redundant_path(nodes_graph, 1, node):
            resilient_nodes += 1
    return max(resilient_nodes, 1)

# Irrelevant utility (minimal distraction - intervention level 4)
def log_event(event_str):
    timestamp = "[LOG] 12:00"
    return f"{timestamp}: {event_str}"

# Build network and compute resilience
network_nodes = build_network()
resilience_score = calculate_resilience(network_nodes)

# Output result
print(f"Result: {resilience_score}")