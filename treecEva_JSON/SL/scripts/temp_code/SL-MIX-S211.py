import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def aggregate_stats(values):
    total = sum(values)
    mean = total / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return {
        'sum': total,
        'mean': mean,
        'variance': variance,
        'std_dev': math.sqrt(variance)
    }

def process_nested_structure(container):
    flattened = []
    for item in container:
        if isinstance(item, list):
            flattened.extend(process_nested_structure(item))
        elif isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, (int, float)):
                    flattened.append(v)
        elif isinstance(item, (int, float)):
            flattened.append(item)
    return flattened

# Main execution starts here
initial_data = [
    [1, 2, {'a': 3, 'b': [4, 5]}, 6],
    {'x': 7, 'y': [8, {'z': 9}]},
    [10, [11, 12], 13]
]

# Step 1: Process nested structure
flat_list = process_nested_structure(initial_data)

# Step 2: Apply complex transformation
transformed_data = complex_transform(flat_list)

# Step 3: Calculate aggregate statistics
stats = aggregate_stats(transformed_data)

# Step 4: Perform bit-wise operations on integer parts of stats
bitwise_results = []
for key in ['sum', 'mean', 'variance', 'std_dev']:
    val = int(stats[key])
    # Perform a series of bit operations
    val = (val & 0xFF) | ((val >> 4) ^ 0xF)
    bitwise_results.append(val)

# Step 5: Apply trigonometric transformations
trig_results = []
for i, val in enumerate(bitwise_results):
    angle = (val * (i + 1)) % 360
    rad = math.radians(angle)
    trig_val = math.sin(rad) * math.cos(rad) * 1000
    trig_results.append(int(trig_val))

# Step 6: Final calculation
final_result = 0
for i, val in enumerate(trig_results):
    if i % 2 == 0:
        final_result += val
    else:
        final_result -= val

# Apply final transformation
final_result = abs(final_result) % 1000

print(f"Result: {final_result}")