import itertools

# Simulated sensor array diagnostics with mixed signal processing
def analyze_signal_strength(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    
    # Irrelevant transformation (distractor)
    normalized = [(x - baseline) ** 2 for x in filtered]  # Not used later
    decay_factor = 0.95
    adjusted_readings = [x * decay_factor for x in filtered]  # Partially relevant

    # Key computation path
    windowed_sums = []
    for i in range(len(adjusted_readings) - 2):
        windowed_sums.append(sum(adjusted_readings[i:i+3]))
    
    return windowed_sums

# Weight optimization via gradient mimicry (mostly decoy)
def optimize_weights(config_vector):
    temp_weights = [abs(x) ** 0.5 for x in config_vector if x != 0]
    
    # Dead code path (misleading)
    if len(temp_weights) > 10:
        inverted = [1/x for x in temp_weights]
        smoothed = list(itertools.accumulate(inverted, lambda a, b: a * 0.8 + b * 0.2))
    
    # Another red herring
    checksum = 0
    for val in temp_weights:
        checksum = (checksum * 31 + int(val)) % 10007
    
    # Actual relevant output
    tuned = [w * 1.2 for w in temp_weights[:5]]
    return tuned if len(tuned) == 5 else [1.0, 1.0, 1.0, 1.0, 1.0]

# Core metric processor (uses output from above)
def compute_stability_index(signal_peaks, weights):
    if not signal_peaks or not weights:
        return 0.0
    
    # Apply weighted moving average concept
    weighted_sum = sum(p * w for p, w in zip(signal_peaks, itertools.cycle(weights[:3])))
    peak_variance = sum((p - sum(signal_peaks)/len(signal_peaks))**2 for p in signal_peaks) / len(signal_peaks)
    
    # Logical operation chain with short-circuiting
    adjustment = 1.5 if peak_variance > 50 and weighted_sum > 0 else (0.8 if peak_variance < 10 or weighted_sum < 0 else 1.0)
    
    return weighted_sum * adjustment

# Final diagnostic integrator
lambda_transform = lambda x: x if x >= 0 else abs(x) * 0.5

def process_metrics(weight_set):
    # Simulate derived inputs
    synthetic_peaks = [weight_set[0] * 2, weight_set[2] * 4, weight_set[4] * 3, weight_set[1] * 5]
    
    # Use of conditional expression (required python feature)
    scaling_factor = 2.1 if any(w > 3 for w in weight_set) else 1.4
    
    # Complex data flow with distractors
    temp_buffer = []
    for sp in synthetic_peaks:
        temp_buffer.append(lambda_transform(sp * scaling_factor))
    
    # Decoy accumulation (unused)
    cumulative = list(itertools.accumulate(temp_buffer, lambda a, b: a + b * 0.1))
    
    # Key logic step
    avg_peak = sum(temp_buffer) / len(temp_buffer)
    max_weight = max(weight_set)
    interaction_score = avg_peak * max_weight
    
    # Final logical combination
    final_value = interaction_score + (50 if len([x for x in weight_set if x > 2]) >= 3 else -25)
    
    return int(final_value)

# Main execution flow
if __name__ == '__main__':
    # Initial sensor input (realistic domain)
    sensor_input = [12, -5, 8, 15, 0, 23, -4, 18, 7]
    
    # Trigger analysis (produces intermediate result)
    peaks = analyze_signal_strength(sensor_input)
    
    # Generate configuration vector (mix of real and fake use)
    config_params = [p % 7 for p in peaks]
    
    # Optimize (contains multiple distractions)
    optimized_weights = optimize_weights(config_params)
    
    # Introduce irrelevant sorting (suggested paradigm, but unused)
    sorted_weights = sorted(optimized_weights, reverse=True)
    median_val = sorted_weights[2]  # Unused
    
    # Core evaluation point
    final_diagnostic = process_metrics(optimized_weights)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")