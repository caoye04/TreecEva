def analyze_pattern(data):
    irrelevant_sum = sum([x * 2 for x in range(10, 20)])  # Distractor computation
    pattern_map = {}
    count = 0
    for i in range(len(data)):
        if i % 2 == 0:
            pattern_map[i] = data[i] * 3
        else:
            pattern_map[i] = data[i] + 5
        count += i * 2  # Misleading accumulation
    
    misleading_total = count * 3 - 50  # Dead calculation
    return pattern_map

def calculate_modifiers(base_values):
    modifiers = {}
    temp_sum = 0
    for key, val in base_values.items():
        if key % 3 == 0:
            modifiers[key] = val // 2
            temp_sum += val * 4  # Irrelevant operation
        elif key % 3 == 1:
            modifiers[key] = val + 8
        else:
            modifiers[key] = val - 3
    
    dead_result = temp_sum // 10 + 25  # Unused computation
    return modifiers

def process_sequence(input_data):
    initial_analysis = analyze_pattern(input_data)
    adjusted_values = calculate_modifiers(initial_analysis)
    
    # Main computation path
    final_result = 0
    processed_count = 0
    for idx, value in adjusted_values.items():
        if idx % 4 == 0:
            final_result += value * 2
            processed_count += 1
        elif idx % 4 == 1:
            final_result += value - 5
        elif idx % 4 == 2:
            final_result += value // 3
        else:
            final_result += value + 10
    
    misleading_offset = processed_count * 15 - 7  # Distractor
    return final_result

# Main execution
sequence_data = [12, 8, 15, 23, 7, 19, 4, 11, 6, 14]
result = process_sequence(sequence_data)
final_output = result + 3  # Final adjustment

# Distractor variables and operations
side_calc = sum(sequence_data) * 2 - 45  # Irrelevant
unused_var = [x ** 2 for x in sequence_data if x > 10]  # Dead code

print(f"Target result: {final_output}")