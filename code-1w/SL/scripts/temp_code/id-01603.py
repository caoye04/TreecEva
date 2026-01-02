def analyze_efficiency(values):
    # Irrelevant computation: calculates sum of squares but not used in final result
    sum_squares = sum(x ** 2 for x in values if x > 0)
    normalized = [v / (max(values) + 1e-5) for v in values]
    return [n for n in normalized if n > 0.1]

# Decoy data structure
system_states = [
    {'id': 1, 'status': 'active', 'load': 45},
    {'id': 2, 'status': 'idle',   'load': 12},
    {'id': 3, 'status': 'active', 'load': 67}
]

# Unused transformation function (dead code path)
def transform_sequence(seq):
    shifted = seq[2:] + seq[:2]
    return [x ^ 7 for x in shifted if x % 2 == 0]

# Auxiliary function with red herring logic
def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 3)

# Key data structures
baseline = [3, 7, 9, 12, 15, 18, 21]
offsets = [2, -1, 0, 3, -2, 1, 4]

# Misleading intermediate calculation
aggregate_offset = sum(abs(x) for x in offsets) // len(offsets)

# Simulate sensor drift (not actually affecting final result)
sensor_drift = [baseline[i] + offsets[i] * 0.5 for i in range(len(baseline))]
drift_correction = compute_entropy([int(x) for x in sensor_drift])

# Real processing begins here
adjusted = [baseline[i] + offsets[i] for i in range(len(baseline))]
filtered = [x for x in adjusted if x % 3 == 0]  # Keep multiples of 3

# Bit manipulation layer
bit_encoded = 0
for val in filtered:
    bit_encoded ^= (val << 1) | 1

# Secondary filter using slicing
trimmed = filtered[1:-1]  # Remove first and last

# Benchmark criteria
thresholds = {"min_perf": 8, "crit_mult": 3}

def evaluate_performance(metrics, benchmark):
    # Logical nesting level 1
    if len(metrics) == 0:
        return 0
    
    # Nested conditional with distractor branch
    base_score = 0
    for m in metrics:
        if m > benchmark['min_perf']:
            # Nesting level 2
            temp_bonus = 0
            # Complex condition with short-circuit red herring
            if m % thresholds['crit_mult'] == 0 and (m < 100 or m > 1000):
                # This block is never reached due to m values
                temp_bonus += (m // 10) * 2
            else:
                # Actual scoring path
                temp_bonus += m // 4
            
            # Nesting level 3
            contribution = 0
            if temp_bonus > 0:
                # Multiple assignment distraction
                factor, offset = (2, -1) if m > 20 else (1, 1)
                contribution = temp_bonus * factor + offset
            base_score += contribution
    
    # Final adjustment with set operation distraction
    unique_remainders = set(m % 5 for m in metrics)
    penalty = len(unique_remainders) if len(unique_remainders) > 3 else 0
    
    # Real answer computation
    result = base_score - penalty
    
    # Dead code: this print is irrelevant
    # print(f'Debug: unique_remainders={unique_remainders}')
    
    return result

# Unused list comprehension decoy
duplicate_check = [x for x in baseline if baseline.count(x) > 1]

# Critical execution point
metrics = trimmed
benchmark_data = thresholds

# Distractor: another unused analysis
efficiency_profile = analyze_efficiency(baseline)

# Key statement
final_score = evaluate_performance(metrics, benchmark_data)

# Additional misleading transformation
shifted_bits = (bit_encoded >> 3) & 0xFFFF

# Output the required result
print(f'Result: {final_score}')