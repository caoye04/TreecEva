def analyze_phase_shift(signal, threshold, mode='strict'):
    if mode == 'strict':
        return sum(1 for x in signal if abs(x) > threshold)
    else:
        return len([x for x in signal if x != 0])


def compute_entropy(data):
    from math import log2
    total = sum(data)
    if total == 0:
        return 0.0
    entropy = 0.0
    for freq in data:
        if freq > 0:
            prob = freq / total
            entropy -= prob * log2(prob)
    return round(entropy, 6)


def transform_sequence(seq, key):
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append(val ^ (key << 1))
        else:
            transformed.append(val | (key >> 1))
    return transformed


def recursive_filter(items, depth):
    if depth <= 0 or not items:
        return [0]
    if len(items) == 1:
        return items
    mid = len(items) // 2
    left = recursive_filter(items[:mid], depth - 1)
    right = recursive_filter(items[mid:], depth - 2)
    return [sum(left), sum(right)]

# Irrelevant helper (distractor)
def unused_checksum(buffer):
    acc = 0
    for b in buffer:
        acc = (acc + b) * 31 % 10007
    return acc

# Unused constant (red herring)
MAX_BUFFER_SIZE = 1024 * 1024

# Simulated sensor readings (real data)
sensor_readings = [128, 64, 32, 16, 8, 4, 2, 1]

# Baseline calibration offset (used later)
baseline_offset = 17

# Decoy data structure (misleading)
status_map = {
    'active': True,
    'debug': False,
    'mode': 'diagnostic',
    'level': 9,
    'flags': [1, 0, 1, 1]
}

# Transform sensor data with key derived from offset
transformation_key = baseline_offset ^ 255
processed_signal = transform_sequence(sensor_readings, transformation_key)

# Analyze phase shift with strict filtering
anomalies_detected = analyze_phase_shift(processed_signal, threshold=100, mode='strict')

# Secondary analysis with different mode (unused result)
weak_analysis = analyze_phase_shift(processed_signal, threshold=50, mode='loose')

# Compute frequency distribution for entropy
freq_count = [processed_signal.count(i) for i in range(min(processed_signal), max(processed_signal)+1)]
entropy_metric = compute_entropy(freq_count)

# Create processing chain using zip and enumerate (required feature)
index_weights = [i * 1.5 for i in range(len(processed_signal))]
processing_chain = []
for idx, (val, weight) in enumerate(zip(processed_signal, index_weights)):
    adjusted = val + weight
    if idx % 3 == 0:
        adjusted = int(adjusted * 1.1)
    processing_chain.append(int(adjusted))

# Dead code path: condition never met (distractor)
if len(processing_chain) > 100:
    backup_result = recursive_filter(processing_chain, 5)
    status_map['recovery'] = True

# Actual recursive processing with limited depth
filter_depth = 3
filtered_output = recursive_filter(processing_chain, filter_depth)

# Aggregate various metrics into final diagnostic score
aggregate_metrics = lambda chain, offset: (
    sum(chain) 
    + offset * 2 
    - anomalies_detected * 5 
    + int(entropy_metric * 10)
    - sum(filtered_output)
)

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, baseline_offset)

# Misleading intermediate print (not the answer)
temp_score = weak_analysis * 100 + int(entropy_metric)

# Correct output
print(f"Result: {final_diagnostic}")