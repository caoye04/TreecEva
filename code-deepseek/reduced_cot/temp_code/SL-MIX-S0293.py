def process_data(input_data):
    # Distractor: complex preprocessing that doesn't affect final result
    processed = {k: (v * 2 if v % 3 == 0 else v // 2) for k, v in input_data.items()}
    
    # Irrelevant intermediate computations
    temp_sum = sum(input_data.values()) * 0.75
    max_val = max(input_data.values()) ^ 15
    
    # Actual logic path
    filtered = {k: v for k, v in input_data.items() if v > 8}
    
    # More distractions
    dead_code_path = lambda x: x ** 2 + 3 * x - 7
    unused_result = dead_code_path(len(filtered))
    
    # Key computation
    result = 0
    for key, value in filtered.items():
        if key.startswith('data_'):
            result += value
        else:
            result -= value // 2
    
    # Final adjustment (critical step)
    adjustment = (result & 0b1111) | ((result >> 4) & 0b1111)
    return result + adjustment

data_pool = {
    'data_alpha': 12,
    'data_beta': 8,
    'data_gamma': 15,
    'temp_data': 20,
    'backup': 6,
    'data_delta': 9
}

# Misleading computations that look important
intermediate_calc = (data_pool['data_alpha'] * data_pool['data_gamma']) % 17
unused_var = intermediate_calc + sum(data_pool.values())

final_value = process_data(data_pool)
print(f"Result: {final_value}")