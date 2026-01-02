import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(data_stream):
    filtered = [x for x in data_stream if x > 0]
    normalized = [round(math.log(val), 3) for val in filtered]
    return normalized

# Legacy function - unused but looks relevant
def deprecated_normalize(arr):
    mean_val = sum(arr) / len(arr)
    return [a - mean_val for a in arr]

# Core transformation pipeline
def transform_sequence(raw_seq):
    shifted = [(x << 1) ^ 3 for x in raw_seq]
    modded = [y % 17 for y in shifted]
    sorted_modded = sorted(modded, reverse=True)
    return sorted_modded

# Red herring: Complex-looking but unused matrix operation
def compute_centrality(matrix):
    size = len(matrix)
    central_value = 0
    for i in range(size):
        for j in range(size):
            central_value += matrix[i][j] * (i + j)
    return central_value ** 0.5

# Unused recursive decoy
def fibonacci_threshold(n, limit=10):
    if n <= 1:
        return n
    elif n > limit:
        return -1
    return fibonacci_threshold(n-1, limit) + fibonacci_threshold(n-2, limit)

# Main evaluation logic
def evaluate_metric(a, b, c):
    temp = (a ^ b) & 0xF
    if temp > c:
        return temp * 2 + c
    else:
        return temp + c * 3

# Higher-order orchestrator with distractors
metric_set = {5, 8, 12, 15, 3, 6}
dummy_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
overlap = metric_set & dummy_set  # Distraction: unused beyond here

# Simulated preprocessing chain
raw_input = [4, 7, 2, 9]
processed = analyze_readings([math.exp(x) for x in raw_input])
transformed = transform_sequence([int(p*10) for p in processed])

# Irrelevant string manipulation - looks like config parsing
def parse_config_line(line):
    parts = line.strip().split('=')
    key = parts[0].lower().replace('_', '')
    value = parts[1].strip() if len(parts) > 1 else ''
    return key, value.upper()

config_lines = ['THRESHOLD=high', 'MODE=auto', 'DEBUG=false']
config_pairs = [parse_config_line(ln) for ln in config_lines]

# Actual metric computation begins here
base_metrics = []
for i, v in enumerate(transformed[:4]):
    computed = evaluate_metric(v, transformed[(i+2)%4], i + 5)
    base_metrics.append(computed)

# Aggregation with red herring intermediate steps
aggregate = 0
scaling_factor = 1.0
for idx, val in enumerate(base_metrics):
    if idx % 2 == 0:
        scaled_val = val * (idx + 1)
        aggregate += int(scaled_val)
    else:
        # This path is taken but contributes to confusion
        adjustment = math.sin(math.pi * idx / 4)
        aggregate -= int(adjustment * val)  # adjustment is 0 or 1

# Decoy list comprehension with side effects (none actually)
device_ids = ['SNSR-A', 'SNSR-B', 'SNSR-C']
classification_tags = [
    tag.split('-')[1].lower() for tag in device_ids 
    if 'B' not in tag
]

# Final scoring logic - depends only on 'aggregate'
penalty_set = {x for x in transformed if x in metric_set}  # Looks important
penalty_score = len(penalty_set) * 7

# Key statement
final_score = evaluate_performance(metric_set)

# Orchestration function that uses the real logic
def evaluate_performance(metrics):
    initial = aggregate  # Depends on prior transformed state
    modifier = len(metrics) * 3
    if modifier > 10:
        result = initial + modifier
    else:
        result = initial * 2
    # Critical override based on bit condition
    bit_check = (result >> 3) & 1
    if bit_check:
        result = result - 15
    else:
        result = result + 23
    return result

print(f"Target result: {final_score}")