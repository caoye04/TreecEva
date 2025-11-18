import re
from collections import defaultdict

def process_message_layer(layer_data, mask):
    return [x ^ mask for x in layer_data]

cipher_layers = [
    [0b110101, 0b101010, 0b111000],
    [0b001100, 0b110011, 0b101010],
    [0b111111, 0b000000, 0b101010]
]

mask_sequence = [0b101010, 0b010101, 0b111111]
verification_pattern = r'^[01]{6}$'

bitwise_checksum = lambda vals: sum(vals) & 0b111111
layer_results = defaultdict(list)

for i, (layer, mask) in enumerate(zip(cipher_layers, mask_sequence)):
    processed = process_message_layer(layer, mask)
    binary_strings = [format(x, '06b') for x in processed]
    valid_count = sum(1 for s in binary_strings if re.match(verification_pattern, s))
    if valid_count >= 2:
        layer_results['valid'].extend(processed)
    else:
        layer_results['invalid'].extend(processed)

final_values = []
if layer_results['valid']:
    checksum = bitwise_checksum(layer_results['valid'])
    adjusted = [(x << 1) | (x >> 5) for x in layer_results['valid']]
    final_values = [x & checksum for x in adjusted]
else:
    fallback = [x | 0b001100 for x in layer_results['invalid']]
    final_values = [x ^ 0b110011 for x in fallback]

verification_code = sum(final_values) >> 2
print(f"Result: {verification_code}")