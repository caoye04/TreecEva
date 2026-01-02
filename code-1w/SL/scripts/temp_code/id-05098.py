def analyze_workload():
    # Simulate a distributed system workload analysis over time slots
    time_slots = [t for t in range(1, 13)]
    base_load = 45
    fluctuation = [2, -5, 3, 0, -1, 4, -3, 6, 1, -2, 0, 3]
    temperature_offset = 1.5  # Minor environmental factor

    # Irrelevant sensor calibration (distractor)
    calibration_factor = 0.98
    sensor_noise = [0.1 * i for i in range(12)]
    adjusted_noise = [noise * calibration_factor for noise in sensor_noise]

    # Core logic: compute dynamic load including resource spikes
    dynamic_load = []
    spike_magnitude = []
    for i, slot in enumerate(time_slots):
        load = base_load + fluctuation[i]
        if slot % 4 == 0:
            spike = (slot // 4) * 8
            spike_magnitude.append(spike)
            load += spike
        else:
            spike_magnitude.append(0)
        
        # Conditional expression for efficiency decay
        decay = 0.99 if load > 60 else 1.0
        corrected_load = load * decay
        dynamic_load.append(int(corrected_load))

    # Secondary computation: average without peaks (semi-relevant)
    non_peak_avg = sum([x for x in dynamic_load if x < 70]) / len(dynamic_load)

    # Track state across phases (distraction with partial relevance)
    phase_status = {}
    for idx, val in enumerate(dynamic_load):
        phase = (idx // 3) + 1
        if phase not in phase_status:
            phase_status[phase] = []
        phase_status[phase].append(val)

    # Unnecessary aggregation (dead path)
    max_per_phase = []
    for p in sorted(phase_status.keys()):
        max_per_phase.append(max(phase_status[p]))

    # Actual usage levels depend on filtered and shifted data
    filtered_loads = dynamic_load[2:10]  # Middle segment of operation
    shift_compensation = sum(fluctuation[2:10]) * 0.1
    usage_levels = [lvl + int(shift_compensation) for lvl in filtered_loads]

    # Introduce zip and enumerate (required python features)
    timestamps = ["T%d" % t for t in time_slots[2:10]]
    log_entries = []
    for t, (ts, ul) in enumerate(zip(timestamps, usage_levels)):
        log_entries.append(f"{ts}: {ul} at index {t}")

    # Key statement
    peak_capacity = max(usage_levels)

    # Print result as required
    print(f"Result: {peak_capacity}")

    # Unused return (distractor)
    return {
        'status': 'analyzed',
        'nominal_average': non_peak_avg,
        'spike_history': spike_magnitude,
        'logs': log_entries
    }

# Execute function
analyze_workload()