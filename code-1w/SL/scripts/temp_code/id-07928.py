from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [14, 18, 22, 19, 25, 30, 28, 24, 20, 17, 23, 27, 31, 26, 21, 16, 15, 29, 33, 35]

# Irrelevant preprocessing: frequency analysis of deltas (red herring)
delta_freq = defaultdict(int)
for i in range(1, len(telemetry_stream)):
    delta = telemetry_stream[i] - telemetry_stream[i-1]
    delta_freq[delta] += 1

# Decoy function: appears useful but unused in critical path
def analyze_trend(data):
    positive = sum(1 for x in data if x > 0)
    negative = sum(1 for x in data if x < 0)
    return 'upward' if positive > negative else 'downward'

# Another decoy: computes statistical moments but not used
mean_val = sum(telemetry_stream) / len(telemetry_stream)
variance = sum((x - mean_val)**2 for x in telemetry_stream) / len(telemetry_stream)
std_dev = math.sqrt(variance)

# Simulated metric weights (misleading normalization)
weight_map = {i: round(math.cos(i * 0.1), 3) for i in range(len(telemetry_stream))}
total_weight = sum(weight_map.values())
normalized_weights = {k: v/total_weight for k, v in weight_map.items()}

# Real processing begins: extract key performance windows
baseline_cache = []
for i, val in enumerate(telemetry_stream):
    if val >= 25 and i % 2 == 0:
        baseline_cache.append(val * 1.1)
    elif val < 20 and i % 3 == 0:
        baseline_cache.append(val * 0.9)

# Distractor: complex filtering that produces unused list
filtered_extremes = [x for x in telemetry_stream if x < 18 or x > 30]
threshold_groups = defaultdict(list)
for x in filtered_extremes:
    if x < 18:
        threshold_groups['critical_low'].append(x)
    else:
        threshold_groups['critical_high'].append(x)

# Core logic hidden among noise: compute moving geometric mean over 3-day windows
geometric_means = []
for i in range(2, len(telemetry_stream)):
    product = telemetry_stream[i-2] * telemetry_stream[i-1] * telemetry_stream[i]
    geo_mean = product ** (1/3)
    geometric_means.append(round(geo_mean, 3))

# Secondary distractor: bit manipulation on indices (dead end)
bit_encoded = 0
for i in range(len(telemetry_stream)):
    if i % 5 == 0:
        bit_encoded ^= (i << 2)
    elif i % 7 == 0:
        bit_encoded |= (1 << (i % 8))

# Actual metric data construction (non-obvious dependency)
metric_data = []
for i, gm in enumerate(geometric_means):
    if i % 4 == 0:
        metric_data.append(gm * 1.25)
    elif i % 4 == 2:
        metric_data.append(gm * 0.85)
    else:
        metric_data.append(gm)

# Critical function buried in distractions
def evaluate_performance(metrics, cache):
    # Hidden accumulation pattern
    accumulator = 0
    penalty = 0
    
    # Complex conditional summation with decoy variables
    temp_result = []
    overflow_flag = False
    
    for idx, val in enumerate(metrics):
        if idx == 0:
            accumulator += val
            continue
        
        prev = metrics[idx-1]
        diff = abs(val - prev)
        
        # Real logic: adaptive accumulation
        if diff > 5 and idx in [3, 7, 12]:
            accumulator += val * 0.7
        elif val > 25:
            accumulator += val * 1.1
        else:
            accumulator += val * 0.9
        
        # Decoy tracking
        if accumulator > 100 and not overflow_flag:
            overflow_flag = True
            temp_result.append(accumulator)
    
    # Final adjustment using cache (key dependency)
    cache_contribution = sum(cache) / len(cache) if cache else 0
    final_component = accumulator * 0.8 + cache_contribution * 1.2
    
    # Additional misdirection: unused transformation
    transformed = []
    for c in cache:
        bits = bin(int(c))[2:]
        flipped = ''.join('1' if b == '0' else '0' for b in bits)
        if flipped:
            transformed.append(int(flipped, 2))
    
    return int(round(final_component))

# Key execution point
final_score = evaluate_performance(metric_data, baseline_cache)

# Print result as required
print(f"Target result: {final_score}")