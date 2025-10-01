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
                if sub_key.startswith('pos'):
                    total += sub_val * 3
                else:
                    total -= sub_val // 2
    return total

def transform_string(s):
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count * len(s)

data_structure = {
    'alpha': [4, -9, 25, -16, 36],
    'beta': {'pos_a': 7, 'neg_b': 14, 'pos_c': 5},
    'gamma': [1, 4, 9, 16],
    'delta': {'pos_x': 10, 'other_y': 20}
}

string_input = "AdvancedProgramming"

numeric_base = process_nested_data(data_structure)
char_metric = transform_string(string_input)

intermediate_value = numeric_base + char_metric

if intermediate_value > 100:
    final_result = intermediate_value * 2 - 50
else:
    final_result = intermediate_value + 100

print(f"Result: {final_result}")