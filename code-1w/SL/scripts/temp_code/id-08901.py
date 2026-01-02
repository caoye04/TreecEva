import itertools

def preprocess_signal(raw_readings):
    # Irrelevant preprocessing (distraction)
    filtered = [x * 0.98 for x in raw_readings if x > 0]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    return [y - baseline for y in filtered]

def evaluate_health_index(telemetry):
    # Misleading health index calculation (dead path)
    if not telemetry:
        return 0
    peak = max(telemetry)
    avg = sum(telemetry) / len(telemetry)
    return (avg / peak) * 100 if peak else 0

def compute_fourier_magnitude(samples):
    # Distractor function: simulates signal analysis but unused
    magnitude = 0
    for k in range(5):
        component = sum(samples[i] * (k * i * 0.1) for i in range(len(samples)))
        magnitude += abs(component)
    return round(magnitude, 3)

def generate_synthetic_load(profile, duration):
    # Generates fake data for red herring purpose
    load_curve = []
    for t in range(duration):
        value = (profile[0] * t ** 2 + profile[1] * t) % 150
        if t % 10 == 0:
            value += 25  # Inject anomalies
        load_curve.append(value)
    return load_curve

def validate_checksum(sequence):
    # Unused validation logic (decoy)
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) & 0xFF
    return checksum == 0xAA

def aggregate_metrics(sensor_data, calibration):
    # Core relevant logic begins here
    calibrated_values = []
    for i in range(min(len(sensor_data), len(calibration))):
        adjusted = sensor_data[i] * calibration[i]
        calibrated_values.append(adjusted)
    
    # Apply windowed transformation using itertools
    windows = list(itertools.pairwise(calibrated_values))  # Overlapping pairs
    derivatives = [abs(b - a) for a, b in windows]
    
    # Accumulate only every third derivative (key step)
    sparse_accumulation = sum(derivatives[j] for j in range(0, len(derivatives), 3))
    
    # Add influence of control sequence sum (hidden dependency)
    control_factor = sum(calibration) % 17
    intermediate = sparse_accumulation * control_factor
    
    # Conditional offset based on length parity (subtle logic)
    if len(calibrated_values) % 2 == 0:
        intermediate -= 42
    else:
        intermediate += 13
    
    # Final transformation
    final_diagnostic = int(intermediate * 1.75)
    
    # Dead code branch (never reached due to prior logic)
    if final_diagnostic < 0:
        final_diagnostic = compute_fourier_magnitude(calibrated_values)
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data (real signal)
    turbine_data = [12, 15, 14, 18, 17, 20, 22, 21, 24, 23, 26]
    calibration_sequence = [1.1, 0.9, 1.0, 1.2, 0.8, 1.1, 0.95, 1.05, 1.0, 0.9, 1.1]
    
    # Irrelevant computations (distractors)
    noise_floor = [0.1 * i for i in range(100)]
    processed_noise = preprocess_signal(noise_floor)
    synthetic_profile = generate_synthetic_load([3, -7], 50)
    dummy_checksum = validate_checksum(synthetic_profile[:10])
    
    # Key statement that determines the answer
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")