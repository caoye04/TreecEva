import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def nested_operation(container):
    total = 0
    for key, value in container.items():
        if isinstance(value, list):
            for item in value:
                total += item if item > 0 else -item
        elif isinstance(value, dict):
            for k, v in value.items():
                total += len(str(k)) * v
    return total

data_structure = {
    'a': [3, -4, 5],
    'b': {
        'key1': 2,
        'longerkey': 3
    },
    'c': [
        complex(1, 2),
        complex(3, 4)
    ]
}

# Process the data structure
processed_values = []
for key in sorted(data_structure.keys()):
    value = data_structure[key]
    if isinstance(value, list):
        if any(isinstance(x, complex) for x in value):
            # For complex numbers, take magnitude
            processed_values.extend([abs(x) for x in value])
        else:
            processed_values.extend(value)
    elif isinstance(value, dict):
        temp = []
        for k, v in value.items():
            temp.append(len(k) * v)
        processed_values.extend(temp)

# Apply transformation
transformed = complex_transform(processed_values)

# Perform nested operation
nested_result = nested_operation(data_structure)

# Calculate final value
X = sum(transformed) + nested_result

# Execution point Y
print(f"Result: {int(X)}")