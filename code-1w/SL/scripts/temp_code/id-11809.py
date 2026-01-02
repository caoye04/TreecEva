def analyze_signal(x, y):
    if x < 0:
        return (y ** 2) % 17
    else:
        return (x + y) // 3

# Irrelevant signal processing chain
def deprecated_filter(data):
    temp = [d * 1.05 for d in data if d > 0]
    return [t for t in temp if t < 100]

def generate_synthetic_data(n):
    result = []
    a, b = 1, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result[:n]

# Unused diagnostic functions
def legacy_calculate_stress(val):
    return (val * 0.88 + 12) // 1

def dummy_normalization(arr):
    max_val = max(arr)
    return [round(x / max_val, 4) for x in arr]

# Core logic with distractors
def compute_baseline_offset(sequence, factor=3):
    offset = 0
    for i, v in enumerate(sequence):
        if i % 2 == 0 and v % 2 == 1:
            offset += factor * (v % 7)
        elif v > 10:
            offset -= factor // 2
    return abs(offset) % 13

threshold_map = {
    'critical': 90,
    'elevated': 70,
    'normal': 50,
    'optimal': 30
}

health_sequence = [12, 7, 15, 4, 9, 11, 6, 14, 8, 10]

# Red herring: complex but unused transformation
cipher_shift = sum([x ^ (i + 5) for i, x in enumerate(health_sequence)]) % 25
scrambled = ''.join([chr((x + cipher_shift) % 26 + ord('a')) for x in health_sequence])

# Decoy calculation tree
auxiliary_score = 0
for val in health_sequence:
    if val in [7, 11, 13]:
        auxiliary_score += analyze_signal(val, 5)
    elif val % 3 == 0:
        auxiliary_score -= val // 3

# Fake normalization pass (dead code path)
if len(health_sequence) > 5:
    normalized = [x / 15.0 for x in health_sequence]
    adjusted = [n * 1.2 for n in normalized]

# Actual relevant logic buried in noise
reference_anchor = compute_baseline_offset(health_sequence, factor=4)

event_flags = []
for idx, reading in enumerate(health_sequence):
    flag = (reading > threshold_map['normal']) << 1
    flag |= (idx % 3 == 0)
    event_flags.append(flag)

aggregated = 0
for i in range(len(event_flags)):
    if event_flags[i] & 1:
        aggregated += health_sequence[i] * 2
    if event_flags[i] & 2:
        aggregated -= reference_anchor

# Conditional expression used as required
interim_result = aggregated if aggregated > 0 else -aggregated

# Critical computation obscured by context
scaling_factor = len([x for x in health_sequence if x > threshold_map['elevated']])
scaled_interim = interim_result * (scaling_factor if scaling_factor > 0 else 1)

# Final processing with conditional expression
final_diagnostic = 0
def process_metrics(seq, tmap):
    base = scaled_interim
    adjustment = 0
    
    # Nested logic with multiple concepts
    for i, val in enumerate(seq):
        if val > tmap['elevated']:
            adjustment += (i + 1) * (val % 5)
        elif val < tmap['optimal']:
            adjustment -= (i // 2)
    
    # Bit manipulation mixed with arithmetic
    packed = (base & 255) ^ (adjustment << 2)
    packed = (packed + len(seq)) % 10000
    
    # Final conditional override pattern
    return packed if base >= 0 else (~packed + 1)

final_diagnostic = process_metrics(health_sequence, threshold_map)

# Output requirement
print(f"Target result: {final_diagnostic}")