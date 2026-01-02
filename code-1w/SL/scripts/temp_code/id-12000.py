def analyze_pattern(sequence):
    if len(sequence) < 5:
        return False
    peaks = [i for i in range(1, len(sequence)-1) if sequence[i-1] < sequence[i] > sequence[i+1]]
    troughs = [i for i in range(1, len(sequence)-1) if sequence[i-1] > sequence[i] < sequence[i+1]]
    return len(peaks) >= 2 and len(troughs) >= 2

# Irrelevant helper (distractor)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation (dead path)
def mirror_sequence(arr):
    return arr + arr[::-1]

# Core logic disguised among distractions
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    import math
    return -sum(p * math.log2(p) for p in probabilities)

# Decoy function with misleading name
def calculate_robustness_index(seq):
    if not seq:
        return 0
    squared_devs = [(x - sum(seq)/len(seq))**2 for x in seq]
    return sum(squared_devs) / len(squared_devs)

# Real processing begins here
def validate_stability(readings):
    threshold = sum(readings) / len(readings)
    fluctuation_count = sum(1 for i in range(1, len(readings)) if abs(readings[i] - readings[i-1]) > threshold * 0.1)
    return fluctuation_count < len(readings) * 0.3

base_threshold = 42

# Simulated sensor metric data (mixture of relevant and red herring fields)
metric_data = {
    'signals': [12, 15, 23, 19, 27, 35, 31, 29, 37],
    'checksums': [0xFF, 0xAB, 0xCD, 0x12],  # Bitwise decoy
    'metadata': {
        'version': '2.1',
        'source_id': 0b1101,
        'flags': 0b1010 ^ 0b0110  # XOR distraction
    },
    'history': [
        {'epoch': 1, 'value': 12},
        {'epoch': 2, 'value': 15},
        {'epoch': 3, 'value': 23}
    ]
}

# Secondary irrelevant computation chain
current_state = [x % 7 for x in metric_data['signals'] if x > 20]
state_entropy = compute_entropy(current_state)  # Misleading intermediate

# Hidden control flow dependency
pattern_valid = analyze_pattern(metric_data['signals'])
stability_ok = validate_stability(metric_data['signals'])

# Destructuring decoy
a, b, *rest = metric_data['signals'][::2]
offset = len(rest) - (b // a)  # Useless but plausible-looking calc

# Critical logic buried in conditionals
def evaluate_performance(metrics, threshold):
    raw_series = metrics['signals']
    n = len(raw_series)
    
    # Real answer derivation path
    window_avg = sum(raw_series[-3:]) / 3
    peak_to_avg_ratio = max(raw_series) / window_avg
    
    # Red herring branch
    if 'debug' in metrics:
        return -999
    
    # Actual logic
    adjustment_factor = 1.0
    if pattern_valid and stability_ok:
        adjustment_factor = 1.25
    elif not pattern_valid:
        adjustment_factor = 0.85
    
    base_score = window_avg * peak_to_avg_ratio
    final_raw = base_score * adjustment_factor
    
    # Final manipulation
    final_ceiling = 100 if n > 5 else 80
    return int(min(final_raw, final_ceiling)) + offset  # offset is distractor

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Output requirement
print(f"Target result: {final_score}")