import math

# Simulated sensor array diagnostics with red herrings and complex processing

def collect_sensor_data():
    raw_values = [i * 1.5 + 2.1 for i in range(18) if i % 2 == 0]
    offset_correction = sum([v ** 0.5 for v in raw_values]) / len(raw_values)
    return [v + offset_correction for v in raw_values]


def filter_anomalies(data):
    threshold = sum(data) / len(data) + 0.5 * (max(data) - min(data))
    filtered = [x for x in data if x < threshold]
    outlier_flags = {idx: True for idx, val in enumerate(data) if val >= threshold}
    return filtered


def compute_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 6)


def generate_checksum(sequence):
    # Irrelevant cryptographic-like checksum (dead path)
    chk = 0
    for num in sequence:
        chk ^= int(num * 100) & 0xFF
    return chk


def derive_key_indices(length):
    # Misleading function that looks important but isn't used in main logic
    indices = []
    a, b = 1, 1
    while a < length:
        indices.append(a)
        a, b = b, a + b
    return set(indices)


def transform_features(raw):
    # Apply non-linear transformation with distractor operations
    temp_store = []
    accumulator = 0
    
    for i, v in enumerate(raw):
        if i % 3 == 0:
            accumulator += math.sin(v) ** 2
        elif i % 4 == 0:
            accumulator -= math.cos(v) ** 2
        temp_store.append(v ** 1.1 + accumulator)
    
    # Dead computation branch
    secondary_cache = [t * 0.95 for t in temp_store if t > 10]
    secondary_cache.reverse()
    
    # Actual relevant output
    return [round(t, 3) for t in temp_store]


def calculate_stability_index(features):
    diffs = [abs(features[i+1] - features[i]) for i in range(len(features)-1)]
    avg_change = sum(diffs) / len(diffs)
    stability = 100 / (1 + avg_change) if avg_change != 0 else 100
    return round(stability, 2)


def validate_integrity(metrics):
    # Decoy validation logic with unused results
    valid_count = sum(1 for m in metrics if isinstance(m, float) and m > 0)
    expected_size = len(metrics) * 2 // 3
    checksum = generate_checksum(metrics)
    log_entry = f"Validation complete: {valid_count}/{len(metrics)} entries, CHK={checksum}"
    # No return usage in downstream


def aggregate_diagnostics(feature_set):
    base_score = sum(feature_set) / len(feature_set)
    peak = max(feature_set)
    normalized_peak = peak / (base_score + 1e-8)
    dispersion = sum((x - base_score) ** 2 for x in feature_set) / len(feature_set)
    quality_flag = normalized_peak < 2.5 and dispersion < 100
    
    # Red herring: create unused diagnostic bundle
    dummy_bundle = {
        'raw_avg': base_score,
        'peak_ratio': normalized_peak,
        'dispersion': dispersion,
        'flag': quality_flag,
        'timestamp': 1678886400
    }
    
    return base_score, dispersion


def analyze_readings(metrics):
    validate_integrity(metrics)  # Side effect only, no meaningful return
    score, spread = aggregate_diagnostics(metrics)
    stability = calculate_stability_index(metrics)
    entropy = compute_entropy(metrics)
    
    # Core calculation buried among distractions
    diagnostic_value = int((score * 3.2) + (stability / 4.1) - (spread * 0.1) + (entropy * 15))
    
    # Multiple misleading intermediate prints (commented out to avoid output pollution)
    # print(f'DEBUG: score={score}, spread={spread}')
    # print(f'DEBUG: stability={stability}, entropy={entropy}')
    
    return diagnostic_value

# --- Main Execution ---
sensor_readings = collect_sensor_data()
filtered_readings = filter_anomalies(sensor_readings)
processed_metrics = transform_features(filtered_readings)
final_diagnostic = analyze_readings(processed_metrics)
print(f"Target result: {final_diagnostic}")