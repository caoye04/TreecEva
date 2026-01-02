from collections import defaultdict

def apply_security_layer(packet_sig, layer_config):
    operation = layer_config['op']
    mask = layer_config['mask']
    condition = layer_config.get('condition', None)
    
    if condition and not condition(packet_sig):
        return packet_sig
    
    if operation == 'AND':
        return packet_sig & mask
    elif operation == 'OR':
        return packet_sig | mask
    elif operation == 'XOR':
        return packet_sig ^ mask
    elif operation == 'LSHIFT':
        return (packet_sig << mask) & 0xFF
    elif operation == 'RSHIFT':
        return packet_sig >> mask
    return packet_sig

def is_high_priority(sig):
    return sig > 0x80

def is_low_priority(sig):
    return sig < 0x40

# Security layer configurations
layer_configs = [
    {'op': 'XOR', 'mask': 0x3C},
    {'op': 'AND', 'mask': 0xF0, 'condition': is_high_priority},
    {'op': 'LSHIFT', 'mask': 2},
    {'op': 'OR', 'mask': 0x0F, 'condition': lambda x: x < 0xC0}
]

# Packet processing pipeline
initial_packet_signature = 0x5F
packet_tracker = defaultdict(list)
packet_tracker['signatures'].append(initial_packet_signature)

for i, config in enumerate(layer_configs):
    current_sig = packet_tracker['signatures'][-1]
    new_sig = apply_security_layer(current_sig, config)
    packet_tracker['signatures'].append(new_sig)
    packet_tracker['layers'].append(f'Layer_{i+1}')

final_packet_signature = packet_tracker['signatures'][-1] if len(packet_tracker['signatures']) > 0 else 0
print(f'Result: {final_packet_signature}')