import itertools

# Simulate multi-stage industrial filtration process with diagnostic telemetry
def run_filtration_sequence(cycle_data, threshold, mode='standard'):
    cumulative_load = 0
    transient_buffer = []
    diagnostic_trace = []
    cycle_phases = []

    for i, reading in enumerate(cycle_data):
        # Irrelevant telemetry logging (distractor)
        if i % 5 == 0:
            diagnostic_trace.append(f"LOG: Cycle {i} initiated")

        # Real computation: pressure adjustment
        adjusted_pressure = (reading * 1.8) + 32  
        phase_flag = 'A' if adjusted_pressure > threshold * 1.2 else 'B'
        cycle_phases.append(phase_flag)

        # Core transformation: nonlinear load accumulation
        if reading > 0:
            cumulative_load += int(pow(reading, 1.5))

        # Dead code path - never executed due to logic above (red herring)
        if mode == 'debug' and reading < 0:
            transient_buffer.extend([reading] * 3)

    # Secondary irrelevant processing: generate phase transitions (misleading)
    phase_transitions = 0
    for j in range(1, len(cycle_phases)):
        if cycle_phases[j] != cycle_phases[j-1]:
            phase_transitions += 1

    # Decoy result - looks important but unused
    efficiency_metric = cumulative_load / (len(diagnostic_trace) or 1)

    # Actual signal extraction: isolate high-frequency oscillations
    oscillation_pattern = [abs(cycle_data[k] - cycle_data[k-1]) for k in range(1, len(cycle_data))]
    significant_swings = list(filter(lambda x: x > threshold * 0.3, oscillation_pattern))

    # Generate combinatorial cycle duplicates (itertools usage)
    augmented_cycles = list(itertools.chain.from_iterable(
        itertools.repeat(x, 2) for x in significant_swings
    ))

    # Filter cycles based on dynamic criteria (key step)
    filtered_cycles = []
    for val in augmented_cycles:
        temp_val = val * 1.7
        if temp_val.is_integer() and temp_val % 2 == 0:
            filtered_cycles.append(int(temp_val))
        elif val > 4:  # This branch actually captures most values
            filtered_cycles.append(int(temp_val) - 3)

    # Critical assignment point
    filtration_yield = sum(filtered_cycles)

    # Unrelated post-processing (distractor)
    compression_ratio = len(cycle_data) / (len(filtered_cycles) or 1)
    status_flags = [1 if x > 10 else 0 for x in filtered_cycles]
    final_diagnostic = sum(status_flags) > len(status_flags) // 2

    return {
        'yield': filtration_yield,
        'phases': phase_transitions,
        'efficiency': efficiency_metric,
        'diagnostics': final_diagnostic
    }


# Sensor input from industrial equipment (realistic domain context)
sensor_readings = [3, 7, 2, 8, 5, 1, 9, 4]
operation_threshold = 6

# Run full simulation
results = run_filtration_sequence(sensor_readings, operation_threshold)

# Extract target variable
filtration_yield = results['yield']

# Print result as required
print(f"Result: {filtration_yield}")