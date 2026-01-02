from collections import defaultdict
import math

# Simulated sensor data ingestion (irrelevant in part)
sensor_log = [
    [1.2, 3.4, 2.1, 5.5],
    [2.3, 1.8, 6.7, 4.4],
    [3.5, 2.2, 1.9, 7.1],
    [4.1, 5.6, 3.3, 2.8]
]

# Irrelevant auxiliary mapping for red herring access
type_codes = {'A': 101, 'B': 207, 'C': 313, 'D': 421}

# Data normalization function (partially relevant)
def normalize_row(row):
    mean_val = sum(row) / len(row)
    return [x / mean_val for x in row]

# Distraction: unused recursive function for prime decomposition
def decompose_primes(n, divisor=2, factors=None):
    if factors is None:
        factors = []
    if n < 2:
        return factors
    if n == divisor:
        factors.append(n)
        return factors
    if n % divisor == 0:
        factors.append(divisor)
        return decompose_primes(n // divisor, divisor, factors)
    return decompose_primes(n, divisor + 1, factors)

# Unused higher-order function as red herring
apply_filter = lambda f, data: [x for x in data if f(x)]

# Core transformation: apply normalization and power scaling
def transform_dataset(raw_data):
    processed = []
    for idx, row in enumerate(raw_data):
        norm_row = normalize_row(row)
        # Apply squaring only to even-indexed rows (key logic)
        if idx % 2 == 0:
            transformed = [x ** 2 for x in norm_row]
        else:
            transformed = [x ** 0.5 for x in norm_row]  # square root
        processed.append(transformed)
    return processed

# Threshold map generation with distraction via complex setup
base_thresholds = [0.8, 1.1, 0.9, 1.05]

# Distractor computation: irrelevant combinatorics
def count_subsequences(arr, limit):
    count = 0
    n = len(arr)
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if i & (1 << j)]
        if subset and sum(subset) <= limit:
            count += 1
    return count

# Real but obfuscated threshold calculation
threshold_map = {}
for i, t in enumerate(base_thresholds):
    # Some values are inverted based on dummy condition
    if i in [1, 3]:
        threshold_map[f'dim_{i}'] = round(t * 1.2, 3)
    else:
        threshold_map[f'dim_{i}'] = round(t * 0.85, 3)

# Diagnostic analysis function with early exits and branching logic
def analyze_pattern(data_batch, limits):
    score_accum = defaultdict(float)
    anomaly_flags = 0

    for i, record in enumerate(data_batch):
        for j, val in enumerate(record):
            dim_key = f'dim_{j}'
            if dim_key not in limits:
                continue

            threshold = limits[dim_key]
            deviation = abs(val - 1.0)  # normalized around 1.0

            if deviation > threshold:
                score_accum[dim_key] += deviation * 100
                anomaly_flags += 1

            # Red herring: unused intermediate flag
            if val > 1.5 and i % 3 == 0:
                _ = math.log(val)  # computed but not stored meaningfully

    # Secondary processing: aggregate diagnostic
    total_score = sum(score_accum.values())
    penalty_factor = 1.0

    # Complex conditional penalty (only some paths matter)
    if anomaly_flags > 5:
        penalty_factor = 1.8
    elif anomaly_flags > 2:
        penalty_factor = 1.4
    else:
        penalty_factor = 1.1

    # Dead code branch: unreachable due to above structure
    if False:
        fallback = 0
        for v in score_accum.values():
            fallback += v ** 0.5
        total_score = fallback

    final_score = total_score * penalty_factor

    # Additional distraction: unused bit manipulation on index
    mask = 0b1010
    masked_index_sum = 0
    for k in range(len(data_batch)):
        masked_index_sum += k ^ mask & 0b111

    return int(round(final_score))

# Main execution flow
transformed_data = transform_dataset(sensor_log)

# Dummy combinatorics call — irrelevant to final result
_ = count_subsequences([1, 2, 3], 5)

# Critical statement: compute final diagnostic value
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

print(f"Result: {final_diagnostic}")