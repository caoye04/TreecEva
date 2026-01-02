from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental monitoring

def collect_sensor_data():
    # Real data generation (relevant)
    raw_readings = [127, 255, 180, 64, 200, 95, 130, 170]
    timestamps = list(range(1000, 1008))
    sensor_ids = ['S1', 'S2', 'S1', 'S3', 'S2', 'S3', 'S1', 'S2']
    return list(zip(raw_readings, timestamps, sensor_ids))

def filter_outliers(data, threshold=200):
    # Irrelevant filtering (distractor: not actually used in final path)
    return [x for x in data if x[0] < threshold]

def apply_calibration(signal, factor=0.78):
    # Relevant transformation
    return int(signal * factor) + 5

def deprecated_normalization(seq):
    # Dead code path (never called)
    return [x / sum(seq) for x in seq]

def preprocess_signal(val, meta):
    # Complex but partially relevant processing
    calibrated = apply_calibration(val)
    
    # Distractor computation
    dummy_weight = math.sin(meta % 31) * 100
    adjusted = calibrated + (meta % 3)
    
    # Red herring: entropy-like calculation (unused)
    temp_bits = bin(adjusted).count('1')
    fake_entropy = temp_bits / 8.0
    
    return adjusted

def transform_batch(readings):
    # Core data transformation with distractions
    grouped = defaultdict(list)
    aux_counter = Counter()  # Used for irrelevant stats
    
    for val, ts, sid in readings:
        grouped[sid].append((val, ts))
        aux_counter[sid] += 1  # Distractor counting
    
    processed = []
    for sensor, records in grouped.items():
        # Only the values are used, rest is distraction
        sorted_vals = sorted(records, key=lambda x: x[1])
        for raw_val, _ in sorted_vals:
            proc_val = preprocess_signal(raw_val, len(processed))
            processed.append(proc_val)
    
    # Decoy operation
    mean_proc = sum(processed) / len(processed) if processed else 0
    deviation_score = sum(abs(x - mean_proc) for x in processed)
    
    return processed

def compute_legacy_metric(arr):
    # Unused legacy function (dead path)
    total = 0
    for i, x in enumerate(arr):
        total += x * (i % 4 + 1)
    return total // 7

def evaluate_stability(sequence):
    # Partially misleading evaluation
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    stability = sum(diffs) / len(diffs) if diffs else 0
    return stability < 15

def aggregate_diagnostics(data):
    # Multi-step diagnostic logic with red herrings
    even_flags = [x % 2 == 0 for x in data]
    mod_stats = [x % 7 for x in data]
    mod_counter = Counter(mod_stats)  # Looks important, barely used
    
    # Key intermediate: harmonic blend
    reciprocals = [1 / (x % 9 + 1) for x in data]
    harmonic_base = len(data) / sum(reciprocals) if reciprocals else 0
    
    # Distractor: pattern matching on bit density
    bit_density = sum(bin(x).count('1') for x in data) / len(data)
    
    # Critical path starts here
    filtered_vals = [x for x in data if x % 2 == 1]  # Only odd values matter
    if not filtered_vals:
        return 0
    
    # Actual core computation
    squared_sum = sum(x * x for x in filtered_vals)
    base_index = len(filtered_vals) % 5 or 1
    normalized = squared_sum / base_index
    
    return normalized

def analyze_readings(signals):
    # Final analysis with heavy interference
    if len(signals) == 0:
        return -1
    
    # Distractor variables
    signal_matrix = [[s + i for i in range(3)] for s in signals[:3]]
    flat_matrix = [item for row in signal_matrix for item in row]
    matrix_checksum = sum(flat_matrix) % 1000
    
    # Another decoy: frequency analysis
    freq_dist = Counter(signals)
    dominant_freq = freq_dist.most_common(1)[0][1] if freq_dist else 0
    
    # Conditional expression with logical operations
    confidence = len(signals) > 5 and evaluate_stability(signals)
    override_flag = False or (dominant_freq > 2 and matrix_checksum < 50)
    
    # Misleading early exit (not taken due to data)
    if override_flag and False:  # Always false
        return matrix_checksum * 2
    
    # Key diagnostic computation (actual answer source)
    primary_diagnostic = aggregate_diagnostics(signals)
    secondary_factor = math.log(primary_diagnostic + 10) if primary_diagnostic > 0 else 0
    
    # Final result with deterministic path
    final_diagnostic = int(primary_diagnostic - secondary_factor * 2)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Orchestration function
def main_pipeline():
    # Collect real data
    raw_data = collect_sensor_data()
    
    # Irrelevant preprocessing branch
    clean_data = filter_outliers(raw_data, threshold=190)
    backup_copy = raw_data.copy()
    
    # Main processing path
    processed_signals = transform_batch(raw_data)  # Uses all data
    
    # Unused alternate transformation
    alt_processed = [apply_calibration(x) for x in [r[0] for r in raw_data]]
    alt_stability = evaluate_stability(alt_processed)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_signals)
    
    return final_diagnostic

# Execute
main_pipeline()