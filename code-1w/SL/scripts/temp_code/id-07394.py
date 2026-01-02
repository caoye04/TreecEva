from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings
def collect_readings():
    raw_samples = [12, 15, 22, 12, 17, 22, 29, 30, 15, 12]
    offset = 5
    adjusted = [x + offset for x in raw_samples]  # Distractor: not actually used later
    return raw_samples

# Irrelevant transformation chain (dead path)
def legacy_filter(data):
    if len(data) == 0:
        return []
    filtered = []
    for x in data:
        if x % 2 == 0:
            filtered.append(x * 1.5)
    return [int(x) for x in filtered]

# Real preprocessing function
def preprocess(stream):
    count_freq = Counter(stream)
    most_common_val = count_freq.most_common(1)[0][1]
    normalized = [x / (most_common_val + 1e-6) for x in stream]  # Avoid division by zero
    scaled = [round(x * 3.7) for x in normalized]
    return scaled

# Bit manipulation decoy (never called)
def obscure_encode(n):
    n ^= 0xFF
    n = (n << 2) & 0xFF
    return n | (n >> 4)

# Auxiliary statistical function (misleading usage)
def get_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Core logic disguised among distractors
def generate_signature(seq):
    signature = 0
    for i, val in enumerate(seq):
        signature += (val * (i + 1)) ^ (i * 7)
    return signature % 1000

# Threshold mapping preparation (partially relevant)
def build_thresholds(base_seq):
    thresh_map = defaultdict(float)
    for idx, val in enumerate(base_seq):
        if idx % 3 == 0:
            thresh_map[f'node_{idx}'] = math.sqrt(val) * 1.8
        elif idx % 3 == 1:
            thresh_map[f'node_{idx}'] = abs(math.cos(val)) * 50
        else:
            thresh_map[f'node_{idx}'] = math.log(val + 1) * 10
    # Add decoy keys
    thresh_map['debug_mode'] = 999.9
    thresh_map['calibration_offset'] = -123.456
    return thresh_map

# Main analysis with critical computation hidden in logic
def analyze_pattern(dataset, thresholds):
    temp_state = []
    for i, item in enumerate(dataset):
        if i % 4 == 0:
            temp_state.append(item + int(thresholds.get(f'node_{i}', 1)))
        elif i % 4 == 2:
            temp_state.append(item - 3)
        else:
            temp_state.append(item)

    # Real computation path
    accumulated = 0
    for j in range(len(temp_state)):
        if temp_state[j] > 10:
            accumulated += j * temp_state[j]
        else:
            accumulated -= j

    # Decoy use of entropy (unused result)
    _ = get_entropy(temp_state)

    # Final masking operation
    final_score = (accumulated ^ 0x5A5A) & 0xFFFF
    if final_score > 32767:
        final_score -= 65536

    return final_score

# Unused recursive distraction
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Orchestration with misleading calls
if __name__ == '__main__':
    readings = collect_readings()                            # Step 1: Load base data
    legacy_output = legacy_filter(readings)                  # Step 2: Dead-end processing
    transformed_data = preprocess(readings)                  # Step 3: Actual transformation
    signature_code = generate_signature(transformed_data)    # Step 4: Side computation (not used)
    threshold_map = build_thresholds(transformed_data)       # Step 5: Prepare map with decoys
    
    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Output required result
    print(f"Result: {final_diagnostic}")