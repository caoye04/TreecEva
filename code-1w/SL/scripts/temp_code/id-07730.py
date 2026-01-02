def transform_input(raw_values):
    # Irrelevant transformation chain
    temp = [x ** 0.5 for x in raw_values if x > 10]
    offset = sum(temp) / len(temp) if temp else 0
    adjusted = [int(x - offset) for x in raw_values]
    return adjusted


def deprecated_metric(v):
    # Dead code path — never called
    return (v >> 2) & 0x3


def calculate_entropy(seq):
    # Misleading statistical distraction
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p) if p > 0 else 0
    return round(entropy, 4)

# Global decoy state
system_flags = {
    'debug_mode': True,
    'legacy_support': False,
    'cache_enabled': True,
    'retry_limit': 3
}

# Irrelevant data mappings
lookup_table = {i: (i * 17) % 23 for i in range(30)}
category_map = {k: ('high' if v > 15 else 'low') for k, v in lookup_table.items()}

base_threshold = 42

# Core input with red herring elements
raw_input_stream = [15, 24, 33, 12, 45, 8, 60, 3, 9, 27]

processed = transform_input(raw_input_stream)

# Simulated sensor weights — unused but plausible
sensor_weights = {f'sensor_{i}': (i + 1) * 0.75 for i in range(1, 6)}

# Distractor: early partial reduction
partial_sum = sum(x for x in processed if x % 2 == 0)

# Key data structure with mixed relevance
metric_data = {
    'readings': processed,
    'version': '2.1a',
    'checksum': sum(processed) * 2 + 5,
    'flags': dict(system_flags),
    'aux_data': [deprecated_metric(x) for x in processed[:4]]  # Computed but unused
}

# Secondary distraction: spurious recursive function
def count_bits(n):
    if n <= 0:
        return 0
    return (n & 1) + count_bits(n >> 1)

# Real logic buried in noise
bit_counts = [count_bits(x) for x in metric_data['readings']]

# Conditional manipulation with obfuscation
adjusted_readings = []
for val in metric_data['readings']:
    if val > base_threshold - 10:
        adjusted_readings.append(val * 1.1)
    elif val < 10:
        adjusted_readings.append(val * 1.5)
    else:
        adjusted_readings.append(val * 0.9)

# Another decoy operation
entropy_value = calculate_entropy([int(x) for x in adjusted_readings if x.is_integer()])

# Core evaluation logic — only this affects final_score
def evaluate_performance(data, threshold):
    readings = data['readings']
    total = 0
    weight = 1
    for r in readings:
        if r > threshold:
            total += r * weight
            weight += 1  # Compounding effect
        else:
            total -= r // 3
    # Introduce dictionary-based adjustment
    adjustment_map = {3: -2, 6: 4, 9: -5}
    adj_key = len(readings) % 10
    total += adjustment_map.get(adj_key, 0)
    return int(total * 0.95)  # Final scaling

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")