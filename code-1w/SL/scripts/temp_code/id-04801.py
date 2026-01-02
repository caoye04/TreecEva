def analyze_feedback(responses):
    sentiment_scores = {'positive': 3, 'neutral': 1, 'negative': -2}
    total = 0
    for r in responses:
        if r in sentiment_scores:
            total += sentiment_scores[r]
    return total // len(responses) if responses else 0

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / len(data)
        entropy -= p * log2(p)
    return round(entropy, 4)

# Unused but plausible transformation
def transform_ratings(ratings):
    adjusted = []
    for i, val in enumerate(ratings):
        if i % 2 == 0:
            adjusted.append(val * 1.5)
        else:
            adjusted.append(val + 0.5)
    return [round(x, 2) for x in adjusted]

# Simulate system health (dead code path)
def check_system_load(loads):
    critical = any(load > 90 for load in loads)
    avg = sum(loads) / len(loads)
    return 'OVERLOADED' if critical else ('STABLE' if avg < 60 else 'MONITORING')

# Core logic with distractions
status_codes = [200, 404, 500, 200, 403]
code_count = {code: status_codes.count(code) for code in set(status_codes)}
ignored_diagnostic = sum(v * k for k, v in code_count.items())  # Misleading aggregate

# Fake normalization layer (distractor)
def normalize_sequence(seq):
    m = min(seq)
    mx = max(seq)
    return [(x - m) / (mx - m) * 100 for x in seq] if mx != m else [50] * len(seq)

# Real processing begins
outcomes = [87, 92, 78, 94, 85]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Bit manipulation red herring
obfuscated_key = 0
for i, w in enumerate(weights):
    shift = i % 4
    obfuscated_key ^= int(w * 100) << shift

# Another decoy: combinatorics distraction
def count_subsequences(arr, threshold):
    count = 0
    n = len(arr)
    for i in range(1, 1 << n):
        subset = [arr[j] for j in range(n) if i & (1 << j)]
        if len(subset) > 1 and sum(subset) > threshold:
            count += 1
    return count

subseq_count = count_subsequences(outcomes, 170)  # Computationally heavy but unused

# Real metric calculation obscured
metric_weights = {
    'accuracy': 0.4,
    'latency': 0.25,
    'throughput': 0.2,
    'consistency': 0.15
}

raw_outcomes = {
    'accuracy': 91.2,
    'latency': 47.8,
    'throughput': 88.0,
    'consistency': 76.4
}

# Secondary distractor: set operations on irrelevant data
timestamps = [1680000000, 1680003600, 1680007200]
date_marks = set(t // 3600 for t in timestamps)
backup_flags = {1, 2, 4, 8}
sync_mask = date_marks & backup_flags  # Useless intersection

# Main evaluation logic hidden among noise
def evaluate_metric(value, target=85.0, weight=1.0):
    deviation = abs(value - target)
    penalty = deviation * 0.1
    return (value - penalty) * weight

def evaluate_performance(scales, results):
    score = 0.0
    audit_log = []
    
    # Use enumerate and zip as required
    for idx, (name, weight) in enumerate(scales.items()):
        if name not in results:
            continue
        raw_val = results[name]
        
        # Simulated calibration offset (meaningful intermediate)
        calibrated = raw_val + (idx * 0.05) if idx % 2 == 0 else raw_val - (idx * 0.03)
        
        # Actual scoring step
        contribution = evaluate_metric(calibrated, target=85.0, weight=weight)
        score += contribution
        
        # Log entry (distraction)
        audit_log.append(f"Step {idx}: {name} -> {contribution:.3f}")
    
    # Final nonlinear adjustment
    if score > 100:
        score = 100 + (score - 100) ** 0.5
    elif score < 0:
        score = 0
    
    return round(score, 6)

# Noise: unused list processing
timestamps_minutes = [t % 3600 // 60 for t in timestamps]
minute_freq = {m: timestamps_minutes.count(m) for m in set(timestamps_minutes)}

# Call that matters
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result as required
print(f"Result: {final_score}")