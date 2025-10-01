import math

def process_data(container):
    total = 0
    for key, values in container.items():
        if isinstance(values, list):
            for i, val in enumerate(values):
                adjusted_val = val ^ (i + 1)
                total += adjusted_val
        elif isinstance(values, dict):
            for sub_key, sub_val in values.items():
                if sub_key.startswith('exp'):
                    total += int(math.exp(sub_val))
    return total

data = {
    'group_a': [7, 14, 23],
    'group_b': {'exp1': 2.5, 'exp2': 1.8},
    'group_c': [31, 42],
    'group_d': {'other': 100}
}

initial_sum = process_data(data)
transformed = bin(initial_sum)[2:]  # Binary representation without '0b'
reversed_bits = transformed[::-1]
integer_from_reversed = int(reversed_bits, 2)

# Perform modular exponentiation
mod_exp_result = pow(integer_from_reversed, 3, 1000000007)

# String manipulation
str_repr = str(mod_exp_result)
split_index = len(str_repr) // 2
left_part = str_repr[:split_index]
right_part = str_repr[split_index:]
concatenated = right_part + left_part

if concatenated.isdigit():
    final_result = int(concatenated) % 987654321
else:
    final_result = -1

print(f'Result: {final_result}')