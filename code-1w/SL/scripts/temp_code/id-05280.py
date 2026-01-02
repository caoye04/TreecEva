from itertools import compress, count

def analyze_growth_cycle(data, threshold=0.75):
    growth_stages = [d['stage'] for d in data]
    maturity_mask = [d['maturity'] >= threshold for d in data]
    filtered_stages = list(compress(growth_stages, maturity_mask))
    return sum(filtered_stages) / len(filtered_stages) if filtered_stages else 0

def calculate_harvest_efficiency(plots, sensors):
    sensor_data = []
    for p_idx, plot in enumerate(plots):
        for s_idx, sensor in enumerate(sensors[p_idx]):
            reading = (plot['soil_quality'] + sensor['moisture']) * sensor['calibration_factor']
            adjusted_reading = reading * (0.9 + (sensor['age'] * 0.01))
            sensor_data.append({'reading': reading, 'adjusted': adjusted_reading})
    
    # Irrelevant aggregation (distractor)
    total_raw = sum(sd['reading'] for sd in sensor_data)
    avg_adjusted = sum(sd['adjusted'] for sd in sensor_data) / len(sensor_data)
    
    # Key computation path
    efficiency_scores = []
    for i, (plot, s_list) in enumerate(zip(plots, sensors)):
        base_yield = plot['base_yield']
        soil_factor = plot['soil_quality'] / 10.0
        
        # Simulate conditional sensor contribution
        valid_sensors = [s for s in s_list if s['status'] == 'active']
        if not valid_sensors:
            efficiency_scores.append(base_yield * 0.5)
            continue
        
        moisture_avg = sum(s['moisture'] for s in valid_sensors) / len(valid_sensors)
        stability_score = sum(1 for s in valid_sensors if s['fluctuation'] < 0.3)
        
        # Core formula
        yield_potential = base_yield * (1 + moisture_avg / 100) * soil_factor
        yield_potential *= (1 + stability_score * 0.1)
        efficiency_scores.append(yield_potential)
    
    # Misleading intermediate (not used in final result)
    dummy_shift = sum(enumerate(count(1, 0.1))) % 5
    
    # Final result
    final_yield = int(sum(efficiency_scores))
    return final_yield

# Setup realistic input data
plots = [
    {'base_yield': 120, 'soil_quality': 8.2},
    {'base_yield': 95, 'soil_quality': 7.4},
    {'base_yield': 110, 'soil_quality': 9.0}
]

sensors = [
    [
        {'moisture': 65, 'calibration_factor': 1.05, 'age': 2, 'status': 'active', 'fluctuation': 0.25},
        {'moisture': 70, 'calibration_factor': 0.98, 'age': 4, 'status': 'active', 'fluctuation': 0.35},
        {'moisture': 60, 'calibration_factor': 1.02, 'age': 1, 'status': 'inactive', 'fluctuation': 0.15}
    ],
    [
        {'moisture': 50, 'calibration_factor': 1.10, 'age': 3, 'status': 'active', 'fluctuation': 0.20},
        {'moisture': 55, 'calibration_factor': 0.95, 'age': 5, 'status': 'active', 'fluctuation': 0.28}
    ],
    [
        {'moisture': 80, 'calibration_factor': 1.00, 'age': 1, 'status': 'active', 'fluctuation': 0.10},
        {'moisture': 75, 'calibration_factor': 1.08, 'age': 2, 'status': 'active', 'fluctuation': 0.12},
        {'moisture': 72, 'calibration_factor': 1.01, 'age': 6, 'status': 'active', 'fluctuation': 0.32}
    ]
]

# Execute main logic
growth_data = [{'stage': i*2+3, 'maturity': 0.6+i*0.1} for i in range(5)]
analyze_growth_cycle(growth_data)

final_yield = calculate_harvest_efficiency(plots, sensors)
print(f"Target result: {final_yield}")