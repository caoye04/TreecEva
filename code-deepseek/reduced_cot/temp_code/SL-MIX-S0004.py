# Adjacency matrix: graph[i][j] = cost from node i to j (0 means no edge)
graph = [
    [0, 10, 15, 0],
    [0, 0, 0, 12],
    [0, 8, 0, 14],
    [0, 0, 0, 0]
]

start_node = 0
target_node = 3
max_hops = 2

# Find all paths within max_hops
valid_paths = []
for intermediate in range(len(graph)):
    # Direct path (1 hop)
    if graph[start_node][intermediate] > 0 and graph[intermediate][target_node] > 0:
        cost = graph[start_node][intermediate] + graph[intermediate][target_node]
        valid_paths.append(cost)

# Calculate minimum cost
if valid_paths:
    min_cost = min(valid_paths)
    num_paths = len(valid_paths)
    
    # Apply discount based on number of paths
    discount_rate = num_paths * 2
    discount = min_cost * discount_rate // 100
    final_cost = min_cost - discount
else:
    final_cost = 0

print(f"Result: {final_cost}")