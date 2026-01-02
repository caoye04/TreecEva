import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_readings():
    raw_readings = [18, 22, 15, 30, 12, 25, 14, 20]
    noise_mask = [i % 3 for i in range(len(raw_readings))]
    filtered = [r - n for r, n in zip(raw_readings, noise_mask)]
    return filtered

# Irrelevant auxiliary function – decoy for signal processing
def compute_harmonic_balance(data):
    total = 0
    for x in data:
        if x != 0:
            total += 1 / x
    return len(data) / total if total != 0 else 0

# Unused transformation path – dead code branch (red herring)
def deprecated_normalization(vec):
    mean_val = sum(vec) / len(vec)
    return [v / mean_val for v in vec]

# Signal transformation: applies moving average and detects rising edges
def transform_signal(readings):
    smoothed = []
    for i in range(2, len(readings)):
        window_avg = (readings[i-2] + readings[i-1] + readings[i]) / 3
        smoothed.append(int(window_avg))
    
    trend_flags = []
    for i in range(1, len(smoothed)):
        trend_flags.append(1 if smoothed[i] > smoothed[i-1] else 0)
    
    # Dummy computation – misleading intermediate
    checksum = sum(smoothed[i] * trend_flags[i-1] for i in range(1, len(trend_flags)))
    return smoothed, trend_flags

# Core pattern analyzer – critical path
def generate_triplet_sequences(data):
    return list(itertools.combinations(data[:5], 3))

# Recursive energy dispersion model – appears complex but partially irrelevant
def calculate_dispersion_energy(seq, level=0):
    if level >= 3 or len(seq) <= 1:
        return seq[0] if seq else 1
    split_idx = len(seq) // 2
    left = calculate_dispersion_energy(seq[:split_idx], level + 1)
    right = calculate_dispersion_energy(seq[split_idx:], level + 1)
    return abs(left - right) + (left * right) % 7

# Main pattern analyzer – only this contributes to final answer
def analyze_pattern(data):
    sequences = generate_triplet_sequences(data)
    scores = []
    for s in sequences:
        if sum(s) > 45:  # arbitrary threshold
            continue
        product = s[0] * s[1] * s[2]
        parity = product % 2
        scores.append(product + parity)
    
    # Final reduction – deterministic and unique
    accumulator = 0
    for val in scores:
        accumulator = (accumulator * 3 + val) % 999983
    return accumulator

# Misleading diagnostic routine – looks important but unused
def evaluate_system_health(data):
    critical_count = sum(1 for x in data if x > 25)
    stability_ratio = (len(data) - critical_count) / len(data)
    return "STABLE" if stability_ratio > 0.5 else "UNSTABLE"

# Orchestration with red herrings and distractions
if __name__ == "__main__":
    # Step 1: Collect sensor data
    sensor_data = collect_sensor_readings()
    
    # Distraction: Compute meaningless harmonic metric
    balance_metric = compute_harmonic_balance(sensor_data)
    
    # Step 2: Transform signal (only part used)
    transformed_data, trends = transform_signal(sensor_data)
    
    # Dead branch: normalization not used
    normalized_data = deprecated_normalization(transformed_data)
    
    # Red herring: dispersion on full data (not connected to output)
    dummy_energy = calculate_dispersion_energy(transformed_data)
    
    # Diagnostic health check – computed but not used
    system_status = evaluate_system_health(transformed_data)
    
    # KEY STATEMENT: Critical analysis that determines result
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output required value
    print(f"Result: {final_diagnostic}")