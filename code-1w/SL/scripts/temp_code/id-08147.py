def calculate_performance(base, data):
    adjustment_factor = 1.2
    penalty_rate = 0.1
    bonus_threshold = base * 0.75
    scaling_factor = 0.01
    
    # Irrelevant transformation (distractor)
    normalized = [max(0, min(x, 100)) for x in data]
    
    # Secondary processing with red herring variables
    filtered = []
    outlier_count = 0
    for val in data:
        if val < 5 or val > 95:
            outlier_count += 1
            continue
        filtered.append(val)
    
    # Distractor: unused statistical calculation
    mean_filtered = sum(filtered) / len(filtered) if filtered else 0
    variance_proxy = sum((x - mean_filtered) ** 2 for x in filtered) / len(filtered) if filtered else 0
    
    # Core logic begins here
    valid_contributions = 0
    total_deviation = 0.0
    for reading in data:
        deviation = abs(reading - base)
        if deviation <= bonus_threshold:
            # Qualify for inclusion
            scaled_contribution = (base / (1 + deviation * scaling_factor))
            valid_contributions += 1
        else:
            scaled_contribution = base * 0.5
        
        # Accumulate only if within system bounds
        if reading >= 10:
            total_deviation += scaled_contribution

    # Additional distraction: entropy-like computation (unused)
    import math
    entropy = 0
    for x in data:
        px = (x + 1) / sum([y + 1 for y in data])
        entropy -= px * math.log(px)

    # Conditional expression used meaningfully
    performance_multiplier = 1.5 if valid_contributions >= len(data) * 0.6 else 0.8

    # Final score calculation – critical path
    raw_score = total_deviation * performance_multiplier
    final_score = int(raw_score + 0.5)  # Round to nearest integer

    return final_score

# Setup input
baseline = 42
readings = [38, 45, 40, 50, 32, 44, 39, 41]

# Execute
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")