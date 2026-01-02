import itertools

def preprocess_readings(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [x / sum(filtered) for x in filtered]
    return normalized

def calculate_thermal_output(segments, efficiency):
    base_energy = sum(segments)
    loss_factor = 0.08
    adjusted = base_energy * (1 - loss_factor) * efficiency
    
    # Distractor: entropy calculation not used in final result
    entropy = sum(-x * abs(x) for x in segments if x != 0)
    entropy *= 0.01
    
    # Additional irrelevant transformation
    reshaped = list(itertools.chain.from_iterable([(x*0.1, x*0.2) for x in segments]))
    reshaped_sum = sum(reshaped)  # Dead computation
    
    # Real computation path
    modifier = 1.15 if len(segments) > 3 else 1.05
    final_output = adjusted * modifier
    
    # Extra red herring variable
    peak_ratio = max(segments) / min(segments) if len(segments) > 1 else 1
    
    return final_output

def analyze_sensor_array():
    raw_input = [12.5, 18.3, 9.7, 22.1, 14.4]
    processed = preprocess_readings(raw_input)
    
    # Simulate multiple segment energy distribution
    energy_segments = [x * 100 for x in processed]  # Scale up to realistic energy units
    
    efficiency_factor = 0.92
    temperature_drift = 0.03  # Unused in logic
    calibration_offset = 1.01  # Distractor
    
    # Key intermediate variable
    total_flux = sum(energy_segments) * efficiency_factor
    
    # Irrelevant container operation
    pairs = list(itertools.combinations(energy_segments, 2))
    pair_count = len(pairs)
    avg_pair = sum(sum(p) for p in pairs) / pair_count if pair_count > 0 else 0
    
    thermal_capacity = 0  # Initialization
    thermal_capacity = calculate_thermal_output(energy_segments, efficiency_factor)
    
    # Print required output format
    print(f"Target result: {thermal_capacity}")
    
    # Extra unused state tracking
    status_log = {'finalized': True, 'version': '2.1', 'capacity': thermal_capacity}

analyze_sensor_array()