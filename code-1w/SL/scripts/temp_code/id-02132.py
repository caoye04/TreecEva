import itertools
from collections import defaultdict, Counter

# Simulated sensor data ingestion with noise and redundancy
def fetch_sensor_readings():
    raw_streams = [
        [1.2, 0.9, 1.5, 2.1, 1.8, 0.0, 3.2, 2.9],
        [0.8, 1.1, 1.4, 0.0, 2.3, 1.9, 3.1, 2.7],
        [1.0, 0.0, 1.6, 2.2, 1.7, 0.0, 3.3, 2.8]
    ]
    return raw_streams

# Irrelevant preprocessing: spectral decomposition (not used in final path)
def compute_spectral_signature(signal):
    magnitude = sum(x ** 2 for x in signal)
    phase_shift = max(signal) - min(signal)
    return magnitude * 0.5 + phase_shift * 0.1

# Redundant transformation chain
def denoise_signal(stream):
    cleaned = [x for x in stream if x > 0.5]  # Remove low-noise artifacts
    smoothed = []
    window = 3
    for i in range(len(cleaned)):
        start = max(0, i - window + 1)
        segment = cleaned[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    return smoothed

# Core transformation pipeline
def apply_calibration(data, factor=1.05):
    calibrated = [[round(x * factor, 3) for x in seq] for seq in data]
    return calibrated

# Misleading feature extraction (dead end)
def extract_temporal_features(seq_list):
    features = defaultdict(float)
    all_vals = list(itertools.chain.from_iterable(seq_list))
    features['jitter'] = sum(abs(a - b) for a, b in zip(all_vals, all_vals[1:]))
    features['trend'] = all_vals[-1] - all_vals[0]
    return features

# Decoy function: looks important but unused in logic path
def validate_consistency(dataset):
    shape_check = all(len(row) == len(dataset[0]) for row in dataset)
    range_check = all(0.5 <= val <= 5.0 for row in dataset for val in row)
    return shape_check and range_check

# Real processing begins here — subtle due to distractions above
def aggregate_signals(calibrated_data):
    flattened = list(itertools.chain.from_iterable(calibrated_data))
    filtered = [x for x in flattened if x >= 1.5]  # Only significant readings
    bucketed = defaultdict(int)
    for val in filtered:
        bucket = int(val * 2) / 2  # Quantize to nearest 0.5
        bucketed[bucket] += 1
    return dict(bucketed)

# Secondary transformation using statistical moments
def compute_moments(values):
    n = len(values)
    if n == 0:
        return 0, 0, 0
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    skewness = sum((x - mean) ** 3 for x in values) / (n * (variance ** 1.5)) if variance > 0 else 0
    return round(mean, 3), round(variance, 3), round(skewness, 3)

# Main metric processor combining multiple concepts
def process_metrics(aggregated_dict, cfg):
    counts = list(aggregated_dict.values())
    keys = list(aggregated_dict.keys())
    
    # Conditional expression based on configuration
    primary_weight = 1.2 if cfg.get('high_sensitivity') else 0.8
    adjustment = 0.1 if len(counts) > 5 else 0.25
    
    # Compute derived statistics
    total_events = sum(counts)
    peak_density = max(counts) if counts else 1
    entropy_proxy = 0
    for count in counts:
        if count > 0 and total_events > 0:
            prob = count / total_events
            entropy_proxy -= prob * __import__('math').log(prob)
    
    # Bit manipulation red herring (unused)
    magic_flag = (total_events << 2) ^ 0xCAFEBABE
    checksum = sum(magic_flag.to_bytes(4, 'little')) & 0xFF
    
    # Actual critical computation path
    base_score = total_events * primary_weight
    penalty = abs(peak_density - 4) * adjustment * 100
    final_value = base_score - penalty + (entropy_proxy * 50)
    
    # Early exit decoy — never triggered under current data
    if checksum < 10:
        return -999
        
    return round(final_value, 3)

# Configuration with misleading fields
cfg_params = {
    'high_sensitivity': True,
    'mode': 'diagnostic',
    'version': '2.1',
    'calibration_needed': False,
    'timeout': 5000
}

# Orchestration with hidden key steps
if __name__ == '__main__':
    # Step 1: Fetch raw data
    raw_input = fetch_sensor_readings()
    
    # Step 2: Denoise each stream (relevant)
    processed_streams = [denoise_signal(stream) for stream in raw_input]
    
    # Step 3: Apply physical calibration (relevant)
    calibrated_data = apply_calibration(processed_streams, factor=1.05)
    
    # Step 4: Aggregate across sensors (critical)
    transformed_data = aggregate_signals(calibrated_data)
    
    # Step 5: Extract temporal features — looks important, not used
    temporal_analysis = extract_temporal_features(calibrated_data)
    
    # Step 6: Validate (unused result)
    validation_status = validate_consistency(calibrated_data)
    
    # Step 7: Compute moments for report (distractor)
    moment_stats = compute_moments(list(itertools.chain.from_iterable(calibrated_data)))
    
    # Step 8: Final diagnostic score (KEY STATEMENT)
    final_diagnostic = process_metrics(transformed_data, cfg_params)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")