import math

# Simulated sensor data from a distributed environmental monitoring system
def fetch_sensor_data():
    return [
        23.4, 19.5, 22.1, 25.6, 18.2, 20.8, 24.0, 26.5, 19.0, 21.3,
        22.7, 24.9, 20.4, 23.8, 18.9, 25.1, 21.6, 22.3, 24.7, 19.9
    ]

# Legacy function – not used in current logic (red herring)
def legacy_normalize(x):
    return (x - min(x)) / (max(x) - min(x))

# Irrelevant transformation chain (dead path)
def transform_readings(data):
    adjusted = [math.sin(x / 10) for x in data]
    scaled = [y * 100 for y in adjusted]
    return sorted(scaled, reverse=True)

# Unused statistical function (distractor)
def compute_skewness(data):
    n = len(data)
    mean_val = sum(data) / n
    stdev = (sum((x - mean_val) ** 2 for x in data) / n) ** 0.5
    if stdev == 0:
        return 0
    skew = sum(((x - mean_val) / stdev) ** 3 for x in data) / n
    return round(skew, 4)

# Misleading intermediate diagnostic (decoy)
def generate_fallback_diagnostics(arr):
    peaks = [x for x in arr if x > 24.0]
    avg_peak = sum(peaks) / len(peaks) if peaks else 0
    return {'peak_count': len(peaks), 'avg_excess': round(avg_peak - 24.0, 2)}

# Core processing function with relevant logic


threshold_map = {
    'warning_low': 19.0,
    'caution_high': 24.5,
    'critical_high': 25.5
}

# String-based status encoder (uses string method – required feature)
def encode_status(value):
    if value < threshold_map['warning_low']:
        return 'LOW_WARNING'.lower()
    elif value > threshold_map['critical_high']:
        return 'CRITICAL_ALERT'.replace('_', '').upper()
    elif value > threshold_map['caution_high']:
        return 'CAUTION_ZONE'.lstrip('C').rstrip('NE')
    else:
        return 'NORMAL'

# Main metric processor
health_scores = []
def process_metrics(readings, config):
    global health_scores
    health_scores = []
    
    # Irrelevant sorting (distractor)
    sorted_readings = sorted(readings)
    reversed_readings = sorted_readings[::-1]
    
    # Dummy accumulator (misleading)
    cumulative_drift = 0.0
    for i in range(len(reversed_readings)):
        if i % 3 == 0:
            cumulative_drift += math.cos(reversed_readings[i])

    # Actual logic: count readings in caution/critical zones
    critical_count = 0
    caution_count = 0
    normal_count = 0
    
    status_log = []
    for val in readings:
        status = encode_status(val)
        status_log.append(status)
        
        # Real branching logic
        if 'CRITICAL' in status:
            critical_count += 1
        elif 'CAUTIO' in status:  # Note: uses transformed string
            caution_count += 1
        elif status == 'NORMAL':
            normal_count += 1
    
    # Compute weighted health score
    base_score = 100.0
    base_score -= critical_count * 15.0
    base_score -= caution_count * 5.0
    base_score += normal_count * 1.0
    
    # Additional penalty if any reading exceeds 26.0 (not in thresholds!)
    if any(x > 26.0 for x in readings):
        base_score -= 10.0
    
    # Hidden rule: if 'CRITICAL_ALERT' appears as full string anywhere in log (it won't due to transform), add bonus
    full_alert = 'CRITICAL_ALERT'
    if full_alert in ''.join(status_log):  # Impossible path
        base_score += 20.0
    
    # Final adjustment based on length of status strings (actual subtle effect)
    total_char_length = sum(len(s) for s in status_log)
    if total_char_length > 120:
        base_score -= 5.0
    
    health_scores.append(round(base_score, 2))
    
    # Secondary metric: stability index (unused in final result)
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    stability_index = round(100 / (1 + variance), 2)
    
    # Key result variable
    final_diagnostic = int(round(base_score))
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    raw_data = fetch_sensor_data()
    
    # Apply irrelevant transformation (distraction)
    processed_noise = transform_readings(raw_data)
    
    # Generate decoy diagnostics
    fallback_diag = generate_fallback_diagnostics(raw_data)
    
    # The real execution path
    final_diagnostic = process_metrics(raw_data, threshold_map)
    
    # Print required result
    print(f"Result: {final_diagnostic}")