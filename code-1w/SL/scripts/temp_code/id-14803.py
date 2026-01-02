from collections import defaultdict, Counter

# Simulate a network node stability analyzer with decoy computations

def analyze_node_health(node_data, threshold=0.75):
    healthy_count = 0
    total_nodes = len(node_data)
    
    for status in node_data.values():
        if status > threshold:
            healthy_count += 1

    # Distractor: irrelevant ratio calculation
    redundancy_ratio = (healthy_count * 2.5) / max(total_nodes, 1)
    failover_score = (total_nodes - healthy_count) ** 0.5

    return healthy_count


def build_dependency_graph(nodes):
    graph = defaultdict(list)
    decoy_map = defaultdict(int)  # Unused structure

    # Real mapping
    for i, deps in enumerate([[1,2], [3], [3], []]):
        graph[i] = deps

    # Irrelevant counter
    for k in range(len(nodes)):
        decoy_map[nodes[k]] = k * 3

    return graph


def detect_cycles(graph, size):
    visited = [False] * size
    rec_stack = [False] * size
    cycle_count = 0

    def dfs(v):
        nonlocal cycle_count
        if not visited[v]:
            visited[v] = True
            rec_stack[v] = True

            for neighbor in graph.get(v, []):
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    cycle_count += 1
                    return True
        rec_stack[v] = False
        return False

    for node in range(size):
        if dfs(node):
            break

    # Decoy return with misleading impact
    return cycle_count + 100 if cycle_count > 0 else 0


def compute_stability_index(nodes):
    # Core data
    health_scores = [0.85, 0.91, 0.67, 0.94]
    node_status = {i: score for i, score in enumerate(health_scores)}

    # Step 1: Count healthy nodes
    stable_count = analyze_node_health(node_status)

    # Step 2: Build dependency graph
    dep_graph = build_dependency_graph(['A', 'B', 'C', 'D'])

    # Step 3: Detect cycles (potential failure points)
    cyclic_threat = detect_cycles(dep_graph, 4)

    # Step 4: Calculate load distribution entropy (red herring)
    loads = [30, 50, 40, 60]
    avg_load = sum(loads) / len(loads)
    variance = sum((x - avg_load) ** 2 for x in loads) / len(loads)
    entropy_decoy = -(sum(p/sum(loads) * __import__('math').log(p/sum(loads)) for p in loads if p > 0))

    # Step 5: Calculate fault tolerance margin (irrelevant)
    active_links = 0
    for neighbors in dep_graph.values():
        active_links += len(neighbors)
    redundancy_factor = active_links / len(nodes) if nodes else 0

    # Step 6: Actual index computation (only this matters)
    base_index = stable_count * 100
    penalty = 25 if cyclic_threat > 0 else 0
    final_index = base_index - penalty

    # Step 7: Apply minor correction based on first node status
    if node_status[0] > 0.8:
        final_index += 10

    # Step 8: Adjust using zip and enumerate (required idiom)
    adjustments = [5, -3, 0, 2]
    for i, (adj, score) in enumerate(zip(adjustments, health_scores)):
        if score > 0.7:
            final_index += adj

    # Final red herring: unused transformation
    decoy_counter = Counter(health_scores)
    normalized_index = final_index / (decoy_counter[0.85] + 1)

    # Critical assignment
    final_diagnostic = int(final_index)  # This is the answer

    return final_diagnostic

# Execution sequence
network_nodes = ['router_a', 'router_b', 'switch_c', 'firewall_d']
baseline_metrics = {'latency': 42, 'jitter': 3.5, 'loss': 0.01}
decoy_list = [x**3 for x in range(10)]  # Dead computation path

intermediate = list(zip(network_nodes, [100, 200, 300, 400]))
offset_map = {k: v for k, v in enumerate([10, 20, 30, 40])}

# Key execution point
final_diagnostic = compute_stability_index(network_nodes)
print(f"Target result: {final_diagnostic}")