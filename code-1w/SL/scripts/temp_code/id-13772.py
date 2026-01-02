def analyze_readings(readings):
    # Irrelevant preprocessing: normalize signal (distractor)
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)) * 100) for x in readings]
    peaks = [i for i in range(1, len(readings)-1) if readings[i-1] < readings[i] > readings[i+1]]
    avg = sum(readings) / len(readings)
    return avg

# Simulated sensor data from multiple sources (some irrelevant)
sensor_a = [120, 135, 142, 139, 158, 162, 150]
sensor_b = [98.6, 99.1, 97.3, 100.2, 98.8, 99.5, 97.9]
sensor_c = [85, 90, 92, 89, 94, 96, 93]  # Oxygen saturation levels

# Misleading aggregation (dead path)
total_avg = (sum(sensor_a) / len(sensor_a) + sum(sensor_b) / len(sensor_b) + sum(sensor_c) / len(sensor_c)) / 3

# Threshold configuration map for health metrics
threshold_map = {
    'hr': {'low': 50, 'high': 100},
    'temp': {'low': 97, 'high': 99},
    'o2': {'critical': 90}
}

# Composite health data structure with red herring fields
health_data = {
    'metrics': {
        'hr': { 'values': sensor_a, 'unit': 'bpm', 'weight': 0.6 },
        'temp': { 'values': sensor_b, 'unit': 'F', 'weight': 0.3 },
        'o2': { 'values': sensor_c, 'unit': '%', 'weight': 0.1 }
    },
    'metadata': {
        'patient_id': 'P7890',
        'timestamp': '2023-11-15T10:30:00Z',
        'location': 'Ward B',
        'device_version': 'v2.1'
    },
    'flags': ['stable_rhythm', 'no_fever', 'needs_review']  # Distractor list
}

# Auxiliary function that looks important but is unused
def compute_stability_index(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 2)

# Core processing function with key logic buried in distractions
def process_metrics(data, thresholds):
    hr_data = data['metrics']['hr']['values']
    temp_data = data['metrics']['temp']['values']
    o2_data = data['metrics']['o2']['values']
    
    # Real computation begins here
    hr_avg = sum(hr_data) / len(hr_data)
    temp_avg = sum(temp_data) / len(temp_data)
    o2_avg = sum(o2_data) / len(o2_data)
    
    # Weighted composite score calculation (critical path)
    composite_score = (
        hr_avg * data['metrics']['hr']['weight'] +
        temp_avg * data['metrics']['temp']['weight'] +
        o2_avg * data['metrics']['o2']['weight']
    )
    
    # Apply non-linear correction based on oxygen levels (key transformation)
    if o2_avg < thresholds['o2']['critical']:
        composite_score *= 0.85
    else:
        composite_score *= 1.05
    
    # Redundant string manipulation (distractor)
    status_msg = f"Vitals: HR={round(hr_avg)}, Temp={round(temp_avg,1)}, O2={o2_avg}%"
    status_tokens = status_msg.split(': ')[1].replace('%', '').split(', ')
    token_sums = sum([sum([ord(c) for c in t]) for t in status_tokens])  # Meaningless checksum
    
    # Nested conditional with early exit red herring (misleading)
    if 'urgent' in data['flags']:
        return -999  # Dead code path
    
    # Final adjustment using slicing and dictionary lookup
    adjustments = {'A': 1.02, 'B': 0.98, 'C': 1.01}
    category = 'B'
    if composite_score > 115:
        category = 'A'
    elif composite_score < 100:
        category = 'C'
    
    # Apply adjustment based on category (uses slicing to extract key)
    adjustment_key = list(adjustments.keys())[list(adjustments.values()).index(max(adjustments.values()))][::-1][::-1]  # Roundabout way to get 'A'
    adjusted_score = composite_score * adjustments[adjustment_key]
    
    # Final diagnostic includes bit shifting distraction
    final_diagnostic = int(adjusted_score) + (len(status_tokens) << 2)  # Adds 4*4=16
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Result: {final_diagnostic}")