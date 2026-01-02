import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [2.1, -1.5, 4.3, 0.0, -3.2, 5.8, -2.9, 1.1]
    offset = 1.7
    adjusted = [x + offset for x in raw_readings]
    return adjusted

# Irrelevant auxiliary function (dead code path)
def calculate_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy

# Data transformation pipeline
def transform_signal(sequence):
    amplified = [x * 1.8 for x in sequence]
    filtered = [x for x in amplified if abs(x) > 1.5]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Threshold logic map (used later)
def generate_threshold_map(levels=4):
    base = 0.3
    growth = 1.25
    # Dead computation: unused list
    temp_debug = [base * (growth ** i) for i in range(10)]
    return {f'level_{i}': base * (growth ** i) for i in range(levels)}

# Core pattern analyzer
def matches_criteria(val, config):
    if val < config['level_0']:
        return 3
    elif val < config['level_1']:
        return 2
    elif val < config['level_2']:
        return 1
    else:
        return 0

# Misleading diagnostic (decoy)
def quick_diagnose(arr):
    total = sum([x**2 for x in arr if x < 0])
    score = total * 0.7
    return int(score)  # Unused result

# Main analysis engine
def analyze_pattern(dataset, thresholds):
    # Count how many values exceed each tier
    tier_counts = {k: 0 for k in thresholds}
    
    for value in dataset:
        for level in sorted(thresholds.keys()):
            if abs(value) >= thresholds[level]:
                tier_counts[level] += 1
    
    # Compute weighted impact score
    weights = {'level_0': 1, 'level_1': 2, 'level_2': 4, 'level_3': 8}
    raw_score = 0
    for k in tier_counts:
        raw_score += tier_counts[k] * weights[k]
    
    # Apply damping factor based on data sparsity
    non_zero_tiers = sum(1 for v in tier_counts.values() if v > 0)
    damping = 0.8 if non_zero_tiers < 3 else 1.0
    
    # Final adjustment using bit manipulation (relevance obfuscated)
    adjusted_score = int(raw_score * damping)
    flag_mask = 0b1111
    final_value = adjusted_score ^ (flag_mask & len(dataset))
    
    # Red herring: unused complex expression
    outlier_ratio = len([x for x in dataset if x > 0.7]) / len(dataset) if dataset else 0
    penalty = math.floor(outlier_ratio * 10) if outlier_ratio > 0.5 else 0
    
    return final_value

# Execution flow
if __name__ == '__main__':
    # Step 1: Collect and adjust raw data
    sensor_data = collect_sensor_readings()
    
    # Step 2: Transform signal through multiple stages
    transformed_data = transform_signal(sensor_data)
    
    # Step 3: Generate configuration map
    threshold_map = generate_threshold_map()
    
    # Step 4: Run decoy function (misleading intermediate result)
    fake_diagnostic = quick_diagnose(transformed_data)
    
    # Step 5: Perform actual analysis
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")