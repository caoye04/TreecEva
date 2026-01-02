from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (irrelevant preprocessing)
def collect_signals(raw_readings):
    signal_cache = defaultdict(list)
    for key, val in raw_readings.items():
        if val > 0.1:
            signal_cache[key].append(val * 1.03)
    return signal_cache

# Unused diagnostic function - red herring
def legacy_analysis(data):
    total_spike = 0
    for entry in data:
        if entry.get('anomaly_score', 0) > 0.8:
            total_spike += 1
    return total_spike

# Core transformation pipeline
def normalize_readings(readings):
    normalized = []
    base_offset = 2.718
    for r in readings:
        adjusted = abs(r - base_offset) / (1 + math.log(1 + r))
        normalized.append(round(adjusted, 4))
    return normalized

# Frequency analysis - mostly irrelevant
def analyze_peaks(values):
    peak_count = 0
    for i in range(1, len(values)-1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peak_count += 1
    smoothed_peak = peak_count / (len(values) or 1)
    return round(smoothed_peak, 3)

# Critical path: metric processing with distractors
def compute_baselines(samples):
    avg = sum(samples) / len(samples)
    variance = sum((x - avg)**2 for x in samples) / len(samples)
    stdev = math.sqrt(variance)
    return {'mean': avg, 'stdev': stdev}

# Decoy state tracker - looks important but unused later
current_state = {
    'stage': 'diagnostic_phase_3',
    'version': 'v2.4.1-debug',
    'active_flags': [0, 1, 0, 1, 1],
    'last_updated': '2023-11-05T14:22:18Z'
}

# Real logic buried within distractions
def evaluate_threshold(score, rules):
    if score < rules['critical_low']:
        return 'alert'
    elif score >= rules['elevated']:
        return 'watch'
    else:
        return 'normal'

# Main processing function with hidden core logic
def process_metrics(data_chunk, config_map):
    # Irrelevant initialization block
    temp_buffer = [0] * 16
    checksum = 0
    for idx, val in enumerate(temp_buffer):
        checksum ^= (idx + val) & 0xFF
    
    # Actual relevant data flow starts here
    processed_items = []
    for k, readings in data_chunk.items():
        norm_vals = normalize_readings(readings)
        stats = compute_baselines(norm_vals)
        processed_items.append(stats['mean'])
    
    # Distracting control flow with unused branches
    mode_hint = 'unknown'
    if len(processed_items) > 5:
        mode_counter = Counter(processed_items)
        mode_hint = mode_counter.most_common(1)[0]
    else:
        mode_hint = 'insufficient_data'
    
    # Key calculation mixed with decoys
    aggregate = sum(x for x in processed_items if x > 0.5)
    suppression_factor = config_map.get('suppression', 1.0)
    adjustment = math.floor(aggregate * 100) / 100.0
    
    # Red herring: complex bit manipulation with no effect
    debug_flag = 0b1010
    mask = (debug_flag << 3) ^ 0b1101
    masked_result = mask & 0xFF
    
    # Final computation path - depends only on specific chain
    threshold = config_map['elevated']
    count_above = 0
    for item in processed_items:
        if item > threshold:
            count_above += 1
    
    # Answer derived from count_above and adjustment
    result_code = int((adjustment * 1000) // (count_above or 1)) + 42
    
    # Final output variable
    final_diagnostic = result_code * 2  # actual answer source
    
    # Dead code path - never reached due to prior assignment
    if final_diagnostic < 0:
        final_diagnostic = -final_diagnostic + 100
        
    return final_diagnostic

# Input data setup with meaningful names
health_data = {
    'sensor_A1': [3.2, 1.8, 2.5, 4.1, 3.6],
    'sensor_B2': [0.9, 1.1, 1.3],
    'sensor_C3': [5.5, 4.8, 5.1, 5.9],
    'sensor_D4': [2.2, 2.0],
    'sensor_E5': [6.1, 6.3, 6.0, 6.4, 6.2],
    'sensor_F6': [1.5, 1.7]
}

threshold_map = {
    'critical_low': 0.4,
    'elevated': 1.25,  # used in evaluation
    'suppression': 0.97
}

# Trigger execution
raw_input = {k: sum(v)/len(v) for k, v in health_data.items()}
signals = collect_signals(raw_input)

# Key statement execution point
final_diagnostic = process_metrics(health_data, threshold_map)

print(f"Target result: {final_diagnostic}")