from collections import defaultdict, Counter
import math

# Simulate sensor data aggregation across multiple nodes
def collect_sensor_readings():
    raw_readings = [
        (1, [23.4, 25.1, 22.7, 24.8]),
        (2, [19.5, 20.3, 18.9, 21.0]),
        (3, [30.2, 31.5, 29.8, 32.1]),
        (4, [15.6, 16.7, 14.9, 17.3])
    ]
    aggregated = defaultdict(list)
    for node_id, readings in raw_readings:
        aggregated[node_id].extend(readings)
    return aggregated

# Irrelevant helper: computes statistical dispersion (not used in final path)
def compute_dispersion(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

# Misleading transformation chain
def filter_outliers(data_block, limit=2.5):
    cleaned = {}
    for k, v in data_block.items():
        cleaned[k] = [x for x in v if x < 35.0]  # All pass, red herring
    return cleaned

# Decoy function: looks important but unused
def generate_compatibility_matrix(n):
    matrix = [[(i * j) % 7 for j in range(n)] for i in range(n)]
    return matrix  # Never called

# Core transformation: shifts and scales relevant data
def transform_readings(aggregated_data):
    shifted = {}
    for idx, (key, vals) in enumerate(aggregated_data.items()):
        offset = (idx + 1) * 1.5
        shifted[key] = [v + offset for v in vals]
    return shifted

# Another distractor: simulates checksum but unused
class ChecksumValidator:
    def __init__(self, seed=100):
        self.seed = seed
        self.history = []
    
    def compute(self, seq):
        total = 0
        for i, x in enumerate(seq):
            total += (x * (i + 1)) % self.seed
        return total % 100

# Heavily nested analysis logic with red herrings
def analyze_pattern(data_input, config_map):
    result_counter = Counter()
    temp_accum = 0
    
    for node_id, samples in data_input.items():
        base_threshold = config_map.get(node_id, 27.0)
        above_count = 0
        below_count = 0
        
        for val in samples:
            # Complex conditional with misleading intermediate flags
            is_critical = val > base_threshold + 3.5
            is_marginal = abs(val - base_threshold) <= 2.0
            is_stable = val < base_threshold - 1.0
            
            if is_critical:
                temp_accum += val * 0.1
            elif is_marginal:
                temp_accum -= 0.05
            
            if is_stable:
                below_count += 1
            else:
                above_count += 1
        
        # Only this line contributes to final result
        result_counter['total_surplus'] += above_count - below_count
    
    # Dead code branch: never reached due to structure
    if temp_accum < 0:
        fallback = sum(result_counter.values()) * -1
        return fallback
    
    # Final computation
    net_balance = result_counter['total_surplus'] * 100
    scaling_factor = config_map.get('scale', 1.0)
    final_score = net_balance * scaling_factor
    
    return int(final_score)

# Unused recursive function (decoy for complexity)
def recursive_hash_chain(n):
    if n <= 1:
        return n
    return recursive_hash_chain(n-1) + recursive_hash_chain(n-2)

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw data
    sensor_data = collect_sensor_readings()
    
    # Step 2: Apply irrelevant filtering (no effect)
    filtered_data = filter_outliers(sensor_data)
    
    # Step 3: Transform data with meaningful shift
    transformed_data = transform_readings(filtered_data)
    
    # Step 4: Build configuration map with decoy entries
    threshold_map = {
        1: 26.0,
        2: 22.0,
        3: 30.5,
        4: 18.0,
        'scale': 1.0,
        'debug_mode': False,
        'timeout': 30
    }
    
    # Step 5: Analyze pattern - critical point
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Print result
    print(f"Target result: {final_diagnostic}")