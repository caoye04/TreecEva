def analyze_readings(readings):
    # Irrelevant signal processing (dead path)
    filtered = [x * 0.9 for x in readings if x > 50]
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    return smoothed  # Never actually used

# Simulated sensor health diagnostics
def evaluate_stability(logs):
    unstable_count = 0
    for log in logs:
        if sum(1 for x in log if x < 10) > 2:
            unstable_count += 1
    return unstable_count > 3  # Misleading stability check

def compute_entropy(data):
    from math import log2
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def process_metrics(data, limits):
    # Core logic starts here
    baseline = data[1:6]  # Slice of interest
    offsets = [abs(b - limits['target']) for b in baseline]
    
    # Decoy structure manipulation
    stats_log = {
        'raw_length': len(data),
        'peak': max(data),
        'variance': sum((x - sum(data)/len(data))**2 for x in data) / len(data),
        'ignored_entropy': compute_entropy(data)
    }
    
    # Real computation path
    active_zones = []
    for i, val in enumerate(data):
        if val > limits['threshold'] and i % 2 == 1:
            active_zones.append(i * val)
    
    # Key transformation using zip and slicing
    paired = list(zip(baseline[:-1], baseline[1:]))
    deltas = [b - a for a, b in paired]
    trend_score = sum(deltas) * len(active_zones)
    
    # Conditional override based on bit manipulation red herring
    flag = 0b1010
    mask = 0b1100
    decoy_flag = flag & mask | 0b0010  # Looks important, unused
    
    # Actual answer derivation
    adjustment = 0
    for i, (a, b) in enumerate(paired):
        if (i + b) % 3 == 0:
            adjustment += a // 2
    
    final_diagnostic = trend_score - adjustment
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    health_data = [85, 92, 88, 95, 87, 90, 76, 83, 80, 89, 91, 84, 77]
    thresholds = {
        'target': 85,
        'threshold': 82,
        'window': 5
    }
    
    # Dead code paths with plausible names
    signal_chain = analyze_readings(health_data)
    system_stable = evaluate_stability([health_data[:5], health_data[5:10], health_data[8:]])
    
    # Distractor variables
    temp_analysis = [x for x in health_data if x > 85]
    cumulative_shift = sum(x * (i+1) for i, x in enumerate(health_data[:7]))
    metadata_summary = {k: v for k, v in thresholds.items()}
    metadata_summary['offsets'] = [abs(health_data[i] - thresholds['target']) for i in range(0, 6, 2)]
    
    # Critical statement
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")