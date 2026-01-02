def calculate_thermal_output(segments):
    base_factor = 1.75
    adjustment = 0.92
    cumulative_stress = 0
    thermal_index = 0

    for segment in segments:
        intensity = segment['heat'] * base_factor
        duration = segment['time']
        stress_level = intensity * duration ** 0.5
        cumulative_stress += stress_level

        # Distractor: vibration analysis (not used in final result)
        vibration_freq = segment.get('vibration', 0)
        harmonic_load = vibration_freq * 0.34
        efficiency_drop = harmonic_load / (1 + harmonic_load) if harmonic_load > 0 else 0

        # Semi-relevant transformation
        if stress_level > 25:
            thermal_index += intensity * adjustment
        else:
            thermal_index += intensity * 0.7

    # Additional distractor variables
    safety_margin = 1.2
    peak_load = max([s['heat'] * s['time'] for s in segments])
    normalized_peak = round(peak_load / 10) * 10  # Unused in logic

    # Final calculation with slicing influence from history
    historical_readings = [23.1, 24.5, 25.3, 26.8, 27.0, 28.2, 29.1, 30.0]
    recent_trend = historical_readings[-len(segments):]  # slice matching segment count
    trend_correction = sum(recent_trend) / len(recent_trend) if recent_trend else 0

    # Actual output formula
    raw_output = cumulative_stress * (1 + trend_correction / 100)
    return int(raw_output)

# Simulated process data
process_segments = [
    {'heat': 12, 'time': 9, 'vibration': 4},
    {'heat': 15, 'time': 6, 'vibration': 6},
    {'heat': 18, 'time': 4, 'vibration': 5}
]

# State-tracking variables (some irrelevant)
status_log = []
consistency_check = True
system_diagnostics = {"temp_stable": True, "flow_rate": 87.4}

# Key computation
thermal_capacity = calculate_thermal_output(process_segments)

# Dictionary operations for logging (distractor)
log_entry = {
    "timestamp": "2023-11-15T14:02:00",
    "capacity_snapshot": thermal_capacity,
    "segments_processed": len(process_segments),
    "diagnostics": system_diagnostics
}
status_log.append(log_entry)

# Output result as required
print(f"Result: {thermal_capacity}")