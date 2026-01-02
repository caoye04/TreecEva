from collections import defaultdict
import itertools

def analyze_network(edges):
    graph = defaultdict(list)
    degree = defaultdict(int)
    
    for u, v in edges:
        graph[u].append(v)
        degree[u] += 1
        degree[v] += 1

    return graph, degree

def simulate_pressure(nodes, base=1.07):
    pressures = {}
    temp_vals = []
    
    for i, node in enumerate(nodes):
        raw = (i + 1) * base ** i
        adjusted = round(raw, 4)
        pressures[node] = adjusted
        temp_vals.append(adjusted * 0.95)
        
    # Irrelevant smoothing
    smoothed = [temp_vals[0]]
    for j in range(1, len(temp_vals)):
        smoothed.append(round((smoothed[-1] + temp_vals[j]) / 2, 4))
        
    return pressures

def calculate_flow(capacity_map, exponents):
    flow = {}
    dummy_calc = 0
    
    for key, cap in capacity_map.items():
        exp = exponents.get(key, 1.5)
        result = cap ** exp
        flow[key] = round(result, 4)
        
        # Distractor: accumulating unused value
        dummy_calc += result * 0.1
        
    return flow

def calculate_distribution(flow_data, pressure_list):
    total = 0.0
    norm_factor = 0.0
    
    # Real computation branch
    valid_keys = [k for k in flow_data.keys() if 'CH' in k]
    for key in valid_keys:
        total += flow_data[key]

    # Secondary distractor loop (no effect on final_load)
    temp_store = []
    for p in pressure_list:
        if p > 2.0:
            temp_store.append(p ** 0.5)
        else:
            temp_store.append(p)
    
    # Actual normalization
    for val in temp_store:
        norm_factor += val
        
    final_load = int(round(total * (norm_factor / len(temp_store))))
    
    # Dead code path (never reached in normal execution)
    if False:
        backup = sum(flow_data.values())
        final_load = int(backup)
        
    return final_load

# Main execution block
if __name__ == "__main__":
    connections = [
        ('A', 'B'), ('B', 'C'), ('C', 'D'),
        ('D', 'E'), ('E', 'F'), ('F', 'A')
    ]
    
    node_set = ['CH01', 'CH02', 'CH03', 'CH04', 'OUT1', 'OUT2']
    
    # Generate pressure values (only some used later)
    pressure_readings = simulate_pressure(node_set)
    pressure_values = list(pressure_readings.values())
    
    # Build auxiliary graph (not directly used in final answer)
    network_graph, node_degree = analyze_network(connections)
    
    # Create capacity map and exponents
    capacities = {
        'CH01': 12, 'CH02': 15, 'CH03': 18, 'CH04': 20,
        'OUT1': 8, 'OUT2': 10
    }
    
    exponents_config = {
        'CH01': 1.2, 'CH02': 1.3, 'CH03': 1.4, 'CH04': 1.5
    }
    
    # Compute flow per channel
    flow_map = calculate_flow(capacities, exponents_config)
    
    # Track intermediate stats (unused)
    avg_flow = sum(flow_map.values()) / len(flow_map)
    max_flow = max(flow_map.values())
    
    # Key statement: compute final load based on CH-type nodes and pressure
    final_load = calculate_distribution(flow_map, pressure_values)
    
    # Print result as required
    print(f"Result: {final_load}")