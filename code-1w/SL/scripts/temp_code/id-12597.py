from collections import defaultdict, Counter
import math

def generate_signature(sequence):
    sig = 0
    for i, val in enumerate(sequence):
        sig += (val * (i + 1)) % 97
    return sig

def shift_window(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    # Irrelevant accumulation
    total_sum = sum(sum(w) for w in windows)
    return windows

def filter_candidates(items, limit):
    # Dead code path - never used
    result = []
    for item in items:
        if item > limit:
            result.append(item * 2)
    return result

def compute_entropy(arr):
    counts = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def merge_dicts(d1, d2):
    # Distractor function: looks important but unused
    merged = defaultdict(int)
    for k in d1: merged[k] += d1[k]
    for k in d2: merged[k] += d2[k]
    return merged

def transform_sequence(seq):
    # Apply modular arithmetic and bit manipulation
    transformed = []
    for x in seq:
        temp = (x ** 2 + 3) % 101
        temp = temp ^ 42  # Bitwise XOR red herring
        if temp % 2 == 0:
            temp = temp // 2
        else:
            temp = (temp * 3) + 1
        transformed.append(temp)
    return transformed

def build_threshold_map(keys):
    # Creates misleading thresholds
    t_map = {}
    for k in keys:
        t_map[k] = (k * 7 + 13) % 50 + 10
    # Add decoy entries
    t_map['debug_override'] = -999
    t_map['legacy_mode'] = 0
    return t_map

def analyze_pattern(windows, thresholds):
    score = 0
    freqs = Counter()
    
    # Extract middle elements from each window
    middles = [w[1] for w in windows]
    
    # Real logic begins: find recurring mid-values
    for m in middles:
        freqs[m] += 1
    
    # Only values appearing at least twice matter
    valid_middles = {k for k, v in freqs.items() if v >= 2}
    
    # Compute diagnostic using only these
    base_value = 0
    for val in valid_middles:
        base_value += val * freqs[val]
    
    # Secondary transformation via modular arithmetic
    base_value = (base_value * 17) % 99991
    
    # Tertiary adjustment using entropy of original pattern positions
    positions = []
    for i, w in enumerate(windows):
        if w[1] in valid_middles:
            positions.append(i)
    
    if positions:
        pos_entropy = compute_entropy(positions)
        base_value += int(pos_entropy * 1000)
    
    # Final trap: ignore threshold_map completely (decoy parameter)
    return base_value

# Main execution with distractions
raw_input = [5, 8, 12, 8, 21, 8, 12, 33, 12, 8]

# Irrelevant preprocessing
checksum = sum(x * x for x in raw_input) % 10007
signature = generate_signature(raw_input)

# Actual relevant transformation
transformed_data = transform_sequence(raw_input)

# Generate sliding windows — this is key
windowed = shift_window(transformed_data, 3)

# Build map that looks important but isn't used in analysis
keys_for_map = [1, 2, 3, 5, 8]
threshold_map = build_threshold_map(keys_for_map)

# Decoy data structure
log_entries = [
    {'id': 'A', 'status': 'failed', 'code': 404},
    {'id': 'B', 'status': 'active', 'code': 200}
]

# Critical statement
final_diagnostic = analyze_pattern(windowed, threshold_map)

print(f"Result: {final_diagnostic}")