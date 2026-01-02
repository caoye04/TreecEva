def analyze_performance(metrics):
    base_score = 0
    for val in metrics:
        if val > 75:
            base_score += val // 10
    return base_score

# Irrelevant helper function (dead code path)
def deprecated_calibrator(x):
    return (x ** 2) % 17

# Another decoy transformation
def transform_signal(data):
    shifted = [d << 2 for d in data]
    return [s ^ 5 for s in shifted]  # Unused result

# Core logic disguised among distractors
def calculate_thermal_rating(config):
    rating = 0
    config_list = list(config)
    
    # Red herring: complex-looking but unused bitwise chain
    temp_debug = 0
    for i in range(len(config_list)):
        temp_debug ^= (i + config_list[i]) & 7
        temp_debug -= (temp_debug >> 1)
    
    # Actual logic hidden in set operations and conditional increments
    benchmark = {60, 70, 80, 90}
    overlap = config & benchmark
    rating += len(overlap) * 15
    
    if len(overlap) >= 3:
        rating += 42
    
    # Modular arithmetic with filtered values
    filtered = [x for x in config_list if x % 10 == 0]
    for val in filtered:
        rating += (val % 13)  # Contributes small increments
    
    # Linear search for a specific pattern (rarely triggered)
    sequence = sorted(config_list)
    found = False
    for idx in range(len(sequence) - 2):
        if sequence[idx] + 10 == sequence[idx+1] and sequence[idx+1] + 10 == sequence[idx+2]:
            found = True
            break
    if found:
        rating += 100  # Not triggered in this case

    # Decoy floating-point distraction
    noise_accumulator = 0.0
    for _ in range(50):
        noise_accumulator += 0.001 * _
    # No effect on output

    return rating

# Distractor data structures
sensor_readings = [65, 78, 82, 91, 54, 43]
signal_chain = {1, 2, 4, 8, 16}  # Unused

# Main execution block
metrics_score = analyze_performance(sensor_readings)
efficiency_set = {60, 78, 82, 90, 100}  # Key input set

# Dead assignment with misleading name
legacy_mode_threshold = deprecated_calibrator(8)

# Signal transformed but not used
distorted = transform_signal(sensor_readings)

# Critical statement: what is thermal_capacity after this?
thermal_capacity = calculate_thermal_rating(efficiency_set)

# Print final result as required
print(f"Result: {thermal_capacity}")