import itertools

# Domain: Environmental Sensor Array Calibration
# Simulate sensor readings and diagnostic adjustments

def analyze_sensor_drift(raw_readings, baseline):
    adjusted = [r - baseline for r in raw_readings]
    drift = sum(abs(a) for a in adjusted if abs(a) > 0.5)
    return drift * 0.75

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def filter_anomalies(data_stream):
    # Irrelevant filtering (dead code path)
    return [x for x in data_stream if 10 <= x <= 100]

def generate_combinations(size):
    # Distractor: generates unused combinatorial data
    return list(itertools.combinations(range(size), 2))

def accumulate_diagnostic_stats(logs):
    # Unused accumulation function (decoy)
    counts = {}
    for entry in logs:
        key = entry // 10
        counts[key] = counts.get(key, 0) + 1
    return sum(counts.values())

def temporal_alignment(sequence, shift):
    # Misleading time-series alignment (not used in final result)
    return sequence[-shift:] + sequence[:-shift]

def validate_consistency(readings):
    # Red herring validation that isn't actually used
    return all(r >= 0 for r in readings)

def calculate_reliability_index(sensors):
    # Complex but irrelevant reliability scoring
    weights = [0.9, 1.0, 0.8, 1.1, 0.7]
    index = 0.0
    for i, s in enumerate(sensors):
        if i % 2 == 0:
            index += s * weights[i % len(weights)]
        else:
            index -= s * 0.5
    return abs(index)

def evaluate_performance(weights, outcomes):
    # Core logic embedded in noise
    base = sum(outcomes) * weights[0]
    bonus = 0
    
    # Real dependency: slice middle three outcomes
    trimmed = outcomes[1:4]
    
    # Real operation: pairwise combinations affecting bonus
    pairs = list(itertools.combinations(trimmed, 2))
    for a, b in pairs:
        if (a + b) % 2 == 0:
            bonus += 1
    
    # Real calculation branch
    adjustment = 0
    for w, val in zip(weights, outcomes[:len(weights)]):
        adjustment += w * val
    
    # Final score depends on base, bonus, and adjustment
    score = base + bonus * 10 + adjustment
    
    # Dead assignment (distractor)
    score = max(score, 50) if sum(trimmed) < 20 else min(score, 200)
    
    # Key: override based on tuple unpacking condition
    meta = (3, 7, 11)
    x, y, z = meta
    if score % y == 0:
        score = score // 2
    
    return int(score)

# --- Main Execution with High Interference ---

# Irrelevant sensor array setup
sensor_ids = [101, 102, 103, 104, 105]
raw_data = [23.5, 18.2, 19.8, 21.0, 17.3]
baseline_ref = 20.0

# Generate unused diagnostic combinations
combo_set = generate_combinations(6)
drift_amount = analyze_sensor_drift(raw_data, baseline_ref)

# Fake entropy computation on irrelevant data
entropy = compute_entropy([len(combo_set), 5, 3])

# Simulated system logs (unused)
system_logs = [101, 102, 102, 103, 104, 104, 104]
log_count = accumulate_diagnostic_stats(system_logs)

# Temporal realignment of unrelated signal
signal_pattern = [1, 0, 1, 1, 0]
shifted_signal = temporal_alignment(signal_pattern, 2)

# Consistency check (computed but not used)
valid = validate_consistency(raw_data)

# Reliability index (red herring)
reliability = calculate_reliability_index(raw_data)

# Real inputs to target function
metric_weights = [0.8, 0.5, 0.3]  # Only first two used meaningfully
raw_outcomes = [12, 6, 8, 4, 10]   # Core data source

# --- Critical Statement ---
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Output result as required
print(f"Result: {final_score}")