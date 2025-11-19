from functools import reduce
from statistics import variance

def custom_hash_transform(block_data):
    # Step 1: Filter out negative numbers and zero
    positive_values = list(filter(lambda x: x > 0, block_data))
    
    # Step 2: Apply XOR folding to reduce the data
    folded_value = reduce(lambda acc, x: acc ^ (x << 2), positive_values, 0)
    
    # Step 3: Compute statistical dispersion measure
    if len(positive_values) > 1:
        disp_measure = int(variance(positive_values) * 100) & 0xFF
    else:
        disp_measure = 0x7F
    
    # Step 4: Apply bit rotation and modular arithmetic
    rotated = ((folded_value >> 3) | (folded_value << 29)) & 0xFFFFFFFF
    mod_result = rotated % 997  # 997 is a prime number
    
    # Step 5: Combine with dispersion measure using OR operation
    combined = mod_result | (disp_measure << 16)
    
    # Step 6: Finalize with bit masking
    final_hash = combined & 0xFFFFFF
    return final_hash

# Transaction block data
transaction_block = [12, -5, 0, 42, 18, 73, -9, 255, 1001, 8]

# Process the block
global_hash_state = custom_hash_transform(transaction_block)

# Additional transformation using context manager
from contextlib import contextmanager

@contextmanager
def hash_enhancer(initial_hash):
    enhanced = initial_hash ^ 0xDEADBEEF
    try:
        yield enhanced
    finally:
        pass

with hash_enhancer(global_hash_state) as enhanced_hash:
    # Final adjustment using bit shifting and addition
    final_hash = (enhanced_hash >> 4) + (enhanced_hash & 0xF)

print(f"Result: {final_hash}")