def analyze_production_cycle(units_produced, downtime_hours):
    peak_capacity = 150
    base_efficiency = 0.85
    total_output = 0
    time_elapsed = len(units_produced) + sum(downtime_hours)
    fluctuation_index = 0
    adjustment_factor = 0.0

    for i, units in enumerate(units_produced):
        if units > peak_capacity:
            overload_penalty = (units - peak_capacity) * 0.1
            adjusted_units = units - overload_penalty
        else:
            adjusted_units = units

        # Irrelevant fluctuation tracking
        if i % 3 == 0:
            fluctuation_index += 1
        elif i % 5 == 0:
            fluctuation_index -= 1

        total_output += adjusted_units

        # Dead code branch - never reached due to logic
        if total_output < 0:
            total_output = 0

    # Dummy sorting with no impact
    sorted_downtime = sorted(downtime_hours, reverse=True)
    avg_downtime = sum(sorted_downtime) / len(sorted_downtime) if sorted_downtime else 0

    # Red herring calculation
    theoretical_max = peak_capacity * len(units_produced)
    utilization_rate = total_output / theoretical_max if theoretical_max > 0 else 0

    # Key statement
    efficiency_score = total_output / (time_elapsed + 1)

    # Unrelated character counting from a label
    status_label = "ProductionCycleComplete"
    vowel_count = sum(1 for c in status_label.lower() if c in 'aeiou')

    # Another irrelevant zip usage
    offsets = [x - avg_downtime for x in sorted_downtime]
    for idx, (off, orig) in enumerate(zip(offsets, sorted_downtime)):
        adjustment_factor += abs(off) / (idx + 1) if idx < 4 else 0

    return efficiency_score

# Input data
production_log = [120, 140, 160, 130, 155]
downtime_schedule = [2, 1, 3, 0, 1]

result = analyze_production_cycle(production_log, downtime_schedule)
print(f"Result: {result}")