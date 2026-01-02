from collections import defaultdict, Counter

# Simulated sensor data from multiple sources
data_packets = [
    [1, 0, 1, 1, 2, 1, 0],
    [2, 1, 0, 1, 1, 3, 1],
    [0, 0, 2, 2, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 4]
]

# Irrelevant statistical cache (distractor)
stats_cache = defaultdict(int)
for packet in data_packets:
    for val in packet:
        stats_cache[val] += 1

# Mapping signal types to weights (used later)
signal_weights = {0: -1, 1: 1, 2: 2, 3: 4, 4: 8}

# Decoy function - looks important but unused
def compute_entropy(vector):
    counts = Counter(vector)
    total = len(vector)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy
    return entropy

# Another red herring: historical baseline (never referenced)
historical_baseline = [
    sum(packet[::2]) - sum(packet[1::2]) for packet in data_packets
]

# Real processing begins here
aggregated = [sum(packet) for packet in data_packets]

# Transform using weights (key step)
weighted_sums = []
for packet in data_packets:
    weighted_sum = 0
    for val in packet:
        if val in signal_weights:
            weighted_sum += signal_weights[val]
    weighted_sums.append(weighted_sum)

# Distractor: unused transformation chain
temp_matrix = [[x * 2 + 1 for x in row] for row in data_packets]
derived_scalars = [max(row) ** min(row + [1]) for row in temp_matrix]

# Threshold logic setup (critical)
threshold_map = defaultdict(lambda: 3)
threshold_map.update({
    'low_noise': 2,
    'high_gain': 5,
    'default': 4
})

# Simulated gain levels from hardware (mixed relevance)
gain_levels = [1.0, 1.5, 1.0, 2.0]
adjusted_weights = [
    w * (1.2 if i % 2 == 0 else 0.8) for i, w in enumerate(weighted_sums)
]

# Core analysis function with recursion
def analyze_signal(data_list, thresholds):
    if len(data_list) <= 1:
        return data_list[0] if data_list else 0
    
    mid = len(data_list) // 2
    left = analyze_signal(data_list[:mid], thresholds)
    right = analyze_signal(data_list[mid:], thresholds)
    
    # Conditional expression determines merge behavior
    correction = thresholds['default']
    if left > thresholds['high_gain']:
        correction += 1
    elif right < thresholds['low_noise']:
        correction -= 1
    
    return (left + right) // correction

# Secondary irrelevant processing path (dead code)
def normalize_packets(packets):
    flat = [item for sublist in packets for item in sublist]
    mean_val = sum(flat) / len(flat)
    return [round((x - mean_val) * 100) for x in flat]

# Unused list comprehension that looks important
correlation_pairs = [
    (data_packets[i][j], data_packets[i][j+1])
    for i in range(len(data_packets))
    for j in range(len(data_packets[i])-1)
    if data_packets[i][j] != 0 and data_packets[i][j+1] != 0
]

# Critical data transformation
processed_data = []
for idx, ws in enumerate(weighted_sums):
    adjusted = ws * gain_levels[idx]
    processed_data.append(int(adjusted))

# This print is just for distraction (not the answer)
print(f"Debug: {sum(aggregated) % 7}")

# Key execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Final output
print(f"Target result: {final_diagnostic}")