import math

# Irrelevant data initialization (distractor)
data_log = [i ** 2 for i in range(15)]
metadata_cache = {'version': '2.1.3', 'debug': True}
temp_offset = sum([(-1) ** i * i for i in range(10)])

# Core problem setup
def generate_sequence(n):
    """Generate a sequence based on combinatorics and modular arithmetic."""
    seq = []
    for i in range(1, n + 1):
        value = (math.comb(2 * i, i) + i ** 3) % 1000
        if i % 4 == 0:
            value = value ^ 255  # Bitwise obfuscation
        seq.append(value)
    return seq

raw_input = 7
sequence_data = generate_sequence(raw_input)

# Transformation with lambda and filtering
transformation_factor = 0.85
transform_fn = lambda x: int(x * transformation_factor) + (x & 7)
transformed_data = [transform_fn(x) for x in sequence_data]

# Red herring: unused transformation branch
def legacy_transform(data):
    return [d // 2 + 10 for d in data if d > 50]

# Decoy function that looks important but isn't used
def compute_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum += val * (i + 1)
    return checksum % 97

# Threshold logic with comparison and closure
def make_threshold(base):
    def threshold(t):
        return t > (base * 1.618)  # Golden ratio distraction
    return threshold

threshold_func = make_threshold(42)

# Sorting (relevant step disguised among distractors)
sorted_data = sorted(transformed_data, reverse=True)

# Dead code path: looks like it modifies data but doesn't affect flow
if len(sorted_data) > 10:
    normalized = [x / max(sorted_data) for x in sorted_data]
else:
    dummy_var = [x + 100 for x in sorted_data]  # Unused

# Key computation with nested logic
intermediate_scores = []
for idx, val in enumerate(sorted_data):
    score = 0
    if val % 2 == 0:
        score += idx * 3
    if val > 50:
        score += 17
    if bin(val).count('1') > 3:  # Bit density check
        score -= 5
    intermediate_scores.append(score)

# Another red herring: complex-looking but unused calculation
shadow_accumulator = 0
for x in intermediate_scores:
    shadow_accumulator += x ** 2
shadow_accumulator = int(math.sqrt(shadow_accumulator))

# Actual analysis function that computes the answer
def analyze_pattern(data_list, thresholder):
    count_above = 0
    total_contribution = 0.0
    for item in data_list:
        if thresholder(item):
            count_above += 1
            total_contribution += item / 10.0
    
    # Composite metric combining count and scaled sum
    if count_above == 0:
        return 0
    raw_metric = total_contribution * count_above
    
    # Final adjustment using bit manipulation
    adjusted = int(raw_metric) ^ 0b1101  # XOR with fixed pattern
    return adjusted

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

# Print result as required
print(f"Result: {final_diagnostic}")