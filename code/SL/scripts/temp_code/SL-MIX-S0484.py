from collections import defaultdict

def rotate_bits(n, width=8):
    # Assumes 8-bit keys for simplicity
    n = n & ((1 << width) - 1)
    return (n >> 1) | ((n & 1) << (width - 1))

def get_canonical_form(key):
    rotations = [key]
    current = key
    for _ in range(7): # For 8-bit keys, there are 8 possible rotations
        current = rotate_bits(current)
        rotations.append(current)
    return min(rotations)

# Historical cryptographic keys (represented as 8-bit integers)
historical_keys = [15, 30, 60, 120, 240, 97, 194, 53, 106, 212, 169, 79, 158, 137, 19, 38, 76, 152, 49, 98]
class_to_keys = defaultdict(set)

for k in historical_keys:
    canonical = get_canonical_form(k)
    class_to_keys[canonical].add(k)

# Greedily select the largest set of mutually inequivalent keys
selected_classes = set()
unique_key_classes = 0

# Sort classes by the number of keys they contain in descending order
sorted_classes = sorted(class_to_keys.items(), key=lambda item: len(item[1]), reverse=True)

for canonical_form, keys_in_class in sorted_classes:
    if not any(canonical_form in selected for selected in selected_classes):
        selected_classes.add(frozenset([canonical_form]))
        unique_key_classes += 1

print(f"Result: {unique_key_classes}")