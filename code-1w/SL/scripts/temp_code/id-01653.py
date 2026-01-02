from collections import defaultdict

# Simulate system health metrics from distributed nodes
def analyze_node_load(loads):
    avg = sum(loads) / len(loads)
    peak = max(loads)
    normalized_peak = round(peak / (avg + 1e-5), 3)
    return avg, normalized_peak

def validate_checksum(sequence):
    # Irrelevant checksum validation (not used in final logic)
    chk = 0
    for num in sequence:
        chk ^= num * 3
    return chk % 100

def process_metrics(raw_data, config):
    stats = defaultdict(int)
    temp_results = []
    total_nodes = len(raw_data)
    
    # Misleading preprocessing: transforms not directly affecting output
    scaled_values = [max(1, int(x ** 0.5)) for x in range(len(raw_data))]  
    dummy_state = [0] * 5
    for i in range(len(dummy_state) - 1):
        dummy_state[i+1] = dummy_state[i] + scaled_values[i % len(scaled_values)]
    
    # Core logic begins
    for node_id, readings in raw_data.items():
        base_avg, stress_ratio = analyze_node_load(readings)
        
        # Conditional expression used for state tracking
        severity = 'high' if stress_ratio > config['stress_threshold'] else 'normal'
        
        stats['total_readings'] += len(readings)
        stats['aggregate_load'] += base_avg
        
        if severity == 'high':
            stats['overloaded'] += 1
            # Add transformed value that will be later filtered out
            temp_results.append(int(base_avg) ^ 15)
        else:
            # Only normal nodes contribute clean data
            temp_results.append(int(base_avg) + 2)

    # Secondary filtering with bitwise distraction
    cleaned = []
    mask = config['bit_filter']
    for val in temp_results:
        masked_val = val & mask
        cleaned.append(masked_val)
    
    # Final aggregation
    raw_sum = sum(cleaned)
    adjustment_factor = 0.85 if stats['overloaded'] > 0 else 1.0
    intermediate = raw_sum * adjustment_factor
    
    # Red herring computation: uses unused helper
    _ = validate_checksum([int(intermediate), stats['overloaded'], total_nodes])
    
    # Key result calculation
    final_score = int(intermediate - stats['aggregate_load'])
    
    return final_score

# Input setup
thresholds = {
    'stress_threshold': 1.4,
    'bit_filter': 0xFF  # 8-bit truncation
}

data = {
    'node_01': [12, 15, 10, 18],
    'node_02': [45, 50, 48, 60],  # High stress
    'node_03': [8, 10, 14, 9],
    'node_04': [55, 52, 58, 61],  # High stress
    'node_05': [20, 18, 22, 21]
}

# Execution point
final_score = process_metrics(data, thresholds)
print(f"Result: {final_score}")