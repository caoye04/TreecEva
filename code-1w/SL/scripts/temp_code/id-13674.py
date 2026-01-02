def analyze_system_health():
    # Simulated sensor readings (irrelevant in part)
    temperature_readings = [23.5, 24.1, 22.9, 25.0, 26.3, 27.1, 25.8]
    voltage_levels = [3.3, 3.2, 3.4, 3.1, 3.0, 3.5, 3.6]
    cycle_counts = [1024, 2048, 4096, 8192, 16384, 32768, 65536]

    # Distractor: unused transformation
    normalized_cycles = [c / max(cycle_counts) for c in cycle_counts]
    adjusted_temps = [round(t - 273.15, 2) for t in [t_val + 273.15 for t_val in temperature_readings]]

    # Core data for computation
    signal_samples = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    fault_flags = {i: (v == 0) for i, v in enumerate(signal_samples)}

    # Misleading intermediate diagnostic (dead-end)
    preliminary_score = sum(1 for flag in fault_flags.values() if flag) * len(voltage_levels)

    # Critical sequence: bit manipulation and pattern detection
    shift_register = 0
    for bit in signal_samples:
        shift_register = (shift_register << 1) | bit
        if shift_register & 0b111 == 0b111:  # detect triple-1 pattern
            shift_register ^= 0b111  # clear last three bits

    # Data transformation using zip and enumerate (required python features)
    weighted_sum = 0
    for idx, (temp, volt) in enumerate(zip(temperature_readings, voltage_levels)):
        if idx % 2 == 1:  # only odd indices contribute
            weighted_sum += temp * volt * (idx + 1)

    # Secondary path: control flow with logical complexity
    thresholds = {"high_temp": 25.0, "low_volt": 3.2}
    breach_log = []
    for i, (t, v) in enumerate(zip(temperature_readings, voltage_levels)):
        temp_breach = t > thresholds["high_temp"]
        volt_breach = v < thresholds["low_volt"]
        if temp_breach and not volt_breach:
            breach_log.append((i, 'TEMP_ONLY'))
        elif not temp_breach and volt_breach:
            breach_log.append((i, 'VOLT_ONLY'))
        elif temp_breach and volt_breach:
            breach_log.append((i, 'BOTH'))

    # Distractor: complex but unused structure
    status_tree = {f"node_{i}": {"raw": cycle_counts[i], "flag": fault_flags[i]} 
                   for i in range(len(cycle_counts)) if cycle_counts[i] > 4096}

    # Key computational chain
    cumulative_shifts = 0
    temp_value = shift_register
    while temp_value:
        cumulative_shifts += temp_value & 1
        temp_value >>= 1

    # Conditional expression with fallback logic
    system_mode = 'STANDBY' if len(breach_log) < 3 else 'ACTIVE'
    recovery_offset = 5 if system_mode == 'ACTIVE' else 0

    # Primary metric calculation
    base_metric = weighted_sum / (len([v for v in signal_samples if v]) or 1)
    adjustment_factor = len(breach_log) - cumulative_shifts
    
    # Multiple assignment and tuple unpacking (required concept)
    primary_adjustment, secondary_adjustment = adjustment_factor, base_metric // 10
    
    # Construct time-series-like diagnostics
    aggregate_metrics = []
    for step in range(3):
        value = (base_metric + step * primary_adjustment - secondary_adjustment) // (step + 1)
        aggregate_metrics.append(int(value))

    # Final system state with red herring keys
    system_state = {
        "status": system_mode,
        "last_cycle": cycle_counts[-1],
        "recovery_offset": recovery_offset,
        "debug_flag": shift_register > 10,
        "unused_metric": sum(normalized_cycles),  # irrelevant
        "timestamp": 1699999999
    }

    # KEY STATEMENT
    final_diagnostic = aggregate_metrics[-1] + system_state.get("recovery_offset", 0)

    # Output result
    print(f"Result: {final_diagnostic}")

analyze_system_health()