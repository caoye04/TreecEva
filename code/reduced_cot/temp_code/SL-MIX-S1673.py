from itertools import product

def simulate_circuit(inputs):
    # Lookup table for caching results
    cache = {}
    
    def compute_gate(a, b, c):
        key = (a, b, c)
        if key in cache:
            return cache[key]
        
        # Custom gate logic
        temp1 = (a & b) ^ c
        temp2 = (a | c) & (~b & 0xF)
        result = (temp1 << 1) ^ temp2
        
        cache[key] = result
        return result
    
    accumulator = 0
    for i, (x, y, z) in enumerate(inputs):
        if i > 0 and inputs[i-1] == (0, 0, 0):
            break
        
        output = compute_gate(x, y, z)
        
        # Conditional modification based on previous state
        if accumulator & 0x8:
            output ^= 0xF
        
        accumulator = (accumulator << 2) | (output & 0x3)
        accumulator &= 0xFF  # Keep only 8 bits
    
    return accumulator

# Generate all possible 3-bit input combinations
input_combinations = list(product([0, 1], repeat=3))

# Add a sentinel value to test the break condition
input_combinations.append((0, 0, 0))
input_combinations.extend([(1, 0, 1), (0, 1, 1)])

final_output = simulate_circuit(input_combinations)
print(f"Result: {final_output}")