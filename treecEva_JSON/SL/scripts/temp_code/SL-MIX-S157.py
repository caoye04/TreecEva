import math

def transform_data(data):
    processed = []
    for key, values in data.items():
        temp = []
        for v in values:
            if isinstance(v, int):
                temp.append(v ** 2)
            elif isinstance(v, str):
                temp.append(len(v))
            else:
                temp.append(0)
        processed.append((key, sum(temp)))
    return dict(processed)

data_structure = {
    'alpha': [3, 'hello', 5],
    'beta': ['world', 2, 3.5, None],
    'gamma': [7, 'test', 'longerstring']
}

transformed = transform_data(data_structure)

# Perform advanced computations
accumulated = 0
for k, v in transformed.items():
    if k == 'gamma':
        accumulated += v * 3
    elif k.startswith('a'):
        accumulated += int(math.sqrt(v))
    else:
        accumulated += v << 2

# Bitwise and modular arithmetic mix
x = accumulated & 0xFF
y = (x ^ 0xAA) % 17
z = y | 0b1100

# Final calculation sequence
interim = (z + 12) * (z - 5)
final_result = interim // 7 + (interim % 7)

print(f'Result: {final_result}')