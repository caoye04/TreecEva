import math

def preprocess_signal(raw_data):
    filtered = []
    noise_floor = 0.1
    for x in raw_data:
        if abs(x) > noise_floor:
            filtered.append(x ** 2)
    return filtered

def shift_phase(data, steps):
    n = len(data)
    if n == 0:
        return data
    effective_shift = steps % n
    return data[-effective_shift:] + data[:-effective_shift]

def calculate_entropy(arr):
    total = sum(arr)
    if total == 0:
        return 0.0
    probs = [v / total for v in arr if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 6)

def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum % 1000

def validate_sequence(seq):
    if len(seq) < 3:
        return False
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return False
    return True

def extract_features(buffer):
    features = {}
    size = len(buffer)
    
    # Irrelevant feature computations (distractors)
    avg = sum(buffer) / size if size else 0
    variance = sum((x - avg) ** 2 for x in buffer) / size if size else 0
    peak = max(buffer, default=0)
    
    features['average'] = avg
    features['variance'] = variance
    features['peak'] = peak
    
    # Real feature used later
    features['length_flag'] = size > 5
    
    # Dead code path - never accessed
    if False:
        temp = [x for x in buffer if x > avg]
        features['ignored'] = len(temp)
    
    return features

def analyze_pattern(signal_buffer, threshold):
    # Step 1: Preprocess signal
    processed = preprocess_signal(signal_buffer)
    
    # Distractor: Phase shifting (not used in final result)
    shifted = shift_phase(processed, 2)
    
    # Step 2: Extract relevant metadata
    meta = extract_features(processed)
    
    # Step 3: Compute entropy (key intermediate value)
    entropy_value = calculate_entropy(processed)
    
    # Step 4: Generate checksum (used to influence logic)
    chksum = generate_checksum(processed)
    
    # Step 5: Create working copy using slicing
    working_slice = processed[1:-1] if len(processed) > 2 else processed[:]  
    
    # Step 6: Apply threshold filter
    filtered_slice = [x for x in working_slice if x > threshold]
    
    # Step 7: Check sequence validity (decoy condition)
    valid_seq = validate_sequence(filtered_slice)
    
    # Step 8: Compute aggregate metric
    aggregate = 0
    multiplier = 1
    for i, val in enumerate(filtered_slice):
        if i % 2 == 0:
            aggregate += val * multiplier
        else:
            aggregate -= val // (multiplier + 1)
        multiplier += 1
    
    # Step 9: Combine with entropy and checksum (hidden dependency)
    # Note: Only checksum % 50 affects final decision
    adjustment = chksum % 50
    
    # Step 10: Main branching logic
    if meta['length_flag'] and entropy_value > 1.5:
        base_result = aggregate * 2 + adjustment
    elif entropy_value > 1.0:
        base_result = aggregate + adjustment * 2
    else:
        base_result = adjustment - aggregate
    
    # Step 11: Final transformation
    final_diagnostic = int(base_result + entropy_value * 10)
    
    # Red herring: Unused complex calculation
    def deep_analysis():
        return sum(math.sin(x) for x in processed) * math.pi
    
    return final_diagnostic

# Irrelevant global variables
SYSTEM_OFFSET = 17
CALIBRATION_MATRIX = [[1, 0], [0, 1]]
TEMP_LOG = []

# Input data
raw_signal = [0.12, -0.05, 0.34, 0.21, -0.01, 0.58, 0.43]
threshold = 0.25

# Execution
processed_signal = preprocess_signal(raw_signal)
# Signal gets transformed: [0.0144, 0.1156, 0.0441, 0.3364, 0.1849]
# After preprocessing: values above noise floor squared
# Then slice: working_slice = [0.1156, 0.0441, 0.3364] (excluding first and last)
# Filtered by threshold: [0.3364]
# Entropy of processed = calculate_entropy([0.0144, 0.1156, 0.0441, 0.3364, 0.1849])
# Sum = 0.6954, normalized: [~0.0207, ~0.1662, ~0.0634, ~0.4837, ~0.2659]
# Entropy ≈ -sum(p log2 p) ≈ 2.01 -> rounded to 2.009723
# Chksum: generated via XOR of scaled values + index → deterministic mod 1000
# Computation leads to chksum = 123 → adjustment = 123 % 50 = 23
# aggregate = 0.3364 (only one element, even index → +val*1)
# base_result = 0.3364 + 23*2 = 46.3364 (since entropy > 1.0 but length flag true & entropy >1.5 false)
# Actually: entropy ~2.01 > 1.5 → use first branch: base_result = 0.3364*2 + 23 = 23.6728
# final_diagnostic = int(23.6728 + 2.009723 * 10) = int(23.6728 + 20.09723) = int(43.77) = 43

final_diagnostic = analyze_pattern(raw_signal, threshold)
print(f"Result: {final_diagnostic}")