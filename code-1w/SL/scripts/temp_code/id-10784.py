import itertools

# Simulated system performance metrics
def generate_diagnostics():
    readings = [127, 255, 192, 64]
    flags = [r & 128 for r in readings]
    return {f'sensor_{i}': (readings[i], flags[i]) for i in range(len(readings))}

# Irrelevant diagnostic transformation (dead path)
def transform_readings(data):
    return [((x >> 2) ^ 15) & 255 for x in data if x > 100]

# Misleading normalization function that isn't used
def normalize(value, max_val=255):
    return round(value / max_val, 6)

# Core evaluation logic
def analyze_metric(value, base):
    if value < base:
        return (base - value) * 2
    elif value == base:
        return 50
    else:
        diff = value - base
        return diff + (diff // 10)  # Bonus for larger deviations

# Unused recursive red herring
def recursive_sum(n):
    return n + recursive_sum(n-1) if n > 0 else 0

# Decoy statistical function
def compute_entropy(vals):
    total = sum(vals)
    probs = [v / total for v in vals]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

# Real processing pipeline
def filter_active_sensors(diag_data):
    return {k: v[0] for k, v in diag_data.items() if v[1] == 128}

# Secondary processing with distractor variables
def extract_trends(values):
    trends = []
    temp_accum = 0
    for i, v in enumerate(values):
        trend_val = (v * (i + 1)) % 17
        temp_accum += trend_val
        if i % 2 == 0:
            trends.append(trend_val)
    # Distractor: unused accumulation
    dummy_calc = temp_accum * 3 % 97
    return trends

# Main evaluation function
def evaluate_performance(metrics, baseline):
    # Step 1: Filter relevant sensors
    active_vals = list(metrics.values())
    
    # Step 2: Apply analysis to each metric
    analyzed = [analyze_metric(v, baseline) for v in active_vals]
    
    # Step 3: Aggregate with weighted sum
    weighted = sum(analyzed[i] * (i + 1) for i in range(len(analyzed)))
    
    # Step 4: Apply modular correction
    corrected = weighted % 10000
    
    # Step 5: Add bonus based on pattern matching
    pairs = list(itertools.combinations(analyzed, 2))
    bonus = len([p for p in pairs if (p[0] + p[1]) % 7 == 0]) * 25
    
    # Step 6: Final adjustment using conditional expression
    adjustment = 100 if any(a > 100 for a in analyzed) else 25
    
    # Step 7: Compute final score
    result = corrected + bonus + adjustment
    
    # Distractor: meaningless set operation
    unique_components = set(analyzed) | {baseline, corrected % 100}
    extra_flag = len(unique_components) > 5 else False
    
    # Final computation
    final = result + (50 if extra_flag else 0)
    return final

# Execution flow
if __name__ == '__main__':
    # Generate raw diagnostics
    diagnostics = generate_diagnostics()
    
    # Extract active sensor values (only those with flag 128)
    filtered_metrics = filter_active_sensors(diagnostics)
    
    # Extract trend patterns (used to mislead)
    trend_sequence = extract_trends(filtered_metrics.values())
    
    # Baseline threshold
    baseline_reference = 192
    
    # Irrelevant entropy calculation (distractor)
    entropy_value = compute_entropy(list(filtered_metrics.values()))
    
    # Key statement: evaluate final performance score
    final_score = evaluate_performance(filtered_metrics, baseline_reference)
    
    # Output target result
    print(f"Result: {final_score}")