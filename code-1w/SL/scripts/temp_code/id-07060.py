import math

# Simulated sensor data processing for environmental monitoring system
def fetch_raw_readings():
    return [32.1, 28.5, 35.6, 40.2, 25.8, 31.4, 37.9, 29.3, 34.0, 38.7]

def filter_outliers(data, threshold=3.0):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) / std_dev <= threshold]

def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def discretize_levels(data, levels=5):
    step = 1.0 / levels
    return [int(value / step) for value in data]

def detect_anomalies(levels):
    # Simulate complex pattern detection with red herrings
    anomalies = []
    for i in range(1, len(levels)):
        if levels[i] == 4 and levels[i-1] == 0:
            anomalies.append(i)
    return anomalies

def compute_entropy(data):
    # Irrelevant computation - distractor
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

def generate_report_summary(logs):
    # Dead code path - never actually used for final result
    summary = {
        'entry_count': len(logs),
        'peak_level': max(logs),
        'stability_index': sum(1 for x in logs if x == 2),
        'transition_points': [i for i in range(1, len(logs)) if logs[i] != logs[i-1]],
        'computed_entropy': compute_entropy(logs)  # Distractor call
    }
    return summary

def calculate_baseline_drift(data):
    # Misleading intermediate calculation
    drift = 0.0
    for i in range(len(data) - 1):
        drift += abs(data[i+1] - data[i])
    return drift / len(data) if data else 0

def temporal_smoothing(values):
    # Unused smoothing function - decoy
    smoothed = [values[0]]
    for i in range(1, len(values)-1):
        smoothed.append(sum(values[i-1:i+2]) / 3)
    smoothed.append(values[-1])
    return smoothed

def validate_consistency(levels):
    # Complex validation with irrelevant logic branches
    if not levels:
        return False
    valid_transitions = True
    transitions = 0
    for i in range(1, len(levels)):
        if abs(levels[i] - levels[i-1]) > 2:
            transitions += 1
            if transitions > 2:
                valid_transitions = False
                break
    high_count = sum(1 for level in levels if level >= 3)
    low_ratio = high_count / len(levels)
    return valid_transitions and 0.1 <= low_ratio <= 0.9

def analyze_readings(processed_logs):
    # Core analysis with embedded distractions
    if not processed_logs or len(processed_logs) < 5:
        return -1
    
    # Key transformation chain
    normalized = normalize_readings(processed_logs)
    discretized = discretize_levels(normalized)
    
    # Distractor: unused transformations
    smoothed_data = temporal_smoothing(normalized)  # Computed but unused
    baseline_shift = calculate_baseline_drift(processed_logs)  # Calculated but irrelevant
    
    # Real logic continues
    if not validate_consistency(discretized):
        return -2
    
    anomalies = detect_anomalies(discretized)
    
    # Secondary irrelevant check
    if len(anomalies) > 0:
        # This block runs but doesn't affect final result directly
        anomaly_severity = sum(discretized[i] for i in anomalies)
        adjustment_factor = math.sin(anomaly_severity) if anomaly_severity > 0 else 0
    else:
        adjustment_factor = 0.0
    
    # Final diagnostic calculation - this is what matters
    base_score = sum(discretized) * 10
    penalty = len([x for x in discretized if x == 0]) * 5
    final_diagnostic = base_score - penalty + 7  # +7 is critical offset
    
    # Red herring: modifying unrelated variables
    report_context = {
        'timestamp': 123456789,
        'version': '2.1.5',
        'diagnostics_run': True,
        'ignored_value': final_diagnostic * 0.1  # Diversion
    }
    
    return int(final_diagnostic)

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = fetch_raw_readings()
    filtered_data = filter_outliers(raw_sensor_data)
    processed_logs = normalize_readings(filtered_data)  # Note: re-normalizing already normalized?
    # Wait - correction: pass through discretization chain properly
    processed_for_analysis = discretize_levels(normalize_readings(filtered_data))
    final_diagnostic = analyze_readings(processed_for_analysis)
    print(f"Target result: {final_diagnostic}")