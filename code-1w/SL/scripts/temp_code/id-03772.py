def analyze_signal(samples, threshold=0.5):
    # Irrelevant signal processing (distractor)
    filtered = [s for s in samples if abs(s) > threshold]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    return sum(normalized) / len(normalized)


def compute_entropy(data):
    # Dead function - never used but looks important
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log(count / total, 2) for count in freq.values())
    return round(entropy, 3)

# Misleading intermediate values
temp_offset = 127
calibration_factor = 0.891
adjustment_matrix = [[1, 0], [0, -1]]  # Unused

# Core data with red herrings
raw_metrics = [0.4, 0.6, 0.8, 0.3, 0.7, 0.5, 0.9, 0.2]
weights = [1, 2, 1, 3, 2, 1, 4, 1]

# Decoy transformation using slicing and lambda (partially relevant)
transformed = list(map(lambda x: x ** 2 if x > 0.5 else x ** 0.5, raw_metrics[1:7]))

# Conditional expression with distractors
base_threshold = 0.6 if len(raw_metrics) % 2 == 0 else 0.4
bonus_applied = False

# Multiple assignments (some irrelevant)
valid_count, total_weight, accumulator = 0, 0, 0.0
aux_data = [(i, v) for i, v in enumerate(raw_metrics) if v >= 0.3]

# Key computation buried in noise
def evaluate_performance(metrics, base):
    global bonus_applied, accumulator
    score = 0
    bonus_trigger = False
    
    for i, val in enumerate(metrics):
        # Weighted contribution
        weight = weights[i] if i < len(weights) else 1
        if val > base:
            score += val * weight
            valid_count += 1  # Shadowed inside function
        elif val < 0.4:
            score -= 0.1 * weight  # Penalty branch
        
        # Side-effect accumulation (distraction)
        accumulator += val * 0.01
        
        # Bit manipulation decoy
        shifted = i << 2
        if shifted & 3 == 0:
            score += 0.05  # Tiny, misleading boost

    # Conditional expression determining bonus
    bonus_trigger = any(m > 0.85 for m in metrics[-3:])
    if bonus_trigger and score > 3.0:
        score *= 1.2
        bonus_applied = True
    
    # Sorting distraction
    sorted_vals = sorted([m for m in metrics if m > base])
    if len(sorted_vals) > 2:
        mid_val = sorted_vals[len(sorted_vals)//2]
        score += mid_val * 0.1  # Small addition
    
    return round(score, 4)

# Unused recursive function (red herring)
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Real execution path buried among distractions
metric_data = raw_metrics[::2]  # Slicing to take every other element

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

# Print required result
print(f"Result: {final_score}")