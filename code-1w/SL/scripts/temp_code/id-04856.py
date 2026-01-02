def analyze_sensor_stream(raw_readings, threshold=0.75):
    # Normalize sensor readings using modular arithmetic
    normalized = [(x % 127) / 100 for x in raw_readings]

    # Filter significant signals above threshold
    strong_signals = [x for x in normalized if x > threshold]

    # Misleading computation: entropy approximation (not used)
    entropy_proxy = 0.0
    distribution = {}
    for sig in normalized:
        rounded = round(sig, 1)
        distribution[rounded] = distribution.get(rounded, 0) + 1
    for freq in distribution.values():
        if freq > 0:
            entropy_proxy -= (freq / len(normalized)) * (freq / len(normalized))

    # Apply damping factor based on signal count
    signal_count = len(strong_signals)
    damping_factor = 0.9 if signal_count > 3 else 0.95

    # Simulate phase shift with lambda-based transformation
    phase_shift = lambda val, shift: (val * 1.1 + shift) % 1.0
    shifted_signals = [phase_shift(s, 0.05) for s in strong_signals]

    # Compute weighted magnitude using linear search for dominant frequency
    dominant_weight = 0
    for i in range(len(shifted_signals)):
        contribution = shifted_signals[i] * (i + 1)
        if contribution > dominant_weight:  # Linear search for max effect
            dominant_weight = contribution

    # Auxiliary metric: signal density (distractor)
    span = max(shifted_signals) - min(shifted_signals) if shifted_signals else 0
    density_score = len(shifted_signals) / (span * 100) if span > 0 else 0

    # Final processing step: scale and truncate
    processed = [int(s * 1000) / 1000 for s in shifted_signals]

    return processed


def integrate_signals(data):
    base_accumulator = 0
    multiplier_map = {0: 2, 1: 3, 2: 1, 3: 4, 4: 2}

    # Use dictionary as frequency-weighted accumulator
    weight_lookup = {i: (i % 3) + 1 for i in range(6)}

    for idx, value in enumerate(data):
        key_index = idx % 5
        weight = weight_lookup.get(key_index, 1)
        adjustment = multiplier_map[key_index] * weight
        base_accumulator += value * adjustment

        # Dead code path: never triggered under current logic
        if idx > 100:
            base_accumulator -= value * 0.5  # unreachable

    # Add constant bias from system calibration
    calibration_offset = 0.18
    base_accumulator += calibration_offset

    return round(base_accumulator, 4)

# Main execution flow
sensor_input = [89, 150, 201, 73, 115, 188, 230, 64]
processed_data = analyze_sensor_stream(sensor_input, threshold=0.72)
final_flux = integrate_signals(processed_data)
print(f"Target result: {final_flux}")