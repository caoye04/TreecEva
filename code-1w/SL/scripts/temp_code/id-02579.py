def calculate_plant_efficiency(readings):
    base_efficiency = 0
    conversion_factor = 1.0
    thermal_loss = 0.0
    temp_history = []
    stability_score = 0
    
    for i, (temp, pressure) in enumerate(zip(readings[::2], readings[1::2])):
        if i % 3 == 0:
            adjustment = (temp / 100) ** 0.5
        else:
            adjustment = 1.0

        if temp > 200:
            status_flag = 'overheat'
            thermal_loss += 0.05
        elif temp < 100:
            status_flag = 'cold'
            thermal_loss += 0.02
        else:
            status_flag = 'stable'
            stability_score += 1

        temp_history.append(f'{temp}C-{status_flag}')

        if i == 3:
            buffer_value = sum(x for x in readings[:4] if x > 150)
            # Irrelevant aggregation, not used later

    # Misleading intermediate calculation
    avg_temp = sum(readings[::2]) / len(readings[::2])
    normalized_pressure = max(readings[1::2]) - min(readings[1::2])

    if stability_score >= 2:
        conversion_factor = 1.25
    else:
        conversion_factor = 0.85

    base_efficiency = 76
    # Key assignment point
    thermal_yield = base_efficiency * conversion_factor

    # Dead code path - never executed due to fixed input
    if False:
        fallback = {'yield': 0, 'risk': 'high'}
        thermal_yield = fallback['yield']

    print(f'Result: {thermal_yield}')

# Input data sequence
data_stream = [120, 85, 190, 92, 210, 88, 95, 94, 180, 90]
calculate_plant_efficiency(data_stream)