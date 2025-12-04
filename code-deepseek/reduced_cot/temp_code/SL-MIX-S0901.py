from collections import defaultdict

def calculate_final_value(data_map, adjustment):
    # Irrelevant computation that looks important
    temp_sum = sum(range(15, 25)) + len(data_map.keys()) * 3
    
    # Main logic path
    processed_values = []
    for key, values in data_map.items():
        if len(values) > 1:
            # Complex nested computation
            base_val = (values[0] ^ values[1]) & 0xFF
            if base_val % 2 == 0:
                processed = base_val * adjustment - len(key)
            else:
                processed = base_val + adjustment + ord(key[0]) if key else 0
            processed_values.append(processed)
    
    # Misleading intermediate variable
    intermediate_result = sum(processed_values) * 2 - temp_sum
    
    # Dead code path that seems relevant
    unused_calculation = intermediate_result // 3 if intermediate_result > 100 else intermediate_result * 2
    
    # Final actual computation
    final_result = sum(processed_values) + adjustment
    return final_result

# Setup data
sample_data = defaultdict(list)
sample_data['alpha'].extend([45, 78])
sample_data['beta'].extend([92, 56])
sample_data['gamma'].extend([33, 67])
sample_data['delta'].extend([89, 24])

# Irrelevant computations
redundant_calc = (45 * 78) // 3 + 92 - 56
misleading_factor = len(sample_data) * 10

# Main execution
adjustment_factor = 17
final_output = calculate_final_value(sample_data, adjustment_factor)

# Print result
print(f"Result: {final_output}")