from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (real-time stream mockup)
sensor_readings = [
    [1.2, 0.8, 1.5, 2.3, 1.1],
    [0.9, 1.0, 1.6, 2.1, 0.7],
    [1.3, 1.4, 1.2, 2.4, 1.0],
    [0.7, 0.6, 1.8, 2.2, 0.5],
    [1.1, 1.3, 1.7, 2.5, 0.9]
]

# Irrelevant auxiliary mapping (distractor - not used in final computation)
legacy_mapping = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + 10,
    'C': lambda x: abs(x - 1)
}

# Preprocessing: normalize and filter noise (relevant)
def preprocess(stream):
    cleaned = []
    for frame in stream:
        # Remove values below noise floor (0.6)
        filtered = [x for x in frame if x >= 0.6]
        if len(filtered) < 3:
            continue
        mean_val = sum(filtered) / len(filtered)
        normalized = [round(x / mean_val, 3) for x in filtered]
        cleaned.append(normalized)
    return cleaned

# Misleading transformation chain (dead path)
def transform_legacy(data):
    result = []
    for row in data:
        temp = []
        for val in row:
            temp.append(legacy_mapping['A'](val))
        result.append(temp)
    return result

# Frequency analysis (partially relevant distractor)
def compute_entropy(signal):
    flat = [item for sublist in signal for item in sublist]
    count = Counter(flat)
    total = len(flat)
    entropy = -sum((freq / total) * math.log2(freq / total) for freq in count.values())
    return round(entropy, 4)

# Core diagnostic logic (relevant)
def detect_anomaly_pattern(seq):
    if len(seq) < 4:
        return False
    # Check for rising-falling-rising pattern
    for i in range(len(seq) - 3):
        if seq[i] < seq[i+1] > seq[i+2] < seq[i+3]:
            return True
    return False

# Threshold configuration map (relevant)
def build_threshold_map(readings):
    thresholds = defaultdict(float)
    col_means = [0] * len(readings[0])
    
    for r in readings:
        for i, v in enumerate(r):
            col_means[i] += v
    
    for i in range(len(col_means)):
        col_means[i] /= len(readings)
        
    # Assign dynamic thresholds (only even indices are used later)
    thresholds['t1'] = col_means[0] * 1.2
    thresholds['t2'] = col_means[2] * 0.8
    thresholds['t3'] = col_means[4] * 1.5  # unused but looks important
    
    # Add decoy keys
    thresholds['deprecated_flag'] = -1.0
    thresholds['calibration_offset'] = 999.0
    
    return thresholds

# Secondary validation (irrelevant - never called)
def validate_checksum(data):
    checksum = 0
    for row in data:
        for val in row:
            checksum ^= int(val * 100)
    return checksum % 17 == 0

# Signal analyzer (relevant)
def analyze_signal(data, config):
    score = 0
    pattern_count = 0
    
    # Real processing
    for sequence in data:
        if detect_anomaly_pattern(sequence):
            pattern_count += 1
        
        # Scoring based on threshold crossings (only t1 and t2 matter)
        above_t1 = sum(1 for x in sequence if x > config['t1'])
        below_t2 = sum(1 for x in sequence if x < config['t2'])
        
        if above_t1 > below_t2:
            score += 2
        else:
            score -= 1
    
    # Final heuristic
    if pattern_count >= 2:
        score += 5
    
    # Hidden adjustment: correct only if both conditions met
    if pattern_count == 0:
        score = -score  # negation trap (not triggered here)
    
    # Decoy operation (looks like correction but isn't executed)
    # if config['deprecated_flag'] > 0: score += 10
    
    return score * 17  # amplification factor

# --- Execution Flow ---
processed_data = preprocess(sensor_readings)

# Dead call (distractor)
entropy_value = compute_entropy(sensor_readings)

# Build actual config
threshold_map = build_threshold_map(sensor_readings)

# Unused transformation (red herring)
transformed = transform_legacy(processed_data)  # computed but ignored

# Key statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")