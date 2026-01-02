from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def legacy_normalize(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return [(x - mean) / math.sqrt(variance) for x in values]

# Decoy transformation (not used in final logic)
def transform_legacy(data):
    result = []
    for item in data:
        if item % 3 == 0:
            result.append(item * 2)
        elif item % 5 == 0:
            result.append(item + 10)
        else:
            result.append(item)
    return result

# Misleading statistical summary (distractor)
def compute_summary_stats(data_list):
    stats = defaultdict(float)
    total = sum(data_list)
    stats['mean'] = total / len(data_list)
    stats['max'] = max(data_list)
    stats['min'] = min(data_list)
    stats['range'] = stats['max'] - stats['min']
    freq = Counter(data_list)
    stats['mode'] = freq.most_common(1)[0][1]
    return stats

# Real processing begins here — but buried under noise
preliminary_filter = lambda x: x > 0

# Simulated sensor readings with noise
raw_readings = [12, -5, 8, 15, 3, 22, -1, 9, 14, 6, 11, 18, 4, 7, 13]
filtered_data = list(filter(preliminary_filter, raw_readings))

# Weight configuration (some irrelevant entries)
weights_config = {
    'w1': 0.1,
    'w2': 0.25,
    'w3': 0.5,
    'w4': 0.05,  # unused weight
    'offset': 1.5 # red herring
}

# Auxiliary structure with cross-references (partial usage)
data_map = defaultdict(list)
for idx, val in enumerate(filtered_data):
    key = 'even_group' if val % 2 == 0 else 'odd_group'
    data_map[key].append(val)

# Bit manipulation decoy (never actually influences output)
current_flag = 0b101010
for val in filtered_data:
    current_flag ^= (val & 0b1111) << 1
    current_flag |= (val % 8)

# Actual core logic hidden in complexity
def apply_weighted_transform(values, w):
    # Only uses w1, w2, w3 — w4 and offset ignored
    weighted_sum = 0.0
    for i, v in enumerate(values):
        if i % 3 == 0:
            weighted_sum += v * w['w1']
        elif i % 3 == 1:
            weighted_sum += v * w['w2']
        else:
            weighted_sum += v * w['w3']
    return weighted_sum

# Higher-order function wrapper (real but obscured)
def calculate_final_score(dataset, config):
    # Secondary filtering based on prime-like pattern (simulated)
    primes_approx = [2, 3, 5, 7, 11, 13, 17, 19]
    enhanced = [x for x in dataset if any(x % p == 0 for p in primes_approx)]
    
    # Sorting as part of transformation (relevant)
    sorted_enhanced = sorted(enhanced, reverse=True)
    
    # String operation distraction
    labels = ['A', 'B', 'C', 'D', 'E']
    label_seq = ''.join(labels[i % len(labels)] for i in range(len(sorted_enhanced)))
    label_hash = sum(ord(c) for c in label_seq) % 10
    
    # Real calculation
    base_value = apply_weighted_transform(sorted_enhanced, config)
    adjustment = len(sorted_enhanced) * 0.5
    
    # Final score computed here — this is the answer point
    final = base_value - adjustment + label_hash
    
    # Irrelevant set operations (distractor)
    unique_vals = set(sorted_enhanced)
    neighbors = set([v+1 for v in unique_vals])
    overlaps = unique_vals & neighbors  # never used
    
    return final

# Execute main logic
data_set = filtered_data.copy()
final_score = calculate_final_score(data_set, weights_config)

# Print result in required format
print(f"Target result: {final_score}")