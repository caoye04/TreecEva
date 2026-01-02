import math

# Simulated system performance analysis with distractors
def analyze_component_health(reading, threshold_map):
    # Irrelevant health check with decoy logic
    if reading < threshold_map.get('low', 0.3):
        return 'CRITICAL'
    elif reading > threshold_map.get('high', 0.8):
        return 'OPTIMAL'
    return 'STABLE'

# Unused recursive function - red herring
def calculate_depth(n):
    if n <= 1:
        return 1
    return n * calculate_depth(n - 2)

# Decoy data transformation pipeline
def transform_stream(data_packets):
    processed = []
    for packet in data_packets:
        temp_val = (packet ** 2 + 7) % 13
        if temp_val > 5:
            processed.append(temp_val * 1.5)
    return processed

# Core evaluation logic disguised among distractions
def compute_efficiency_index(values):
    total = 0
    weight_factor = 1.0
    for v in values:
        if v > 0:
            total += math.log(v + 1) * weight_factor
            weight_factor *= 0.9  # Decay factor
    return round(total, 6)

# Misleading aggregation function that's never called
def aggregate_diagnostics(records):
    stats = {}
    for r in records:
        key = r['type']
        if key not in stats:
            stats[key] = []
        stats[key].append(r['value'])
    return {k: sum(v)/len(v) for k, v in stats.items()}

# Real computation buried in noise
def evaluate_performance(log, config):
    # Extract relevant metrics from nested structure
    readings = log['metrics']['cpu_load_history'][-5:]  # Last 5 readings
    
    # Distractor: irrelevant slice and transformation
    shadow_buffer = log['metrics']['memory_trace'][::2][:8]
    shadow_sum = sum([x * 0.1 for x in shadow_buffer if x > 50])
    
    # Red herring dictionary operations
    temp_registry = {f'item_{i}': math.sqrt(readings[i]) for i in range(len(readings))}
    temp_registry.update({'dummy_flag': True, 'version': '2.1'})
    
    # Actual signal extraction
    filtered_readings = [r for r in readings if config['threshold'] <= r <= 95.0]
    
    # Decoy list comprehension with side-effect-free computation
    derived_features = [[x + y for x in readings[:3]] for y in (2, 5)]
    feature_total = sum(sum(row) for row in derived_features)
    
    # Critical calculation path
    base_score = compute_efficiency_index(filtered_readings)
    adjustment = len(readings) - len(filtered_readings)
    penalty = adjustment * config['penalty_unit']
    
    # Hidden correction using slicing and condition
    history_slice = log['metrics']['cpu_load_history']
    recent_trend = history_slice[-3:]
    if all(r < 70 for r in recent_trend):
        penalty -= 0.75  # Recovery bonus
    
    # Final composition
    raw_result = base_score - penalty
    final_value = max(1.0, round(raw_result, 6))
    
    # Dead code path - never executed due to logic
    if False and 'debug' in log:
        print(f'Debug: {final_value}')
        backup_copy = log.copy()
        backup_copy['audit'] = True
        
    return final_value

# Main execution block
if __name__ == '__main__':
    # Simulated input data with extra fields
    metrics_log = {
        'timestamp': 1712345678,
        'node_id': 'CN-4X',
        'metrics': {
            'cpu_load_history': [65.2, 78.1, 88.3, 72.4, 69.8, 75.6, 81.2, 66.9, 70.1, 73.7],
            'memory_trace': [45, 67, 89, 52, 78, 91, 44, 63, 82, 58, 77, 93],
            'disk_iops': [120, 135, 110, 140],
            'network_kbps': [8000, 8200, 7950]
        },
        'version': '3.4.1'
    }

    # Configuration with misleading entries
    baseline_config = {
        'threshold': 68.0,
        'penalty_unit': 0.85,
        'activation_window': 3,
        'debug_mode': False,
        'retention_days': 30
    }

    # Spurious variable assignments
    temp_analysis = metrics_log['metrics']['memory_trace'][1:6:2]
    normalization_factor = sum(temp_analysis) / len(temp_analysis)
    adjusted_values = [x / normalization_factor for x in temp_analysis]

    # Key execution point
    final_score = evaluate_performance(metrics_log, baseline_config)
    
    # Secondary distractor computation
    outlier_count = 0
    for val in metrics_log['metrics']['cpu_load_history']:
        if val > 90 or val < 40:
            outlier_count += 1
    compliance_rate = (1 - (outlier_count / len(metrics_log['metrics']['cpu_load_history']))) * 100

    # Output only the target result
    print(f"Target result: {final_score}")