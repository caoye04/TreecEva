def analyze_signal(samples, baseline):
    adjusted = [s - baseline for s in samples]
    magnitude = sum(abs(x) for x in adjusted)
    noise_floor = 0.25 * len(samples)  # irrelevant metric
    return magnitude if magnitude > noise_floor else 0

samples_a = [0.3, -0.7, 1.2, 0.9, -0.4]
samples_b = [0.6, -0.1, 0.8, -0.5, 1.1]

# Irrelevant pre-processing block
temp_sum = 0
for x in samples_a + samples_b:
    temp_sum += x ** 2
    if temp_sum > 10:
        break

baseline_a = 0.1
baseline_b = 0.2

metric_a = analyze_signal(samples_a, baseline_a)
metric_b = analyze_signal(samples_b, baseline_b)

# Bitwise obfuscation layer (partially relevant)
def encode_metric(m, key):
    raw_val = int(m * 10)
    return (raw_val ^ key) & 0xFF

encoded_a = encode_metric(metric_a, 0x5A)
encoded_b = encode_metric(metric_b, 0xA5)

# Dummy transformation chain
def transform_code(x):
    if x < 50:
        return (x << 2) | 1
    elif x < 100:
        return (x >> 1) ^ 3
    else:
        return (x + 17) % 100

transformed_a = transform_code(encoded_a)
transformed_b = transform_code(encoded_b)

# Decoy function that looks important but isn't used
def calculate_entropy(data):
    from math import log2
    total = sum(data)
    if total == 0:
        return 0
    probs = [d / total for d in data if d > 0]
    return -sum(p * log2(p) for p in probs)

# Real aggregation begins here
aggregate_data = [
    {'id': 'A', 'val': metric_a, 'flag': transformed_a},
    {'id': 'B', 'val': metric_b, 'flag': transformed_b}
]

# Complex conditional mapping with red herring thresholds
threshold_map = {
    'A': 2.0 if len(samples_a) >= 5 else 1.5,
    'B': 1.8,
    'C': 3.0  # unused key - red herring
}

# Core processing logic with conditional expression
primary_weight = 1.5 if metric_a > metric_b else 0.8
secondary_weight = 0.7 if encoded_a & 0x0F > 8 else 1.1  # uses bits

# Distractor: complex-looking but unused calculation
phantom_score = (
    (transformed_a ^ transformed_b) * 100 // 
    (len(samples_a) + len(samples_b))
) % 97

# Actual computation path
weighted_total = 0
for entry in aggregate_data:
    key = entry['id']
    base_val = entry['val']
    weight = primary_weight if key == 'A' else secondary_weight
    weighted_total += base_val * weight

# Simulated normalization (irrelevant constants)
normalization_factor = 1.0 / (len(aggregate_data) or 1)
adjusted_total = weighted_total * normalization_factor

# Final diagnostic using conditional expression and bit flag analysis
def process_metrics(data_list, thresholds):
    total = 0
    for item in data_list:
        id_key = item['id']
        val = item['val']
        flag = item['flag']
        thresh = thresholds.get(id_key, 0)
        
        # Conditional expression determines inclusion
        contribution = val * 1.2 if val >= thresh else val * 0.3
        
        # Bitwise filter: only count if flag has even parity
        flag_parity = bin(flag).count('1') % 2
        if flag_parity == 0:
            total += contribution
        else:
            total -= contribution * 0.1  # minor penalty
    
    # Final adjustment based on aggregate properties
    high_flag_count = sum(1 for d in data_list if d['flag'] > 100)
    bonus = 5.0 if high_flag_count >= 1 else 0
    return total + bonus

# Execution point of interest
final_diagnostic = process_metrics(aggregate_data, threshold_map)

# Additional decoy operation after target point
deco_result = calculate_entropy([metric_a, metric_b])

print(f"Result: {final_diagnostic}")