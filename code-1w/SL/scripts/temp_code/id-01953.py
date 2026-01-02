import math

def analyze_signal_strength(raw_samples, calibration_factor):
    filtered = [x for x in raw_samples if x > 50]
    adjusted = [x * calibration_factor for x in filtered]
    avg = sum(adjusted) / len(adjusted) if adjusted else 0
    return avg

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

def evaluate_health_status(sensor_readings):
    baseline = 75.0
    deviation = sum(abs(x - baseline) for x in sensor_readings)
    normalized_risk = deviation / 1000
    return normalized_risk < 0.4

def legacy_diagnostic_check(data):
    # Obsolete function - not used in current logic
    return sum(data) % 2 == 0

def main():
    # Simulated telemetry data from IoT sensors
    temperature_samples = [68, 72, 76, 80, 85, 90, 65, 73, 77, 81]
    pressure_readings = [101.3, 102.1, 100.9, 103.5, 101.8]
    signal_packets = [120, 135, 98, 142, 110, 133, 118]
    historical_load = [0.45, 0.62, 0.58, 0.71, 0.67, 0.53]

    # Irrelevant intermediate computations (distractors)
    avg_temp = sum(temperature_samples) / len(temperature_samples)
    temp_variance = sum((x - avg_temp) ** 2 for x in temperature_samples)
    peak_pressure = max(pressure_readings)
    pressure_anomalies = [p for p in pressure_readings if p < 101.0]

    # Unused data transformations
    inverted_packets = list(map(lambda x: 255 - x, signal_packets))
    packet_histogram = {val: signal_packets.count(val) for val in set(signal_packets)}

    # Core diagnostic variables
    system_thresholds = {
        'critical_load': 0.65,
        'recovery_window': 3,
        'decay_rate': 0.88,
        'min_stability': 0.72
    }

    # Simulated log data with multiple metrics
    log_data = [
        {'timestamp': 1001, 'load': 0.48, 'jitter': 0.03, 'errors': 2},
        {'timestamp': 1002, 'load': 0.52, 'jitter': 0.05, 'errors': 1},
        {'timestamp': 1003, 'load': 0.68, 'jitter': 0.12, 'errors': 4},
        {'timestamp': 1004, 'load': 0.59, 'jitter': 0.08, 'errors': 2},
        {'timestamp': 1005, 'load': 0.73, 'jitter': 0.18, 'errors': 6}
    ]

    # Dead code path - never executed due to flag
    debug_mode = False
    if debug_mode:
        print("Debug: Initializing verbose tracing")
        for entry in log_data:
            entry['debug_hash'] = hash(str(entry)) % 1000

    # Real-time signal analysis (used later)
    calibrated_avg = analyze_signal_strength(signal_packets, 1.05)

    # Entropy computation on historical load pattern
    load_pattern_binary = [1 if x > 0.6 else 0 for x in historical_load]
    system_entropy = compute_entropy(load_pattern_binary)

    # Health evaluation using sensor data
    health_status = evaluate_health_status(temperature_samples)

    # Unused complex transformation (red herring)
    transformation_chain = lambda x: x.replace('load', 'weight').upper() if isinstance(x, str) else str(x)
    processed_keys = [transformation_chain(k) for d in log_data for k in d.keys()]

    # Key processing function
    def process_metrics(log_entries, thresholds):
        recent = log_entries[-thresholds['recovery_window']:]  # Last 3 entries

        # Extract relevant time-series values
        loads = [entry['load'] for entry in recent]
        errors = [entry['errors'] for entry in recent]

        # Compute weighted instability score
        instability_score = 0
        for i, load in enumerate(loads):
            weight = thresholds['decay_rate'] ** i  # More recent = higher weight
            instability_score += (load / thresholds['critical_load']) * weight

        # Add penalty for error spikes
        error_spike = any(e > 3 for e in errors)
        if error_spike:
            instability_score *= 1.25

        # Apply stability threshold adjustment
        base_stable = all(load < thresholds['critical_load'] for load in loads)
        if base_stable and not error_spike:
            instability_score *= 0.8

        # Normalize to diagnostic range
        final_score = int(1000 * (1 - math.exp(-instability_score)))

        # Combine with entropy and signal metrics (cross-concept dependency)
        global_calibrated = globals().get('calibrated_avg', 120)
        entropy_contribution = int(100 * system_entropy)
        composite_input = final_score + entropy_contribution + int(global_calibrated)

        # Final nonlinear transformation
        result = int((composite_input ** 0.5) * 3.7)
        return result

    # Critical execution point
    final_diagnostic = process_metrics(log_data, system_thresholds)

    # Additional irrelevant output masking the real answer
    dummy_analysis = {
        'packet_count': len(inverted_packets),
        'temp_extremes': (min(temperature_samples), max(temperature_samples)),
        'calibration_offset': avg_temp * 0.01,
        'legacy_flag': legacy_diagnostic_check(historical_load)
    }

    # Print only the target result
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()