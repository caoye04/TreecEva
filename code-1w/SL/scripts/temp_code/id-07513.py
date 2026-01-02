def analyze_system_performance(input_sequence, threshold_multiplier=0.85):
    # Simulate multi-stage industrial process with monitoring
    base_levels = [x * 1.7 for x in range(1, 12)]
    temp_buffer = []
    for idx, val in enumerate(base_levels):
        if idx % 3 == 0:
            temp_buffer.append(val * 0.92)
        else:
            temp_buffer.append(val * 1.03)

    # Irrelevant diagnostic check (dead code path)
    def internal_diagnostic():
        return sum(x for x in temp_buffer if x > 10) // len(temp_buffer)

    # Real processing begins here
    shifted_data = [int(x * threshold_multiplier) for x in temp_buffer]
    paired_readings = list(zip(shifted_data[:-1], shifted_data[1:]))
    
    # Misleading transformation (not used in final result)
    decoy_aggregate = 0
    for a, b in paired_readings:
        if a > b:
            decoy_aggregate += a ^ b
        else:
            decoy_aggregate -= a & b

    # Core logic hidden among distractions
    cycle_map = {}
    for i, val in enumerate(shifted_data):
        cycle_map[i] = val + (i % 4)

    # Another red herring: unused statistical smoothing
    smoothed = []
    window_size = 3
    for j in range(len(shifted_data)):
        start = max(0, j - window_size // 2)
        end = min(len(shifted_data), j + window_size // 2 + 1)
        avg = sum(shifted_data[start:end]) / (end - start)
        smoothed.append(round(avg, 2))

    # Actual signal extraction
    raw_cycles = [cycle_map[k] for k in sorted(cycle_map.keys()) if k % 2 == 1]
    
    # Decoy filtering (never applied)
    def strict_filter(data, limit=25):
        return [x for x in data if x < limit]

    # Critical operation embedded in noise
    outlier_mask = [x for x in raw_cycles if x % 2 == 0]
    filtered_cycles = [x for x in raw_cycles if x not in outlier_mask and x > 10]
    
    # THIS IS THE KEY STATEMENT
    filtration_yield = sum(filtered_cycles)
    
    # Print required at the end
    print(f"Result: {filtration_yield}")

    # Unused telemetry dump (distractor)
    telemetry_summary = {
        'peak': max(shifted_data),
        'baseline': sum(base_levels) // len(base_levels),
        'decoy': decoy_aggregate,
        'ignored': len(smoothed)
    }
    
    return filtration_yield

# Input has no effect due to self-contained logic
result = analyze_system_performance(list(range(15, 25)))