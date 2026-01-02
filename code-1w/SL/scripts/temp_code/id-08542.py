import math

# Simulated system telemetry and diagnostic processing
def collect_timing_samples():
    samples = []
    for i in range(1, 100):
        if i % 3 == 0:
            samples.append(i * 0.7 + (i % 7))
        elif i % 5 == 0:
            samples.append(i * 0.4)
    return samples

def compute_hash_code(label: str) -> int:
    # Irrelevant hashing function - distractor
    return sum(ord(c) * (index + 1) for index, c in enumerate(label)) % 97

def analyze_phase_shift(signal: list) -> float:
    # Unused analytical function - red herring
    total = 0.0
    for val in signal:
        total += math.sin(val) * math.cos(val + 1)
    return total / len(signal) if signal else 0

def validate_checksum(data: list) -> bool:
    # Dead code path - never actually used in logic
    checksum = sum(d % 10 for d in data)
    return checksum % 8 == 0

# Core data structures
timing_log = collect_timing_samples()
system_flags = {
    'overload': False,
    'sync_error': True,
    'phase_lock': len(timing_log) > 50,
    'legacy_mode': False
}

# Misleading intermediate computations
average_sample = sum(timing_log) / len(timing_log) if timing_log else 0
variance_guess = sum((x - average_sample) ** 2 for x in timing_log[:30]) / 30
normalization_factor = math.sqrt(variance_guess) if variance_guess > 1 else 1.0

temp_correction = [round(t / normalization_factor, 3) for t in timing_log[-10:]]
shift_index = len(temp_correction) // 2
offset_lookup = {i: temp_correction[i] * 1.5 for i in range(len(temp_correction))}

# Decoy statistical analysis
mean_shift = sum(offset_lookup.values()) / len(offset_lookup) if offset_lookup else 0
flag_weights = {'overload': 10, 'sync_error': -5, 'phase_lock': 8, 'legacy_mode': -3}
weighted_score = sum(flag_weights[k] * (1 if v else 0) for k, v in system_flags.items())

# Real processing chain buried in noise
def extract_critical_windows(data, threshold=0.65):
    windows = []
    for i in range(len(data) - 4):
        window = data[i:i+5]
        if sum(1 for w in window if w > threshold * average_sample) >= 3:
            windows.append(window)
    return windows

def calculate_entropy(values):
    freq = {}
    for v in values:
        key = int(v)
        freq[key] = freq.get(key, 0) + 1
    probs = [f / len(values) for f in freq.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def aggregate_metrics(log_data, flags):
    # Key logic hidden among distractions
    critical_windows = extract_critical_windows(log_data)
    if not critical_windows:
        return -1
    
    flat_data = [item for window in critical_windows for item in window]
    entropy = calculate_entropy(flat_data)
    size_factor = len(critical_windows) * (flags['phase_lock'] + 1)
    
    # Conditional expression - required Python feature
    adjustment = 1.25 if flags['sync_error'] else 0.85
    
    # Final computation
    raw_metric = entropy * size_factor * adjustment
    
    # Secondary filter based on decoy variables (but only one matters)
    if mean_shift > 0 and normalization_factor > 0.5:  # Uses two misleading vars
        raw_metric += 2.5  # Minor red herring influence
    
    return int(round(raw_metric))

# Execute core logic
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output result as required
print(f"Result: {final_diagnostic}")