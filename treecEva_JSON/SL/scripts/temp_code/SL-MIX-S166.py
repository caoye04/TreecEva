import math

def compute_layered_hash(data):
    total = 0
    for key in sorted(data.keys()):
        val = data[key]
        if isinstance(val, list):
            sub_sum = sum([x**2 for x in val if isinstance(x, (int, float))])
            total += sub_sum * len(key)
        elif isinstance(val, dict):
            nested_total = compute_layered_hash(val)
            total += nested_total * len(str(key))
        elif isinstance(val, str):
            ascii_sum = sum(ord(c) for c in val)
            total += ascii_sum + len(val)
    return total

data_structure = {
    'alpha': [1, 2, 3],
    'beta': {
        'gamma': [4, 5],
        'delta': {
            'epsilon': 'hello',
            'zeta': [6, 7, 8, 9]
        }
    },
    'theta': 'world'
}

# Step 1: Compute initial hash
initial_hash = compute_layered_hash(data_structure)

# Step 2: Apply transformation using trigonometric modulation
modulated_value = initial_hash * math.sin(math.radians(30))  # sin(30°) = 0.5

# Step 3: Nested conditional transformations
if modulated_value > 50:
    transformed = modulated_value ** 1.5
else:
    transformed = modulated_value * 2

# Step 4: Bitwise adjustments
bit_adjusted = int(transformed) & 0xFF  # Mask to 8-bit

# Step 5: Final aggregation with exponential weighting
final_result = bit_adjusted + int(math.exp(3))

print(f'Result: {final_result}')