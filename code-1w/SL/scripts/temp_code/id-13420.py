def analyze_faults(nodes, log):
    base_threshold = 7
    adjustment_factor = 0.85
    transient_mask = 3
    cumulative_score = 0
    
    # Irrelevant preprocessing (distractor)
    normalized_log = [entry % 97 for entry in log if entry > 0]
    filtered_nodes = {x for x in nodes if x % 2 == 1}  # Only odd nodes considered
    
    # Secondary analysis with dead-end computation
    potential_risk = sum(1 for x in normalized_log if x in [12, 24, 48])
    risk_penalty = potential_risk * 2 if potential_risk > 5 else 0  # Not actually used
    
    # Core logic with set operations and bitwise interference
    fault_signatures = set()
    for node in nodes:
        if node < 10:  # Early skip condition
            continue
        temp_val = node ^ 5  # XOR transformation
        if temp_val in log:
            fault_signatures.add(temp_val)
    
    # Additional distraction: unused state tracking
    state_history = []
    for i in range(min(len(log), 5)):
        shifted = log[i] >> 2
        state_history.append(shifted * 3)  # Computation not used later
    
    # Main accumulation with conditional logic
    for sig in fault_signatures:
        if sig % 4 == 0:
            cumulative_score += sig // 4
        else:
            cumulative_score += sig % 7
    
    # Final adjustment using threshold and factor
    final_diagnostic = cumulative_score * adjustment_factor + base_threshold
    
    # Dead code path (misleading control flow)
    if final_diagnostic < 0:
        final_diagnostic = 0  # Never reached due to positive components
    
    return int(final_diagnostic)

# Input data
detected_nodes = [12, 15, 18, 21, 24, 27]
system_log = [10, 13, 17, 25, 29, 31, 9, 7, 14]

# Execution point
final_diagnostic = analyze_faults(detected_nodes, system_log)
print(f"Result: {final_diagnostic}")