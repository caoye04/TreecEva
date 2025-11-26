from collections import defaultdict

def validate_input(data):
    # Distractor function - not used in main flow
    validation_flags = [True, False, True, True]
    return sum(validation_flags) * 2

def calculate_stats(values):
    # Misleading intermediate calculations
    temp_sum = sum(values)
    avg = temp_sum / len(values)
    squared_diff = [(x - avg) ** 2 for x in values]
    variance = sum(squared_diff) / len(values)
    return variance * 3.14  # Irrelevant scaling factor

def process_data(data_items, settings):
    # Main processing logic with distractions
    processed_values = []
    counter = defaultdict(int)
    
    # Distractor loop with unused results
    for i, item in enumerate(data_items):
        counter[item % 4] += 1
        temp = item * 2 + i  # Unused calculation
        
    # Actual relevant processing
    filtered_data = [x for x in data_items if x % settings['filter_mod'] == 0]
    
    # More distractions
    redundant_stats = calculate_stats(data_items)
    validation_score = validate_input(data_items)
    
    # Core logic with bitwise operations
    if settings['use_bitwise']:
        result = 0
        for val in filtered_data:
            result |= (val & 0x0F)
        result ^= settings['xor_key']
    else:
        result = sum(x * settings['multiplier'] for x in filtered_data)
    
    # Final adjustment (actual answer depends on this)
    return result // settings['divisor']

def analyze_pattern(data):
    # Dead code path - never called
    pattern_sum = 0
    for i in range(len(data) - 1):
        pattern_sum += abs(data[i] - data[i + 1])
    return pattern_sum

# Main execution
main_data = [12, 25, 8, 17, 33, 41, 6, 19, 27, 14]
config = {
    'filter_mod': 3,
    'use_bitwise': True,
    'xor_key': 7,
    'multiplier': 2,
    'divisor': 4
}

# Distractor variable assignments
backup_data = main_data[:]
validation_check = validate_input(main_data)
stats_analysis = calculate_stats(main_data)

# Key statement
final_result = process_data(main_data, config)

print(f"Target result: {final_result}")