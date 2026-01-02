def analyze_process_efficiency():
    raw_data = [15, 25, 30, 45, 60, 80, 90, 100]
    thresholds = [20, 50, 75]
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)) * 100) for x in raw_data]
    
    # Semi-relevant preprocessing
    filtered_values = [x for x in raw_data if x > 25]
    temp_sum = sum([x ** 0.5 for x in filtered_values if x < 95])
    
    # Tracking state across iterations (relevant)
    cycle_count = 0
    total_output = 0
    spike_count = 0
    decay_factor = 1.0
    
    for i, value in enumerate(filtered_values):
        if i % 2 == 0:
            cycle_count += 1
            total_output += value // (i + 1)
        else:
            # Dead code path (misleading computation)
            adjustment = value * 0.1
            decay_factor *= 0.95

        # Check for spikes (irrelevant to final result)
        if value > 85:
            spike_count += 1

    # Core logic embedded among distractions
    baseline_reference = sum(thresholds) / len(thresholds)
    adjustment_offset = len(normalized) - len(raw_data)  # Always zero, but looks meaningful
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0
    
    # Final red herring: unused derived metric
    synthetic_index = efficiency_score * decay_factor + adjustment_offset
    
    print(f"Result: {efficiency_score}")

analyze_process_efficiency()