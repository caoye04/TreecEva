def transform_and_calculate(operations, value):
    result = value
    for op_key, multiplier in operations.items():
        if op_key.startswith('shift'):
            result += multiplier * 2
        elif op_key.endswith('mod'):
            result %= multiplier
    return result

operation_map = {'shift_left': 3, 'rotate_mod': 5, 'scale_mod': 7}
base_value = 28
final_output = transform_and_calculate(operation_map, base_value)
print(f"Result: {final_output}")