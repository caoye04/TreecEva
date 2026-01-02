def analyze_system_stability(readings):
    total_samples = len(readings)
    valid_threshold = total_samples * 0.7
    
    # Extract high-frequency components (distractor computation)
    high_freq_energy = sum(x ** 2 for x in readings if x > 50)
    energy_baseline = 1250
    spike_ratio = high_freq_energy / energy_baseline if energy_baseline else 0

    # Core processing: find stable segments using slicing and enumeration
    stability_flags = []
    for i, val in enumerate(readings[:-2]):
        segment = readings[i:i+3]
        if all(abs(segment[j] - segment[j+1]) < 15 for j in range(2)):
            stability_flags.append(True)
        else:
            stability_flags.append(False)

    stable_count = sum(stability_flags)
    
    # Secondary path: correlation analysis with zip (semi-relevant)
    shifted_readings = readings[1:]
    correlations = [a * b for a, b in zip(readings, shifted_readings)]
    avg_correlation = sum(correlations) / len(correlations) if correlations else 0

    # Distractor: unused statistical measures
    mean_val = sum(readings) / total_samples if total_samples else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in readings) / total_samples if total_samples else 0
    outlier_count = sum(1 for x in readings if abs(x - mean_val) > 2 * (variance_proxy ** 0.5))

    # Decision logic based on stability
    if stable_count >= valid_threshold:
        base_score = 400
        adjustment_factor = 25
    else:
        base_score = 150
        adjustment_factor = -10

    # Simulate corrective iterations (nested loop - state tracking)
    convergence_steps = 0
    temp_score = base_score
    while temp_score > 100 and convergence_steps < 5:
        temp_score = temp_score // 1.5
        convergence_steps += 1
    
    # Final computation chain
    intermediate_sum = 0
    for idx, flag in enumerate(stability_flags):
        if flag:
            intermediate_sum += idx * 3
    
    cumulative_offset = intermediate_sum % 97
    final_tally = base_score + cumulative_offset
    
    # Key statement
    equilibrium_score = final_tally // 2 + adjustment_factor
    
    print(f"Result: {equilibrium_score}")

# Input data
sensor_data = [88, 85, 87, 45, 90, 89, 91, 77, 76, 78, 102, 44, 80, 81, 80]
analyze_system_stability(sensor_data)