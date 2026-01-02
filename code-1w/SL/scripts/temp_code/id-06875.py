from collections import defaultdict
import itertools

# Simulate sensor data aggregation and performance scoring with red herrings

def collect_diagnostics(raw_logs):
    # Irrelevant diagnostic parsing (dead-end function)
    errors = defaultdict(int)
    for log in raw_logs:
        if 'ERROR' in log:
            errors[log.split()[1]] += 1
    return dict(errors)

def transform_data(stream):
    # Unused transformation pipeline
    shifted = [(x << 2) ^ 3 for x in stream if x % 2 == 1]
    return [y >> 1 for y in shifted]

def analyze_trend(values):
    # Decoy trend analysis with no impact
    avg = sum(values) / len(values)
    deviation = [abs(v - avg) for v in values]
    return sum(deviation) / len(deviation)

def calculate_entropy(data):
    # Misleading complexity: computes entropy but unused
    from math import log2
    freq = defaultdict(int)
    for d in data:
        freq[d] += 1
    total = len(data)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 4)

def filter_outliers(seq, threshold=2):
    # Dead code path: never called
    mean_val = sum(seq) / len(seq)
    return [x for x in seq if abs(x - mean_val) <= threshold]

# Core logic disguised among distractions
base_metrics = [85, 92, 78, 96, 88]
weights = [0.1, 0.2, 0.3, 0.15, 0.25]

# Irrelevant bit manipulation chain
obfuscated_shift = ((92 ^ 78) << 3) & 0xFF
scrambled = [m ^ obfuscated_shift for m in base_metrics]
descrambled = [s ^ obfuscated_shift for s in scrambled]  # Restores original

# Fake recursive smoothing (never used)
def smooth_recursive(data, depth=3):
    if depth == 0 or len(data) < 2:
        return data
    smoothed = [data[0]] + [(a + b) / 2 for a, b in zip(data, data[1:])] + [data[-1]]
    return smooth_recursive(smoothed[1:-1], depth - 1)

# Real evaluation logic buried in noise
threshold_map = {k: v * 1.1 for k, v in enumerate(weights)}
adjustment_factor = sum([descrambled[i] * weights[i] for i in range(len(weights))])

# Dummy case conversion operation (red herring)
status_flags = ['OK', 'WARNING', 'CRITICAL']
case_variants = list(map(str.lower, status_flags))

# Key lambda: masks actual weighting logic among distractors
weight_applier = lambda m, w: m * w
weighted_sum = sum(weight_applier(descrambled[i], weights[i]) for i in range(len(weights)))

# Simulated multi-stage validation (only last stage matters)
validation_chain = []
for idx, val in enumerate(descrambled):
    temp_check = val >= (80 + idx * 2)
    validation_chain.append(temp_check)

# Final score computed from correct path
final_score = 0
if all(validation_chain):  # Depends on descrambled values
    final_score = round(adjustment_factor * 1.05, 6)
else:
    final_score = round(weighted_sum * 0.95, 6)

# Irrelevant itertools usage to increase interference
combinations = list(itertools.combinations_with_replacement([0.1, 0.25, 0.5], 2))
shuffle_sim = [sum(combo) for combo in combinations if combo[0] != combo[1]]

# Critical print statement
print(f"Result: {final_score}")