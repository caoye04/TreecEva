def evaluate_performance(output, risk_profile):
    base_score = 0
    penalty = 0
    
    # Distractor: Irrelevant calculation for legacy system compatibility
    legacy_adjustment = (len(risk_profile) * 2) % 7 if risk_profile else 0
    temp_offset = sum([x % 3 for x in output]) // 2
    
    # Real logic begins: assess productivity quartiles
    threshold = sum(output) / len(output) if output else 0
    high_performers = [x for x in output if x > threshold]
    low_performers = [x for x in output if x <= threshold]
    
    # Use set operations to identify outlier risks in high-output group
    high_ids = set(range(len(output)))
    risky_indices = {i for i, val in enumerate(output) if val in risk_profile}
    volatile_high = high_ids.intersection(risky_indices).intersection(set([i for i, x in enumerate(output) if x in high_performers]))
    
    # Conditional expression for score boost
    boost = 1.5 if len(volatile_high) < 3 else 0.8
    
    # Core scoring logic
    base_score += len(high_performers) * 10
    base_score -= len(low_performers) * 3
    
    # Risk penalties
    for idx in risky_indices:
        if idx < len(output) and output[idx] > threshold:
            penalty += 5

    # Distractor: unused dead-end path
    debug_mode = False
    if debug_mode:
        print(f"Debug: {legacy_adjustment}, {temp_offset}")
    
    final = base_score - penalty
    final = int(final * boost)  # Apply conditional boost
    return final

# Main execution
productivity = [85, 90, 78, 92, 67, 76, 99, 88]
risk_set = {78, 99, 55, 43}

# Auxiliary distractor variables
aux_data = [x**2 for x in productivity if x < 80]
shadow_copy = productivity.copy()
processed = False
for i in range(len(shadow_copy)):
    if shadow_copy[i] > 90:
        processed = True
        shadow_copy[i] //= 2  # Not used later

interim_value = sum(aux_data) // 4 if aux_data else 0  # Semi-relevant but not critical

# Key statement
final_score = evaluate_performance(productivity, risk_set)

print(f"Result: {final_score}")