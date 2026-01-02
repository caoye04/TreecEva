def system_diagnostic(log_entries):
    base_load = 0
    peak_capacity = 0
    temp_buffer = []
    cumulative_stress = 0
    stress_factor = 1.7

    # Irrelevant tracking variables (distractors)
    debug_mode = False
    log_version = "2.1.5"
    deprecated_flag = False

    # Real processing begins
    for entry in log_entries:
        load = entry['load']
        timestamp = entry['ts']

        if load > 100:
            temp_buffer.append(load * 0.9)

        base_load += load

        # Nested condition with actual impact
        if load > 50:
            adjustment = 1 if load % 2 == 0 else -1
            cumulative_stress += stress_factor * adjustment

            # Secondary check that affects peak
            if load > peak_capacity:
                peak_capacity = load

    # Red herring computation (not used in final result)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    diagnostic_code = hash(tuple(temp_buffer)) % 100 if temp_buffer else -1

    # Critical use of enumerate and zip (required features)
    indices = list(enumerate([x for x in temp_buffer if x > 80]))
    paired_data = list(zip([base_load] * len(indices), [peak_capacity + i[0] for i in indices]))

    # Final adjustment logic (depends on prior state)
    for base, adjusted_peak in paired_data:
        if base > 300 and adjusted_peak > peak_capacity:
            peak_capacity += 1

    # Unused helper function (dead code path - distractor)
    def internal_audit():
        return sum(1 for x in log_entries if x['load'] < 10)

    # Key assignment statement
    final_analysis = {'capacity': peak_capacity, 'stress': cumulative_stress}

    # Print required output
    print(f"Result: {peak_capacity}")
    return final_analysis

# Input data
log_data = [
    {'ts': 1000, 'load': 45},
    {'ts': 1001, 'load': 120},
    {'ts': 1002, 'load': 67},
    {'ts': 1003, 'load': 150},
    {'ts': 1004, 'load': 55},
    {'ts': 1005, 'load': 130}
]

# Execute
result_obj = system_diagnostic(log_data)