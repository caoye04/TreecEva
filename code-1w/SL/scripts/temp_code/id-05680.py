import itertools

def analyze_sensor_readings(readings):
    # Irrelevant analysis branch (dead end)
    if len(readings) == 0:
        return {'status': 'empty', 'value': -999}
    
    filtered = [r for r in readings if r > 25]
    adjusted = [r * 0.95 for r in filtered]
    
    # Misleading intermediate computation
    avg_temp = sum(adjusted) / len(adjusted) if adjusted else 0
    temp_deviation = [abs(t - avg_temp) for t in adjusted]
    
    # This function doesn't affect final result but looks important
    def compute_thermal_gradient(data):
        return [data[i+1] - data[i] for i in range(len(data)-1)] if len(data) > 1 else [0]
    
    gradients = compute_thermal_gradient(adjusted)  # Red herring
    
    # Relevant transformation
    scaled = [int(t // 2) for t in adjusted]
    return {'status': 'valid', 'data': scaled}


def transform_sequence(seq):
    # Complex-looking but partially irrelevant transformation
    paired = list(itertools.combinations(seq, 2))
    sums = [a + b for a, b in paired]
    products = [a * b for a, b in paired]
    
    # Only this part is actually used later
    unique_sums = list(set(sums))
    return sorted(unique_sums)


def generate_reference_map(keys):
    # Distractor: builds a dictionary not fully used
    ref_map = {k: (k ** 2) % 7 for k in keys}
    ref_map['offset'] = 333  # Unused field
    ref_map['scale'] = 1.75  # Unused
    
    # But one value is extracted later
    return ref_map


def calculate_optimal_yield(data_dict):
    raw = data_dict['values']
    base = data_dict['base_offset']
    
    # Real logic starts here
    shifted = [x + base for x in raw]
    
    # Conditional filtering that affects outcome
    if len(shifted) > 5:
        processed = [x for x in shifted if x % 2 == 1]  # Keep only odds
    else:
        processed = [x for x in shifted if x % 2 == 0]  # Evens
    
    # Further reduction
    limited = processed[:4]
    
    # Final calculation
    total = sum(limited)
    multiplier = data_dict['config']['factor']
    yield_value = total * multiplier
    
    # Dead code path
    if yield_value < 0:
        yield_value = 0
    
    return yield_value

# Main execution flow
sensor_data = [30, 45, 20, 50, 35, 40, 28]
analysis_result = analyze_sensor_readings(sensor_data)

# Extract meaningful part
primary_sequence = analysis_result['data']  # [14, 21, 23, 26, 16]

# Transform with irrelevant overhead
transformed_sums = transform_sequence(primary_sequence)

# Build reference map (only one value used)
ref_keys = [1, 2, 3, 4, 5]
reference_map = generate_reference_map(ref_keys)

# Construct input for yield calculation
config_settings = {
    'factor': reference_map[3],  # (3**2)%7 = 2
    'version': '2.1'
}

# Prepare actual data payload
processed_data = {
    'values': transformed_sums[:6],           # Take first 6 of sorted unique sums
    'base_offset': len(primary_sequence) * 2,   # 10
    'config': config_settings
}

# Critical statement
final_yield = calculate_optimal_yield(processed_data)
print(f"Result: {final_yield}")