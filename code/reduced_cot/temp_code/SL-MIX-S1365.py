zones_energy_data = {
    'ZONE_A': [120, 135, 125],
    'ZONE_B': [200, 210, 190],
    'ZONE_C': [80, 85, 75]
}

state_machine = {
    'LOW': lambda x: x * 0.8,
    'MED': lambda x: x * 1.0,
    'HIGH': lambda x: x * 1.2
}

current_state = 'MED'
final_efficiency_score = 0

for zone, values in zones_energy_data.items():
    avg_consumption = sum(values) / len(values)
    adjusted_avg = state_machine[current_state](avg_consumption) if avg_consumption > 100 else avg_consumption
    final_efficiency_score += int(adjusted_avg) if zone != 'ZONE_C' else int(adjusted_avg) * 2

final_efficiency_score = final_efficiency_score if final_efficiency_score > 300 else final_efficiency_score * 2
print(f'Result: {final_efficiency_score}')