import itertools

# Simulated sensor array data with noise and redundancy
def collect_sensor_readings():
    raw_signals = [18, 22, 19, 25, 30, 28, 21]
    noise_profile = [1, -2, 1, 0, -1, 2, -1]
    adjusted = [sig + noise for sig, noise in zip(raw_signals, noise_profile)]
    return adjusted

# Irrelevant auxiliary function – dead code path (distractor)
def calculate_wind_chill(temps):
    return [13.12 + 0.6215*t - 11.37*(3**0.16) + 0.3965*t*(3**0.16) for t in temps]

# Data filtering with red herring normalization
def filter_outliers(data, threshold=25):
    filtered = []
    exceeded = []
    for val in data:
        if val < threshold:
            filtered.append(val)
        else:
            exceeded.append(val)
    # Misleading intermediate: appears important but unused later
    normalized = [round((x - min(filtered)) / (max(filtered) - min(filtered)) * 10, 2) for x in filtered]
    return filtered

# Complex transformation with bit manipulation decoy
def transform_data_sequence(seq):
    seq_xored = [x ^ 5 for x in seq]  # Bitwise distraction
    seq_paired = list(itertools.pairwise(seq_xored))  # Real use of itertools
    rolled = [seq_xored[-1]] + seq_xored[:-1]  # Rotate right
    # Decoy accumulation with no impact
    accumulation_chain = []
    temp_acc = 0
    for num in rolled:
        temp_acc += num
        accumulation_chain.append(temp_acc)
    return seq_xored  # Only this is returned; rest are distractions

# Higher-order logic with conditional early exit red herring
def analyze_pattern(values):
    if len(values) % 2 == 0:
        return sum(values) * 0.9  # Dead branch — never taken
    else:
        base_sum = sum(v ** 0.5 for v in values)  # Relevant operation
        parity_check = sum(1 for v in values if v % 2 == 1)
        adjustment = parity_check * 1.1 if parity_check > 3 else -2.5
        return base_sum + adjustment

# Secondary processing chain with unused tuple unpacking
def compute_diagnostic_metrics(data):
    n = len(data)
    avg = sum(data) / n
    variance = sum((x - avg) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    # Destructuring distraction
    first, *middle, last = data
    mid_avg = sum(middle) / len(middle) if middle else 0
    
    # Fake diagnostic score (never used)
    fake_risk_score = (last - first) * std_dev + 17.3
    
    # Real contribution
    stability_index = (avg / (std_dev + 1e-8))  # Avoid division by zero
    return stability_index, avg

# Main execution with multiple abstraction layers
if __name__ == '__main__':
    # Step 1: Collect sensor data
    signal_chain = collect_sensor_readings()  # [19, 20, 20, 25, 29, 30, 20]

    # Step 2: Filter outliers (threshold=25) -> keeps values <25
    clean_signal = filter_outliers(signal_chain, threshold=25)  # [19,20,20,20]

    # Step 3: Transform with XOR and pairwise generation (only uses transformed result)
    processed_seq = transform_data_sequence(clean_signal)  # [22,23,23,23]

    # Step 4: Analyze pattern on processed sequence
    pattern_metric = analyze_pattern(processed_seq)  # sqrt sum + adjustment

    # Step 5: Compute diagnostic metrics
    diag_stability, mean_val = compute_diagnostic_metrics(processed_seq)

    # Irrelevant combinatorics (distractor using itertools)
    permutations_count = len(list(itertools.permutations([mean_val, diag_stability], 2)))

    # Critical path begins here — real computation chain
    aggregate_score = 0
    aggregate_score += pattern_metric           # First component
    aggregate_score += diag_stability * 1.5      # Second component

    # Correction factor based on initial signal length (hidden dependency)
    initial_length = len(collect_sensor_readings())  # 7
    correction_factor = (initial_length % 4) * 2.5   # 3 % 4 = 3 → 3*2.5 = 7.5

    # Final diagnostic calculation
    final_diagnostic = aggregate_score + correction_factor

    print(f"Target result: {final_diagnostic}")