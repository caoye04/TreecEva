import math

# Simulated sensor data processing with heavy distractions
def preprocess_segment(segment):
    return [x * 1.05 for x in segment if x > 0]

def compute_checksum(data):
    # Irrelevant checksum function (not used in final path)
    chk = 0
    for d in data:
        chk = (chk << 1) ^ int(d)
    return chk & 0xFFFF

def validate_frame(frame):
    # Dead code path — looks important but unused
    if len(frame) == 0:
        return False
    return sum(frame) % 2 == 0

# Distractor: complex-looking but unused transformation
def spectral_transform(signal):
    transformed = []
    for i in range(len(signal)):
        val = signal[i] * math.sin(i * math.pi / 8)
        transformed.append(round(val, 3))
    return transformed

# Decoy function that computes something plausible but irrelevant
def estimate_entropy(sequence):
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Real logic buried under noise
def extract_features(raw_stream, window_size=4):
    features = []
    for i in range(0, len(raw_stream) - window_size + 1, 2):
        window = raw_stream[i:i+window_size]
        avg = sum(window) / len(window)
        fluctuation = max(window) - min(window)
        if fluctuation > 0:
            score = (avg ** 2) / fluctuation
        else:
            score = avg
        features.append(round(score, 3))
    return features

def build_threshold_map(levels):
    # Looks like it's doing something critical, but only a subset is used
    base_map = {i: (10 + i*5)**1.5 for i in range(levels)}
    adjustment = {k: v * 0.85 for k, v in base_map.items()}
    # Only key 3 and 5 are actually used later
    return {k: v for k, v in adjustment.items() if k in [3, 5]}

def filter_anomalies(dataset, limit=100):
    # Unused filtering logic — red herring
    clean_set = []
    for entry in dataset:
        if abs(entry) < limit:
            clean_set.append(entry)
    return clean_set

def analyze_signal(buffer, thresholds):
    # Core logic: uses slicing, bitwise, arithmetic, and conditional logic
    segment_a = buffer[1:6]   # indices 1-5
    segment_b = buffer[4:9]   # overlapping slice
    
    # Key computation hidden among distractions
    pivot = buffer[0] ^ buffer[-1]  # XOR of first and last
    
    temp_val = 0
    for i, val in enumerate(segment_a):
        temp_val += (val * (i+1))
    
    secondary_sum = 0
    for j, num in enumerate(segment_b):
        secondary_sum += num * (j * 2)
    
    # This is the actual answer path
    raw_score = temp_val - secondary_sum
    adjustment_factor = thresholds.get(3, 0) * 0.1
    if raw_score > adjustment_factor:
        adjusted_score = raw_score * (thresholds.get(5, 1) * 0.01)
    else:
        adjusted_score = raw_score + adjustment_factor
    
    # Final transformation using slicing and arithmetic
    str_rep = str(abs(int(adjusted_score * 100)))
    sliced_part = str_rep[1:-1] if len(str_rep) > 2 else '0'  # Middle digits
    if sliced_part == '0':
        final_scalar = 1
    else:
        # Sum of middle digits
        final_scalar = sum(int(d) for d in sliced_part)
    
    return int(adjusted_score) + final_scalar

# --- Main execution with extensive distractions ---
if __name__ == "__main__":
    # Simulated input data
    sensor_input = [-2, 4, 7, 1, 8, 3, 6, 2, 9, -5]
    config_level = 7
    max_tolerance = 150
    debug_mode = False

    # Irrelevant preprocessing chain
    processed_input = preprocess_segment(sensor_input)
    frame_valid = validate_frame(processed_input)
    entropy_metric = estimate_entropy(processed_input)
    spectral_data = spectral_transform(processed_input)
    anomaly_filtered = filter_anomalies(sensor_input, max_tolerance)

    # Real data flow begins here
    feature_vector = extract_features(sensor_input, window_size=4)
    pattern_buffer = feature_vector + [13.5, 2.1, 8.9]  # Augmented buffer

    # Threshold map construction (only parts are used)
    threshold_map = build_threshold_map(config_level)

    # Dummy variables to mislead
    dummy_1 = compute_checksum([1, 2, 3, 4])
    dummy_2 = [math.sqrt(x) for x in range(1, 6)]
    temp_state = {"buffer_len": len(pattern_buffer), "version": "2.1-debug"}

    # Critical statement
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

    print(f"Result: {final_diagnostic}")