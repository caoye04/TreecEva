def analyze_system_equilibrium():
    raw_data = [18, 22, 35, 41, 29, 33, 37, 44]
    offset_key = 3
    
    # Preprocess: shift and filter relevant signals
    shifted_signals = [x - offset_key for x in raw_data if x > 25]
    
    # Irrelevant transformation (distractor)
    inverted_map = {i: val for i, val in enumerate([100 - x for x in shifted_signals])}
    temp_shadow = sum(inverted_map.values()) % 17  # Unused later
    
    # Core processing with conditional logic and counting
    cycle_count = 0
    cumulative_power = 0
    suppression_factor = 0
    
    for idx, signal in enumerate(shifted_signals):
        if idx % 2 == 0 and signal > 30:
            cumulative_power += signal ** 2
            cycle_count += 1
        elif signal < 35:
            cumulative_power += signal * 1.5
            suppression_factor += 5

    # Secondary loop with zip and enumerate (semi-relevant)
    audit_log = ['A', 'B', 'C', 'D']
    for i, (log, val) in enumerate(zip(audit_log, shifted_signals)):
        if i < len(shifted_signals) and val % 2 == 0:
            suppression_factor -= 1  # Minor adjustment

    # Red herring: string-based computation
    status_flag = "NORMAL" if cycle_count > 2 else "WARNING"
    diagnostic_hash = len(status_flag) * 113  # Not used
    
    # Final calculations with integer division
    baseline_reference = sum(shifted_signals) // len(shifted_signals)
    fluctuation_index = cumulative_power / (baseline_reference + 1)
    final_tally = int(fluctuation_index) + suppression_factor * 2
    
    # Key statement
    equilibrium_score = final_tally // (cycle_count + 1)
    
    print(f"Result: {equilibrium_score}")

analyze_system_equilibrium()