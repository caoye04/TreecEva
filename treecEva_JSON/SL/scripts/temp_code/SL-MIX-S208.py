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
                if item > 0:
                    total += item
                else:
                    total -= item * 2
        elif isinstance(value, dict):
            for k, v in value.items():
                total += k * v
    return total

data_structure = {
    'a': [3, -1, 4, -1, 5],
    'b': {
        2: 7,
        3: -2,
        5: 1
    },
    'c': [
        [2, 3],
        [-1, 4],
        [5, -2]
    ]
}

# Phase 1: Transform the primary list
transformed = complex_transform(data_structure['a'])

# Phase 2: Process nested lists
nested_sum = 0
for sublist in data_structure['c']:
    sub_transformed = complex_transform(sublist)
    nested_sum += sum(sub_transformed)

# Phase 3: Combine results with bitwise operations
intermediate = nested_operation(data_structure)
combined = (int(intermediate) & 0xFF) ^ (int(sum(transformed)) << 2)

# Phase 4: Apply trigonometric and logarithmic operations
angle = (combined % 360) * (math.pi / 180)
sin_component = math.sin(angle)
cos_component = math.cos(angle)
log_component = math.log(abs(sin_component) + 1e-10) if sin_component != 0 else 0

# Phase 5: Final calculation
final_result = int((sin_component * 1000) + (cos_component * 500) + (log_component * 100) + nested_sum)

print(f"Result: {final_result}")