def calculate_thermal_properties(efficiencies):
    base_factor = 0.87
    adjustment = 1.03
    cumulative_stress = 0
    thermal_capacity = 0

    # Irrelevant stress accumulation (distractor)
    for cycle in range(3):
        for phase in range(2):
            cumulative_stress += (cycle + 1) * (phase + 0.5) * 0.1

    # Real computation path
    efficiency_values = list(efficiencies.values())
    normalized = [val * base_factor for val in efficiency_values if val > 0.7]  # List comprehension

    # Additional distraction: unused transformation
    inverted_map = {k: 1/v for k, v in efficiencies.items()}
    avg_inverted = sum(inverted_map.values()) / len(inverted_map)

    # Actual logic contributing to answer
    peak_efficiency = max(normalized)
    stability_score = len(normalized)  # Related but indirect

    # Final calculation
    thermal_capacity = (peak_efficiency * adjustment) + (stability_score * 0.25)

    return thermal_capacity

# Simulate sensor efficiency readings over time
sensor_readings = {
    'sensor_a': 0.92,
    'sensor_b': 0.65,  # Below threshold, filtered out
    'sensor_c': 0.88,
    'sensor_d': 0.95,
    'sensor_e': 0.73
}

# Misleading pre-processing (dead code path)
def analyze_redundancy(data):
    redundant_count = 0
    for key, value in data.items():
        if 'b' in key or value < 0.7:
            redundant_count += 1
    return redundant_count

# Unused but plausible helper
redundant_sensors = analyze_redundancy(sensor_readings)

# Core execution point
thermal_capacity = calculate_thermal_properties(sensor_readings)
print(f"Result: {thermal_capacity}")