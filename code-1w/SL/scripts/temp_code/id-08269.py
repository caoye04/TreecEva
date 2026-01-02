import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return [val ** 2 + 1 for val in x if val % 3 == 0]

# Decoy statistical calculator (misleading intermediate result)
def decoy_stats(seq):
    mean = sum(seq) / len(seq)
    variance = sum((x - mean) ** 2 for x in seq) / len(seq)
    return {'avg': mean, 'var': variance, 'decoy_flag': True}

# Core signal filter: removes outliers beyond 1.5 IQR (relevant)
def filter_outliers(arr):
    sorted_vals = sorted(arr)
    q1 = sorted_vals[len(sorted_vals) // 4]
    q3 = sorted_vals[3 * len(sorted_vals) // 4]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [x for x in arr if lower <= x <= upper]

# Frequency encoder using bit manipulation (relevant)
def encode_frequency(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    # Bitwise pack: use lower 8 bits for frequency, higher bits for value * 10
    packed = []
    for k, f in freq_map.items():
        if f > 1:  # Only pack repeated values
            packed.append(int(k * 10) << 8 | (f & 0xFF))
    return packed

# Data normalizer with red herring scaling (partially relevant)
def normalize_data(series, scale=100):
    min_val, max_val = min(series), max(series)
    if max_val == min_val:
        return [0] * len(series)
    # Apply normalization but scale misleadingly
    normalized = [(x - min_val) / (max_val - min_val) for x in series]
    fake_scaled = [round(n * 42) for n in normalized]  # Red herring computation
    return normalized  # Only this line matters

# Main processing pipeline (key logic)
def process_pipeline(raw):
    # Step 1: Filter noise (arithmetic + conditional)
    clean_data = filter_outliers(raw)
    
    # Step 2: Encode repeated patterns (dictionary + bit manipulation)
    encoded_signals = encode_frequency(clean_data)
    
    # Step 3: Normalize for uniform range (list comprehension)
    processed = normalize_data(clean_data)
    
    # Step 4: Compute weighted harmonic influence (advanced arithmetic)
    weights = [1 / (i + 1) for i in range(len(processed))]  # Decay weights
    weighted_sum = sum(w * p for w, p in zip(weights, processed))
    total_weight = sum(weights)
    avg_influence = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Step 5: Aggregate encoded signal entropy (bit-level logic)
    entropy = 0
    for code in encoded_signals:
        # Extract frequency from lower byte
        freq_part = code & 0xFF
        # Add entropy contribution only if even frequency
        if freq_part % 2 == 0:
            entropy += freq_part * math.log2(freq_part) if freq_part > 1 else 0
    
    # Step 6: Combine results through non-linear transformation
    if entropy > 5:
        final_score = avg_influence * (entropy ** 0.5)
    else:
        final_score = avg_influence * 10
    
    # Misleading secondary output (distractor)
    auxiliary_result = {
        'raw_length': len(raw),
        'clean_length': len(clean_data),
        'encoding_count': len(encoded_signals),
        'ghost_metric': sum(1 for x in raw if x > 50)  # Unused downstream
    }
    
    # Final transformation: apply sigmoid-like clamp (composite math)
    final_output = int((1 / (1 + math.exp(-final_score))) * 10000)
    
    return final_output

# Irrelevant global constants (red herrings)
MAX_BUFFER_SIZE = 1024
temp_cache = {i: i**3 for i in range(10)}
DECOY_THRESHOLD = 0.78

# Simulated sensor data stream (input)
data_stream = [12, 15, 12, 18, 20, 12, 25, 30, 15, 12, 40, 100, 5, 8, 12, 15, 18, 20]

# Execute main logic
final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")