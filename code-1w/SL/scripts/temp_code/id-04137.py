import math

# System resource configuration (irrelevant initial setup)
def initialize_nodes():
    node_specs = {}
    for i in range(5):
        node_specs[f'node_{i}'] = {
            'power': (i + 1) ** 3,
            'latency': 100 // (i + 1),
            'active': i % 2 == 0
        }
    return node_specs

# Misleading diagnostic function (dead code path)
def calculate_health_score(config):
    score = 0
    for k, v in config.items():
        if 'node' in k:
            score += v['power'] // max(1, v['latency'])
    return score * 0.75

# Unused but plausible-looking transformation
resource_cache = []
def cache_resource_entry(data):
    timestamp = len(resource_cache) * 100 + 5
    entry = {**data, 'ts': timestamp}
    resource_cache.append(entry)

# Core simulation parameters
base_frequencies = [2.4, 3.1, 2.8, 3.6, 2.9]  # GHz
task_loads = [[120, 80, 95], [60, 110, 70], [100, 100, 100], [40, 130, 60], [85, 90, 80]]
overhead_factor = 0.88

# Simulate thermal throttling effect (partially relevant)
def apply_throttling(freq, temperature):
    if temperature > 75:
        return freq * (0.8 + (85 - temperature) / 100)
    return freq

# Decoy data structure with realistic values
temperature_log = {
    'sensor_1': [70, 72, 75, 78, 74],
    'sensor_2': [68, 70, 71, 73, 70],
    'sensor_3': [75, 77, 80, 82, 79]
}

# Auxiliary calculation - appears important but not used in final result
efficiency_curve = []
for f in base_frequencies:
    efficiency_curve.append(round((f ** 1.1) / 2.5, 4))

# Resource matrix from task distribution
resource_matrix = []
for i, loads in enumerate(task_loads):
    row = []
    for load in loads:
        # Complex transformation with slicing distraction
        history = base_frequencies[:i+1] if i > 0 else [base_frequencies[0]]
        avg_freq = sum(history) / len(history)
        adjusted_load = load * (avg_freq / 3.0) * overhead_factor
        row.append(int(adjusted_load))
    resource_matrix.append(row)

# Create efficiency map using dictionary and set operations
node_ids = [f'n{i}' for i in range(len(task_loads))]
active_indices = {i for i in range(len(task_loads)) if i % 2 == 1}
efficiency_map = {}
for idx in range(len(task_loads)):
    key = node_ids[idx]
    base_eff = 0.85 if idx in active_indices else 0.75
    # Incorporate bit manipulation red herring
    magic_shift = (idx << 2) ^ 5
    efficiency_map[key] = base_eff * (1 + (math.sin(magic_shift) ** 2) * 0.1)

# Secondary distraction: simulate cache warming
for row in resource_matrix:
    cache_resource_entry({'data': row, 'size': len(row)})

# Critical function: aggregate throughput computation
def aggregate_throughput(matrix, efficiency):
    total = 0.0
    weights = [0.5, 1.0, 0.7]  # Weight by task type
    
    # Nested processing with conditional accumulation
    for i, row in enumerate(matrix):
        row_total = 0
        for j, val in enumerate(row):
            # Apply efficiency based on node
            node_key = f'n{i}'
            if node_key in efficiency:
                scaled = val * efficiency[node_key] * weights[j]
                if scaled > 70:
                    row_total += int(scaled // 1.8)  # Integer division and rounding
                else:
                    row_total += int(scaled * 0.9)
        
        # Conditional bonus (simulates optimization)
        if len([x for x in row if x > 80]) >= 2:
            row_total = int(row_total * 1.1)
            
        # Summation with filtering
        filtered = [x for x in row if x % 5 == 0]
        bonus = sum(filtered) // 10  # Irrelevant bonus calculation
        row_total += bonus // 5  # Minimal impact but distracts
        
        total += row_total
    
    # Final adjustment using set operation (distraction)
    unique_values = set()
    for r in matrix:
        unique_values.update(r)
    entropy_factor = math.log(len(unique_values) + 1)
    
    return total * (overhead_factor ** 2) * (1 + 0.1 * math.sin(entropy_factor))

# Execute main computation
final_bandwidth = aggregate_throughput(resource_matrix, efficiency_map)

# Print result as required
print(f"Result: {final_bandwidth}")