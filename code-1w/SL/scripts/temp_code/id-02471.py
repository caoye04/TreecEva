import itertools

# Simulated sensor fusion module for aerospace telemetry
# Processes time-series data with diagnostic flags and noise filtering

def process_telemetry_stream(raw_readings, calibration_factor):
    timing_log = []
    temp_buffer = []
    checksum = 0
    accumulator = 0
    spike_count = 0
    baseline_shift = 0.0

    # Irrelevant pre-scan: energy consumption simulation (dead code path)
    energy_profile = [x * 0.05 for x in range(100)]
    total_energy = sum(energy_profile)
    efficiency_ratio = total_energy / 99 if total_energy > 1 else 0

    # Real processing loop
    for i, reading in enumerate(raw_readings):
        adjusted = reading * calibration_factor + 2.5
        
        # Noise detection heuristic
        if abs(adjusted - accumulator) > 15 and i > 0:
            spike_count += 1
            adjusted = accumulator  # Suppress spike
        
        accumulator = (accumulator * 0.7) + (adjusted * 0.3)
        temp_buffer.append(adjusted)
        
        if i % 7 == 0:
            timing_log.append((i, accumulator, spike_count))

        # Distractor: unused physics model
        velocity = i * 0.3 + 2.1
        drag_force = velocity ** 2 * 0.08
        # End of irrelevant block

        checksum ^= int(adjusted) & 0xFF

    # Decoy function call (no side effects)
    def simulate_failure_modes():
        return [False] * 12
    
    failure_states = simulate_failure_modes()

    # Critical data transformation using lambda and itertools
    filtered_entries = list(itertools.filterfalse(lambda x: x[2] > 5, timing_log))
    
    # Baseline correction based on trend
    if len(temp_buffer) > 10:
        recent_avg = sum(temp_buffer[-10:]) / 10
        historical_avg = sum(temp_buffer[:10]) / 10
        baseline_shift = recent_avg - historical_avg

    # System flags generated from internal state
    system_flags = {
        'spike_threshold_exceeded': spike_count > 3,
        'stable_calibration': abs(baseline_shift) < 5.0,
        'checksum_valid': (checksum & 0xF) == 0x7,
        'data_density': len(timing_log) > 8
    }

    # Red herring: unused signal reconstruction
    reconstructed = []
    for t in timing_log:
        sample = t[1] + (t[0] * 0.01)
        if sample > 40:
            sample -= baseline_shift
        reconstructed.append(sample)

    # Aggregation logic (key statement)
    def aggregate_metrics(log_data, flags):
        metric = 0
        for entry in log_data:
            index, value, spikes = entry
            if index % 2 == 0:
                metric += int(value) * 3
            else:
                metric -= int(value) // 2
        
        # Flag-based adjustments
        if flags['spike_threshold_exceeded']:
            metric += 100
        if not flags['stable_calibration']:
            metric -= 50
        if flags['checksum_valid']:
            metric += 25
        if flags['data_density']:
            metric += 75
            
        # Final adjustment based on accumulated logic
        final_adjustment = len(log_data) - len(filtered_entries)
        metric += final_adjustment * 15
        
        return metric + 1  # Off-by-one to test reasoning precision

    # Execute critical statement
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    
    # Unused post-processing distraction
    report_summary = []
    for i in range(3):
        dummy_calc = (final_diagnostic ^ i) * 0.95
        report_summary.append(round(dummy_calc, 2))
    
    # Output target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data - deterministic sensor readings
readings = [12, 15, 14, 18, 22, 19, 25, 28, 26, 30, 33, 31, 35, 38]
calibration = 1.8

# Run simulation
process_telemetry_stream(readings, calibration)