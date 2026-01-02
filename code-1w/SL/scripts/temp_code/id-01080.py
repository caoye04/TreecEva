def analyze_system_load(base_load, threshold, efficiency_factor):
    temp_adjustment = 0
    peak_moment = False
    historical_data = [base_load * (1.1 ** i) for i in range(5)]
    adjusted_loads = []

    for load in historical_data:
        if load > threshold:
            temp_adjustment += 1
            if not peak_moment:
                peak_moment = True
                critical_index = historical_data.index(load)
        adjusted_value = load * efficiency_factor
        adjusted_loads.append(round(adjusted_value, 2))

    # Misleading computation - looks important but unused
    predicted_failure_rate = (temp_adjustment / len(historical_data)) ** 2
    safety_margin = 1.0 - (sum(adjusted_loads) / (threshold * 5))

    performance_vector = [val for val in adjusted_loads if val < threshold]
    compression_ratio = len(performance_vector) / len(historical_data) if historical_data else 0

    # Simulate resource reallocation based on XOR pattern
    allocation_key = len(adjusted_loads) ^ temp_adjustment
    if allocation_key & 1:
        allocation_key += 2

    # Core logic disguised among distractions
    base_metric = sum(performance_vector)
    bonus_factor = 1 + (compression_ratio if compression_ratio > 0.6 else 0.5)
    stability_bonus = 10 if not peak_moment else (5 if safety_margin > 0 else 0)

    # Actual answer computation
    final_score = int(base_metric * bonus_factor) + stability_bonus

    # Red herring: complex dictionary operations that don't affect result
    diagnostics = {
        'load_profile': {f'entry_{i}': v for i, v in enumerate(historical_data)},
        'adjustments': set([int(x) for x in adjusted_loads]),
        'flags': {"peak": peak_moment, "stable": safety_margin > 0.1},
        'checksum': sum(historical_data[:3]) // 3
    }
    
    # Another distraction: unused conditional expression
    fallback_mode = 'active' if diagnostics['checksum'] > (base_load * 1.2) else 'inactive'
    
    # Final output
    print(f"Result: {final_score}")
    return final_score

# Entry point with realistic parameters
result = analyze_system_load(base_load=42, threshold=60, efficiency_factor=0.93)