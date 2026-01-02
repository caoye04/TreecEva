def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Misleading intermediate calculation (red herring)
raw_metrics = [1.8, 2.3, 1.9, 3.1, 2.7, 4.5, 3.6]
scaled_values = [x * 1.75 for x in raw_metrics if x > 2.0]
avg_scaled = sum(scaled_values) / len(scaled_values) if scaled_values else 0

# Core logic disguised among distractions
def generate_base_weights(n):
    weights = []
    for i in range(1, n+1):
        if i % 3 == 0:
            weights.append(i * 0.7)
        elif i % 5 == 0:
            weights.append(i * 0.4)
        else:
            weights.append(i * 0.9)
    return weights

def filter_outliers(data, factor=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Unused but plausible-looking function (dead code path)
def adjust_for_bias(arr, bias_factor=0.1):
    return [x * (1 - bias_factor) if x > 0 else x * (1 + bias_factor) for x in arr]

# Critical function chain
base_inputs = [4, 7, 13, 18, 22, 25, 28, 33]
effective_weights = [w ** 0.5 for w in generate_base_weights(len(base_inputs))]

# Distractor: complex list comprehension with no impact
diagnostic_flags = [
    (i, val, 'high') if val > 10 else (i, val, 'low')
    for i, val in enumerate([x*2 for x in base_inputs if x % 4 == 0])
]

# Bit manipulation decoy (irrelevant to final result)
bit_analysis = 0
for x in base_inputs:
    bit_analysis ^= (x << 2) | (x >> 1)
bit_analysis = bit_analysis & 0xFFFF

# Conditional expression red herring
status_code = 200 if len(diagnostic_flags) > 3 else 404
log_entry = f"Status: {status_code} - {'Valid' if status_code == 200 else 'Invalid'}"

# Key validation logic buried in abstraction
def validate_threshold(weights_list):
    filtered = filter_outliers(weights_list, factor=2.0)
    if not analyze_pattern(filtered):
        return sum(filtered) * 0.85
    else:
        mid = len(filtered) // 2
        return (filtered[mid-1] + filtered[mid]) / 2 if len(filtered) % 2 == 0 else filtered[mid]

# Secondary irrelevant computation
redundant_calc = max(scaled_values) - min(scaled_values) if scaled_values else 0

# Noise: unused dictionary construction
profile_summary = {
    'count': len(base_inputs),
    'max_raw': max(base_inputs),
    'min_raw': min(base_inputs),
    'version': '2.1-alpha',
    'active': True
}

# The actual critical execution point
threshold_score = validate_threshold(effective_weights)

# Final output
print(f"Result: {threshold_score}")