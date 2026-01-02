from collections import defaultdict

# Simulate sensor readings with bit flags
def process_data(readings):
    stats = defaultdict(int)
    mask = 0b1101  # Filter pattern for valid data
    filtered = []

    for val in readings:
        if val & mask == mask:  # Check bitwise condition
            stats['valid'] += 1
            filtered.append(val ^ 0b1010)  # Transform using XOR
        else:
            stats['invalid'] += 1

    aggregate = 0
    for num in filtered:
        aggregate += num % 7

    result = aggregate + stats['valid']
    return result

values = [13, 15, 12, 14, 8]
result = process_data(values)
print(f"Target result: {result}")