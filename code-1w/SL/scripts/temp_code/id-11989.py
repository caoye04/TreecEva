def analyze_sensor_noise(data):
    """Dummy function to simulate irrelevant analysis (dead-end)."""
    noise_level = 0
    for i in range(len(data)):
        if i % 3 == 0:
            noise_level += data[i] * 0.1
        elif i % 5 == 0:
            noise_level -= data[i] * 0.05
    return round(noise_level, 4)


def smooth_data(stream):
    """Another distraction: applies moving average but not used in final result."""
    smoothed = []
    window = 3
    for i in range(len(stream) - window + 1):
        smoothed.append(sum(stream[i:i+window]) / window)
    return smoothed


def calculate_optimal_yield(temps, pressures):
    # Core logic: correlate temperature and pressure readings across time
    if len(temps) != len(pressures):
        raise ValueError("Mismatched input sizes")
    
    # Track cumulative efficiency adjustments
    efficiency_log = []
    spike_count = 0
    base_yield = 100.0  # Base yield in units
    
    # Use enumerate and zip together (required python idiom)
    for idx, (t, p) in enumerate(zip(temps, pressures)):
        # Real logic step 1: temperature correction factor
        temp_factor = 1.0
        if t > 25:
            temp_factor = 0.8 + (t - 25) * 0.01  # Efficiency drops with heat
        elif t < 15:
            temp_factor = 0.9 + (15 - t) * 0.005

        # Real logic step 2: pressure adjustment
        press_factor = 1.0
        if p > 100:
            excess_ratio = p / 100.0
            press_factor = min(1.2, 1.0 + (excess_ratio - 1) * 0.3)
        elif p < 80:
            press_factor = 0.9

        # Real logic step 3: interaction effect
        interaction_boost = 1.0
        if t > 20 and t < 28 and p > 90 and p < 105:
            interaction_boost = 1.15  # Optimal zone
            spike_count += 1

        # Compute adjusted yield contribution
        step_yield = base_yield * temp_factor * press_factor * interaction_boost
        efficiency_log.append(step_yield)

    # Final yield is average of all step yields, adjusted by spike count
    avg_efficiency = sum(efficiency_log) / len(efficiency_log)
    final_adjustment = 1 + (spike_count * 0.02)  # Bonus for stable optimal zone hits
    return int(avg_efficiency * final_adjustment)

# Simulated sensor inputs (real data)
temperature_readings = [22, 26, 24, 18, 27, 23, 25, 20]
pressure_readings = [95, 105, 98, 75, 110, 92, 102, 88]

# Irrelevant preprocessing (distractor code)
noise_t = analyze_sensor_noise(temperature_readings)
noise_p = analyze_sensor_noise(pressure_readings)
smoothed_temps = smooth_data(temperature_readings)
smoothed_press = smooth_data(pressure_readings)

# Key statement that determines answer
final_yield = calculate_optimal_yield(temperature_readings, pressure_readings)

# Print result as required
print(f"Result: {final_yield}")