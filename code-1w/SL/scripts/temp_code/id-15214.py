from itertools import compress, cycle

def analyze_sensor_data(temps, pressures):
    # Normalize sensor readings using baseline offset
    baseline_temp = 25.0
    baseline_pressure = 101.3
    normalized_temps = [t - baseline_temp for t in temps]
    normalized_pressures = [p - baseline_pressure for p in pressures]

    # Irrelevant transformation: frequency modulation simulation (dead computation)
    sample_rate = 44100
    time_steps = [i / sample_rate for i in range(len(temps))]
    modulated_freqs = [t * 100 * (p / 50) for t, p in zip(time_steps, normalized_pressures)]  # Not used later

    # Identify stable conditions: where temp variation is low and pressure is rising
    stability_mask = []
    for i in range(1, len(normalized_temps)):
        temp_stable = abs(normalized_temps[i] - normalized_temps[i-1]) < 1.5
        pressure_rising = normalized_pressures[i] > normalized_pressures[i-1]
        stability_mask.append(temp_stable and pressure_rising)
    stability_mask.append(False)  # Pad to match length

    # Extract segments under stable conditions
    stable_temps = list(compress(normalized_temps, stability_mask))
    stable_pressures = list(compress(normalized_pressures, stability_mask))

    # Secondary distractor: cyclic pattern matching with no impact
    pattern_wheels = cycle([1, -1, 0])
    wheel_values = [next(pattern_wheels) * tp for tp, _ in zip(stable_temps, range(len(stable_temps)))]  # Unused

    # Compute conditional yield index
    yield_index = 0
    for t, p in zip(stable_temps, stable_pressures):
        if t > 0:
            yield_multiplier = 1.8 if p > 0 else 1.2
            yield_index += t * p * yield_multiplier
        else:
            yield_index -= abs(t) * 0.5

    return max(yield_index, 0)

def calculate_optimal_yield(temp_data, pressure_data):
    # Filter out invalid sensor spikes (preprocessing)
    filtered_temps = [t for t in temp_data if 15 <= t <= 35]
    filtered_pressures = [p for p in pressure_data if 95 <= p <= 110]

    # Truncate to shortest length for pairing
    n = min(len(filtered_temps), len(filtered_pressures))
    trimmed_temps = filtered_temps[:n]
    trimmed_pressures = filtered_pressures[:n]

    # Distractor: simulate redundant checksum validation
    temp_checksum = sum(int(t * 10) % 7 for t in trimmed_temps)
    pressure_checksum = sum(int(p * 5) % 3 for p in trimmed_pressures)
    validity_flag = (temp_checksum + pressure_checksum) % 2 == 0  # Not actually affecting logic

    # Core analysis
    base_yield = analyze_sensor_data(trimmed_temps, trimmed_pressures)

    # Adjustment based on operational thresholds
    avg_temp = sum(trimmed_temps) / n if n > 0 else 25.0
    temp_deviation_penalty = 0.3 * abs(avg_temp - 26.5)

    final_yield = base_yield - temp_deviation_penalty
    final_yield = round(final_yield, 4)

    return final_yield

# Main execution
if __name__ == '__main__':
    temperature_readings = [26.1, 25.8, 27.3, 14.9, 26.9, 27.1, 26.0, 36.2, 25.7]
    pressure_logs = [102.1, 101.9, 102.4, 94.8, 103.2, 103.5, 102.8, 112.0, 102.0]
    
    # Key statement
    final_yield = calculate_optimal_yield(temperature_readings, pressure_logs)
    
    print(f"Target result: {final_yield}")