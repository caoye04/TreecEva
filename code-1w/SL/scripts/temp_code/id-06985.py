def analyze_crop_health(sensor_readings):
    healthy_count = 0
    stress_threshold = 0.75
    temp_log = []

    for reading in sensor_readings:
        normalized = reading / 100.0
        if normalized > stress_threshold:
            healthy_count += 1
        temp_log.append(f'Value:{normalized:.3f}')

    summary_str = ''.join(temp_log)
    is_stable = summary_str.count('0.8') > 2
    return healthy_count, is_stable


def calculate_growth_potential(temperature_seq, moisture_level):
    base_potential = 1.0
    fluctuation_penalty = 0.05
    stability_score = 0

    for i in range(1, len(temperature_seq)):
        diff = abs(temperature_seq[i] - temperature_seq[i-1])
        if diff > 3:
            base_potential -= fluctuation_penalty

    # Distractor: unused computation
    peak_moisture = max(moisture_level) if moisture_level else 0
    avg_moisture = sum(moisture_level) / len(moisture_level) if moisture_level else 0

    for m in moisture_level:
        if 40 < m < 60:
            stability_score += 1

    adjusted_potential = base_potential + (stability_score * 0.02)
    return min(adjusted_potential, 1.2)


def calculate_harvest_efficiency(fields):
    total_efficiency = 0.0
    efficiency_list = []
    buffer_zone = []  # Unused tracking variable (distractor)

    for field in fields:
        crop_data = field['crops']
        env_data = field['environment']

        health_count, is_consistent = analyze_crop_health(crop_data)
        growth_model = calculate_growth_potential(env_data['temps'], env_data['moisture'])

        # Real logic path
        base_efficiency = health_count * growth_model
        
        # String distractor
        field_name = field['name']
        code_suffix = field_name[-3:] if len(field_name) > 2 else field_name
        checksum = sum(ord(c) for c in code_suffix) % 5

        # Actual adjustment
        if is_consistent and checksum == 0:
            base_efficiency *= 1.15

        efficiency_list.append(base_efficiency)

        # Dead code branch (distractor)
        if len(buffer_zone) > 100:
            buffer_zone.clear()

    # Final aggregation
    total_efficiency = sum(efficiency_list)
    final_yield = int(total_efficiency * 100) // len(fields) if fields else 0
    
    # Critical output
    print(f'Result: {final_yield}')
    return final_yield

# Input data setup
field_data = [
    {
        'name': 'AlphaPlot_01',
        'crops': [82, 88, 90, 76, 85],
        'environment': {
            'temps': [22, 23, 26, 28, 27],
            'moisture': [55, 58, 52, 48]
        }
    },
    {
        'name': 'BetaRidge_XYZ',
        'crops': [91, 87, 93, 89, 85],
        'environment': {
            'temps': [20, 21, 20, 23, 25],
            'moisture': [60, 56, 53, 59]
        }
    },
    {
        'name': 'GammaValley_88',
        'crops': [76, 79, 81, 77, 80],
        'environment': {
            'temps': [18, 19, 21, 24, 26],
            'moisture': [45, 47, 43, 46]
        }
    }
]

# Execution point
final_yield = calculate_harvest_efficiency(field_data)