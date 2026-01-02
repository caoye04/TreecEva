import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_readings():
    base_signals = [i * 1.5 for i in range(18)]
    noise_profile = [math.sin(i) * 0.7 for i in range(18)]
    readings = [base_signals[i] + noise_profile[i] for i in range(18)]
    return readings

# Irrelevant helper: used to mislead about signal source
def estimate_source_direction(data):
    weighted_sum = sum(d * (idx + 1) for idx, d in enumerate(data[:10]))
    normalization = sum(idx + 1 for idx in range(10))
    fake_direction = weighted_sum / normalization if normalization else 0
    return round(fake_direction, 3)

# Decoy function: appears useful but unused in critical path
def apply_calibration(signal_list, factor=1.05):
    calibrated = [s * factor for s in signal_list]
    return calibrated

# Noise mask generation — only partially relevant
def generate_interference_mask(seeds):
    mask = []
    for s in seeds:
        if s % 3 == 0:
            mask.append(int(s ** 0.5) % 2)
        elif s % 5 == 0:
            mask.append((s // 5) % 2)
        else:
            mask.append(1)
    return mask

# Core analysis logic
def filter_anomalous_peaks(signal_seq, threshold_multiplier=1.8):
    mean_val = sum(signal_seq) / len(signal_seq)
    std_dev = (sum((x - mean_val) ** 2 for x in signal_seq) / len(signal_seq)) ** 0.5
    upper_bound = mean_val + threshold_multiplier * std_dev
    filtered = [x for x in signal_seq if x <= upper_bound]
    return filtered

# Real processing chain — key component
def extract_spectral_components(readings):
    components = []
    for i, val in enumerate(readings):
        if i % 4 == 0:
            components.append(abs(val) ** 1.1)
        elif i % 3 == 0:
            components.append(abs(val) * 0.95)
        else:
            components.append(val + 0.1)
    return components

# Integration and reduction
def compute_coherence_score(components, weights):
    score = 0.0
    for c, w in zip(components, weights):
        score += c * (w % 1.5)
    return round(score, 6)

# Unused distraction: simulates hardware check
def validate_hardware_sync(timestamps):
    if len(timestamps) < 5:
        return False
    deltas = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_delta = sum(deltas) / len(deltas)
    return abs(avg_delta - 0.25) < 0.01

# Main pattern analyzer — actually used
def analyze_signal_patterns(raw_readings, mask):
    # Step 1: Filter anomalies
    clean_readings = filter_anomalous_peaks(raw_readings)
    
    # Step 2: Extract spectral content
    spectral_data = extract_spectral_components(clean_readings)
    
    # Step 3: Apply selective mask (only even indices matter)
    masked_data = []
    for i, (val, m) in enumerate(zip(spectral_data, mask * 3)):
        if i >= len(mask): break
        if m == 1:
            masked_data.append(val * 1.1)
        else:
            masked_data.append(val * 0.9)
    
    # Step 4: Generate positional weights using enumerate idiom
    weight_profile = []
    for index, value in enumerate(masked_data):
        adjustment = 1 + (index % 3) * 0.05
        weight_profile.append(adjustment)
    
    # Step 5: Coherence computation
    raw_score = compute_coherence_score(masked_data, weight_profile)
    
    # Step 6: Secondary correction based on set uniqueness
    unique_floor_values = set(int(x) for x in spectral_data)  # Set operation
    diversity_bonus = len(unique_floor_values) * 0.01
    
    # Step 7: Combine results
    final_score = raw_score + diversity_bonus
    
    # Step 8: Final diagnostic classification
    if final_score > 45.0:
        level = 3
    elif final_score > 30.0:
        level = 2
    else:
        level = 1
    
    # Step 9: Inject result into named diagnostic variable
    final_diagnostic = int(final_score) + level  # Key assignment
    
    # Dead code branch — misleading
    if False:
        fallback = apply_calibration(raw_readings)
        final_diagnostic -= sum(fallback) * 0.001
    
    return final_diagnostic

# Orchestration
if __name__ == '__main__':
    # Collect real data
    collected_readings = collect_sensor_readings()
    
    # Generate interference context
    seed_sequence = [7, 12, 15, 21, 22, 25, 27, 30, 33]
    interference_mask = generate_interference_mask(seed_sequence)
    
    # Fake timestamp series (unused)
    timing_log = [round(0.1 + i * 0.25, 2) for i in range(20)]
    hardware_ok = validate_hardware_sync(timing_log)  # Irrelevant call
    
    # Actual analysis
    final_diagnostic = analyze_signal_patterns(collected_readings, interference_mask)
    
    # Output target result
    print(f"Result: {final_diagnostic}")