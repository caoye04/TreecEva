from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_health_status(vitals):
    return sum(v > 75 for v in vitals) * 0.3

# Misleading data transformation
def transform_readings(data):
    scaled = [d * 1.05 for d in data]
    offset = [s - 2.1 for s in scaled]
    return [round(o, 2) for o in offset]

# Unused sorting function (dead code path)
def sort_by_priority(items):
    return sorted(items, key=lambda x: (x[1], -x[0]))

# Distractor: complex but unused bit manipulation
def encode_signal(value):
    if value < 0:
        value = (1 << 16) + value
    encoded = ((value & 0xFF) << 8) | ((value >> 8) & 0xFF)
    return encoded ^ 0x55AA

# Real logic starts here — subtle and buried among noise
def preprocess_metrics(raw):
    # Slice only the middle portion (relevant)
    trimmed = raw[2:-2]
    # Count frequencies (collections.Counter used)
    counts = Counter(trimmed)
    mode_val = counts.most_common(1)[0][1]
    return [x for x in trimmed if x % 2 == 1], mode_val

def compute_enhancement(values, base):
    enhancement = 0
    for i, v in enumerate(values):
        if i % 3 == 0:
            enhancement += int(math.log2(v + 1))  # Use of logarithm
        elif v > base:
            enhancement += (v // base)
    return enhancement

def validate_integrity(sequence):
    checksum = 0
    for i, s in enumerate(sequence):
        checksum ^= (s + i)  # Bitwise XOR red herring
    return checksum % 7 == 0

# Main evaluation logic (obscured by noise)
def evaluate_performance(metrics):
    # Step 1: Preprocess to extract odd-positioned values and mode count
    filtered, mode_count = preprocess_metrics(metrics)
    
    # Step 2: Apply enhancement based on dynamic base
    base_threshold = len(metrics) // 2
    boost = compute_enhancement(filtered, base_threshold)
    
    # Step 3: Simulate performance ceiling
    ceiling = 0
    temp_val = base_threshold
    while temp_val > 1:
        temp_val = temp_val // 2
        ceiling += 1
    
    # Step 4: Use string method as control gate (irrelevant string)
    flag_str = "system_ready_2024"
    if flag_str.upper().replace("_", "").isalpha():  # Always true
        ceiling *= 2
    
    # Step 5: Early return decoy (never triggered due to data)
    if sum(filtered) < 0:
        return -999
    
    # Step 6: Actual score computation
    raw_score = mode_count * boost * ceiling
    
    # Step 7: Apply false normalization (but not really used)
    normalized = raw_score / (1 + abs(raw_score) * 0.01)
    
    # Step 8: Final adjustment — this is where answer is set
    final_score = int(normalized) + 17
    
    # Dead code: unreachable print with slicing distraction
    debug_slice = str(final_score)[::-1]
    if debug_slice.startswith('9'):
        print(f'Debug: {debug_slice}')
    
    return final_score

# Irrelevant global variables (distractors)
vital_signs = [88, 92, 76, 101, 85]
signal_data = [encode_signal(i * 10) for i in range(5)]
priority_queue = [(3, 'low'), (1, 'high'), (2, 'medium')]

# Input data carefully constructed to yield deterministic result
metric_data = [4, 6, 7, 8, 7, 10, 7, 12, 7, 5]

# Key execution point
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")