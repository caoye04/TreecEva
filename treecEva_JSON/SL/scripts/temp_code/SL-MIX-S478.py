import math

def process_nested_data(data):
    total = 0
    for key, values in data.items():
        if isinstance(values, list):
            for i, val in enumerate(values):
                if i % 2 == 0:
                    total += val ** 2
                else:
                    total -= math.sqrt(abs(val))
        elif isinstance(values, dict):
            for sub_key, sub_val in values.items():
                total += len(sub_key) * sub_val
    return total

def transform_string(s):
    vowels = 'aeiou'
    transformed = ''
    for char in s:
        if char.lower() in vowels:
            transformed += char.upper()
        else:
            transformed += char.lower()
    return transformed

data_structure = {
    'alpha': [4, -9, 2, 16, -25],
    'beta': {'gamma': 3, 'delta_epsilon': 7},
    'chi': [1, 4, 9, -16, 25]
}

numeric_sum = process_nested_data(data_structure)
transformed_text = transform_string('DynamicProgrammingIsFun')
vowel_count = sum(1 for c in transformed_text if c.isupper())

# Perform a series of mathematical operations
intermediate_value = numeric_sum * 2 + vowel_count
log_value = math.log(abs(intermediate_value)) if intermediate_value != 0 else 0
sin_component = math.sin(log_value)
cos_component = math.cos(log_value)
complex_expr = sin_component ** 2 + cos_component ** 2

bitwise_a = 0b1101
bitwise_b = 0b1011
bitwise_xor = bitwise_a ^ bitwise_b
shifted_value = bitwise_xor << 2

# Final calculation combining all components
final_result = int(complex_expr * 1000) + shifted_value + vowel_count
print(f'Result: {final_result}')