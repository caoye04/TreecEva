from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    normalized = [(x - 10) / (100 - 10) for x in filtered]
    scaled = [int(x * 1000) for x in normalized]
    return scaled

# Irrelevant helper - dead path
def deprecated_filter(data):
    return [x for x in data if x > 50]

# Transform data using sliding window statistics
def sliding_window_stats(seq, size=3):
    if len(seq) < size:
        return []
    stats = []
    for i in range(len(seq) - size + 1):
        window = seq[i:i+size]
        mean_val = sum(window) / size
        var = sum((x - mean_val) ** 2 for x in window) / size
        stats.append(round(math.sqrt(var)))
    return stats

# Unused transformation - red herring
transform_strategy = lambda w: [x**2 for x in w if x % 2 == 0]

# Core transformation function
def transform_signal(amplitudes):
    halved = [a // 2 for a in amplitudes]
    shifted = [a >> 1 for a in halved]
    return [a + 5 for a in shifted]

# Frequency counter with irrelevant aggregation
def count_patterns(data):
    freq_map = defaultdict(int)
    for d in data:
        freq_map[d] += 1
    # Decoy computation
    entropy = 0.0
    total = sum(freq_map.values())
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return freq_map  # entropy unused

# Main pattern analyzer
def analyze_patterns(dataset, threshold):
    # Step 1: Count occurrences
    counts = Counter(dataset)
    
    # Step 2: Filter by threshold
    significant = {k: v for k, v in counts.items() if v >= threshold}
    
    # Step 3: Compute weighted score
    weight_fn = lambda k, v: (k * v) if k % 2 == 1 else (k * v // 2)
    weighted_total = sum(weight_fn(key, val) for key, val in significant.items())
    
    # Step 4: Apply correction factor based on bit properties
    bit_correction = 0
    for k in significant.keys():
        binary_rep = bin(k)[2:]
        ones = binary_rep.count('1')
        zeros = binary_rep.count('0')
        bit_correction += (ones - zeros) * 3
    
    # Step 5: Combine results
    raw_score = weighted_total + bit_correction
    
    # Step 6: Adjust based on distribution skew
    values = list(significant.values())
    if len(values) > 1:
        mean_v = sum(values) / len(values)
        variance = sum((v - mean_v) ** 2 for v in values) / len(values)
        skew_adjustment = int(variance ** 0.5) * 5
        raw_score += skew_adjustment
    
    # Step 7: Final clamping (not triggered)
    if raw_score > 10000:
        raw_score = 9999
    
    # Step 8: Diagnostic calculation
    diagnostic_code = (raw_score * 3) + 7
    return diagnostic_code

# --- Simulation Setup ---

# Real sensor readings (simulated)
sensor_log = [85, 92, 15, 73, 88, 94, 67, 85, 92, 73, 88, 94, 67, 85, 73, 94, 88, 94]

# Irrelevant preprocessing path (dead code)
cleaned_stream = deprecated_filter(sensor_log)

# Core execution path
processed = preprocess_readings(sensor_log)
transformed_signal = transform_signal(processed)
window_features = sliding_window_stats(transformed_signal, 3)

# Additional decoy structure
analysis_cache = {}
temp_result = count_patterns(window_features)  # result not used downstream

# Key threshold determined from meta-analysis (fixed for determinism)
key_threshold = len(processed) // 7  # evaluates to 2

# Data transformation before final analysis
temp_data = [x + 1 for x in transformed_signal]
filtered_data = [x for x in temp_data if x % 3 != 0]
shifted_data = [x << 1 for x in filtered_data]

# Final transformation step
transformed_data = [x ^ 25 for x in shifted_data]  # XOR with constant

# Critical execution point
final_diagnostic = analyze_patterns(transformed_data, key_threshold)

print(f"Result: {final_diagnostic}")