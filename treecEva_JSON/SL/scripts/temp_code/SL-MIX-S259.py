import math

def recursive_transform(data, depth=0):
    if isinstance(data, dict):
        return {k: recursive_transform(v, depth + 1) for k, v in data.items()}
    elif isinstance(data, list):
        return [recursive_transform(item, depth + 1) for item in data]
    elif isinstance(data, int):
        if depth % 2 == 0:
            return data ^ (data << 2)
        else:
            return data & ~(data >> 1)
    else:
        return data

data_structure = {
    'level1': {
        'level2a': [1, 2, {'nested': [3, 4]}],
        'level2b': [5, 6, [7, 8]],
        'level2c': 9
    },
    'level1b': [10, {'deep': [11, 12]}, 13]
}

transformed_data = recursive_transform(data_structure)

# Extract all integers from transformed_data using a recursive helper function
def extract_integers(obj):
    integers = []
    if isinstance(obj, dict):
        for v in obj.values():
            integers.extend(extract_integers(v))
    elif isinstance(obj, list):
        for item in obj:
            integers.extend(extract_integers(item))
    elif isinstance(obj, int):
        integers.append(obj)
    return integers

all_integers = extract_integers(transformed_data)

# Perform mathematical aggregation
product_log_sum = 0
for num in all_integers:
    if num > 0:
        product_log_sum += math.log(num) * num

# Bitwise manipulation chain
bitwise_chain = 0
for i, val in enumerate(all_integers):
    if i % 3 == 0:
        bitwise_chain |= val
    elif i % 3 == 1:
        bitwise_chain &= val
    else:
        bitwise_chain ^= val

# Final calculation combining both results
final_result = int((product_log_sum * bitwise_chain) % 1000000)
print(f'Result: {final_result}')
