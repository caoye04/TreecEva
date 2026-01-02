from itertools import combinations

# Simulate sensor stress levels across structural beams
def analyze_beam_stress(readings):
    filtered_readings = [r for r in readings if r > 0]
    sorted_readings = sorted(filtered_readings)
    
    # Compute moving average window (irrelevant to final result)
    window_avg = []
    for i in range(len(sorted_readings) - 1):
        window_avg.append((sorted_readings[i] + sorted_readings[i+1]) / 2)
    
    # Identify anomalous spikes (distractor computation)
    spike_pairs = list(combinations(sorted_readings, 2))
    spike_count = 0
    for a, b in spike_pairs:
        if abs(a - b) > 30:
            spike_count += 1

    # Key computation path
    base_threshold = 15
    valid_stress = [v for v in sorted_readings if v >= base_threshold]
    total_stress = sum(valid_stress)
    measurement_count = len(valid_stress)
    
    if measurement_count == 0:
        avg_stress = 0
    else:
        avg_stress = total_stress / measurement_count

    # Correction logic based on system load history (semi-relevant)
    recent_loads = [88, 92, 76, 85, 90]
    peak_load = max(recent_loads)
    load_ratio = peak_load / 100.0
    
    # Dead code: this function is defined but not used
    def calculate_risk_factor(data):
        return sum(d**2 for d in data) / len(data)
    
    # Unused intermediate
    normalized_readings = [x / max(valid_stress) for x in valid_stress if max(valid_stress) > 0]
    
    # Core result calculation
    stability_factor = 0.85 if avg_stress > 50 else 1.15
    correction_factor = stability_factor * (1 + (load_ratio * 0.1))
    equilibrium_score = round(avg_stress * correction_factor, 2)
    
    # Irrelevant transformation chain
    mapped_scores = list(map(lambda x: x * 1.05, window_avg))
    filtered_mapped = [m for m in mapped_scores if m < 100]
    
    # Print final target result
    print(f"Result: {equilibrium_score}")
    return equilibrium_score

# Input data from sensor array
sensor_data = [12, -5, 67, 45, 33, 78, 0, 23, 55, 61, 14, 48, 39, 82]
analyze_beam_stress(sensor_data)