from itertools import permutations

def evaluate_path_stress(path):
    stress = 0
    for i in range(len(path) - 1):
        stress += abs(path[i] - path[i + 1])
    return stress

def calculate_network_flow(capacity_map, routes):
    total_flow = 0
    max_stress = 0
    stress_readings = []

    for route in routes:
        route_flow = min(capacity_map[edge] for edge in route)
        total_flow += route_flow

        # Irrelevant stress computation (distractor)
        stress = evaluate_path_stress([capacity_map[edge] for edge in route])
        stress_readings.append(stress)

    # Distractor: simulate diagnostic check
    avg_stress = sum(stress_readings) / len(stress_readings) if stress_readings else 0
    diagnostic_flag = avg_stress > 5

    # Real logic: adjust flow based on base redundancy
    redundancy = len(routes) - len(capacity_map)
    adjusted_flow = total_flow - abs(redundancy)

    # Final adjustment based on pattern symmetry (semi-relevant)
    sorted_values = sorted(capacity_map.values())
    mid_val = sorted_values[len(sorted_values)//2] if sorted_values else 1
    if mid_val % 2 == 0:
        adjusted_flow += 1

    return adjusted_flow

# Main execution
edges = ['E1', 'E2', 'E3', 'E4']
capacities = {e: (ord(e[-1]) * 3) % 17 for e in edges}

# Generate all possible 3-edge paths (permutations as routes)
flow_paths = list(permutations(edges, 3))

# Dead code: unused alternative path generation (red herring)
# full_cycles = [p for p in permutations(edges) if p[0] == p[-1]]

# Simulate test measurement (irrelevant to final result)
test_measurement = sum(capacities[e] ** 0.5 for e in edges) // 1

def monitor_system_load():
    return sum(capacities.values()) % 10

# Unused monitoring call (dead code path)
system_load = monitor_system_load()

# Key statement
final_capacity = calculate_network_flow(capacities, flow_paths)
print(f"Result: {final_capacity}")