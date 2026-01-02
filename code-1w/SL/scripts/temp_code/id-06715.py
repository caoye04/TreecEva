def analyze_production_cycle(yield_log, cycle_metadata):
    total_batches = len(yield_log)
    cumulative_waste = 0
    batch_efficiencies = []
    temp_shadow = [0] * total_batches  # irrelevant tracking

    for i, (input_units, output_units) in enumerate(yield_log):
        waste = input_units - output_units
        cumulative_waste += waste
        if input_units > 0:
            efficiency = output_units / input_units
            batch_efficiencies.append(efficiency)
        else:
            batch_efficiencies.append(0)
        
        # Distractor: complex but unused shadow calculation
        temp_shadow[i] = (waste ** 2) + (i * 0.1) if waste > 5 else temp_shadow[max(0, i-1)]

    # Irrelevant aggregation
    average_waste = cumulative_waste / total_batches if total_batches else 0
    high_waste_threshold = 10
    waste_alert_count = sum(1 for w in temp_shadow if w > high_waste_threshold)

    # Real computation begins
    total_input = sum(pair[0] for pair in yield_log)
    total_output = sum(pair[1] for pair in yield_log)
    baseline_capacity = max(pair[0] for pair in yield_log)

    # Multiple metadata unpacking with distractors
    config_keys = ['cycle_time', 'pressure', 'temperature', 'calibration_offset']
    metadata_dict = {k: v for k, v in zip(config_keys, cycle_metadata)}
    
    cycle_time = metadata_dict['cycle_time']
    pressure_factor = metadata_dict['pressure'] / 100
    temperature_bias = metadata_dict['temperature'] * 0.01
    
    # Dummy state tracking
    state_history = []
    for idx, entry in enumerate(batch_efficiencies):
        state = "STABLE" if entry > 0.8 else "VARIABLE"
        state_history.append((idx, state, entry * temperature_bias))
    
    # Key statement
    efficiency_score = total_output / (cycle_time * 0.95)
    
    # Additional red herring
    synthetic_index = sum(pressure_factor * e for e in batch_efficiencies) + len(state_history)
    
    return efficiency_score

# Input data
production_log = [
    (100, 94), (98, 92), (105, 99), (97, 90), (102, 96),
    (100, 88), (99, 94), (101, 95), (96, 91), (103, 97)
]
cycle_specs = [40, 87, 225, 0.15]  # cycle_time, pressure, temperature, offset

result = analyze_production_cycle(production_log, cycle_specs)
print(f"Result: {result}")