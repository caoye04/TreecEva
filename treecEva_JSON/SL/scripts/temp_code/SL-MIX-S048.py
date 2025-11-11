from itertools import combinations

def transform_sequence(bits, depth=0):
    if depth >= 3:
        return bits
    
    # Apply XOR folding
    folded = 0
    for i in range(len(bits)):
        folded ^= bits[i] << (i % 8)
    
    # Generate combinatorial mask
    mask_elements = list(combinations(range(8), 3))
    comb_mask = 0
    for idx in mask_elements[depth if depth < len(mask_elements) else -1]:
        comb_mask |= (1 << idx)
    
    # Apply mask and shift
    masked = folded & comb_mask
    shifted = masked >> (depth + 1)
    
    # Recursive call with modified sequence
    new_bits = [(shifted >> i) & 1 for i in range(8)]
    return transform_sequence(new_bits, depth + 1)

# Initial bit sequence for encryption
initial_bits = [1, 0, 1, 1, 0, 1, 0, 0]
transformed = transform_sequence(initial_bits)

# Compute security key from transformed bits
security_key = 0
for i, bit in enumerate(transformed):
    security_key |= (bit << i)
    
print(f"Result: {security_key}")