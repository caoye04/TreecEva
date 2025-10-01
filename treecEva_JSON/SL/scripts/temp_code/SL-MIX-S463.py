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

data_structure = {
    'alpha': [4, 9, -16, 25],
    'beta': {'gamma': 3, 'delta_epsilon': 7},
    'chi': [-49, 64, -81]
}

intermediate_sum = process_nested_data(data_structure)

# Perform bitwise and arithmetic operations
a, b, c = 24, 17, 9
bitwise_and = a & b
bitwise_or = a | c
shifted_value = b << 2

complex_calculation = ((bitwise_and + intermediate_sum) * bitwise_or) - shifted_value

# Apply modulo and exponentiation
if complex_calculation > 0:
    exponential_part = int(math.log(complex_calculation, 2))
else:
    exponential_part = 0

modulo_operation = exponential_part % 7

# Final adjustment using trigonometric function
angle_in_radians = math.pi / 4
trigonometric_factor = round(math.sin(angle_in_radians) * 100)

final_result = (complex_calculation // 3) + modulo_operation + trigonometric_factor
print(f'Result: {final_result}')