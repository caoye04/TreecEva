import math

def analyze_component_health(sensor_data, threshold_map):
    # Irrelevant function - dead code path
    return {k: v > threshold_map.get(k, 75) for k, v in sensor_data.items()}

def preprocess_metrics(raw_entries):
    # Distractor: performs transformation but not used in final result
    processed = []
    for entry in raw_entries:
        if 'temp' in entry and entry['temp'] > 100:
            continue
        entry['norm'] = round(math.log(entry['value'] + 1), 3)
        processed.append(entry)
    return processed

def compute_trend(sequence):
    # Misleading function: looks important but unused
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

def calculate_weighted_sum(data_slice, weights):
    total = 0.0
    for i, val in enumerate(data_slice):
        total += val * weights.get(i, 0.5)
    return total

def evaluate_performance(log, config):
    # Core logic embedded in distractions
    
    # Red herring variables
    temp_cache = {}
    debug_trace = []
    cumulative_risk = 0
    
    # Relevant data extraction
    recent_values = [record['reading'] for record in log[-10:]]  # slicing operation
    
    # Decoy dictionary updates
    stats_summary = {
        'peak': max(recent_values),
        'trough': min(recent_values),
        'range': max(recent_values) - min(recent_values),
        'count': len(recent_values)
    }
    
    # Real computation begins
    filtered_readings = [x for x in recent_values if x >= config['min_valid']]
    
    # Bit manipulation distraction (irrelevant)
    bitmask = 0b101010
    masked_values = [v ^ bitmask for v in filtered_readings][:5]
    
    # Actual signal: average of middle 6 after sorting
    sorted_filtered = sorted(filtered_readings)
    mid_section = sorted_filtered[1:7]  # slicing again
    signal_base = sum(mid_section) / len(mid_section)
    
    # Use dictionary lookup for dynamic scaling
    adjustment_map = {'alpha': 1.2, 'beta': 0.9, 'gamma': 1.1}
    adjusted_signal = signal_base * adjustment_map.get(config['mode'], 1.0)
    
    # Apply modular arithmetic to simulate cyclic correction
    corrected = (adjusted_signal % 89) + (adjusted_signal // 100) * 12
    
    # Final nonlinear transformation
    final_score = int(math.floor((corrected ** 1.5) / 10))
    
    # Dead branch - never executed
    if len(debug_trace) > 1000:
        reset_system_state()
    
    return final_score

def reset_system_state():
    # Unused function - decoy
    pass

# Simulated input data
baseline_config = {
    'min_valid': 40,
    'mode': 'gamma',
    'timeout': 300,
    'retries': 3
}

metrics_log = [
    {'timestamp': '00:00', 'reading': 65, 'source': 'A'},
    {'timestamp': '00:05', 'reading': 70, 'source': 'B'},
    {'timestamp': '00:10', 'reading': 45, 'source': 'A'},
    {'timestamp': '00:15', 'reading': 95, 'source': 'C'},
    {'timestamp': '00:20', 'reading': 80, 'source': 'A'},
    {'timestamp': '00:25', 'reading': 35, 'source': 'B'},  # below threshold
    {'timestamp': '00:30', 'reading': 75, 'source': 'C'},
    {'timestamp': '00:35', 'reading': 85, 'source': 'A'},
    {'timestamp': '00:40', 'reading': 60, 'source': 'B'},
    {'timestamp': '00:45', 'reading': 55, 'source': 'C'},
    {'timestamp': '00:50', 'reading': 90, 'source': 'A'},
    {'timestamp': '00:55', 'reading': 50, 'source': 'B'}
]

# Sensor data - irrelevant but looks important
sensor_input = {
    'cpu_temp': 80,
    'gpu_load': 65,
    'mem_usage': 70,
    'disk_io': 45
}

thresholds = {'cpu_temp': 90, 'gpu_load': 75}

# Preprocessing call - result unused
unused_processed = preprocess_metrics(metrics_log)

# Trend analysis on unrelated sequence
dummy_sequence = [10, 20, 15, 25, 22]
unused_trend = compute_trend(dummy_sequence)

# Analyze health - completely irrelevant
health_report = analyze_component_health(sensor_input, thresholds)

# Key execution point
final_score = evaluate_performance(metrics_log, baseline_config)

print(f"Result: {final_score}")