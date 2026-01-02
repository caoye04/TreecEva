from collections import defaultdict, Counter
import math

# Simulated agricultural yield optimization with noise and distractors
def preprocess_sensors(raw_data):
    processed = {}
    for k, v in raw_data.items():
        if 'sensor_' in k:
            processed[k] = v * 1.08 + 3.2
    return processed

def validate_cluster_integrity(graph):
    visited = set()
    components = 0
    for node in graph:
        if node not in visited:
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    stack.extend(graph[curr])
            components += 1
    return components > 0
def compute_legacy_index(data):
    # Irrelevant legacy calculation (dead path)
    total = 0
    for x in data:
        total += (x ** 2) % 7
    return total // 2
def analyze_growth_phases(temperatures):
    phases = []n    for t in temperatures:
        if t < 15:
            phases.append('dormant')
        elif t < 25:
            phases.append('growth')
        else:
            phases.append('mature')
    counter = Counter(phases)
    return counter.get('growth', 0) - counter.get('dormant', 0)
def generate_mock_topology(n):
    # Distractor: creates unused structure
    topo = defaultdict(list)
    for i in range(n):
        for j in range(i+1, min(i+4, n)):
            topo[i].append(j)
            topo[j].append(i)
    return topo
def calculate_harvest_efficiency(clusters, performance_metrics):
    efficiency = 0
    base_adjustment = len(clusters) * 0.7
    
    # Real logic begins here — complex but focused
    cluster_map = {k: v for k, v in clusters.items() if v['size'] > 2}
    
    # Sum relevant yields
    raw_yields = []
    for cid, props in cluster_map.items():
        if props['soil_quality'] >= 5:
            adjusted_yield = props['base_yield']
            adjusted_yield *= (props['sun_exposure'] / 10.0)
            adjusted_yield += performance_metrics.get(f'bonus_{cid}', 0)
            raw_yields.append(adjusted_yield)
    
    # Accumulation step
    total_yield = sum(raw_yields)
    
    # Apply decay factor based on overcrowding
    overcrowded = 0
    for props in cluster_map.values():
        if props['size'] > 5:
            overcrowded += 1
    decay_factor = 0.95 ** overcrowded
    
    # Main computation
    temp_data = [22, 18, 26, 14, 28, 20]
    growth_score = analyze_growth_phases(temp_data)
    
    # Red herring: irrelevant transformation
    dummy_transform = [math.log(abs(x) + 1) for x in temp_data]
    dummy_sum = sum(dummy_transform) / len(dummy_transform)
    
    # Key integration
    efficiency = total_yield * decay_factor
    if growth_score > 0:
        efficiency *= (1 + growth_score * 0.05)
    
    # Final adjustment using dictionary operations
    modifiers = {'humidity': 1.08, 'wind': 0.97, 'pests': 0.89}
    for mod in modifiers.values():
        if mod < 0.9:
            efficiency *= mod
    
    return int(efficiency)  # Final result as integer

# --- Execution Context ---
if __name__ == '__main__':
    # Input data setup
    sensor_data = {f'sensor_{i}': 10+i for i in range(8)}
    processed_sensors = preprocess_sensors(sensor_data)
    
    # Real input structures
    cluster_map = {
        1: {'size': 3, 'soil_quality': 6, 'base_yield': 120, 'sun_exposure': 8},
        2: {'size': 6, 'soil_quality': 7, 'base_yield': 140, 'sun_exposure': 9},
        3: {'size': 4, 'soil_quality': 4, 'base_yield': 100, 'sun_exposure': 7},  # low soil quality
        4: {'size': 7, 'soil_quality': 8, 'base_yield': 130, 'sun_exposure': 6},
        5: {'size': 2, 'soil_quality': 9, 'base_yield': 200, 'sun_exposure': 10}   # filtered out by size
    }
    
    metrics = {
        'bonus_1': 10,
        'bonus_2': 15,
        'bonus_4': 5,
        'irrelevant_metric_x': 999,
        'debug_flag': True
    }
    
    # Unused graph for distraction
    topology = generate_mock_topology(12)
    is_valid = validate_cluster_integrity(topology)
    
    # Legacy analysis (no effect)
    dummy_array = [4, 7, 2, 9, 1]
    legacy_index = compute_legacy_index(dummy_array)
    
    # --- Critical Statement ---
    final_yield = calculate_harvest_efficiency(cluster_map, metrics)
    
    # Output result
    print(f"Result: {final_yield}")