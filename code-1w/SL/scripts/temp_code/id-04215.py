import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_data():
    raw_readings = [18, 22, 15, 30, 25, 12, 8, 40, 38, 29]
    baseline_offset = 7
    adjusted = [r - baseline_offset for r in raw_readings]
    return adjusted

# Irrelevant helper - simulates temperature calibration (not used in final result)
def calibrate_temperature(reading):
    if reading < 15:
        return reading * 1.8 + 32
    else:
        return reading

# Distraction function - processes unrelated actuator signals
def evaluate_actuators():
    signals = [0.1, 0.7, 0.3, 0.9, 0.5]
    thresholds = [0.25, 0.65, 0.85]
    activation_count = sum(1 for s in signals if any(abs(s - t) < 0.1 for t in thresholds))
    return activation_count * 100  # Dead end value

# Noise reduction using moving median filter
def reduce_noise(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-1):min(len(data), i+2)]
        sorted_window = sorted(window)
        median = sorted_window[len(sorted_window) // 2]
        smoothed.append(median)
    return smoothed

# Transform metrics using combinatorial pairing and amplitude scaling
def transform_metrics(noise_filtered):
    # Generate all pairwise absolute differences
    pairs = list(itertools.combinations(noise_filtered, 2))
    diffs = [abs(a - b) for a, b in pairs]
    
    # Scale based on system pressure coefficient (fixed)
    pressure_coeff = 0.4
    scaled = [d * pressure_coeff for d in diffs]
    
    # Add decoy computation: frequency analysis (unused)
    frequency_map = {}
    for d in diffs:
        rounded = round(d)
        frequency_map[rounded] = frequency_map.get(rounded, 0) + 1
    
    # Only this part matters: take every third element above threshold
    filtered_gaps = [s for i, s in enumerate(scaled) if s > 5.0 and i % 3 == 0]
    return filtered_gaps

# Core pattern analyzer - determines diagnostic code based on entropy-like measure
def analyze_pattern(transformed_metrics):
    if not transformed_metrics:
        return -1
    
    # Calculate weighted dispersion index
    total_power = sum(val ** 2 for val in transformed_metrics)
    peak_response = max(transformed_metrics)
    metric_count = len(transformed_metrics)
    
    # Dummy logic path: simulate fault isolation (irrelevant)
    suspected_nodes = []
    for idx, val in enumerate(transformed_metrics):
        if val > peak_response * 0.85 and idx % 2 == 0:
            suspected_nodes.append(idx * 3)
    
    # Actual determining factor: normalized power ratio
    normalization_base = metric_count * (peak_response + 1e-6)
    diagnostic_score = total_power / normalization_base
    
    # Final mapping to discrete diagnostic code
    code = int(diagnostic_score * 17) + 5
    return code

# Misleading initialization sequence (distractor block)
def initialize_system():
    system_state = {
        'version': '2.1.7',
        'nodes_active': 8,
        'security_lock': True,
        'calibration_cycle': 'completed'
    }
    return system_state

# Orchestrate full diagnostic chain
def run_diagnostics():
    # Step 1: Collect raw sensor data
    readings = collect_sensor_data()  # [11, 15, 8, 23, 18, 5, 1, 33, 31, 22]
    
    # Step 2: Apply noise reduction
    cleaned = reduce_noise(readings)  # Smoothed signal
    
    # Step 3: Transform into analytical metrics
    transformed_metrics = transform_metrics(cleaned)
    
    # Step 4: Compute final diagnostic code
    final_diagnostic = analyze_pattern(transformed_metrics)
    
    # DEAD CODE PATHS AND DISTRACTIONS BELOW
    _ = evaluate_actuators()  # Unused result
    _ = initialize_system()  # System state ignored
    for i in range(3):  # Fake retry loop
        pass
    
    # OUTPUT THE TARGET RESULT
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    run_diagnostics()