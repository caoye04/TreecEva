def analyze_signal(samples, threshold):
    filtered = [s for s in samples if abs(s) > threshold]
    transformed = []
    cumulative_power = 0
    phase_shift = 0.5
    normalization_factor = 0.98
    
    # Irrelevant signal processing branch (dead logic)
    temp_buffer = []
    for idx, val in enumerate(samples):
        if idx % 3 == 0:
            temp_buffer.append(val * 0.1)
    
    # Distractor: complex but unused transformation
    spectral_weights = {i: (i+1)**0.3 for i in range(len(samples))}
    weighted_sum = sum(spectral_weights.get(i, 0) * s for i, s in enumerate(samples))
    adjusted_weights = [weighted_sum / (i + 1e-6) for i in range(50)]  # Unused

    # Relevant processing path
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            transformed.append(val ** 2 * normalization_factor)
        else:
            transformed.append(abs(val) * 1.1)
        cumulative_power += transformed[-1]
        if cumulative_power > 100:
            cumulative_power *= phase_shift

    energy_signature = sum(transformed) / (len(transformed) + 1e-6)
    return energy_signature


def extract_features(data_stream):
    base_features = []
    decoy_accumulator = 0
    
    for i, x in enumerate(data_stream):
        if i < len(data_stream) // 2:
            feature = (x + i) ** 0.5
            base_features.append(feature)
        else:
            # Dead code path — never executed due to condition above
            decoy_accumulator += x * i

    # Meaningless set operations as distractors
    indices = set(range(len(data_stream)))
    evens = {i for i in indices if i % 2 == 0}
    primes = {2, 3, 5, 7, 11}
    overlap = evens & primes
    shift_value = len(overlap) * 0.2  # Unused

    return base_features


def aggregate_metrics(features, offset):
    metric_stack = []
    temp_cache = []
    
    for j, f in enumerate(features):
        temp = f * (j + 1)
        if j % 3 == 0:
            temp_cache.append(temp)  # Red herring
        metric_stack.append(temp + offset)

    # Core calculation (key path)
    total = sum(metric_stack)
    correction = len(temp_cache) * 0.5
    final_score = total - correction
    
    # Decoy complex structure
    audit_log = {}
    for step in range(3):
        audit_log[f'step_{step}'] = {"value": step * 2, "valid": False}
    
    return int(final_score)

# Main execution with mixed data flows
raw_samples = [12, -8, 15, 3, -22, 9, 4, -13]
reference_grid = list(range(7, 15))

# Distractor: zipped but unused iteration
for a, b in zip(raw_samples, reference_grid):
    _ = a ^ b  # Bitwise red herring

engineered_features = extract_features([x*0.7 for x in raw_samples])
baseline_offset = analyze_signal(raw_samples, threshold=10)

# Key statement
final_diagnostic = aggregate_metrics(engineered_features, baseline_offset)

print(f"Result: {final_diagnostic}")