def transform_signal(signal, depth):
    if depth == 0:
        return signal
    else:
        transformed = (signal << 1) ^ (signal >> 1)
        return transform_signal(transformed & 0xFF, depth - 1)

initial_pattern = 0b11001010
circuit_layers = [
    {'type': 'amplify', 'factor': 3},
    {'type': 'attenuate', 'mask': 0b10101111},
    {'type': 'modulate', 'base': 7, 'modulus': 16},
    {'type': 'invert', 'xor_mask': 0b11110000}
]

propagated_signals = []
for layer_idx in range(len(circuit_layers)):
    layer = circuit_layers[layer_idx]
    if layer['type'] == 'amplify':
        adjusted = initial_pattern * layer['factor']
        propagated_signals.append(adjusted)
    elif layer['type'] == 'attenuate':
        adjusted = initial_pattern & layer['mask']
        propagated_signals.append(adjusted)
    elif layer['type'] == 'modulate':
        adjusted = pow(initial_pattern, layer['base'], layer['modulus'])
        propagated_signals.append(adjusted)
    elif layer['type'] == 'invert':
        adjusted = initial_pattern ^ layer['xor_mask']
        propagated_signals.append(adjusted)

processed_outputs = [transform_signal(s, 2) for s in propagated_signals]

aggregated_result = 0
for i in range(len(processed_outputs)):
    for j in range(i+1, len(processed_outputs)):
        aggregated_result ^= processed_outputs[i] & processed_outputs[j]

final_signal_strength = aggregated_result % 256
print(f"Result: {final_signal_strength}")