from collections import defaultdict, Counter

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, count):
    return [baseline + (i * 0.3) % 2.5 for i in range(count)]

def filter_outliers(data, limit=1.75):
    return [x for x in data if x <= limit]

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

def compute_entropy(arr):
    freqs = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simulated pseudo-entropy
    return round(entropy, 6)

def assess_coherence(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs) if diffs else 0.0

def map_severity(value):
    if value < 0.5:
        return 'low'
    elif value < 1.2:
        return 'medium'
    else:
        return 'high'

# Irrelevant helper - dead code path
def deprecated_normalization(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [x/magnitude for x in vec] if magnitude else vec

def analyze_readings(data, thresholds):
    # Complex nested logic with distractors
    temp_log = []
    alert_count = 0
    cumulative_score = 0.0
    mode_distribution = defaultdict(int)
    
    for idx, val in enumerate(data):
        category = 'unknown'
        if val < thresholds['critical']:
            category = 'safe'
        elif val < thresholds['warning']:
            category = 'elevated'
        else:
            category = 'critical'
            
        # Distractor: complex but unused transformation
        transformed = (val ** 2 + 1e-4) ** 0.5
        normalized = transformed / (transformed + 1)
        temp_log.append({'index': idx, 'raw': val, 'norm': normalized, 'cat': category})
        
        mode_distribution[category] += 1
        cumulative_score += val * (idx + 1)  # Weighted accumulation

    # Unused intermediate results - red herring
    distribution_stats = dict(mode_distribution)
    peak_category = max(distribution_stats, key=distribution_stats.get)
    coherence_metric = assess_coherence(data)
    entropy_value = compute_entropy([round(x, 2) for x in data])

    # Decoy computation - looks important but not used
    anomaly_score = 0
    for k, v in mode_distribution.items():
        if k != 'safe':
            anomaly_score += v * {'elevated': 1.5, 'critical': 3.0}[k]

    # Actual answer path - subtle and interwoven
    adjustment_factor = 0.87
    if mode_distribution['critical'] > 0:
        adjustment_factor *= 0.7
    if coherence_metric < 0.6:
        adjustment_factor *= 1.15
    
    base_index = int(cumulative_score // 10)
    final_diagnostic = int((base_index * adjustment_factor) - (entropy_value * 10))
    
    # Final irrelevant transformation
    checksum = sum(f'{final_diagnostic}'.encode()) % 100
    final_diagnostic += checksum // 10  # Minor deterministic bump
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate realistic sensor data
    raw_sensor_data = generate_signals(baseline=0.42, count=35)
    
    # Apply filtering - relevant
    filtered_data = filter_outliers(raw_sensor_data, limit=1.9)
    
    # Smoothing - relevant to final data
    processed_data = rolling_average(filtered_data, window=3)
    
    # Threshold configuration - critical
    threshold_map = {
        'critical': 0.85,
        'warning': 1.35,
        'maintenance': 1.6
    }
    
    # Dead variables - distraction
    calibration_sequence = list(enumerate([x*0.98 for x in processed_data[::3]]))
    alignment_matrix = [[i+j for j in range(3)] for i in range(3)]
    metadata_trace = dict(zip(['v1', 'v2', 'v3'], [len(processed_data), sum(processed_data), processed_data[-1]]))
    
    # Lambda-based transform - looks important but unused
    enhance_signal = lambda arr, factor: [x * (factor + 0.1) for x in arr]
    boosted_readings = enhance_signal(processed_data, 1.05)  # Computed but unused
    
    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")