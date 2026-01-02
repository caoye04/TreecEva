import math

# Simulated biomedical signal processing pipeline
# Contains multiple layers of data transformation with red herrings

def analyze_waveform(signal_data, sample_rate):
    window_size = 64
    filtered = [x for x in signal_data if abs(x) > 0.5]  # Ignore low-amplitude noise
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered)-2)]
    peak_count = sum(1 for i in range(1, len(smoothed)-1) if smoothed[i-1] < smoothed[i] > smoothed[i+1])
    return peak_count * sample_rate // window_size

# Irrelevant auxiliary function - dead code path (distractor)
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 3)

# Signal integrity validation (partially relevant)
def validate_synchronization(lock_status, phase_offset):
    if lock_status == 'UNSYNCED':
        return False
    adjusted = abs(phase_offset) % 360
    return adjusted < 15 or adjusted > 345

# Core diagnostic engine
baseline_thresholds = {
    'amplitude': 2.1,
    'variance_cap': 0.87,
    'min_peaks': 3,
    'recovery_window': 120
}

health_snapshot = [
    0.3, 1.8, 2.5, 1.9, 0.7,
    2.3, 2.6, 2.4, 1.1, 0.4,
    2.7, 2.9, 2.8, 0.9, 0.5
]

# Distractor: unused but plausible-looking dataset
telemetry_log = [
    {'time': 1001, 'value': 1.2, 'status': 'OK'},
    {'time': 1002, 'value': 0.9, 'status': 'WARNING'},
    {'time': 1003, 'value': 1.5, 'status': 'OK'}
]

# Complex preprocessing with slicing and filtering (some steps are decoys)
cleaned_signal = [x for x in health_snapshot if x > 0.6][:12]  # Truncate and filter
differential = [cleaned_signal[i+1] - cleaned_signal[i] for i in range(len(cleaned_signal)-1)]
abs_diff = [abs(d) for d in differential]
avg_change = sum(abs_diff) / len(abs_diff) if abs_diff else 0

# Red herring: elaborate but unused statistical analysis
signal_set_1 = set(health_snapshot)
signal_set_2 = set(round(x * 2) / 2 for x in health_snapshot)  # Quantized version
divergence_profile = signal_set_1.symmetric_difference(signal_set_2)
size_anomaly = len(divergence_profile) > 4

# Actual core logic buried among distractions
def compute_stability_index(seq, threshold=2.0):
    above_thresh = [x for x in seq if x >= threshold]
    if not above_thresh:
        return 0.0
    mean_high = sum(above_thresh) / len(above_thresh)
    variance = sum((x - mean_high) ** 2 for x in above_thresh) / len(above_thresh)
    return round(mean_high * (1 - min(variance, 1)), 4)

# Secondary metric with misleading intermediate purpose
def evaluate_consistency(measurements, window=4):
    if len(measurements) < window:
        return 0
    chunks = [measurements[i:i+window] for i in range(0, len(measurements), window)]
    valid_blocks = [chunk for chunk in chunks if len(chunk) == window and max(chunk) - min(chunk) < 1.0]
    return len(valid_blocks)

# Main processing function combining multiple concepts
def process_metrics(snapshot, thresholds):
    # Step 1: Preprocess using slicing and filtering
    clipped = snapshot[1:-1]  # Remove first and last
    strong_signals = [x for x in clipped if x >= thresholds['amplitude']]
    
    # Step 2: Compute stability (this is critical)
    stability = compute_stability_index(strong_signals, thresholds['amplitude'])
    
    # Step 3: Consistency check (partially relevant)
    consistency_score = evaluate_consistency(snapshot)
    
    # Step 4: Additional validation using set operations (distractor-heavy)
    unique_count = len(set(snapshot))
    expected_range = set(round(x*10) for x in snapshot)
    anomaly_set = {x for x in expected_range if x % 3 == 0}  # Unused
    
    # Step 5: Final computation - only stability and consistency matter
    raw_metric = stability * 100 + consistency_score * 10
    
    # Step 6: Apply artificial gain (red herring: complex but fixed behavior)
    adjustment_factor = 1.0
    for i in range(3):
        if raw_metric > 100 * (i + 1):
            adjustment_factor += 0.1
    
    # Step 7: Apply adjustment (but it's linear and predictable)
    adjusted_metric = raw_metric * adjustment_factor
    
    # Step 8: Final clamping and type coercion (key step)
    final_value = int(round(adjusted_metric))
    
    # Numerous irrelevant transformations below (heavy distraction)
    binary_rep = bin(final_value)[2:]
    parity_check = binary_rep.count('1') % 2
    shifted = final_value >> 2
    masked = shifted & 0x3FFFFFFF
    hashed_variant = hash((masked, parity_check)) % 10000
    
    # The real answer was determined before the noise
    return final_value

# Execute main logic
sync_valid = validate_synchronization('LOCKED', 5.0)
if sync_valid:
    peak_diagnostic = analyze_waveform(health_snapshot, sample_rate=50)
    # This call is irrelevant to final_diagnostic

# Critical execution point
final_diagnostic = process_metrics(health_snapshot, baseline_thresholds)

# Output the required result
print(f"Result: {final_diagnostic}")