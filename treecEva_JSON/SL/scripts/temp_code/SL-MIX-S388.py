import math

def process_data(data):
    total = 0
    for key, value in data.items():
        if isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    for sub_key, sub_value in item.items():
                        if isinstance(sub_value, str):
                            numeric_part = ''.join(filter(str.isdigit, sub_value))
                            if numeric_part:
                                total += int(numeric_part) * (i + 1) * len(sub_key)
                        elif isinstance(sub_value, (int, float)):
                            total += sub_value ** (1/3) * math.log(abs(sub_value) + 1)
                elif isinstance(item, (int, float)):
                    total += math.sin(item) * math.cos(item)
        elif isinstance(value, dict):
            for k, v in value.items():
                if isinstance(v, list):
                    total += sum(v) % (len(k) + 1)
                elif isinstance(v, str):
                    total += len(v) * v.count('a')
    return total

data_structure = {
    'level1': [
        {'alpha': 'value123test', 'beta': 27.5},
        [45, 67.2, {'gamma': 'data456end', 'delta': -81.0}],
        1.57
    ],
    'level2': {
        'inner': [12, 23, 34, 45],
        'text': 'banana'
    },
    'level3': [
        3.14,
        {'epsilon': 'final789check', 'zeta': 64},
        [99, 88]
    ]
}

# Intermediate processing
intermediate = process_data(data_structure)

# Bitwise and mathematical transformations
shifted = (int(intermediate) << 2) ^ 0xFF
log_shifted = math.log(abs(shifted) + 1)

# String manipulation based on intermediate results
repr_str = repr(intermediate)[:5]
if repr_str.isdigit():
    digit_sum = sum(int(d) for d in repr_str)
else:
    digit_sum = sum(ord(c) for c in repr_str if c.isdigit())

# Final calculation step
result = (digit_sum * log_shifted) % (shifted // 10 + 1)

print(f"Result: {result}")