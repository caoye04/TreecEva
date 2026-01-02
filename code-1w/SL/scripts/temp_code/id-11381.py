def analyze_system_efficiency(elements, threshold=0.75):
    efficiency_map = {}
    cumulative_weight = 0
    
    for idx, elem in enumerate(elements):
        weight = elem.get('mass') * elem.get('density')
        stress_factor = elem.get('stress') / (elem.get('resilience') or 1)
        efficiency = weight / (stress_factor + 1) if stress_factor > 0 else weight
        efficiency_map[idx] = efficiency
        cumulative_weight += weight

    normalized_efficiency = {k: v / cumulative_weight for k, v in efficiency_map.items()}
    return sum(v for v in normalized_efficiency.values() if v > threshold)


def calculate_thermal_capacity(profile, flux):
    base_integral = 0
    adjustment_factor = 0.0
    transient_peaks = []
    
    for reading in profile:
        adjusted_reading = reading * 0.95
        if adjusted_reading > 50:
            transient_peaks.append(adjusted_reading)
        base_integral += adjusted_reading ** 0.5

    if len(transient_peaks) > 2:
        adjustment_factor = sum(transient_peaks[:3]) / 3
    else:
        adjustment_factor = base_integral * 0.1

    # Irrelevant aggregation
    dummy_aggregate = 0
    for i in range(len(profile)):
        if i % 2 == 0:
            dummy_aggregate += flux[i] // 2

    capacity = base_integral + adjustment_factor

    # Misleading intermediate
    temp_correction = 0
    for f in flux:
        temp_correction += f ** 0.1
        if temp_correction > 10:
            break

    return int(capacity)

# Simulated sensor data
energy_profile = [45, 67, 89, 34, 78, 91]
temperature_flux = [3, 7, 12, 5, 9, 11]

# Dead computation - unrelated to final result
system_elements = [
    {'mass': 12, 'density': 8, 'stress': 40, 'resilience': 5},
    {'mass': 15, 'density': 6, 'stress': 60, 'resilience': 8},
    {'mass': 10, 'density': 9, 'stress': 35, 'resilience': 4}
]
efficiency_score = analyze_system_efficiency(system_elements)

# Key statement
thermal_capacity = calculate_thermal_capacity(energy_profile, temperature_flux)

# Irrelevant post-processing
final_diagnostic = efficiency_score * 0.5 if thermal_capacity > 30 else efficiency_score * 1.2

print(f"Result: {thermal_capacity}")