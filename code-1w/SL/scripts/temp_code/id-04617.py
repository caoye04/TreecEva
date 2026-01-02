from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition (distractor: some values are irrelevant)
sensor_readings = [14, 19, 24, 35, 46, 57, 68, 79, 83, 94, 105, 116, 127, 138, 149]

def apply_filter(data, threshold=50):
    # Only values above threshold are processed further (partial relevance)
    filtered = [x for x in data if x > threshold]
    return [x - 50 for x in filtered]  # Normalize high-frequency signals

def generate_checksum(seq):
    # Irrelevant utility function — looks important but unused in critical path
    return sum(x * (i + 1) for i, x in enumerate(seq)) % 1000

def transform_sequence(seq):
    # Applies bit manipulation and arithmetic (mixed operations)
    transformed = []
    for val in seq:
        temp_val = (val << 1) ^ 7  # Left shift and XOR
        if temp_val % 3 == 0:
            temp_val = int(math.sqrt(temp_val)) + 2
        transformed.append(temp_val)
    return transformed

def evaluate_peaks(data):
    # Misleading analysis: computes peaks but not used in final result
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return len(peaks)

def accumulate_diagnostic(values):
    # Core accumulation logic with conditional expressions
    total = 0
    multiplier = 1
    for v in values:
        # Conditional expression affecting multiplier
        multiplier = 2 if v > 20 else 1
        total += v * multiplier
    return total

def extract_features(data):
    # Uses enumerate and zip to pair indices and values (required idiom)
    indexed = list(enumerate(data))
    shifted = [v - 1 for v in data[1:]] + [0]
    pairs = list(zip(data, shifted))  # Structural pairing
    features = []
    for idx, val in indexed:
        if idx % 2 == 0:
            features.append(val * 2)
    return features

def analyze_signal(raw):
    # Main processing chain
    stage1 = transform_sequence(raw)
    
    # Dead code path: this variable is never used
    checksum_probe = generate_checksum(stage1)
    
    # This call looks important but doesn't affect output
    _ = evaluate_peaks(stage1)
    
    stage2 = extract_features(stage1)
    stage3 = accumulate_diagnostic(stage2)
    
    # Final computation step
    adjustment = sum(1 for x in stage1 if x > 10)  # Count significant signals
    final_score = stage3 + (adjustment * 3)
    
    # Decoy variables that look like they might be used
    debug_log = {'stage': 'final', 'score': final_score, 'valid': True}
    validation_flag = final_score > 100 and len(raw) > 5
    
    # Actual answer carrier
    final_diagnostic = final_score if validation_flag else -1
    return final_diagnostic

# Irrelevant data structure: distractor
historical_stats = defaultdict(lambda: 0)
for val in sensor_readings:
    historical_stats[val // 10] += 1

# Unused counter operation
freq_count = Counter(sensor_readings)

# Signal preprocessing pipeline
raw_data_snapshot = sensor_readings.copy()
processed_data = apply_filter(raw_data_snapshot)

# Key execution point
final_diagnostic = analyze_signal(processed_data)

# Output the target result
print(f"Target result: {final_diagnostic}")