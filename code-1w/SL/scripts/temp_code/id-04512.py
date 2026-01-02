import itertools

# Simulated sensor array data processing with red herrings and complex flow
def preprocess_sensors(raw_readings, filter_mask):
    processed = []
    temp_accum = 0
    for val in raw_readings:
        if val & filter_mask:  # bitwise relevance check (partially used)
            temp_accum += val ^ 0xAAAA
        else:
            temp_accum -= val >> 2
    checksum = sum(raw_readings) % 17

    # Distractor: dead computation path
    anomaly_score = 0
    for i in range(len(raw_readings)):
        anomaly_score += (raw_readings[i] * (i + 1)) % 9
    anomaly_score = (anomaly_score * 0.1)  # unused

    # Real transformation
    processed = [x * 3 + 7 for x in raw_readings if x % 2 == 1]
    return processed

# Irrelevant helper (decoy function)
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Signal compression using slicing and set operations
def compress_signal(sequence):
    if len(sequence) < 5:
        return sequence
    
    # Real logic: use every 3rd element, reverse middle slice
    mid_start = len(sequence) // 3
    mid_end = 2 * len(sequence) // 3
    segment_a = sequence[:mid_start]
    segment_b = sequence[mid_start:mid_end][::-1]  # reversed
    segment_c = sequence[mid_end:]
    
    # Combine with offset shift
    combined = [x + 10 for x in segment_a] + [x + 5 for x in segment_b] + [x + 2 for x in segment_c]
    
    # Slicing final portion
    compressed = combined[::3]  # take every third
    
    # Distractor: set operation with no downstream use
    unique_vals = set(combined)
    outliers = {x for x in unique_vals if x > 50}
    adjustment_factor = len(outliers) * 0.5  # never used
    
    return compressed

# Threshold mapping with dictionary and logical evaluation
def build_threshold_map(config_code):
    base_map = {}
    for i in range(10):
        key = chr(ord('A') + i)
        base_map[key] = (i * config_code) % 13
    
    # Unused alternate map
    alt_map = {k: v * 2 for k, v in base_map.items() if v % 3 == 0}
    
    # Return main map
    return base_map

# Core analysis with multiple concepts
def analyze_signal(data, thresholds):
    # Use itertools to generate combinations
    pairs = list(itertools.combinations(data[:6], 2))
    pair_scores = []
    
    for a, b in pairs:
        score = (a & b) + (a | b)  # bitwise mix
        if a > b:
            score -= (a - b) * 0.5
        pair_scores.append(int(score))
    
    # Aggregate with conditional logic
    total_impulse = sum(pair_scores)
    
    # Control flow with dictionary lookup
    category = 'UNKNOWN'
    if total_impulse > thresholds['D'] * 4:
        category = 'HIGH'
    elif total_impulse > thresholds['G'] * 2:
        category = 'MEDIUM'
    else:
        category = 'LOW'
    
    # Final diagnostic calculation
    modifier = thresholds['F'] if category == 'MEDIUM' else thresholds['B']
    final_diagnostic = (total_impulse // modifier) + len(pair_scores)
    
    # Dead code path: irrelevant state machine
    state = 0
    for ps in pair_scores:
        state = (state * 3 + ps) % 100
        if state > 80:
            break
    # state value never used
    
    return final_diagnostic

# --- Main Execution ---
if __name__ == "__main__":
    # Initial sensor readings
    sensor_input = [12, 15, 22, 27, 34, 39, 41, 46, 53]
    mask_filter = 0x5

    # Step 1: Preprocess sensors
    filtered_stream = preprocess_sensors(sensor_input, mask_filter)
    
    # Distractor variables
    normalized = [round(x * 0.85, 2) for x in filtered_stream]  # not used
    max_normalized = max(normalized) if normalized else 0  # decoy
    
    # Step 2: Compress signal
    compressed_data = compress_signal(filtered_stream)
    
    # Distractor: slicing misuse
    test_slice = compressed_data[2:2]  # empty
    if test_slice:
        compressed_data = [x * 2 for x in compressed_data]
    
    # Step 3: Build threshold map
    threshold_map = build_threshold_map(7)
    
    # Key statement
    final_diagnostic = analyze_signal(compressed_data, threshold_map)
    
    # Output result
    print(f"Target result: {final_diagnostic}")