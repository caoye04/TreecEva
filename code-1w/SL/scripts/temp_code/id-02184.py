import math

# Simulated sensor fusion system for environmental monitoring
base_readings = [144, 81, 64, 121, 169]
dummy_offsets = [7, 13, 22, 35, 41]  # Unused in final calculation (red herring)

def transform_readings(data):
    # Applies modular arithmetic and square root normalization
    processed = []
    for val in data:
        temp = int(math.sqrt(val)) % 10
        processed.append(temp)
    return processed

def calculate_entropy(values):
    # Irrelevant entropy computation (dead code path)
    total = sum(values)
    entropy = 0.0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * math.log(prob)
    return round(entropy, 6)

def filter_anomalies(seq, threshold=3):
    # Filters based on set membership (relevant logic)
    valid_set = {0, 1, 2, 3, 4, 5}
    filtered = [x for x in seq if x in valid_set]
    return filtered

def accumulate_weighted_sum(series):
    # Weighted accumulation with alternating signs
    total = 0
    for i, val in enumerate(series):
        weight = (-1) ** i
        total += weight * val * (i + 1)
    return total

def generate_reference_map(keys):
    # Creates a decoy dictionary (misleading intermediate)
    ref_map = {}
    for k in keys:
        ref_map[k] = (k * 11) % 7
    return ref_map  # Never used later

def evaluate_performance(metrics, dataset):
    # Core evaluation logic buried in distractions
    stage1 = transform_readings(dataset)
    
    # Distraction: entropy-like computation that doesn't affect result
    _ = calculate_entropy(dataset)
    
    stage2 = filter_anomalies(stage1)
    
    # Another red herring: unused reference map
    _ = generate_reference_map(stage2)
    
    # Conditional manipulation based on length
    if len(stage2) > 3:
        stage2 = [x + 1 for x in stage2]  # Increment all due to condition
    
    # Set deduplication with ordered preservation
    seen = set()
    unique_vals = []
    for x in stage2:
        if x not in seen:
            unique_vals.append(x)
            seen.add(x)
    
    # Final aggregation using weighted sum
    score = accumulate_weighted_sum(unique_vals)
    
    # Secondary adjustment based on modular checksum
    checksum = sum(unique_vals) % 5
    if checksum > 0:
        score -= checksum * 2
    
    return score

# Main execution flow
metric_set = {'precision', 'accuracy', 'stability'}  # Partially irrelevant
benchmark_data = base_readings  # Actual input source

# Spurious variable manipulations (distractors)
offset_correction = sum(dummy_offsets) // len(dummy_offsets)
shadow_copy = [x * 2 for x in base_readings]
intermediate_result = [math.ceil(math.sqrt(x)) for x in shadow_copy]

# Key statement
final_score = evaluate_performance(metric_set, benchmark_data)

# Output the required result
print(f"Target result: {final_score}")