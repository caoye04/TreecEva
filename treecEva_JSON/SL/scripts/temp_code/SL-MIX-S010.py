import math

def process_data(data):
    transformed = []
    for key, values in data.items():
        squared_values = [v**2 for v in values if isinstance(v, (int, float))]
        if squared_values:
            avg = sum(squared_values) / len(squared_values)
            transformed.append((key, round(math.sqrt(avg), 2)))
    return transformed

def aggregate_results(results):
    total = 0
    count = 0
    for _, value in results:
        total += value
        count += 1
    return total / count if count else 0

data_dict = {
    'group_a': [1, 2, 3, 'skip', 4],
    'group_b': [2.5, 3.5, None, 4.5],
    'group_c': ['ignore', 5, 6, 7],
    'group_d': [8, 9, 10]
}

processed = process_data(data_dict)
average_of_processed = aggregate_results(processed)

# Perform bit-wise operations on integer parts
int_part = int(average_of_processed)
bitwise_result = (int_part << 2) ^ 0b1010

# String transformation
label = ''.join([chr(ord(c) + 1) for c in 'Xpsl'])

# Final calculation
final_result = bitwise_result + len(label) * 3
print(f'Result: {final_result}')