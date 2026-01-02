from collections import defaultdict

# Simulated sensor data with timestamps and readings
data_log = [
    {'time': 0.1, 'sensor_a': 5, 'sensor_b': 3, 'status': 'active'},
    {'time': 0.2, 'sensor_a': 7, 'sensor_b': 8, 'status': 'active'},
    {'time': 0.3, 'sensor_a': 6, 'sensor_b': 4, 'status': 'idle'},
    {'time': 0.4, 'sensor_a': 9, 'sensor_b': 9, 'status': 'active'},
    {'time': 0.5, 'sensor_a': 3, 'sensor_b': 7, 'status': 'active'}
]

# Irrelevant baseline for distraction
baseline_offset = 0.05
scaling_factor = 1.2
offset_tracker = [baseline_offset * i for i in range(5)]

# Distractor: unused helper function
def normalize_value(x):
    return (x - min(2, x)) / max(1, x)

# Main processing function
def process_metrics(log_entries, threshold=6):
    cumulative = 0
    event_count = 0
    status_counter = defaultdict(int)
    transient_buffer = []

    # Secondary loop for time coherence check (partially relevant)
    for entry in log_entries:
        status_counter[entry['status']] += 1
        
    # Primary logic: compute efficiency based on high-activity events
    for entry in log_entries:
        raw_sum = entry['sensor_a'] + entry['sensor_b']
        active_boost = 1.5 if entry['status'] == 'active' else 1.0
        weighted = raw_sum * active_boost
        
        # Track only entries above threshold after boosting
        if weighted > threshold:
            cumulative += weighted
            event_count += 1
            transient_buffer.append(weighted)  # used only for length
        
        # Distractor: dead code path (never executed due to data)
        if entry['time'] < 0.05:
            cumulative -= 2  # unreachable

    # Efficiency defined as average of qualifying events, adjusted by buffer size
    base_efficiency = cumulative / event_count if event_count > 0 else 0
    
    # Distractor: complex but unused calculation
    peak_moment = max(entry['sensor_a'] * entry['sensor_b'] for entry in log_entries)
    decay_constant = sum(offset_tracker) * scaling_factor

    # Key computation
    adjustment_factor = len(transient_buffer)  # depends on control flow history
    final_adjustment = lambda x, adj: x + (adj * 0.1)
    
    efficiency_score = final_adjustment(base_efficiency, adjustment_factor)
    
    # Misleading transformation
    post_processed = [efficiency_score * scaling_factor for _ in range(2)]
    
    final_output = efficiency_score  # Final assignment
    return final_output

# Execution point of interest
efficiency_score = process_metrics(data_log, threshold=6)
print(f"Result: {efficiency_score}")