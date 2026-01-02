def process_metrics(dataset, config):
    temp_sum = 0
    scaling_factor = 1.75
    adjustment = 0.23
    base_offset = 12
    
    # Irrelevant precomputation (distractor)
    dummy_calc = (len(dataset) * 2 + 5) % 7
    if dummy_calc > 3:
        dummy_calc = (dummy_calc ** 2) // 3
    
    # Actual logic begins
    valid_keys = ['temp', 'pressure', 'humidity']
    pressure_val = dataset.get('pressure', 0)
    temp_val = dataset.get('temp', 0)
    humidity_val = dataset.get('humidity', 0)
    
    # Bitwise flag analysis (semi-relevant)
    flag_state = 0
    for key in config:
        if config[key]:
            flag_state ^= 1 << list(config.keys()).index(key)
    
    # Secondary distraction: unused transformation
    transformed_data = {}
    for k, v in dataset.items():
        if isinstance(v, int):
            transformed_data[k] = (v + base_offset) * scaling_factor
    
    # Core metric computation
    raw_score = temp_val * 1.5 + pressure_val // 10 - (humidity_val & 7)
    
    # Conditional adjustment based on dictionary keys
    if 'calibrated' in dataset and dataset['calibrated']:
        raw_score += 5
    
    # Distractor: complex but unused expression
    noise = (base_offset * adjustment) / (scaling_factor + 1e-5)
    noise *= len(config) if len(config) % 2 else 0
    
    # Final score depends only on specific conditions
    final_multiplier = 1
    if flag_state & 2:  # Only second flag matters
        final_multiplier = 2
    
    result = int(raw_score * final_multiplier)

    return result

# Setup input data
data_map = {
    'temp': 24,
    'pressure': 1013,
    'humidity': 61,
    'calibrated': True,
    'device_id': 9901
}

flags = {
    'debug_mode': False,
    'enhanced': True,
    'logging': False
}

# Unused helper (dead code path)
def validate_entry(entry):
    return entry.get('device_id', 0) > 1000

# Key execution point
final_score = process_metrics(data_map, flags)
print(f"Result: {final_score}")