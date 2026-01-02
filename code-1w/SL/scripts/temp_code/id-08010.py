import itertools

# Simulated sensor array data from environmental monitoring system
def acquire_sensor_data():
    base_values = [0.8, 1.2, 0.9, 1.5, 1.1]
    noise_offsets = [0.01 * i for i in range(5)]
    return [base_values[i] + noise_offsets[i] for i in range(5)]

# Irrelevant auxiliary function - dead code path
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Preprocess signal with calibration and filtering
def preprocess_signal(raw_signal):
    calibrated = [x * 0.97 for x in raw_signal]
    filtered = [x for x in calibrated if 0.85 <= x <= 1.45]
    extended_padding = [0.0] * (5 - len(filtered))
    return filtered + extended_padding

# Secondary transformation using set operations to eliminate redundancy
def generate_signature(profile):
    rounded_set = {round(x, 2) for x in profile}
    baseline = {0.82, 0.87, 0.92, 0.97, 1.02, 1.07, 1.12, 1.17, 1.22, 1.27, 1.32, 1.37}
    overlap = rounded_set & baseline
    return len(overlap) * 1.5

# Analyze temporal coherence across multiple readings
def evaluate_coherence(readings):
    pairs = list(itertools.combinations(readings, 2))
    coherent_count = 0
    for a, b in pairs:
        if abs(a - b) < 0.3:
            coherent_count += 1
    return coherent_count * 0.7

# Core diagnostic engine - computes stability metric
def compute_stability_index(signal_chunk):
    if len(signal_chunk) == 0:
        return 0.0
    mean_val = sum(signal_chunk) / len(signal_chunk)
    variance = sum((x - mean_val) ** 2 for x in signal_chunk) / len(signal_chunk)
    return (mean_val * 1.8) - (variance * 2.5)

# High-level analysis orchestrator (contains red herring logic)
def integrate_diagnostics(primary_score, secondary_score, legacy_mode=False):
    if legacy_mode:
        return (primary_score + secondary_score) * 0.5
    adjustment_factor = 1.3
    # Following line appears important but is unused
    deprecated_threshold = primary_score * 0.67
    return (primary_score * adjustment_factor) + secondary_score

# Main processing pipeline
raw_input = acquire_sensor_data()
processed_signals = preprocess_signal(raw_input)

# Dead-end computation - misleading intermediate result
outlier_detection_score = len([x for x in raw_input if x > 1.4]) * 10

# Generate side-channel metrics (partially irrelevant)
signature_weight = generate_signature(processed_signals)
temporal_coherence = evaluate_coherence(processed_signals)

# Compute core stability index (this contributes to final answer)
stability_index = compute_stability_index(processed_signals)

# Unused diagnostic branches - decoy logic paths
consistency_check = True
for i in range(len(processed_signals) - 1):
    if processed_signals[i] > processed_signals[i+1]:
        consistency_check = False
        break

# Phantom aggregation layer
aggregation_buffer = []
for val in processed_signals:
    aggregation_buffer.append(val * 1.1)
composite_metric = sum(aggregation_buffer) / len(aggregation_buffer) if aggregation_buffer else 0

# Final diagnostic fusion - only stability_index is actually used
# All other parameters are red herrings
final_diagnostic = integrate_diagnostics(stability_index, signature_weight, legacy_mode=False)

# Additional distraction: complex set operation with no impact
historical_records = {round(0.8 + 0.05*i, 2) for i in range(20)}
current_profile = {round(x, 2) for x in processed_signals}
divergence_index = len(historical_records - current_profile)

# Print target result
print(f"Result: {final_diagnostic}")