from itertools import combinations

def analyze_readings(readings):
    filtered = [r for r in readings if r > 25]
    pairs = list(combinations(filtered, 2))
    diffs = [abs(a - b) for a, b in pairs]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    return avg_diff

def calculate_efficiency(energy_map, limit):
    total_input = sum(energy_map.values())
    total_output = 0
    waste_log = []
    efficiency_factors = []

    for key, value in energy_map.items():
        if 'core' in key:
            adjusted = value * 0.87
        elif 'aux' in key:
            adjusted = value * 0.76
        else:
            adjusted = value * 0.91
        
        temp_cap = value * 0.05
        capped_value = min(adjusted, value - temp_cap)
        total_output += capped_value
        
        # Irrelevant tracking (distractor)
        if adjusted > limit:
            waste_log.append(adjusted - limit)
        
        efficiency_factors.append(capped_value / value)

    # Real computation
    base_efficiency = total_output / total_input
    penalty = len([w for w in waste_log if w > limit * 0.1]) * 0.01
    thermal_efficiency = base_efficiency - penalty
    
    # Dead code path (distractor)
    if len(efficiency_factors) == 0:
        fallback = sum(efficiency_factors) / len(efficiency_factors)
        thermal_efficiency = max(thermal_efficiency, fallback)

    return round(thermal_efficiency, 4)

# Main execution
sensor_data = [23, 27, 30, 45, 29, 26]
noise_floor = 22
anomaly_score = analyze_readings(sensor_data)

energy_map = {
    'core_alpha': 120.0,
    'core_beta': 110.0,
    'aux_power_1': 45.0,
    'aux_power_2': 38.0,
    'backup_unit': 30.0
}

threshold = 100.0

# Simulate intermediate checks (irrelevant to final result)
diagnostic_codes = ['OK', 'CHKD', 'NORM']
system_status = diagnostic_codes[len(diagnostic_codes) // 2]

baseline_avg = sum(sensor_data) / len(sensor_data)
variance = sum((x - baseline_avg) ** 2 for x in sensor_data) / len(sensor_data)
std_deviation = variance ** 0.5

# Key computation step
thermal_efficiency = calculate_efficiency(energy_map, threshold)

# Print final answer as required
print(f"Result: {thermal_efficiency}")