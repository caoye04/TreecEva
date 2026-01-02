import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, count):
    """Generates synthetic sensor signals with noise (irrelevant for final result)"""
    signals = []
    for i in range(count):
        noise = math.sin(i * 0.5) * 0.1
        signals.append(baseline + noise + (i % 7))
    return signals


def extract_features(data_list):
    """Extract statistical features from data (partial red herring)"""
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    peak = max(data_list)
    return {
        'avg': mean_val,
        'var': variance,
        'peak': peak,
        'score': mean_val * 0.7 + peak * 0.3  # misleading metric
    }


def transform_sequence(seq, key_offset):
    """Apply bitwise transformation to sequence (distractor logic)"""
    transformed = []
    mask = 0b1101
    for i, val in enumerate(seq):
        shifted = (val * 3) ^ (i << 2)
        masked = shifted & mask
        transformed.append((masked + key_offset) % 25)
    return transformed


def filter_anomalies(raw_readings, limit):
    """Filter values exceeding threshold (partially used, adds complexity)"""
    clean_set = [x for x in raw_readings if abs(x - 50) < limit]
    outlier_count = len(raw_readings) - len(clean_set)
    if outlier_count > 5:
        clean_set.append(-1)  # flag
    return clean_set


def compute_checksum(items):
    """Compute XOR checksum of list (dead-end function)"""
    checksum = 0
    for item in items:
        checksum ^= int(item) % 100
    return checksum


def build_lookup(symbols):
    """Create mapping dictionary (set/dict operation - relevant)"""
    symbol_map = {}
    for idx, sym in enumerate(symbols):
        symbol_map[sym] = (idx * 19) % 37
    return symbol_map


def integrate_measurements(data_chunks, mode='standard'):
    """Aggregate multiple sensor chunks (intermediate processing)"""
    aggregated = []
    for chunk in data_chunks:
        if mode == 'standard':
            chunk_sum = sum(x * 0.9 for x in chunk if x > 0)
        else:
            chunk_sum = sum(abs(x) for x in chunk)
        aggregated.append(int(chunk_sum))
    return aggregated


def analyze_readings(dataset, config_map):
    """Core analysis function - computes final diagnostic value"""
    # Relevant code begins here
    base_key = config_map.get('base', 10)
    scale_factor = config_map.get('scale', 3)
    
    readings_set = set(dataset)  # use of set
    filtered_set = {x for x in readings_set if x % 2 == 1}  # set comprehension
    
    temp_store = {}
    for i, val in enumerate(sorted(filtered_set)):
        temp_store[i] = val * scale_factor + base_key
    
    # Critical computation path
    accumulation = 0
    for k, v in temp_store.items():
        if k % 3 == 0:
            accumulation += v
        elif k % 4 == 0:
            accumulation -= v
    
    # Secondary adjustment using dictionary lookup
    category_map = build_lookup(['A', 'B', 'C', 'D'])
    adjustment = category_map['C']  # deterministic: 'C' -> index 2 -> (2*19)%37 = 1
    
    final_score = accumulation + adjustment
    
    # Irrelevant post-processing (distractor)
    diagnostics_log = []
    for _ in range(3):
        diagnostics_log.append({
            'status': 'OK',
            'code': compute_checksum([final_score, adjustment])
        })
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Generate initial signal data (red herring - not directly used)
    raw_signals = generate_signals(baseline=45.0, count=100)
    
    # Extract features (used to mislead focus)
    signal_features = extract_features(raw_signals)
    
    # Simulate multiple sensor channels (partially relevant)
    channel_a = [64, 32, 18, 45, 77, 21, 93, 15, 44, 81]
    channel_b = [55, 29, 41, 76, 33, 19, 67, 22, 88, 14]
    channel_c = [48, 37, 52, 61, 25, 73, 11, 95, 30, 63]
    
    all_channels = [channel_a, channel_b, channel_c]
    
    # Transform each channel (distractor)
    transformed_a = transform_sequence(channel_a, key_offset=7)
    transformed_b = transform_sequence(channel_b, key_offset=7)
    transformed_c = transform_sequence(channel_c, key_offset=7)
    
    # Integrate measurements (semi-relevant preprocessing)
    integrated_values = integrate_measurements(all_channels, mode='standard')
    
    # Filter anomalies (creates modified dataset)
    cleaned_data = filter_anomalies(integrated_values, limit=40)
    
    # Build configuration map using dict operations (relevant)
    threshold_map = build_lookup(['base', 'scale', 'offset', 'limit'])
    threshold_map['base'] = 12  # override
    threshold_map['scale'] = 4
    
    # Processed data used in final analysis
    processed_data = [x + 1 for x in cleaned_data if x != -1]  # remove flag
    
    # Core diagnostic analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result
    print(f"Result: {final_diagnostic}")