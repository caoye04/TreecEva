def analyze_system_load(loads):
    # Irrelevant function: analyzes system load but not used in main logic
    return sum(load ** 0.5 for load in loads if load > 10)

# Distractor variables
temp_cache = [i * 2 + 1 for i in range(15)]
system_flags = {'debug': True, 'verbose': False, 'mode': 'production'}

# Real data disguised among noise
raw_metrics = [85, 92, 78, 96, 88]
weights = [0.1, 0.2, 0.3, 0.25, 0.15]

# Unused transformation chain
decoy_transform = list(map(lambda x: (x - 70) * 1.5, raw_metrics))
filtered_data = [x for x in raw_metrics if x > 80]

# Dead code path - looks important but unused
if len(filtered_data) > 3:
    adjustment_factor = 1.1
else:
    adjustment_factor = 0.9

# Meaningful intermediate: normalize metrics to 0-1 scale
normalized = [(m / 100) for m in raw_metrics]

# Decoy sorting operation
sorted_temp = sorted(normalized, reverse=True)

# Another red herring: bit manipulation with no effect
bitmask = 0b101010
encoded_value = sum([(n * 100) & bitmask for n in normalized])

# Key function with recursion and distractors
def recursive_weight_accumulate(values, wts, idx=0):
    if idx >= len(values):
        return 0
    contribution = values[idx] * wts[idx]
    # Misleading early return that doesn't trigger
    if idx == 100:
        return -999  # dead branch
    return contribution + recursive_weight_accumulate(values, wts, idx + 1)

# Fake scoring using different method
dummy_score = sum([a*b for a,b in zip(raw_metrics, weights)]) / 100

# List of thresholds - partially used as distraction
thresholds = {"pass": 60, "distinction": 85, "elite": 90}
elite_count = sum(1 for m in raw_metrics if m >= thresholds["elite"])

# Another irrelevant enumeration block
offset_correction = 0
for i, val in enumerate(temp_cache):
    if i % 7 == 0:
        offset_correction += val

# Real evaluation logic buried in distractions
def evaluate_performance(mets, wts):
    # Use slicing to take only first N weights matching metrics
    effective_weights = wts[:len(mets)]
    # Normalize weights to ensure they sum to 1.0
    weight_sum = sum(effective_weights)
    normalized_weights = [w / weight_sum for w in effective_weights]
    
    # Apply normalized weights using zip and lambda
    weighted_sum = sum(map(lambda pair: pair[0] * pair[1], zip(mets, normalized_weights)))
    
    # Additional processing: apply experience bonus if high performer
    high_performer = all(m >= 75 for m in mets)
    bonus = 5 if high_performer else 0
    
    # Final score calculation
    raw_final = weighted_sum / 100  # Scale to fraction
    scaled_up = raw_final * 100  # Back to percentage
    return scaled_up + bonus

# Critical execution point
final_score = evaluate_performance(raw_metrics, weights)

# Print result as required
print(f"Target result: {final_score}")