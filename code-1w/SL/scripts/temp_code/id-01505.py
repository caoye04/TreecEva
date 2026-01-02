from collections import defaultdict

# Simulate sensor data aggregation with noise filtering and weighted scoring
def collect_sensor_data():
    raw_data = [
        ('temp', 23.5), ('pressure', 101.3), ('temp', 24.1),
        ('humidity', 45.0), ('pressure', 102.1), ('temp', 22.9),
        ('humidity', 47.2), ('light', 800), ('light', 810)
    ]
    
    aggregated = defaultdict(list)
    for sensor, value in raw_data:
        aggregated[sensor].append(value)
    
    # Misleading computation: average but not used in final logic
    averages = {}
    for sensor in aggregated:
        averages[sensor] = sum(aggregated[sensor]) / len(aggregated[sensor])
    
    # Actual processing: use median to resist outliers
    processed = {}
    for sensor, values in aggregated.items():
        sorted_vals = sorted(values)
        mid = len(sorted_vals) // 2
        processed[sensor] = sorted_vals[mid] if len(sorted_vals) % 2 == 1 else (sorted_vals[mid-1] + sorted_vals[mid]) / 2
    
    return processed

def apply_calibration(data):
    # Simulate hardware-specific calibration offsets
    calibrations = {'temp': -0.8, 'pressure': 0.5, 'humidity': 1.2, 'light': -10}
    calibrated = {}
    for sensor, value in data.items():
        if sensor in calibrations:
            calibrated[sensor] = value + calibrations[sensor]
        else:
            calibrated[sensor] = value
    
    # Dead code path - never accessed
    if False:
        for k in calibrated:
            calibrated[k] *= 1.0  # No-op

    # Introduce irrelevant transformation
    temp_rh_ratio = calibrated.get('temp', 0) / max(calibrated.get('humidity', 1), 0.1)
    
    return calibrated

def calculate_stability_index(data):
    # Assess environmental stability based on inverse variance proxy
    reference = {'temp': 23.0, 'pressure': 101.0, 'humidity': 45.0, 'light': 800}
    deviations = 0
    for sensor, ref in reference.items():
        if sensor in data:
            deviations += abs(data[sensor] - ref) * 0.1
    return max(5.0 - deviations, 0.5)  # Clamp to reasonable range

def calculate_final_score(data, weights):
    # Weights for each sensor contribution
    score_components = {}
    for sensor, weight in weights.items():
        if sensor in data:
            score_components[sensor] = data[sensor] * weight
    
    # Aggregate total score
    total = sum(score_components.values())
    
    # Apply non-linear boost based on stability
    stability = calculate_stability_index(data)
    boosted = total * (1 + stability / 10)
    
    # Unused intermediate that looks important
    normalized = boosted / (sum(weights.values()) + 1e-5)
    
    # Final adjustment: offset by fixed calibration residue
    final_score = int(boosted - 42.7)  # Deterministic integer output
    
    return final_score

# Main execution flow
def main():
    weights = {'temp': 0.3, 'pressure': 0.25, 'humidity': 0.2, 'light': 0.15}
    
    # Step 1: Collect and clean sensor data
    raw_results = collect_sensor_data()
    
    # Step 2: Apply physical calibration
    calibrated_results = apply_calibration(raw_results)
    
    # Step 3: Calculate final score using weights and stability
    final_score = calculate_final_score(calibrated_results, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")

    return final_score

# Execute
result = main()