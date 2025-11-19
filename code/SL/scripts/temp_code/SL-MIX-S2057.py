from functools import reduce

def rotate_key(key, steps):
    return ((key << steps) | (key >> (8 - steps))) & 0xFF

class CipherState:
    def __init__(self, initial):
        self.state = initial
    
    def transform(self, key):
        self.state ^= key
        self.state = rotate_key(self.state, 3)
        return self.state

def hex_to_ascii_sum(hex_string):
    return sum(ord(c) for c in bytes.fromhex(hex_string).decode('utf-8'))

# Initialize cipher parameters
base_seed = 0x42
message_blocks = ['4142', '4344', '4546']
round_keys = [0x15, 0x2A, 0x3F]

# Setup cipher state
cipher_engine = CipherState(base_seed)
current_state = cipher_engine.state

# Process each message block through multiple transformation rounds
for block_idx in range(len(message_blocks)):
    block_value = hex_to_ascii_sum(message_blocks[block_idx])
    
    for round_idx in range(3):
        # Apply bitwise transformations
        transformed_key = round_keys[round_idx] ^ block_value
        shifted_key = (transformed_key << 1) & 0xFF
        
        # Update cipher state
        current_state = cipher_engine.transform(shifted_key)
        
        # Additional string transformation
        state_chars = list(hex(current_state)[2:].zfill(2))
        transformed_chars = list(map(lambda c: chr((ord(c) + block_idx + round_idx) % 256), state_chars))
        char_sum = sum(map(ord, transformed_chars))
        
        # Final state adjustment
        current_state ^= (char_sum & 0xFF)

final_cipher_state = current_state
print(f"Result: {final_cipher_state}")