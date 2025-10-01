import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, list):
            temp = 0
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    sub_temp = 1
                    for sub_key, sub_value in item.items():
                        if isinstance(sub_value, str):
                            sub_temp *= len(sub_value)
                        elif isinstance(sub_value, int):
                            sub_temp += sub_value
                    temp += sub_temp
                elif isinstance(item, int):
                    temp += item * (i + 1)
            result += temp
        elif isinstance(value, dict):
            sub_result = 0
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, list):
                    for i, elem in enumerate(sub_value):
                        if isinstance(elem, int):
                            sub_result += elem * pow(i, 2)
                        elif isinstance(elem, str):
                            sub_result += ord(elem[0])
            result += sub_result
    return result

def transform_values(x, y, z):
    a = x & (y | z)
    b = (x ^ y) << 2
    c = ~(a & b)
    d = math.floor(math.sqrt(abs(c)))
    return d

data_structure = {
    'alpha': [
        5,
        {'beta': 'hello', 'gamma': 7},
        3,
        {'delta': 'world', 'epsilon': 2}
    ],
    'zeta': {
        'eta': [1, 'A', 3, 'B'],
        'theta': [4, 'X', 2]
    },
    'iota': [
        10,
        20,
        {'kappa': 'test', 'lambda': 5}
    ]
}

intermediate_value = process_nested_data(data_structure)
final_result = transform_values(intermediate_value, 0b1101, 0o17)
print(f'Result: {final_result}')