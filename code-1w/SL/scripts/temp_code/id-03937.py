def analyze_system_performance(input_data):
    base_rating = 0
    efficiency_factor = 1.0
    transient_loads = []
    correction_offsets = [0.1, -0.05, 0.2, 0.0]
    
    for i, entry in enumerate(input_data):
        if i % 2 == 0:
            base_rating += entry['value'] ** 0.5
        else:
            offset_index = (i + 1) % len(correction_offsets)
            # Irrelevant adjustment to mislead
            temp_adjust = entry['value'] * correction_offsets[offset_index]
            transient_loads.append(temp_adjust)
    
    # Red herring: complex filtering that doesn't affect final result
    filtered_entries = [e for e in input_data if e['flag'] and e['value'] > 10]
    secondary_sum = sum(e['value'] for e in filtered_entries)

    scaling_weights = [0.8, 1.1, 0.9, 1.2]
    weighted_avg = sum(scaling_weights[i % len(scaling_weights)] * input_data[i]['value'] 
                        for i in range(len(input_data))) / len(input_data)
    
    # Actual key computation
    efficiency_factor = 0.75 + (len(filtered_entries) * 0.05)
    
    # Key assignment point
    thermal_capacity = base_rating * efficiency_factor
    
    # Distractor: unused derived metrics
    peak_stress = max(input_data, key=lambda x: x['value'])['value'] * 0.3
    normalized_score = (weighted_avg + base_rating) / (peak_stress + 1)
    
    return thermal_capacity

# Input preparation
sensor_readings = [
    {'value': 16, 'flag': True},
    {'value': 25, 'flag': False},
    {'value': 36, 'flag': True},
    {'value': 49, 'flag': True},
    {'value': 64, 'flag': False}
]

result = analyze_system_performance(sensor_readings)
print(f"Result: {result}")