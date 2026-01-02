from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(raw):    
    temp_adjusted = [x * 0.95 + 2.1 for x in raw if x > -50]
    filtered = [x for x in temp_adjusted if x < 100]
    outlier_count = len([x for x in raw if x < -40])  # irrelevant metric
    scaling_factor = 1.0 + (outlier_count * 0.01)
    calibrated = [x * scaling_factor for x in filtered]
    return calibrated

# Irrelevant auxiliary function (dead path)
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Core transformation chain
def encode_timestamps(length):
    timestamps = []
    for i in range(length):
        ts = (i * 17) % 127
        if ts % 3 == 0:
            ts = ts ^ 15  # bit manipulation red herring
        timestamps.append(ts)
    return timestamps

# Data fusion with conditional logic and distractors
def fuse_modalities(primary, secondary):
    fused = []
    aux_weights = [0.8, 1.2] * (len(primary) // 2 + 1)
    weight_index = 0
    
    for a, b in zip(primary, secondary):
        # Complex conditional mixing
        if a > 50 and b < 60:
            fused.append((a * 0.7 + b * 0.3) * aux_weights[weight_index])
        elif a < 30:
            fused.append(a + b * 0.1)
        else:
            fused.append((a + b) / 2.0)
        weight_index += 1
    
    # Dead computation branch
    if len(fused) > 100:
        smoothed = [sum(fused[i:i+3])/3 for i in range(len(fused)-2)]
    else:
        dummy_var = [x ** 0.5 for x in fused if x > 0]  # unused
    
    return fused

# Recursive frequency analysis (key component)
def analyze_frequency(seq, depth=0):
    if depth >= 3 or len(seq) <= 1:
        return sum(seq) / len(seq) if seq else 0
    
    grouped = defaultdict(list)
    for i, val in enumerate(seq):
        bucket = i % 4
        grouped[bucket].append(val)
    
    results = []
    for key in sorted(grouped.keys()):
        subset = grouped[key]
        transformed = [x * (1 + depth * 0.1) for x in subset]
        results.append(analyze_frequency(transformed, depth + 1))
    
    return sum(results) / len(results)

# Main processing pipeline
def process_signal_chain(raw_input):
    # Step 1: Preprocessing
    stage1 = preprocess_sensor_readings(raw_input)
    
    # Step 2: Encoding (irrelevant to final result but looks important)
    time_codes = encode_timestamps(len(stage1))
    encoded_pairs = list(zip(stage1, time_codes))
    
    # Step 3: Fusing with dummy secondary source
    dummy_sensor = [abs(hash(str(x)) % 100) for x in time_codes[:len(stage1)]]
    stage2 = fuse_modalities([p[0] for p in encoded_pairs], dummy_sensor)
    
    # Step 4: Frequency domain transformation
    spectral = [x * math.sin(i * 0.1) for i, x in enumerate(stage2)]
    spectral_clean = [x for x in spectral if not math.isnan(x)]
    
    # Step 5: Statistical summarization (distractor)
    summary_stats = {
        'mean': sum(spectral_clean) / len(spectral_clean),
        'peak': max(spectral_clean),
        'variance': sum((x - sum(spectral_clean)/len(spectral_clean))**2 for x in spectral_clean) / len(spectral_clean)
    }
    
    # Step 6: Actual critical transformation
    magnitude_vector = [abs(x) ** 0.8 for x in spectral_clean]
    normalized = [x / (1 + max(magnitude_vector)) for x in magnitude_vector]
    return normalized

# Final diagnostic logic
def analyze_signal(data_sequence):
    # Count patterns (uses Counter - required feature)
    pattern_counter = Counter()
    for x in data_sequence:
        if x < 0.1:
            pattern_counter['low'] += 1
        elif x < 0.5:
            pattern_counter['med'] += 1
        else:
            pattern_counter['high'] += 1
    
    # Bitwise analysis red herring
    bitwise_tally = 0
    for val in data_sequence[:10]:
        int_val = int(abs(val * 1000))
        bitwise_tally += (int_val & 7) ^ (int_val >> 2)  # complex but irrelevant
    
    # Critical recursive calculation
    freq_metric = analyze_frequency(data_sequence)
    
    # Conditional aggregation
    adjustment = 0.0
    if pattern_counter['high'] > 5:
        adjustment = 12.5
    elif pattern_counter['med'] > 10:
        adjustment = 8.2
    else:
        adjustment = 3.7
    
    # Final computation
    base_score = freq_metric * 100
    final_score = base_score + adjustment + (bitwise_tally * 0.01)  
    return int(round(final_score))

# Execution flow
if __name__ == '__main__':
    # Initial raw data
    sensor_data = [23.5, 67.2, -15.8, 89.1, 5.0, 102.3, -30.4, 77.6, 44.8, 95.9, 
                  12.1, 66.7, 200.0, -8.9, 33.4, 71.2, 55.5, 88.3, 19.7, 62.4,
                  47.8, 36.9, 53.1, 74.2, 29.5, 81.6, 38.3, 45.7, 69.8, 57.2]
    
    # Irrelevant baseline computation
    baseline_ref = sum(x ** 2 for x in sensor_data if x > 0) ** 0.5
    
    processed_data = process_signal_chain(sensor_data)
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")