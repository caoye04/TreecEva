import re
from functools import reduce
from itertools import compress

def transform_component(comp):
    return (comp ^ 0b101010) & 0xFF

def validate_segment(segment):
    return bool(re.match(r'^[A-F0-9]{2}$', segment))

token_segments = ['A1', 'B2', 'C3', 'D4']
transformed_values = []

for idx, seg in enumerate(token_segments):
    if validate_segment(seg):
        hex_val = int(seg, 16)
        transformed = transform_component(hex_val)
        if transformed > 0x50:
            transformed_values.append(transformed)
    else:
        transformed_values.append(0)

mask = [val > 0x60 for val in transformed_values]
filtered_vals = list(compress(transformed_values, mask))

if filtered_vals:
    final_token_value = reduce(lambda x, y: x | y, filtered_vals)
else:
    final_token_value = 0

print(f"Result: {final_token_value}")