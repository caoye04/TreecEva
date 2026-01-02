from itertools import combinations

# Simulate sensor data validation and scoring for an autonomous drone system
def validate_sensor_readings(readings):
    valid_count = 0
    temp_alerts = []
    for reading in readings:
        if not (0 <= reading['temp'] <= 100):
            temp_alerts.append(reading['id'])
        if reading['status'] == 'OK' and reading['temp'] < 85:
            valid_count += 1
    return valid_count

def calculate_redundancy_score(groups):
    total_pairs = 0
    for group in groups:
        total_pairs += len(list(combinations(group, 2)))
    return total_pairs

def assess_consistency(log_entries):
    changes = 0
    prev_mode = log_entries[0]['mode']
    for entry in log_entries[1:]:
        if entry['mode'] != prev_mode:
            changes += 1
            prev_mode = entry['mode']
    return changes

def preliminary_normalization(data):
    # Irrelevant normalization function - distractor
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) / mean_val for x in data]
    return [round(x, 3) for x in normalized]

def evaluate_performance(metrics, weights):
    score = 0.0
    weight_sum = 0.0
    
    # Real computation steps
    if metrics['sensor_valid'] > 3:
        score += metrics['sensor_valid'] * weights['sensor']
        weight_sum += weights['sensor']
    
    consistency_penalty = metrics['mode_changes'] * 2.5
    score += (10 - consistency_penalty) * weights['consistency']
    weight_sum += weights['consistency']
    
    redundancy_bonus = min(metrics['redundant_pairs'], 15)
    score += redundancy_bonus * weights['redundancy']
    weight_sum += weights['redundancy']
    
    # Distractor calculation - does not affect final result
    phantom_metric = metrics.get('phantom', 0)
    debug_factor = 1.0
    if phantom_metric > 5:
        debug_factor *= 0.9
    
    # Final weighted score
    final = score / weight_sum if weight_sum > 0 else 0
    return round(final, 4)

# Main execution
if __name__ == '__main__':
    # Sensor data
    sensors = [
        {'id': 'S1', 'temp': 72, 'status': 'OK'},
        {'id': 'S2', 'temp': 88, 'status': 'OK'},
        {'id': 'S3', 'temp': 65, 'status': 'OK'},
        {'id': 'S4', 'temp': 91, 'status': 'ERROR'},
        {'id': 'S5', 'temp': 77, 'status': 'OK'}
    ]
    
    # Grouping for redundancy check (distractor has partial relevance)
    sensor_groups = [['S1', 'S2', 'S3'], ['S4', 'S5']]
    
    # System mode logs
    logs = [
        {'time': 1, 'mode': 'IDLE'},
        {'time': 2, 'mode': 'IDLE'},
        {'time': 3, 'mode': 'FLIGHT'},
        {'time': 4, 'mode': 'FLIGHT'},
        {'time': 5, 'mode': 'LANDING'},
        {'time': 6, 'mode': 'IDLE'}
    ]
    
    # Extract key metrics
    valid_sensors = validate_sensor_readings(sensors)
    redundant_pairs = calculate_redundancy_score(sensor_groups)
    mode_transitions = assess_consistency(logs)
    
    # Irrelevant data processing - distractor
    temp_data = [72, 88, 65, 91, 77]
    normalized_temps = preliminary_normalization(temp_data)
    
    # Performance weights
    weights = {
        'sensor': 0.4,
        'consistency': 0.35,
        'redundancy': 0.25
    }
    
    # Key metrics dictionary
    performance_metrics = {
        'sensor_valid': valid_sensors,           # 3 valid: S1, S3, S5 (S2 temp>=85, S4 status ERROR)
        'mode_changes': mode_transitions,        # Changes: IDLE->FLIGHT, FLIGHT->LANDING, LANDING->IDLE => 3
        'redundant_pairs': redundant_pairs,      # C(3,2)=3, C(2,2)=1 => 4
        'phantom': 7  # Unused field - red herring
    }
    
    # Critical statement
    final_score = evaluate_performance(performance_metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")