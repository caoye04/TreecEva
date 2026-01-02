import itertools

def analyze_sensor_readings(readings):
    # Irrelevant preprocessing: normalize readings (not actually used in final path)
    normalized = [r / max(readings) for r in readings]
    filtered = [r for r in readings if r > 50]  # Only used in decoy branch
    
    # Distractor: complex transformation with no downstream effect
    shifted = list(itertools.starmap(lambda x, y: x - y, zip(filtered[1:], filtered[:-1])))
    smoothed = [sum(shifted[i:i+3]) / 3 for i in range(len(shifted) - 2)] if len(shifted) > 2 else [0]

    # Real logic buried here: compute variance-like metric
    mean_val = sum(readings) / len(readings)
    deviation_sq = sum((x - mean_val) ** 2 for x in readings)
    return deviation_sq / len(readings) if readings else 0

def validate_turbine_health(status_code):
    # Dead code path — never called but looks important
    critical_codes = {"E101", "E205", "W99"}
    return status_code in critical_codes

def decode_operational_mode(mode_str):
    # Unused function — red herring
    mode_map = {'A': 1, 'B': 2, 'C': 3}
    return mode_map.get(mode_str, 0)

def calculate_efficiency_score(rpm, load):
    # Decoy calculation that seems relevant but isn't used
    base = rpm * 0.01
    penalty = 0.1 * (load < 70)
    return round(base - penalty, 4)

def aggregate_metrics(sensor_data, limits):
    # Key variable initialization (distractor)
    temp_buffer = []
    diagnostic_log = []
    
    # Loop with enumerate and zip — required python features
    for idx, (key, readings) in enumerate(sensor_data.items()):  # enumerate used
        if idx % 2 == 0:
            # Simulate some logging (irrelevant)
            temp_buffer.append(f"Processing {key} at index {idx}")

        # Real computation hidden among distractions
        quality_index = analyze_sensor_readings(readings)
        threshold = limits.get(key, 1000)
        
        # Misleading conditional — evaluates but doesn't affect outcome
        if quality_index > threshold:
            diagnostic_log.append((key, "OVER_THRESHOLD"))
            adjustment_factor = -0.1  # Never used
        else:
            diagnostic_log.append((key, "NORMAL"))

        # Core state update: accumulates only this value
        temp_buffer.append(quality_index * 0.75)  # Only this contributes to result
    
    # Secondary distraction: zipping unrelated sequences
    indices = list(range(len(temp_buffer)))
    labeled_data = list(zip(indices, temp_buffer))  # zip used
    
    # Final aggregation — only this matters
    raw_total = sum(temp_buffer)
    correction_offset = sum(x for x in indices if x % 3 == 0)  # adds fixed offset
    final_diagnostic = int(raw_total - correction_offset + 17)  # deterministic integer result
    
    # Dead code block — looks like post-processing
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
    elif final_diagnostic > 1000:
        final_diagnostic = 999  # not triggered due to design

    return final_diagnostic

# Main execution context
if __name__ == "__main__":
    # Simulated turbine sensor data (real input)
    turbine_data = {
        "rotor_vibration": [120, 115, 118, 122, 117],
        "bearing_temp": [88, 91, 87, 90, 89],
        "oil_pressure": [65, 63, 66, 64, 65],
        "coolant_flow": [50, 52, 51, 53, 50]
    }
    
    # Thresholds map — some irrelevant entries
    thresholds = {
        "rotor_vibration": 300,
        "bearing_temp": 400,
        "oil_pressure": 200,  # Not impactful
        "coolant_flow": 150,
        "voltage_spike": 500  # Unused key
    }
    
    # Spurious variables to increase interference
    calibration_sequence = [i * 2 + 1 for i in range(10)]
    audit_trail = list(itertools.combinations(calibration_sequence[:5], 2))  # No effect
    metadata_index = {k: len(v) for k, v in turbine_data.items()}  # Unused
    
    # Key execution point
    final_diagnostic = aggregate_metrics(turbine_data, thresholds)
    
    # Output required format
    print(f"Target result: {final_diagnostic}")