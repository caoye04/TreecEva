def analyze_component(reading, threshold=0.7):
    return reading > threshold

# Irrelevant sensor simulation
temperature_readings = [0.65, 0.72, 0.81, 0.69]
humidity_readings = [0.55, 0.78, 0.63, 0.82]

# Distractor: Unused function
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Distractor: Dead computation
redundant_sum = sum([x * 1.5 for x in humidity_readings if x < 0.75])

# Real data for evaluation
baseline_metrics = {
    'latency': 0.45,
    'throughput': 0.88,
    'accuracy': 0.92,
    'stability': 0.76,
    'scalability': 0.68
}

# Benchmark weights (some are misleadingly labeled)
benchmark_weights = {
    'latency': 0.2,
    'throughput': 0.25,
    'accuracy': 0.3,
    'stability': 0.15,
    'scalability': 0.1,
    'robustness': 0.0  # Irrelevant key with zero weight
}

# Simulated auxiliary data (not used in final calculation)
external_factors = [0.5, 0.7, 0.9]
adjusted_scores = {k: v * 1.1 for k, v in baseline_metrics.items() if k != 'scalability'}

# Linear search for invalidation (distractor path)
invalid_found = False
for key, val in baseline_metrics.items():
    if val < 0.4 and key == 'nonexistent':
        invalid_found = True

# Conditional red herring
if len(temperature_readings) > 3:
    temp_correction = 0.05
    # But correction not applied anywhere meaningful

# Core logic disguised among distractors
def evaluate_performance(metrics, weights):
    score = 0.0
    count = 0
    
    # Mix of relevant and irrelevant operations
    bonus_applied = False
    for idx, (key, base_val) in enumerate(metrics.items()):
        if key not in weights:
            continue  # Skip unknown metrics
        
        weighted_contribution = base_val * weights[key]
        score += weighted_contribution
        
        # Real conditional logic affecting result
        if base_val >= 0.8 and key in ['throughput', 'accuracy']:
            score += 0.02  # Bonus for high performers
        
        # Distractor condition that never triggers
        if idx > 10 or key == 'robustness':
            count += 1
            bonus_applied = True
    
    # Final adjustment based on hidden rule
    if score > 0.8:
        score *= 1.05
    
    return round(score, 6)

# Unused recursive helper (decoy)
def recursive_discount(n):
    if n <= 1:
        return n
    return 0.9 * recursive_discount(n - 1)

# Tuple unpacking distraction
(_, primary, secondary, _) = [x * 2 for x in temperature_readings]

# List comprehension with side effect (irrelevant)
processed_flags = [analyze_component(val, 0.75) for val in humidity_readings]

# Critical execution point
final_score = evaluate_performance(baseline_metrics, benchmark_weights)

# Print required output
print(f"Result: {final_score}")