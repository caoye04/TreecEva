import math

# Simulated sensor data processing with performance scoring
def collect_telemetry():
    raw_data = [23.5, 45.0, 12.8, 56.3, 34.1, 78.9, 11.2]
    filtered = [x for x in raw_data if x > 20]  # Only consider values above threshold
    normalized = [round((x - min(filtered)) / (max(filtered) - min(filtered)) * 100) for x in filtered]
    return normalized

# Irrelevant auxiliary function – distractor
def generate_checksum(data):
    acc = 0
    for i, val in enumerate(data):
        acc += val * (i + 1)
    return acc % 1000

# Misleading transformation – looks important but unused in final path
def transform_legacy_format(data):
    return [int(x * 1.5) % 256 for x in data]

# Complex weight adjustment logic with red herring branches
def adjust_weights(wts, mode='standard'):
    temp = wts.copy()
    if len(temp) > 3:
        temp[0] *= 1.1
        temp[1] -= 0.05
        # Dead branch: mode 'legacy' never used
        if mode == 'legacy':
            temp = [t * 0.9 for t in temp]
    else:
        temp = [t + 0.1 for t in temp]
    # Decoy mutation
    temp.append(999)  # Never gets used
    return temp[:len(wts)]  # Return original length

# Core evaluation logic – depends on specific conditions
def evaluate_metric(value, baseline):
    if value >= 85:
        return 4
    elif value >= 70:
        return 3
    elif value >= 50:
        return 2
    elif value >= baseline:
        return 1
    else:
        return 0

# Scoring aggregation with list comprehension and set operations
def evaluate_performance(metrics, weights):
    baseline_thresholds = {1, 2, 3}  # Set usage as per requirement
    scores = [evaluate_metric(val, 30) for val in metrics]
    weighted = [s * w for s, w in zip(scores, weights)]
    
    # Distractor: unused intermediate calculation
    avg_score = sum(scores) / len(scores) if scores else 0
    penalty = 0
    if len(set(scores)) == 1:
        penalty = 5  # Uniformity penalty – not actually applied
    
    # Real computation path
    total = sum(weighted)
    if sum(1 for s in scores if s >= 3) >= 4:  # At least 4 strong scores
        total += 10  # Bonus for consistency
    
    # Final nonlinear adjustment
    final = math.floor(total * 1.05)
    return final

# Unused recursive function – major red herring
def calculate_recursive_depth(n):
    if n <= 1:
        return 1
    return n * calculate_recursive_depth(n - 2)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Gather and process telemetry
    signal_data = collect_telemetry()  # Returns [0.0, 23.0, 43.0, 95.0, 58.0, 100.0]
    
    # Step 2: Apply irrelevant transformations (distractors)
    checksum = generate_checksum(signal_data)
    legacy_blob = transform_legacy_format(signal_data)
    
    # Step 3: Prepare evaluation parameters
    metrics = signal_data  # Direct use of processed telemetry
    weights = [0.3, 0.2, 0.2, 0.15, 0.1, 0.05]
    
    # Step 4: Adjust weights (only meaningful part retained)
    adjusted_weights = adjust_weights(weights, mode='standard')
    
    # Step 5: Evaluate performance (key statement)
    final_score = evaluate_performance(metrics, adjusted_weights)
    
    # Print result as required
    print(f"Result: {final_score}")