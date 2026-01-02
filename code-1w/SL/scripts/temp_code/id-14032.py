def analyze_production_cycle(yield_data, thresholds):
    total_output = 0
    rejected_units = 0
    cycle_count = len(yield_data)
    peak_capacity = max(yield_data) if yield_data else 0
    efficiency_history = []

    adjustment_factor = 0.85
    baseline_target = sum(thresholds) / len(thresholds) if thresholds else 0
    temp_buffer = [x * adjustment_factor for x in yield_data]  # Distractor: not directly used

    for i, output in enumerate(yield_data):
        if output < thresholds[i % len(thresholds)]:
            rejected_units += 1
        else:
            total_output += output

        if (i + 1) % 3 == 0:
            recent_efficiency = total_output / (i + 1)
            efficiency_history.append(round(recent_efficiency, 2))

    # Misleading intermediate calculation
    avg_rejection_rate = rejected_units / cycle_count if cycle_count > 0 else 0
    projected_loss = avg_rejection_rate * peak_capacity * 2  # Dead computation

    # Key statement
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0

    # Additional red herring: string manipulation unrelated to result
    status_flag = ''.join([chr(ord('A') + min(int(eff), 25)) for eff in efficiency_history[-3:]]) if efficiency_history else 'N/A'

    # Output the target result
    print(f"Result: {efficiency_score}")
    return efficiency_score

# Input data
production_yields = [95, 87, 92, 88, 96, 76, 89]
quality_thresholds = [85, 90, 80, 88]

# Execute function
efficiency_score = analyze_production_cycle(production_yields, quality_thresholds)