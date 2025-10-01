import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, list):
            temp_sum = sum([x**2 for x in value if isinstance(x, (int, float))])
            result += int(math.sqrt(temp_sum)) if temp_sum > 0 else 0
        elif isinstance(value, dict):
            sub_result = 1
            for k, v in value.items():
                if isinstance(v, str) and v.isnumeric():
                    sub_result *= int(v)
            result += sub_result
    return result

data_structure = {
    'a': [3, 4, 'hello', 5],
    'b': {'x': '2', 'y': 'abc', 'z': '7'},
    'c': [2.5, 3.5, None, 1],
    'd': {'m': '4', 'n': '0', 'o': '-3'}
}

intermediate_value = process_nested_data(data_structure)

# Perform additional transformations
factorial_part = math.factorial(intermediate_value % 6)
log_part = math.log(max(1, intermediate_value - 10))
trig_part = math.sin(intermediate_value) * math.cos(intermediate_value)

complex_expression = (factorial_part * int(log_part)) + int(trig_part * 100)

bitwise_operation = (complex_expression & 0xFF) ^ 0xAA
shifted_value = bitwise_operation << 2

final_result = shifted_value + (intermediate_value % 7)
print(f'Result: {final_result}')