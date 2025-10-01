import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, str):
                temp.append(len(val) * (i + 1))
            elif isinstance(val, int):
                temp.append(val ** (j + 1))
            elif isinstance(val, float):
                temp.append(round(math.sqrt(val), 2))
        result.append(temp)
    return result

def compute_aggregate(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total

def transform_and_calculate(base_value, operations):
    current = base_value
    for op in operations:
        if op['type'] == 'add':
            current += op['value']
        elif op['type'] == 'multiply':
            current *= op['value']
        elif op['type'] == 'power':
            current = current ** op['value']
        elif op['type'] == 'modulo':
            current = current % op['value']
    return current

data_structure = [
    ["hello", 2, 9.0, "world"],
    [4, "test", 16.0],
    ["a", "bb", 3, 5.0, 2]
]

processed_data = process_nested_data(data_structure)
aggregate_sum = compute_aggregate(processed_data)

operations_list = [
    {'type': 'add', 'value': 10},
    {'type': 'multiply', 'value': 3},
    {'type': 'power', 'value': 2},
    {'type': 'modulo', 'value': 1000}
]

transformed_value = transform_and_calculate(aggregate_sum, operations_list)

# Final calculation
final_result = (transformed_value & 0xFF) ^ 0xAA  # Bitwise AND with 255, then XOR with 170

print(f"Result: {final_result}")