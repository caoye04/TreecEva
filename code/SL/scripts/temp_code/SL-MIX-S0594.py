import itertools

def calculate_bitwise_pattern():
    base_values = [5, 12, 9, 7]
    pairs = list(itertools.combinations(base_values, 2))
    
    x = 0
    y = 0
    
    for pair in pairs:
        temp_xor = pair[0] ^ pair[1]
        if temp_xor > x:
            x = temp_xor
            y = pair[0] & pair[1]
            break
    
    final_value = x ^ y
    print(f"Target result: {final_value}")

calculate_bitwise_pattern()