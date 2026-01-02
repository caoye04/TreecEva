def preprocess_signal(raw):
    # Irrelevant transformation chain (distractor)
    filtered = [x * 0.95 for x in raw if x > 0]
    normalized = [y / max(filtered) for y in filtered]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    return smoothed + [0] * (len(raw) - len(smoothed))  # Padding to preserve length


def compute_entropy(data):
    # Dead function: not used in final logic
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    return -sum((count/total) * log(count/total) for count in freq.values())


def shift_sequence(seq, key):
    # Bit manipulation red herring
    rotated = [(x << 1) ^ key % 17 for x in seq]
    return rotated[:len(seq)//2]  # Truncation — unused path


def extract_features(dataset):
    # Complex slicing and case conversion distraction
    text_trace = ''.join([chr(97 + (x % 26)) for x in dataset[:10]])
    inverted = text_trace[::-1].upper()  # Reversed uppercase string — irrelevant
    code_points = [ord(c) - 96 for c in inverted.lower()]
    return code_points  # Unused return


def transform_readings(values):
    # Core relevant computation buried in noise
    base = [v ** 0.5 for v in values if v % 2 == 1]  # Only odd values are processed
    adjusted = [b * 1.5 for b in base]
    shifted = [int(a) << 1 for a in adjusted]  # Left bit shift by 1
    return shifted  # This is critical for later step


def analyze_pattern(signal, limit):
    # Main analysis with slicing and conditional logic
    if len(signal) < limit:
        return -1
    
    # Real computation begins here
    segment = signal[1:-1]  # Slice out first and last
    doubled = [x * 2 for x in segment]
    
    # Conditional filtering
    candidates = []
    for d in doubled:
        if d > 50 and (d & 1) == 0:  # Greater than 50 and even
            candidates.append(d)
    
    # Sorting is required to find median
    sorted_candidates = sorted(candidates)
    mid = len(sorted_candidates) // 2
    
    if len(sorted_candidates) == 0:
        return 0
    elif len(sorted_candidates) % 2 == 1:
        return sorted_candidates[mid] + 3
    else:
        return (sorted_candidates[mid-1] + sorted_candidates[mid]) // 2 - 7

# --- Distractor Variables (Misleading Initializations) ---
baseline_score = 88.4
reference_map = {i: chr(65 + i) for i in range(20)}
data_buffer = [0] * 15
offset_key = sum(range(5, 12))  # 57 — looks important

# --- Simulated Sensor Array Readings (Input Data) ---
raw_input = [25, 49, 81, 100, 144, 169, 196, 225, 256, 289]

# --- Irrelevant Processing Chain ---
temp_analysis = preprocess_signal(raw_input)
entropy_metric = compute_entropy(temp_analysis)
reduced_set = shift_sequence(raw_input, offset_key)
feature_codes = extract_features(raw_input)

# --- Key Execution Path ---
transformed_data = transform_readings(raw_input)  # sqrt of odds, scaled, bit-shifted
threshold = 3

# --- Critical Statement ---
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")