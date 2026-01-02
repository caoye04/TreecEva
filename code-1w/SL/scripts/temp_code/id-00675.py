def analyze_pattern(sequence):
    if not sequence:
        return 0
    transformed = [x ** 2 for x in sequence if x % 2 == 1]  # only odd numbers squared
    return sum(transformed) if len(transformed) > 3 else len(transformed)

# Irrelevant data processing (red herring)
def compute_entropy(data):
    import math
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    probabilities = [count / len(data) for count in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 4)

def filter_outliers(values, factor=1.5):
    """Dead code path – never called"""
    median_val = sorted(values)[len(values) // 2]
    mad = sum(abs(x - median_val) for x in values) / len(values)
    threshold = factor * mad
    return [v for v in values if abs(v - median_val) <= threshold]

def validate_checksum(record):
    # Complex but irrelevant validation
    checksum = 0
    for i, char in enumerate(record['id']):
        checksum += ord(char) * (i + 1)
    return checksum % 17 == record['version']

# Distractor variables
temp_cache = {f'key_{i}': i**3 for i in range(10)}
debug_flags = set(['verbose', 'tracing', 'optimized'])
system_config = {'mode': 'legacy', 'strict': False, 'timeout': 30}

# Real computation begins
raw_metrics = [3, 5, -2, 7, 4, 9, -6, 8]
scaling_factor = 1.25
offset_adjustment = -0.75

# Apply transformation with list comprehension and filtering
processed = [round((x * scaling_factor) + offset_adjustment) for x in raw_metrics]

# Bit manipulation decoy
bitmask = 0b101010
masked_values = [x & bitmask for x in range(5)]

# Conditional aggregation using boolean logic and comparisons
aggregate = 0
for val in processed:
    if val > 5 or (val < 0 and abs(val) % 2 == 0):
        aggregate += val
    elif val == 4:
        aggregate += 10  # special bonus case

# Simulated metric data with noise
dummy_payload = [{'type': 'ping', 'value': i*11} for i in range(5)]

# Core function that determines final result
def evaluate_performance(metrics, threshold):
    base = sum(metrics)
    adjustment = 0
    
    # String-based control flow (uses string method)
    mode_flag = 'adjust_high'
    if mode_flag.startswith('adjust'):
        if 'high' in mode_flag:
            adjustment = base * 0.1
    
    temp_result = base + adjustment
    
    # Logical short-circuit evaluation
    override = False and temp_result > 1000  # dead condition
    
    if override:
        return -999  # unreachable
    
    # Final transformation using set operations
    unique_remainders = set(temp_result % n for n in [2, 3, 5, 7] if n < temp_result)
    penalty = len(unique_remainders) if temp_result > threshold else 0
    
    return int(temp_result - penalty)

# Critical execution point
base_threshold = 35
metric_data = [x for x in processed if x != -2]  # remove placeholder

# Redundant unpacking (distraction)
a, b, *rest = metric_data[:4]

# Early termination simulation (not triggered)
if len(metric_data) < 0:  # always false
    final_score = 0
else:
    final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")