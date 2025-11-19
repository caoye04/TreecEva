from itertools import permutations
from functools import reduce
import operator

def crypto_prep_routine():
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    all_perms = list(permutations(symbols))
    
    # Key derivation using bitwise operations
    key_components = [0b1101, 0b1010, 0b0110]
    derived_key = reduce(operator.xor, key_components) & 0xF
    
    # Skip initial permutations based on derived key
    skip_count = derived_key * 2
    
    # Early termination condition for invalid skips
    if skip_count >= len(all_perms):
        return -1
    
    # Find first permutation with specific property
    target_pattern = ('A', 'B', 'C')
    selected_permutation_index = -1
    
    for i in range(skip_count, len(all_perms)):
        perm = all_perms[i]
        if perm[:3] == target_pattern:
            selected_permutation_index = i
            break
    
    return selected_permutation_index

result = crypto_prep_routine()
print(f"Result: {result}")