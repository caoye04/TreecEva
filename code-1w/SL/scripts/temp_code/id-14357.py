def analyze_readings(readings):
    # Irrelevant transformation (dead path)
    normalized = [x * 0.95 + 2 for x in readings]
    
    # Distractor: complex but unused calculation
    baseline_shift = sum([abs(a - b) for a, b in zip(readings[1:], readings[:-1])]) / len(readings) if len(readings) > 1 else 0
    
    # Relevant: compute moving average over 3 points
    moving_avg = [(readings[i] + readings[i+1] + readings[i+2]) / 3 for i in range(len(readings)-2)]
    
    # Red herring: unused lambda
    outlier_score = lambda x: (x - min(readings)) / (max(readings) - min(readings)) if max(readings) != min(readings) else 0
    
    # Distractor: dead code with bitwise decoy
    mask = 0b101010
    masked_values = [x ^ mask & 0xF for x in readings]
    
    # Relevant: count how many are above 75
    high_count = len([x for x in readings if x > 75])
    return moving_avg, high_count

# Simulated health sensor data
temp_data = [68, 72, 76, 81, 85, 83, 77, 73, 70, 69]

# Unused secondary data (distractor)
blood_pressure = [118, 122, 127, 130, 135, 132, 128, 124, 121, 119]
heart_rate = [72, 74, 79, 85, 88, 86, 80, 75, 73, 71]

# Threshold configuration (mixed relevance)
thresholds = {
    'temp_crisis': 80,
    'warning_level': 75,  # Actually used
    'decay_factor': 0.88,
    'bit_pattern': 0xFF00
}

# Decoy function with recursive red herring
def compute_stability(data, depth=0):
    if depth >= 3:
        return 0
    shifted = [data[i+1] - data[i] for i in range(len(data)-1)]
    return abs(sum(shifted)) + compute_stability(shifted, depth + 1)

# Real processing pipeline
health_data = {
    'metrics': temp_data,
    'source': 'sensor_array_A',
    'version': 'v2.1'
}

# Lambda transformation (actually used later)
data_enhancer = lambda d: [x + 1 for x in d['metrics'] if x < 80]

# Intermediate irrelevant computation
shadow_metric = (sum(temp_data) // len(temp_data)) ^ 0b1111

# Another decoy: sorting unrelated list
sorted_bpm = sorted(heart_rate, reverse=True)
ranked_bpm = {i: val for i, val in enumerate(sorted_bpm)}  # Unused dict

# Core logic disguised among distractions
def process_metrics(data, config):
    raw_vals = data['metrics']
    enhanced = data_enhancer(data)
    
    # Real operation hidden in noise
    avg_enhanced = sum(enhanced) / len(enhanced) if enhanced else 0
    
    # Distractor: complex dictionary manipulation
    metadata_ops = {
        k: v * 2 if isinstance(v, int) else v.upper() for k, v in data.items() if k != 'metrics'
    }
    
    # Bitwise red herring
    trigger_flag = (len(raw_vals) << 2) & 0xFF
    
    # Critical step: use of comparison and filtering
    critical_count = len([x for x in raw_vals if x > config['warning_level']])
    
    # Real aggregation
    base_mean = sum(raw_vals) / len(raw_vals)
    
    # Final composite score - only one path matters
    stability_index = abs(base_mean - avg_enhanced) * 10
    diagnostic_score = base_mean + (critical_count * 2) - stability_index
    
    # Dead branch (never taken due to fixed condition)
    if trigger_flag < 0:
        diagnostic_score ^= 0xFFFF
    
    return int(diagnostic_score)

# Execute main logic
interim_results = analyze_readings(temp_data)
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")