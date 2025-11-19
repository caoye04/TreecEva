import math

def tokenize(message):
    return [ord(c) for c in message]

def hash_token(token):
    return (token * 31) % 256

def process_layer(tokens, shift_val):
    hashed = [hash_token(t) for t in tokens]
    shifted = [(h << (i % 3)) & 0xFF for i, h in enumerate(hashed)]
    xor_result = 0
    for s in shifted:
        xor_result ^= s
    return xor_result >> shift_val

token_sequence = tokenize("SECURE")
layer1_result = process_layer(token_sequence, 1)
layer2_result = process_layer(token_sequence[::-1], 2)
auth_signature = (layer1_result ^ layer2_result) & 0xFF
exp_component = int(math.log2(layer1_result + 1)) if layer1_result > 0 else 0
auth_signature = (auth_signature << 2) | exp_component
print(f"Result: {auth_signature}")