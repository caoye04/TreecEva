import math

# Sensor network diagnostic system with noise filtering and anomaly detection
def collect_sensor_readings():
    raw_readings = [14.2, 18.7, 25.3, 16.8, 999, 15.1, 19.4, 22.8, 17.5, 999, 20.1, 18.9]
    calibration_offset = 1.2
    adjusted_readings = [x - calibration_offset for x in raw_readings if x != 999]
    return adjusted_readings

# Irrelevant auxiliary function - dead code path
def compute_signal_strength(signal_list):
    if not signal_list:
        return 0.0
    power_sum = sum([s ** 2 for s in signal_list])
    return math.sqrt(power_sum) / len(signal_list)

# Noise filter based on statistical deviation (relevant)
def filter_outliers(data, stdev_multiplier=1.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    stddev = math.sqrt(variance)
    lower_bound = mean_val - stdev_multiplier * stddev
    upper_bound = mean_val + stdev_multiplier * stddev
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    
    # Distractor: unused transformation
    normalized = [(x - mean_val) / (stddev + 1e-8) for x in data]
    scaled_result = [round(x * 1.05, 2) for x in normalized]  # Not used
    
    return filtered

# Set-based interference logic (partially relevant)
def generate_threshold_set(base_value):
    base_set = {base_value + i for i in range(-5, 6)}
    decoy_set = {i * 3 for i in range(20) if i % 2 == 0}  # Irrelevant set
    control_set = {x for x in range(80, 100) if x % 7 == 0}  # Unused control
    return base_set  # Only this matters

# Main analysis function with key computation
def analyze_readings(readings, thresholds):
    count_in_threshold = 0
    rolling_product = 1.0
    debug_values = []
    
    for val in readings:
        rounded_val = round(val)
        if rounded_val in thresholds:
            count_in_threshold += 1
            rolling_product *= val
        
        # Misleading intermediate metric
        inverse = 1 / (val + 1e-5)
        debug_values.append(inverse)  # Collected but unused
    
    # Complex aggregation: harmonic mean of debug values (distractor)
    if debug_values:
        harmonic_mean = len(debug_values) / sum(1/v for v in debug_values)
        adjusted_harmonic = round(harmonic_mean, 3)  # Computed but irrelevant
    
    # Key result derived from count and product
    stability_factor = len(readings) > 5
    weight = 10 if stability_factor else 5
    
    # Secondary distractor: string processing unrelated to output
    status_label = "STABLE" if count_in_threshold >= 3 else "FLUCTUATING"
    char_count = sum(1 for c in status_label if c in 'AEIOU')  # Useless calc
    
    # Final diagnostic combines count and transformed product
    product_log = math.log(rolling_product) if rolling_product > 0 else 0
    final_score = (count_in_threshold * weight) + round(product_log)
    
    # Dead branch - never executed due to logic
    if char_count < 2:
        fallback = sum(thresholds) / len(thresholds)
        final_score = int(fallback)
    
    return final_score

# Orchestration function with red herrings
def run_diagnostics():
    # Step 1: Collect sensor data
    sensor_data = collect_sensor_readings()
    
    # Unused duplicate collection
    backup_readings = [x * 1.01 for x in sensor_data]  # Slight variation, not used
    
    # Step 2: Filter noisy readings
    filtered_data = filter_outliers(sensor_data, stdev_multiplier=1.8)
    
    # Step 3: Generate dynamic threshold set
    base_diagnostic = int(sum(filtered_data) / len(filtered_data))
    threshold_set = generate_threshold_set(base_diagnostic)
    
    # Irrelevant dictionary mapping
    mode_registry = {
        'A': 'Aggressive',
        'B': 'Balanced',
        'C': 'Conservative'
    }
    active_mode = mode_registry['B']  # Retrieved but unused
    
    # Step 4: Compute final diagnostic value
    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    
    # Distractor: post-processing that doesn't affect result
    if final_diagnostic > 50:
        saturation_level = final_diagnostic / 100.0
        capped = min(final_diagnostic, 95)  # No assignment back
    
    print(f"Result: {final_diagnostic}")

# Execution entry point
if __name__ == "__main__":
    run_diagnostics()