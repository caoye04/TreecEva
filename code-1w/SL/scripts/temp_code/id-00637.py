import itertools

# Simulated sensor diagnostics system
def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    # Check for oscillation pattern (alternating increase/decrease)
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    signs = [1 if d > 0 else -1 for d in diffs]
    alternates = all(signs[i] != signs[i+1] for i in range(len(signs)-1))
    return alternates

# Misleading auxiliary function (dead end)
def calculate_entropy(data):
    from math import log
    freq_map = {}
    total = len(data)
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy  # Never actually used

# Bit manipulation red herring
def scramble_bits(value, key=13):
    """Irrelevant bit scrambling"""
    return (value << 3) ^ key ^ (value >> 4)

# Unused diagnostic mode
DIAGNOSTIC_MODE = True
MAX_HISTORY = 500
BUFFER_SIZE = 1024  # Unused constant

# Core processing function
def process_readings(readings, limits):
    # Extract baseline from first segment
    baseline_window = readings[:7]
    baseline_avg = sum(baseline_window) / len(baseline_window)
    
    # Distractor: complex transformation with no impact
    transformed = [(x - baseline_avg) ** 2 + 2 for x in readings]
    normalized = [abs((x - min(transformed)) / (max(transformed) - min(transformed))) for x in transformed]
    
    # Real logic begins: find critical segments above threshold
    threshold = limits['critical']
    critical_indices = [i for i, val in enumerate(readings) if val > threshold]
    
    # Compute gaps between spikes
    if len(critical_indices) > 1:
        gaps = [critical_indices[i+1] - critical_indices[i] for i in range(len(critical_indices)-1)]n    else:
        gaps = []
    
    # Analyze sub-segments using itertools to group consecutive high readings
    spike_clusters = []
    current_cluster = []
    for i, val in enumerate(readings):
        if val > limits['warning']:
            current_cluster.append(val)
        else:
            if current_cluster:
                spike_clusters.append(current_cluster)
                current_cluster = []
    if current_cluster:
        spike_clusters.append(current_cluster)
    
    # Only clusters of size >=3 are relevant
    significant_spikes = [c for c in spike_clusters if len(c) >= 3]
    
    # Use dictionary operation to aggregate cluster stats
    cluster_stats = {
        'count': len(significant_spikes),
        'max_size': max([len(c) for c in significant_spikes], default=0),
        'total_peaks': sum([len(c) for c in significant_spikes])
    }
    
    # Key logic: check oscillation in first significant spike
    has_oscillation = False
    if cluster_stats['count'] > 0:
        first_spike = significant_spikes[0]
        has_oscillation = analyze_pattern(first_spike)
    
    # Slicing distraction: reverse every other segment (unused)
    sliced_parts = [readings[i:i+5] for i in range(0, len(readings), 5)]
    processed_slices = []
    for idx, part in enumerate(sliced_parts):
        if idx % 2 == 0:
            processed_slices.append(part[::-1])  # Reversed
        else:
            processed_slices.append(part)
    
    # Final computation path
    base_score = cluster_stats['total_peaks'] * 17
    if has_oscillation:
        base_score += 23
    if cluster_stats['max_size'] > 4:
        base_score += 11
    
    # Apply bitwise mask (only some bits matter)
    masked_score = base_score & 0xFF  # Keep only lowest 8 bits
    
    # One more irrelevant transformation
    final_hash = scramble_bits(masked_score, key=99)
    
    # ACTUAL answer derivation (obscured by distractions)
    adjustment = 1 if gaps and all(g < 10 for g in gaps) else 0
    final_diagnostic = masked_score + adjustment  # This is the real result
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Real input data
    sensor_data = [88, 92, 95, 101, 97, 103, 89, 76, 85, 90, 102, 105, 108, 104, 106, 99, 87, 73]
    thresholds = {
        'warning': 90,
        'critical': 100
    }
    
    # Dead code branch (never reached in practice)
    debug_snapshot = None
    if DIAGNOSTIC_MODE and False:  # Always false
        debug_snapshot = {
            'raw': sensor_data.copy(),
            'scrambled': [scramble_bits(x) for x in sensor_data]
        }
    
    # Key assignment statement
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")