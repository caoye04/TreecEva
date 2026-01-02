import math

# Simulated sensor array diagnostics with noise filtering and health scoring
def collect_sensor_data():
    raw_values = [127, 255, 192, 64, 96, 144, 224, 32]
    noise_floor = 30
    filtered = [v for v in raw_values if v > noise_floor]
    return filtered

# Irrelevant helper - looks useful but unused in critical path
def deprecated_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Signal processing: applies gain, removes outliers, computes RMS
def process_signal_chunk(chunk, gain=1.5):
    amplified = [x * gain for x in chunk]
    # Outlier removal: exclude values beyond 2*std from mean
    mean_val = sum(amplified) / len(amplified)
    variance = sum((x - mean_val) ** 2 for x in amplified) / len(amplified)
    std_dev = math.sqrt(variance)
    cleaned = [x for x in amplified if abs(x - mean_val) <= 2 * std_dev]
    
    # Dead code path - never executed due to fixed condition
    if False:
        fallback = [x + 10 for x in amplified]
        return fallback
    
    return cleaned

# Data enrichment with decoy transformations
def enrich_with_metadata(readings):
    metadata_tag = 'VER_2.1'
    timestamp_offset = 1623478900
    sequence_ids = [hash(f'{timestamp_offset + i}') % 1000 for i in range(len(readings))]
    # Decoy structure - not used later
    extended = [{'value': v, 'seq': s, 'tag': metadata_tag} for v, s in zip(readings, sequence_ids)]
    return [item['value'] for item in extended]  # Only values matter

# Core analysis function (critical path)
def compute_health_index(values):
    # Apply logarithmic weighting to compress dynamic range
    weighted = [math.log(v + 1) for v in values]
    base_score = sum(weighted)
    
    # Interference: complex-looking but unused branching
    mode_flag = 'NORMAL'
    if len(values) > 10:
        mode_flag = 'OVERSIZED'
    elif len(values) % 2 == 0:
        mode_flag = 'EVEN_COUNT'
    else:
        mode_flag = 'ODD_COUNT'
    
    # Real logic: apply threshold-based penalty
    penalty = 0
    for v in values:
        if v < 100:
            penalty += 5
    adjusted_score = base_score - penalty
    
    # Bit manipulation red herring
    binary_mask = 0b110101
    masked_score = int(adjusted_score) & binary_mask  # Misleading use of bitwise AND
    
    # Final score uses original adjusted_score, ignoring masked_score
    return round(adjusted_score * 1.05, 4)

# Secondary transformation chain (distraction)
def legacy_compatibility_layer(data):
    if not data:
        return [0]
    transformed = []
    for x in data:
        if x % 2 == 0:
            transformed.append(x >> 2)  # Right shift even numbers
        else:
            transformed.append(x << 1)  # Left shift odd numbers
    return transformed

# Main pipeline functions
processed_cache = {}
def process_signal(signal_id, data):
    if signal_id in processed_cache:
        return processed_cache[signal_id]
    
    chunk_result = process_signal_chunk(data)
    enriched = enrich_with_metadata(chunk_result)
    processed_cache[signal_id] = enriched
    return enriched

# Aggregation across multiple sensors
def aggregate_diagnostics(sensor_list):
    all_readings = []
    for sid in sensor_list:
        raw = collect_sensor_data()
        processed = process_signal(sid, raw)
        all_readings.extend(processed[:4])  # Limit per sensor
    
    # Filtering out low-amplitude signals
    significant = [x for x in all_readings if x >= 80]
    return significant

# Final analysis with conditional branching distraction
def analyze_readings(readings):
    if len(readings) == 0:
        return -1.0
    
    # Redundant validation block
    valid_types = all(isinstance(x, (int, float)) for x in readings)
    if not valid_types:
        return -999.0
    
    # Key computation
    health_index = compute_health_index(readings)
    
    # Distractor: elaborate state machine that defaults always
    states = ['INIT', 'ACQUIRE', 'PROCESS', 'FINALIZE']
    current_state = states[3]
    timeout_threshold = None
    
    for s in states:
        if s == 'INIT':
            timeout_threshold = 100
        elif s == 'FINALIZE':
            timeout_threshold = 50  # Overwritten
    
    # Conditional expression distraction
    status_flag = 'OK' if health_index > 20 else 'LOW' if health_index > 10 else 'CRIT'
    debug_code = 200 + (1 if status_flag == 'OK' else 0)
    
    # Critical assignment - this is the answer point
    final_diagnostic = health_index + (10 if debug_code == 201 else 0)
    
    # Unused telemetry
    telemetry_snapshot = {
        'final_flag': status_flag,
        'debug': debug_code,
        'threshold': timeout_threshold,
        'readings_count': len(readings)
    }
    
    return final_diagnostic

# Execution flow
sensor_ids = [101, 102, 103]
signal_pool = aggregate_diagnostics(sensor_ids)
processed_signals = [x for x in signal_pool if x % 2 == 1]  # Keep only odd-valued signals

# Key statement
final_diagnostic = analyze_readings(processed_signals)

print(f"Target result: {final_diagnostic}")