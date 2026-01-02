import itertools

def analyze_pattern(sequence):
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

def validate_consistency(pattern):
    changes = 0
    for i in range(1, len(pattern)):
        if pattern[i] != pattern[i-1]:
            changes += 1
    return changes < 5

def compute_volatility(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return variance ** 0.5

def filter_outliers(data, threshold=2):
    vol = compute_volatility(data)
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) <= threshold * vol]
    return filtered if len(filtered) > 2 else data

def process_metrics(raw_data, importance_weights):
    # Step 1: Clean and prepare data
    cleaned_data = filter_outliers(raw_data)
    
    # Distractor: unused transformation
    normalized = [x / max(cleaned_data) for x in cleaned_data] if cleaned_data else [0]
    
    # Step 2: Analyze trend pattern
    trend_directions = analyze_pattern(cleaned_data)
    is_stable = validate_consistency(trend_directions)
    
    # Step 3: Compute base metrics
    base_metric = sum(cleaned_data) // len(cleaned_data)  # integer average
    volatility = compute_volatility(cleaned_data)
    
    # Step 4: Apply weight adjustments using dictionary lookup
    adjustment_map = {0: 1.0, 1: 1.2, 2: 0.8, 3: 1.1}
    total_weight = sum(importance_weights)
    adjusted_weights = [w / total_weight for w in importance_weights[:len(cleaned_data)]]
    
    # Step 5: Simulate weighted contributions (only first few matter)
    weighted_sum = sum(val * adj for val, adj in itertools.zip_longest(cleaned_data, adjusted_weights, fillvalue=1.0))
    
    # Step 6: Conditional boost based on stability
    stability_bonus = 10 if is_stable else -5
    
    # Step 7: Final score computation (this is the key result)
    final_score = int(weighted_sum // 10) + base_metric + stability_bonus
    
    # Red herring: complex but irrelevant calculation
    phantom_cycle = 0
    for combo in itertools.combinations_with_replacement([1,2,3], 3):
        phantom_cycle += combo[0] * combo[2]
    dummy_tracker = {f'iter_{i}': phantom_cycle % (i+1) for i in range(5)}
    
    return final_score

data = [15, 18, 16, 20, 19, 22, 21, 23]
weights = [3, 2, 4, 1, 3, 2, 1, 4]
final_score = process_metrics(data, weights)
print(f"Target result: {final_score}")