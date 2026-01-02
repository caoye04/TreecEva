import itertools

# Simulated sensor data aggregation and health diagnostics
raw_readings = [145, 273, 98, 412, 256, 77, 314, 189, 403, 221]

def analyze_pattern(sequence):
    trend_scores = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_scores.append(1)
        elif sequence[i] < sequence[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return trend_scores

def filter_outliers(data, threshold=300):
    # Irrelevant filtering path - distractor
    return [x for x in data if x <= threshold]

def compute_hash(data):
    # Decoy function - never used in final computation
    result = 0
    for val in data:
        result ^= val * 3
    return result % 10000

def generate_pairs(lst):
    # Creates distracting combinations
    return list(itertools.combinations(lst, 2))

def calculate_entropy(data):
    # Misleading complex math that isn't used
    total = sum(data)
    probabilities = [x / total for x in data]
    from math import log2
    return -sum(p * log2(p) for p in probabilities if p > 0)

def extract_features(signal):
    # Extracts statistical features, some relevant later
    length = len(signal)
    avg = sum(signal) / length
    deviance_map = [abs(x - avg) for x in signal]
    high_deviation_count = len([d for d in deviance_map if d > avg * 0.5])
    return {
        'mean': avg,
        'deviant_peaks': high_deviation_count,
        'range': max(signal) - min(signal),
        'size': length
    }

def transform_signal(signal, factor=0.85):
    # Applies scaling transformation
    return [int(x * factor) for x in signal]

def merge_segments(segments):
    # Dead code path - not invoked
    merged = []
    for seg in segments:
        merged.extend(seg)
    return merged

def validate_integrity(checksum, data):
    # Unused validation logic
    computed = sum(data) % 1024
    return checksum == computed

# System configuration with red herring parameters
config = {
    'threshold': 200,
    'gain': 1.5,
    'mode': 'diagnostic',
    'debug_trace': True,
    'sample_rate': 10,
    'hash_key': 7761  # Never actually used
}

# Intermediate processing steps with distractions
analysis_log = []
trend_analysis = analyze_pattern(raw_readings)
filtered_diagnostics = filter_outliers(raw_readings, threshold=250)  # Partially processed but unused

# Real processing begins here — buried among distractions
transformed_data = transform_signal(raw_readings, factor=0.92)
feature_set = extract_features(transformed_data)

# Distracting use of set operations (set difference)
unique_values = set(transformed_data)
disallowed = {x for x in unique_values if x % 13 == 0}  # Filter by arbitrary modulus
cleaned_values = list(unique_values - disallowed)

# Generate irrelevant combinatorial pairs
pairwise_combinations = generate_pairs(cleaned_values[:6])  # Only first few used as decoy

# Another distraction: entropy calculation on filtered subset
subset_for_entropy = [x for x in transformed_data if x > 150]
entropy_metric = calculate_entropy(subset_for_entropy)  # Computed but unused

# Core logic hidden in plain sight
primary_diagnostics = {
    'baseline': feature_set['mean'],
    'instability': feature_set['deviant_peaks'] * 2,
    'span': feature_set['range'] // 10
}

# Secondary metrics using itertools.cycle to simulate windowing
cycle_buffer = []
cycler = itertools.cycle(subset_for_entropy)
for _ in range(20):
    cycle_buffer.append(next(cycler))
windowed_avg = sum(cycle_buffer[::4]) / len(cycle_buffer[::4])  # Distractor metric

# Actual critical computation chain
def evaluate_stability(metrics, cfg):
    score = 0
    score += int(metrics['baseline'])
    score -= metrics['instability'] * 3
    span_factor = cfg['gain'] * metrics['span']
    score += int(span_factor)
    if metrics['instability'] > 5:
        score -= 50
    return score

# Final processing pipeline
intermediate_result = evaluate_stability(primary_diagnostics, config)

# Final diagnostic depends on conditional transformation
if primary_diagnostics['span'] > 20:
    adjustment = len(pairwise_combinations) // 5
else:
    adjustment = 0

final_diagnostic = intermediate_result + adjustment

# Output required result
print(f"Result: {final_diagnostic}")