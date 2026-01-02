def analyze_system_load(readings):
    avg_load = sum(readings) / len(readings)
    peak = max(readings)
    normalized = [x / peak for x in readings]
    return avg_load, normalized


def compute_entropy(data):
    from math import log2
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy

# Irrelevant utility function (decoy)
def validate_checksum(buffer):
    checksum = 0
    for byte in buffer:
        checksum ^= byte
        checksum = (checksum << 1) & 0xFF
    return checksum == 0xAA

# Unused but plausible transformation
def transform_coordinates(coords):
    transformed = []
    for i, (x, y) in enumerate(coords):
        if i % 2 == 0:
            transformed.append((x * 2, y + 1))
        else:
            transformed.append((x + 5, y * 3))
    return transformed

# Misleading intermediate calculation
def estimate_latency(bandwidth, distance):
    base = 0.01 * distance
    adjustment = 1000 / (bandwidth + 1)
    penalty = 0 if distance < 500 else (distance - 500) * 0.002
    return round(base + adjustment + penalty, 4)

# Real computation chain begins
config_modes = ['debug', 'release', 'profile', 'trace']
mode_index = len(config_modes) - 2  # evaluates to 2

timestamps = [1623456789, 1623456795, 1623456801, 1623456810, 1623456815]
time_diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]

# Simulate packet sizes in bytes
packet_sizes = [128, 256, 128, 512, 256, 128]
size_stats = {
    'total': sum(packet_sizes),
    'unique': len(set(packet_sizes)),
    'mode_freq': max([packet_sizes.count(x) for x in set(packet_sizes)])
}

# Distractor: unused complex structure
network_graph = {
    'nodes': [f'node_{i}' for i in range(8)],
    'edges': list(zip(['a','b','c','d'], [1,2,3,4]))
}

# Key data structures
metrics = {
    'throughput': 87.5,
    'stability': sum(time_diffs) / len(time_diffs),
    'consistency': compute_entropy(packet_sizes),
    'redundancy': size_stats['mode_freq'] / size_stats['unique']
}

benchmark_weights = {
    'throughput': 0.4,
    'stability': 0.3,
    'consistency': 0.2,
    'redundancy': 0.1
}

# Heavily distracted evaluation function
def evaluate_performance(perf, weights):
    # Irrelevant pre-checks
    if len(perf) != len(weights):
        raise ValueError("Mismatched dimensions")
    
    # Dummy normalization (not actually used)
    temp_vals = []
    for k, v in perf.items():
        temp_vals.append(v * 0.95 if k != 'throughput' else v)
    
    # Actual weighted sum
    raw_score = 0.0
    for key in perf:
        if key in weights:
            raw_score += perf[key] * weights[key]
    
    # Extra transformations (some irrelevant)
    adjusted = raw_score * 1.05
    capped = min(adjusted, 100.0)
    final_adjustment = 0.0
    
    # Conditional red herring
    if adjusted > 90:
        final_adjustment = 2.5
    elif adjusted > 80:
        final_adjustment = 1.2
    else:
        final_adjustment = -1.0  # This will be taken
    
    # Final score with adjustment
    result = round(capped + final_adjustment, 4)
    
    # Dead code path (never reached due to logic above)
    if result < 0:
        backup_weights = {k: 1/len(weights) for k in weights}
        alt = sum(perf[k] * backup_weights[k] for k in perf)
        result = alt  # decoy assignment
        
    return result

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark_weights)

# Print required output
print(f"Target result: {final_score}")