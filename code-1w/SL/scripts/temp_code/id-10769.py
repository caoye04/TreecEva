from collections import defaultdict, Counter

# Simulated sensor data stream with noise and metadata
def fetch_sensor_stream():
    raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
    metadata = {'source': 'alpha', 'version': '2.1', 'active': True}
    return raw, metadata

def apply_noise_filter(data):
    # Real processing: smooth out spikes using median logic
    filtered = []
    for i in range(len(data)):
        window = data[max(0, i-1):min(len(data), i+2)]
        median_val = sorted(window)[len(window)//2]
        filtered.append(median_val)
    return filtered

def generate_checksum(sequence):
    # Irrelevant red herring function - not used in final result
    chk = 0
    for val in sequence:
        chk = (chk * 31 + val) % 10007
    return chk

def extract_patterns(seq):
    # Extract repeating subsequences of length 3
    patterns = []
    for i in range(len(seq) - 2):
        patterns.append(tuple(seq[i:i+3]))
    pattern_count = Counter(patterns)
    return pattern_count

def calculate_entropy(counts):
    # Decoy calculation - looks important but unused
    from math import log2
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

def validate_sequence(seq):
    # Superfluous validation check that doesn't affect outcome
    if len(seq) < 5:
        return False
    cumulative = 0
    for val in seq:
        cumulative = (cumulative + val) % 17
    return cumulative == 3

def transform_signal(signal):
    # Applies transformation involving slicing and shifting
    shifted = signal[1:] + [signal[0]]  # Rotate left by 1
    doubled = [x * 2 for x in signal]
    combined = [a ^ b for a, b in zip(shifted, doubled)]  # Bitwise XOR mix
    return combined[:len(combined)//2]  # Return only first half

def analyze_pattern(counts, limit):
    # Critical function: computes diagnostic score based on frequent patterns
    total_weight = 0
    for pattern, freq in counts.items():
        if freq >= limit:
            # Weight by sum of elements in pattern
            weight = sum(pattern) * freq
            total_weight += weight
    adjustment = len(counts) % 9  # Minor deterministic tweak
    return total_weight - adjustment

# --- Main Execution with Distractors ---
data, meta = fetch_sensor_stream()

cleaned = apply_noise_filter(data)

# DEAD PATH: checksum calculated but never used
decoy_checksum = generate_checksum(cleaned)

# DEAD PATH: entropy computed on irrelevant basis
fake_entropy = calculate_entropy(Counter(cleaned))

# Transform data through signal processing
transformed_data = transform_signal(cleaned)

# Extract meaningful patterns from transformed data
pattern_bank = extract_patterns(transformed_data)

# Validate original data (result ignored)
validity_flag = validate_sequence(data)

# Slicing distraction: analyze only part of the pattern bank
subset_keys = list(pattern_bank.keys())[::2]  # Every other key
interim_test = [sum(k) for k in subset_keys if len(k) == 3]

temp_summary = defaultdict(int)
for key in subset_keys:
    temp_summary['total_tuples'] += 1
    temp_summary['max_sum'] = max(temp_summary['max_sum'], sum(key))

threshold = len(transformed_data) // 4  # Dynamic threshold

# Key Statement
final_diagnostic = analyze_pattern(pattern_bank, threshold)

# Print required output
print(f"Result: {final_diagnostic}")