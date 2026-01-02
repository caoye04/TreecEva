import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis

def collect_sensor_readings():
    raw_signals = [2.1, 3.5, 4.6, 3.3, 7.2, 8.1, 6.9, 5.5, 4.8, 5.2]
    noise_floor = 2.0
    filtered = [x for x in raw_signals if x > noise_floor]
    baseline_shift = 0.8
    adjusted = [x - baseline_shift for x in filtered]
    return adjusted


def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 4)


def generate_checksum(data):
    # Irrelevant function: simulates data integrity check but not used in final result
    checksum = 0
    for d in data:
        checksum ^= int(d * 10)  # bitwise XOR on scaled values
    return checksum


def evaluate_stability(metrics):
    # Distractor function: calculates variance but not used in main logic
    mean = sum(metrics) / len(metrics)
    variance = sum((x - mean) ** 2 for x in metrics) / len(metrics)
    return variance < 1.5


def extract_features(signal_stream):
    peaks = [s for s in signal_stream if s > 4.0]
    avg_peak = sum(peaks) / len(peaks) if peaks else 0
    
    # Destructuring assignment (tuple unpacking)
    first, *middle, last = sorted(signal_stream)
    spread = last - first
    
    # Bitwise manipulation as red herring
    magic_flag = (int(avg_peak) << 2) & 0xFF
    
    # Set operations: identify unique binned categories
    binned = set(int(s // 1) for s in signal_stream)
    high_band = {b for b in binned if b >= 5}
    mid_band = {b for b in binned if 3 <= b < 5}
    overlap = high_band & mid_band
    
    # This section appears meaningful but is ultimately unused
    decoy_analysis = {
        'range': spread,
        'peaks_count': len(peaks),
        'magic_flag': magic_flag,
        'band_overlap': len(overlap)
    }
    
    # Actual relevant feature extraction
    magnitude_score = sum(signal_stream) * 0.75
    return magnitude_score


def analyze_pattern(dataset, criteria):
    # Main logic path begins here
    reference = criteria['base']
    tolerance = criteria['tolerance']
    
    # List comprehension with filtering
    valid_entries = [d for d in dataset if reference - tolerance <= d <= reference + tolerance]
    
    # Multiple simultaneous assignments
    count, total = len(valid_entries), sum(valid_entries)
    average = total / count if count > 0 else 0
    
    # Complex conditional with short-circuit evaluation
    if count > 3 and (average > reference or (reference - average) < tolerance * 2):
        adjustment_factor = math.sqrt(average) if average > 0 else 0
    else:
        adjustment_factor = 0.5
    
    # Core calculation disguised among distractions
    base_result = average * adjustment_factor
    secondary_weight = len(dataset) % 4 + 1
    final_score = int(base_result * secondary_weight * 100)
    
    # Red herring: string-based encoding that isn't used
    status_msg = "DIAGNOSTIC_PASS" if final_score > 200 else "DIAGNOSTIC_PENDING"
    encoded_status = ''.join(chr(ord(c) ^ 3) for c in status_msg)  # meaningless transformation
    
    return final_score

# Entry point
if __name__ == '__main__':
    # Irrelevant setup code
    system_id = "SENS-ARRAY-7X"
    calibration_matrix = [[1, 0], [0, 1]]
    timestamp = 1712345678
    
    # Collect real data
    collected_data = collect_sensor_readings()
    
    # Unused variable - misleading intermediate result
    entropy_metric = compute_entropy(collected_data)
    
    # Feature extraction (partially distractive)
    extracted_mag = extract_features(collected_data)
    
    # Another decoy computation
    stability_flag = evaluate_stability(collected_data)
    dummy_checksum = generate_checksum(collected_data)
    
    # Critical threshold configuration
    thresholds = {
        'base': 4.5,
        'tolerance': 1.2
    }
    
    # Key execution point
    final_diagnostic = analyze_pattern(collected_data, thresholds)
    
    # Output target result
    print(f"Result: {final_diagnostic}")