from collections import Counter, defaultdict

# Simulate sensor data with noise and metadata
def generate_sensor_data():
    raw_values = [23, 45, 45, 12, 67, 67, 67, 89, 12, 23]
    timestamps = [1623456780 + i for i in range(10)]
    statuses = ['OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK', 'ERROR', 'OK', 'OK', 'WARNING']
    
    # Misleading transformation
    processed_noise = [x * 2 - 1 for x in raw_values if x > 20]
    filtered_pairs = [(raw_values[i], statuses[i]) for i in range(len(raw_values)) if timestamps[i] % 2 == 1]
    
    return list(zip(raw_values, timestamps, statuses))

# Analyze frequency and state transitions
def analyze_patterns(data):
    freq_counter = Counter()
    state_transitions = defaultdict(int)
    prev_status = None
    total_valid = 0
    
    for val, ts, status in data:
        freq_counter[val] += 1
        
        # Irrelevant aggregation
        temp_calc = (ts % 1000) * 0.01
        
        if prev_status is not None:
            state_transitions[(prev_status, status)] += 1
        prev_status = status
        
        if status == 'OK':
            total_valid += 1

    # Dead computation path (not used later)
    avg_interval = sum(timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)) / (len(timestamps)-1) if len(timestamps) > 1 else 0
    
    return freq_counter, state_transitions, total_valid

# Core scoring logic with distractors
def calculate_final_score(data, thresholds):
    freqs, transitions, valid_count = analyze_patterns(data)
    
    # Extract key values
    most_common_value = freqs.most_common(1)[0][1]  # frequency of most common reading
    unique_readings = len(set(v[0] for v in data))
    
    # Distractor variables
    error_transitions = transitions[('OK', 'ERROR')] + transitions[('WARNING', 'ERROR')]
    warning_count = sum(1 for _, _, s in data if s == 'WARNING')
    pseudo_entropy = len(transitions) * 0.5
    
    # Red herring calculation
    anomaly_score = 0
    for val, _, _ in data:
        if val > 50:
            anomaly_score += 1
        elif val < 15:
            anomaly_score += 0.5

    # Actual scoring components
    base_score = most_common_value * 10
    diversity_penalty = max(0, 5 - unique_readings) * 2
    stability_bonus = valid_count * 3
    
    # Final composition
    final_score = base_score - diversity_penalty + stability_bonus
    
    # Unused intermediate
    normalized_score = round(final_score / 10.0, 2) if unique_readings > 0 else 0.0
    
    return int(final_score)

# Main execution block
data = generate_sensor_data()
timestamps = [entry[1] for entry in data]  # unused duplicate extraction
thresholds = {'high': 50, 'low': 20, 'critical': 80}

# Key statement
final_score = calculate_final_score(data, thresholds)

print(f"Result: {final_score}")