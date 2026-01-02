import math

# Simulated sensor data processing system with diagnostic logic
def collect_sensor_data():
    raw_values = [127, 255, 192, 64, 96, 159]
    timestamps = [1623456780, 1623456781, 1623456782, 1623456783, 1623456784, 1623456785]
    metadata = {'version': '2.1', 'calibrated': True}
    return list(zip(raw_values, timestamps))

# Irrelevant transformation: converts to hex strings (not used in final result)
def convert_to_hex(data):
    return [hex(x[0]) for x in data]

# Noise filtering using moving average (partially relevant)
def smooth_signal(signal):
    window = 3
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        segment = [signal[j][0] for j in range(start, i + 1)]
        smoothed.append(sum(segment) / len(segment))
    return [(val, signal[i][1]) for i, val in enumerate(smoothed)]

# Legacy function – unused but looks important
def legacy_normalization(arr):
    max_val = max([x[0] for x in arr])
    return [(x[0]/max_val, x[1]) for x in arr]

# Bitmask-based anomaly detection (distractor)
def check_bit_anomalies(values):
    anomalies = 0
    for v in values:
        if bin(v).count('1') % 2 == 0:
            anomalies += 1
    return anomalies

# Core processing: identifies spikes and computes diagnostic score
def detect_spikes(readings, threshold_multiplier=1.5):
    values = [r[0] for r in readings]
    avg = sum(values) / len(values)
    std_dev = (sum((x - avg) ** 2 for x in values) / len(values)) ** 0.5
    spike_threshold = avg + threshold_multiplier * std_dev
    
    spike_magnitudes = [v - spike_threshold for v in values if v > spike_threshold]
    return spike_magnitudes if spike_magnitudes else [0.0]

# Recursive integration of prior diagnostics (simple recursion)
def integrate_prior(priors, index):
    if index == 0:
        return priors[0] * 0.8
    return priors[index] * 0.8 + integrate_prior(priors, index - 1) * 0.2

# Data enhancement with decoy features
def enrich_with_context(logs):
    enhanced = []
    for val, ts in logs:
        # Decoy computations
        phase = math.sin(ts % 100 * 0.1)
        harmonic = abs(math.cos(val % 50))
        # Actual useful derived feature
        entropy_component = bin(int(val)).count('1') / 8.0
        enhanced.append((val, ts, entropy_component))
    return enhanced

# Main analysis pipeline
def process_diagnostics(raw_logs):
    # Step 1: Smooth the signal
    filtered_logs = smooth_signal(raw_logs)
    
    # Step 2: Enrich with context (only entropy_component is used later)
    enriched_logs = enrich_with_context(filtered_logs)
    
    # Step 3: Extract processed values
    processed = [(log[0], log[2]) for log in enriched_logs]  # (smoothed_value, entropy_part)
    
    # Irrelevant side calculation
    dummy_stats = {
        'peak_count': check_bit_anomalies([int(p[0]) for p in processed]),
        'phase_var': sum([math.sin(p[0]) for p in processed[:3]])
    }
    
    # Unused backup method
    def fallback_correction(data):
        return [x + 0.1 for x in data]
    
    return processed

# Final diagnostic engine
def analyze_readings(enriched_data):
    # Extract base values and entropy components
    base_vals = [item[0] for item in enriched_data]
    entropy_parts = [item[1] for item in enriched_data]
    
    # Compute weighted combination
    weights = [1 + e for e in entropy_parts]
    weighted_sum = sum(b * w for b, w in zip(base_vals, weights))
    total_weight = sum(weights)
    
    # Intermediate distractor variable
    pseudo_entropy = sum([e ** 1.5 for e in entropy_parts]) / len(entropy_parts)
    
    # Use list comprehension to filter significant contributions
    significant_contributions = [b*w for b, w in zip(base_vals, weights) if b*w > weighted_sum / len(weights)]
    
    # Apply recursive adjustment based on historical dummy data
    history = [42.0, 38.5, 45.2, 40.1, 39.8]
    adjustment_factor = integrate_prior(history, len(history) - 1) / 100.0
    
    # Final computation
    raw_diagnostic = weighted_sum / total_weight
    adjusted_diagnostic = raw_diagnostic * (1 + adjustment_factor)
    
    # Red herring: complex bit manipulation that doesn't affect output
    mask = 0b101010
    masked = int(adjusted_diagnostic) ^ mask & 0b111111
    
    # Critical assignment
    final_diagnostic = round(adjusted_diagnostic * 1000) / 1000
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    # Collect raw sensor input
    raw_input = collect_sensor_data()
    
    # Apply irrelevant hex conversion (dead path)
    hex_data = convert_to_hex(raw_input)
    
    # Process through main pipeline
    processed_logs = process_diagnostics(raw_input)
    
    # Generate final diagnostic score
    final_diagnostic = analyze_readings(processed_logs)
    
    # Print result
    print(f"Result: {final_diagnostic}")