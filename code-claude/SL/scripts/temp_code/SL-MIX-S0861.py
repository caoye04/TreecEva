def count_chars(text):
    char_map = {}
    for c in text:
        if c.isalnum():
            char_map[c] = char_map.get(c, 0) + 1
    return char_map

def filter_map(mapping, condition_func):
    return {k: v for k, v in mapping.items() if condition_func(k, v)}

def apply_transformations(char_freq, operations):
    result = 0
    priority_chars = set(['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9'])
    
    # Distractor calculations
    vowel_count = sum(char_freq.get(c, 0) for c in 'aeiou')
    digit_sum = sum(char_freq.get(str(d), 0) for d in range(10))
    max_freq = max(char_freq.values()) if char_freq else 0
    
    # Misleading operation sequence
    temp_score = vowel_count * 10 - digit_sum * 5
    complexity_factor = len(set(char_freq.keys()) & priority_chars)
    adjustment = (max_freq // 2) if max_freq > 5 else max_freq
    
    # Actual operation logic
    for op in operations:
        if op == 'sum_values':
            result += sum(char_freq.values())
        elif op == 'weighted_count':
            result += sum(v * (2 if k in priority_chars else 1) for k, v in char_freq.items())
        elif op == 'char_positions':
            # Distractor calculation
            positions_sum = sum(ord(k) for k in char_freq.keys())
            # Unused variable
            position_factor = positions_sum % 100
        elif op == 'frequency_product':
            # Distractor calculation
            if char_freq:
                product = 1
                for v in char_freq.values():
                    if v > 1:
                        product *= v
                # Unused calculation
                complexity_score = product % 1000
    
    # More distractions
    potential_bonus = complexity_factor * adjustment
    if vowel_count > digit_sum:
        # Dead code path
        alternate_result = result * 1.5
        bonus_points = potential_bonus * 2
    else:
        # Another dead code path
        alternate_result = result * 0.8
        bonus_points = potential_bonus // 2
    
    return result

def process_data(input_text, frequency_threshold):
    # Initial processing
    char_frequencies = count_chars(input_text)
    
    # Distracting filters that don't affect the final result
    common_chars = filter_map(char_frequencies, lambda k, v: v >= frequency_threshold)
    rare_chars = filter_map(char_frequencies, lambda k, v: v < frequency_threshold)
    
    # Distracting calculations
    total_common = sum(common_chars.values())
    total_rare = sum(rare_chars.values())
    ratio = total_common / total_rare if total_rare > 0 else float('inf')
    
    # Misleading variable names
    primary_result = apply_transformations(char_frequencies, ['sum_values', 'weighted_count'])
    secondary_result = apply_transformations(common_chars, ['weighted_count'])
    tertiary_result = apply_transformations(rare_chars, ['char_positions', 'frequency_product'])
    
    # More distraction with lambda functions
    normalizer = lambda x, y: x / (y if y > 0 else 1)
    scorer = lambda a, b, c: a + b - c
    
    # Distractor calculations
    normalized_common = normalizer(secondary_result, len(common_chars) if common_chars else 1)
    normalized_rare = normalizer(tertiary_result, len(rare_chars) if rare_chars else 1)
    
    # Complex but irrelevant scoring
    complexity_score = scorer(normalized_common, normalized_rare, ratio if ratio != float('inf') else 0)
    
    # The actual result we care about
    return primary_result

# Input data
input_text = "Hello123World456"
frequency_threshold = 2

# Process the data
target_value = process_data(input_text, frequency_threshold)

# Additional distractor code after the target calculation
modified_text = input_text.lower().replace('l', '1').replace('o', '0')
modified_result = process_data(modified_text, frequency_threshold - 1)
final_calculation = (target_value + modified_result) // 2

# Print the target value
print(f"Target result: {target_value}")

# Print distractor values
print(f"Modified result: {modified_result}")
print(f"Final calculation: {final_calculation}")