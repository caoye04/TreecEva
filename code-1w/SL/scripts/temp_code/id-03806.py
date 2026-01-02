from collections import defaultdict, Counter
import math

# Simulated telemetry data from a distributed sensor array (distractor context)
data_stream = [12, 45, 23, 67, 34, 89, 34, 56, 23, 45, 45, 12, 89]

# Irrelevant preprocessing: frequency analysis of values (red herring)
frequency_map = Counter(data_stream)
mode_value = frequency_map.most_common(1)[0][0]

# Misleading transformation: reverse and offset (dead path)
reversed_offset = [100 - x for x in reversed(data_stream)]
threshold_filtered = [x for x in data_stream if x > 30]

# Decoy function: appears relevant but unused in critical path
def analyze_pattern(seq):
    return sum(x * x for x in seq if x % 2 == 0)

# Auxiliary calculation with plausible but irrelevant logic
total_energy = sum(math.log(x + 1) for x in data_stream)
normalized_avg = total_energy / len(data_stream)

# Real processing begins: group by magnitude bands (relevant)
def group_by_band(values):
    bands = defaultdict(list)
    for v in values:
        if v < 25:
            bands['low'].append(v)
        elif v < 50:
            bands['medium'].append(v)
        else:
            bands['high'].append(v)
    return bands

# Secondary decoy: complex but unused spectral transform
def spectral_decompose(seq):
    result = []
    for i in range(len(seq)):
        component = 0
        for j in range(len(seq)):
            component += seq[j] * math.cos(math.pi * i * j / len(seq))
        result.append(round(component, 2))
    return result

# Core logic chain with nested dependencies
def compute_weighted_median(bands):
    target_list = sorted(bands.get('medium', []) + bands.get('high', []))
    if not target_list:
        return 0
    n = len(target_list)
    if n % 2 == 1:
        return target_list[n // 2]
    else:
        return (target_list[n // 2 - 1] + target_list[n // 2]) / 2

# Multi-stage processing with distraction
intermediate_score = len(threshold_filtered) * normalized_avg

# Another red herring: recursive summation (unrelated to final result)
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] ** 0.5 + recursive_sum(arr, idx + 1)

unused_recursive_result = recursive_sum(frequency_map.values())

# Actual critical function with embedded logic steps
def process_sequence(seq):
    # Step 1: group into bands
    grouped = group_by_band(seq)
    
    # Step 2: calculate band statistics (some used, some not)
    low_count = len(grouped['low'])
    med_vals = grouped['medium']
    high_vals = grouped['high']
    
    # Step 3: derive adjustment factor from low-frequency behavior
    adjustment = 1.0
    if low_count > 0:
        adjustment = (sum(grouped['low']) / low_count) / 20.0
    
    # Step 4: compute weighted median (core computation)
    raw_median = compute_weighted_median(grouped)
    
    # Step 5: apply adjustment only if high-band has duplicates
    high_has_dups = any(count > 1 for count in Counter(high_vals).values())
    
    # Step 6: conditional amplification
    if high_has_dups and raw_median > 40:
        adjusted_result = raw_median * (1 + adjustment)
    else:
        adjusted_result = raw_median - adjustment * 5
    
    # Step 7: clamp to operational bounds (final constraint)
    clamped = max(10, min(adjusted_result, 95))
    
    # Step 8: secondary correction based on sequence length parity
    if len(seq) % 2 == 0:
        clamped += 2.5
    else:
        clamped -= 1.75
    
    # Step 9: finalize with integer flooring (critical step)
    final_value = math.floor(clamped * 100) / 100  # Two decimal precision
    
    return final_value

# Execution point of interest
final_output = process_sequence(data_stream)

# Output the target result
print(f"Target result: {final_output}")