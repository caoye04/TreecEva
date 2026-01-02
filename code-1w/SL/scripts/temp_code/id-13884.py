import itertools

# System health monitoring simulation with diagnostic scoring

def collect_sensor_data():
    return [0.85, 0.92, 0.76, 0.88, 0.91]

def compute_baseline(readings):
    total = 0
    for r in readings:
        total += r ** 2
    return total / len(readings)

def normalize_readings(readings):
    norm = []
    factor = 1.0 / sum(readings)
    for r in readings:
        norm.append(r * factor * 100)
    return norm

def evaluate_stability_index(norm_readings):
    index = 0
    for i in range(len(norm_readings)):
        if norm_readings[i] > 20:
            index += 1.5
        elif norm_readings[i] > 10:
            index += 0.7
    return index

def generate_combinations(data):
    # Irrelevant combinatorial explosion (distractor)
    combs = []
    for i in range(1, len(data)+1):
        combs.extend(itertools.combinations(data, i))
    return combs  # Never used in final calculation

def filter_anomalies(readings):
    # Dead code path - never actually called
    return [r for r in readings if 0.7 < r < 0.95]

def calculate_entropy(readings):
    # Misleading complexity: entropy not used in final result
    import math
    entropy = 0
    for r in readings:
        if r > 0:
            entropy -= r * math.log(r)
    return entropy

def assess_critical_thresholds(readings):
    # Distractor function with decoy logic
    thresholds = [0.75, 0.80, 0.85, 0.90]
    breaches = 0
    for t in thresholds:
        for r in readings:
            if r > t:
                breaches += 1
    return breaches  # Computed but irrelevant

def aggregate_metrics(diagnostics, load_profile):
    base_score = diagnostics['stability']
    adjustment = 0
    
    # Real logic begins here
    if load_profile['peak'] > 0.9:
        adjustment -= 10
    if load_profile['variance'] < 0.05:
        adjustment += 5
    
    # Core computation
    raw_value = base_score + adjustment
    
    # Apply hidden correction based on initial sensor count
    sensor_count = len(load_profile['raw'])
    if sensor_count == 5:
        raw_value += 3  # Hidden dependency
    
    return int(raw_value * 2)  # Final transformation

# Main execution flow
if __name__ == "__main__":
    # Primary data collection
    raw_sensor_data = collect_sensor_data()
    
    # Compute baseline metric (used later)
    power_baseline = compute_baseline(raw_sensor_data)
    
    # Normalize for proportional analysis (used)
    normalized = normalize_readings(raw_sensor_data)
    
    # Evaluate system stability (used in final)
    stability_index = evaluate_stability_index(normalized)
    
    # Generate all possible combinations (RED HERRING)
    all_combinations = generate_combinations(raw_sensor_data)
    combination_count = len(all_combinations)  # Distractor variable
    
    # Calculate entropy (DECOY - looks important)
    signal_entropy = calculate_entropy(normalized)
    
    # Assess threshold breaches (DECOY metric)
    breach_count = assess_critical_thresholds(raw_sensor_data)
    
    # Simulate system load profile
    system_load = {
        'raw': raw_sensor_data,
        'peak': max(raw_sensor_data),
        'variance': (max(raw_sensor_data) - min(raw_sensor_data)),
        'average': sum(raw_sensor_data) / len(raw_sensor_data)
    }
    
    # Prepare diagnostic summary (only stability used)
    diagnostics = {
        'stability': stability_index,
        'entropy': signal_entropy,
        'breaches': breach_count,
        'combinations': combination_count
    }
    
    # --- KEY STATEMENT ---
    final_diagnostic = aggregate_metrics(diagnostics, system_load)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")