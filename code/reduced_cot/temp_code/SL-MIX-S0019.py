from functools import reduce

class SignalOptimizer:
    def __init__(self, initial_state):
        self.state = initial_state
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Initial register configuration
initial_register = 0b110101101001

with SignalOptimizer(initial_register) as optimizer:
    # Step 1: Apply greedy bit flipping for optimization
    temp_bits = [optimizer.state >> i & 1 for i in range(12)]
    flipped_indices = []
    
    # Greedy selection: flip bits that reduce overall Hamming weight
    for idx in sorted(range(len(temp_bits)), key=lambda x: (-1 if temp_bits[x] == 1 else 1)):
        if len(flipped_indices) < 3 and temp_bits[idx] == 1:
            temp_bits[idx] ^= 1
            flipped_indices.append(idx)
    
    # Step 2: Reconstruct intermediate register
    intermediate_register = reduce(lambda acc, bit: (acc << 1) | bit, reversed(temp_bits), 0)
    
    # Step 3: Perform modular arithmetic adjustment
    modulus_key = 0x1F
    adjusted_register = (intermediate_register * 17 + 0x1A3) % modulus_key
    
    # Step 4: Apply XOR mask with sorted bit positions
    xor_mask = reduce(lambda x, y: x | (1 << y), sorted(flipped_indices), 0)
    masked_register = adjusted_register ^ xor_mask
    
    # Step 5: Bitwise shift operations
    shifted_left = masked_register << 2
    shifted_right = shifted_left >> 1
    
    # Step 6: Final register optimization using bitwise AND with pattern
    pattern = 0b10101010
    optimized_register = shifted_right & pattern

print(f"Result: {optimized_register}")