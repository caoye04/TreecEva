import itertools

# System telemetry simulation for distributed node health assessment
def simulate_node_response(time_slice, noise_factor=0.05):
    base_signal = (time_slice ** 2) % 7
    jitter = (time_slice * 11) % 13
    return (base_signal + jitter) % 10

# Irrelevant helper: simulates network latency (unused in final calculation)
def calculate_latency(nodes, bandwidth):
    return [((n * bandwidth) % 17) / 100 for n in nodes]

# Core signal processing pipeline
def extract_oscillations(data_stream):
    filtered = [x for x in data_stream if x > 3]
    return filtered[::2]  # Every other high-value reading

# Misleading aggregation function (looks important but unused)
def compute_stress_factor(readings, weights=None):
    if weights is None:
        weights = [0.1] * len(readings)
    weighted_sum = sum(r * w for r, w in zip(readings, weights))
    return weighted_sum * 1.7

# Real transformation: applies threshold masking and normalization
def apply_threshold_mask(signal, thresholds):
    processed = []
    for val, thresh_list in zip(signal, thresholds):
        valid_count = sum(1 for t in thresh_list if val >= t)
        processed.append(valid_count)
    return processed

# Central metric aggregator (key function used in final result)
def aggregate_metrics(scores, load_profile, mask):
    # Unpack nested structure
    flat_mask = [item for sublist in mask for item in sublist]
    score_sum = sum(s * 1.3 for s in scores)
    load_penalty = sum(l ** 0.5 for l in load_profile if l > 0)
    
    # Red herring: complex-looking but unused entropy calc
    entropy = 0
    for i in range(1, len(scores)):
        diff = abs(scores[i] - scores[i-1])
        if diff > 0:
            entropy += diff * 0.1
    dummy_offset = int(entropy * 3)  # Looks meaningful but not applied
    
    # Actual computation path
    masked_effect = 0
    for i, s in enumerate(scores):
        if i < len(flat_mask) and flat_mask[i] > 0:
            masked_effect += s * flat_mask[i]
    
    # Final combination
    result = int(score_sum - load_penalty + masked_effect)
    return result

# --- Simulation Setup ---

# Generate time-series sensor input
time_frames = list(range(5, 15))
sensor_readings = [simulate_node_response(t) for t in time_frames]

# Dead code path: pretends to calibrate but does nothing
baseline_calib = [r * 0.98 for r in sensor_readings]
deviation_norm = [(r - 5.0) ** 2 for r in baseline_calib]  # Unused quadratic deviations

# Extract key oscillation pattern
reliable_pulses = extract_oscillations(sensor_readings)

# Fake stress test (distractor)
stress_levels = compute_stress_factor(reliable_pulses, [0.2]*len(reliable_pulses))

# Real data structures used in answer
reliability_scores = [r * 2 for r in reliable_pulses]  # Amplify clean signals
system_load = [abs((i * 7) % 9 - 4) for i in range(len(reliability_scores))]

# Complex threshold matrix with cross-dimensional logic
threshold_row_a = [1, 2, 1]
threshold_row_b = [3, 1, 2]
threshold_row_c = [2, 3, 1]
threshold_matrix = [threshold_row_a, threshold_row_b, threshold_row_c]

# Apply real preprocessing
preprocessed_reliability = apply_threshold_mask(reliability_scores, [threshold_matrix[0]] * len(reliability_scores))

# Introduce slicing red herring
slice_preview = preprocessed_reliability[1:4:2]  # Skipped slice - not used later

# Generate combinatoric feature expansion (partially irrelevant)
expanded_pairs = list(itertools.combinations(reliability_scores[:4], 2))
interaction_energy = sum(abs(a - b) for a, b in expanded_pairs)  # Distractor metric

# Critical assignment statement
final_diagnostic = aggregate_metrics(reliability_scores, system_load, threshold_matrix)

# Output result as required
print(f"Result: {final_diagnostic}")