from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def collect_readings():
    raw_samples = [127, 63, 191, 31, 223, 95, 255, 0, 159, 239]
    processed = []
    for val in raw_samples:
        if val > 127:
            processed.append(val ^ 64)
        else:
            processed.append(val | 32)
    return processed

def apply_filter(data):
    # Irrelevant smoothing filter (unused path)
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) // 3)
    smoothed.append(data[-1])
    return smoothed

def generate_checksum(signal):
    # Unused checksum function - red herring
    chk = 0
    for x in signal:
        chk = (chk << 1) ^ x ^ (chk >> 7)
    return chk & 255

def transform_signal(seq):
    # Key transformation: bit-reversal followed by modulo clustering
    reversed_bits = []
    for x in seq:
        rev = int('{:08b}'.format(x)[::-1], 2)
        reversed_bits.append(rev)
    
    # Distractor: frequency analysis with unused result
    freq = Counter(reversed_bits)
    dominant = freq.most_common(1)[0][1] if freq else 0
    
    # Actual relevant transformation
    clustered = [x % 17 for x in reversed_bits]
    return clustered

def build_threshold_map(values):
    # Create adaptive thresholds based on statistical dispersion
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    
    # Redundant complex mapping (only part is used later)
    thresholds = defaultdict(float)
    for i, v in enumerate(values):
        thresholds[f'node_{i % 5}'] = abs(math.sin(v) * std_dev) + 0.1
    
    # Critical threshold subset
    critical_keys = ['node_0', 'node_2', 'node_4']
    return {k: thresholds[k] for k in critical_keys}

def evaluate_stability(indices):
    # Decoy analysis - never called but looks important
    window_size = 3
    stability_score = 0
    for i in range(len(indices) - window_size + 1):
        window = indices[i:i+window_size]
        if all(w < 10 for w in window):
            stability_score += 1
    return stability_score

def analyze_pattern(dataset, limits):
    # Core logic: count how many entries exceed dynamic thresholds cyclically
    cycle_length = len(limits)
    limit_values = list(limits.values())
    count = 0
    for idx, item in enumerate(dataset):
        # Uses cycling threshold comparison
        threshold = limit_values[idx % cycle_length]
        normalized_item = item / 16.0  # Scale to match threshold range
        if normalized_item > threshold:
            count += 1
            # Bit manipulation side-effect (distractor)
            temp_flag = (item << 2) & 0xFF
            temp_flag ^= 0xAA
    return count

# Execution flow with dead branches and irrelevant assignments
sensor_data = collect_readings()

# Dead code path - filtered data is never used
filtered_data = apply_filter(sensor_data)
checksum_value = generate_checksum(sensor_data)  # Unused

# Key transformation
transformed_data = transform_signal(sensor_data)

# Threshold construction
threshold_map = build_threshold_map(transformed_data)

# Diagnostic computation
baseline_index = sum(transformed_data) % 100  # Misleading intermediate
reference_key = f"node_{baseline_index % 3}"  # Looks important, unused

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")