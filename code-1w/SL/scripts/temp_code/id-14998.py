def analyze_growth_factors(conditions):
    base_rate = 1.0
    stress_modifier = 0.0
    temp_stress = 0
    humidity_factor = 0.0

    for temp, humidity in conditions:
        if temp > 30:
            temp_stress += 1
            stress_modifier -= 0.05
        elif temp < 15:
            temp_stress += 1
            stress_modifier -= 0.07

        adjusted_humidity = humidity / 100.0
        humidity_factor += adjusted_humidity

    normalized_stress = max(0.5, 1 + stress_modifier)
    return base_rate * normalized_stress, humidity_factor


def extract_critical_periods(logs):
    critical_phases = []
    for entry in logs:
        day, phase, metrics = entry
        if 'bloom' in phase.lower():
            critical_phases.append((day, metrics['temp'], metrics['humidity']))
    return critical_phases


def calculate_harvest_potential(environmental_record):
    # Misleading preprocessing
    summary_stats = {}
    total_entries = len(environmental_record.get('readings', []))
    avg_temp_offset = 0.0
    phantom_sum = 0

    for i in range(total_entries):
        reading = environmental_record['readings'][i]
        label = f"entry_{i}"
        if len(label) > 5:
            phantom_sum += i * 0.1  # Irrelevant accumulation

    # Actual logic begins
    growth_conditions = [(r['temp'], r['humidity']) for r in environmental_record['readings']]
    base_yield, total_humidity_influence = analyze_growth_factors(growth_conditions)

    log_history = environmental_record.get('phenology', [])
    bloom_periods = extract_critical_periods(log_history)
    
    # Secondary influence: number of bloom days
    bloom_boost = len(bloom_periods) * 0.02

    # Distractor: unused transformation
    transformed_data = {f'day_{i}': readings['temp'] ** 0.5 
                        for i, readings in enumerate(environmental_record['readings']) if readings['temp'] > 20}

    # Final calculation
    final_yield = int((base_yield + bloom_boost) * 1000 + total_humidity_influence * 10)
    
    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Simulated input data
climate_input = {
    'readings': [
        {'temp': 22, 'humidity': 60},
        {'temp': 33, 'humidity': 45},
        {'temp': 18, 'humidity': 70},
        {'temp': 12, 'humidity': 80},
        {'temp': 25, 'humidity': 55}
    ],
    'phenology': [
        (120, 'early_bloom', {'temp': 22, 'humidity': 60}),
        (125, 'peak bloom', {'temp': 24, 'humidity': 58}),
        (140, 'fruit set', {'temp': 26, 'humidity': 50})
    ]
}

final_yield = calculate_harvest_potential(climate_input)