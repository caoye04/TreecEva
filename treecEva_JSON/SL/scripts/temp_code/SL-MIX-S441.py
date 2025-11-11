import math
from itertools import combinations
from statistics import variance

# Sampled waveform data
samples = [12, 7, 23, 8, 15, 3, 19, 5]

# Step 1: Apply modular transformation with XOR
mod_samples = [(x ^ 0b1101) % 16 for x in samples]

# Step 2: Generate all 3-element combinations and compute their bitwise AND
comb_results = [math.prod(c) & 0b1111 for c in combinations(mod_samples, 3)]

# Step 3: Filter combinations with even parity (even number of 1s in binary representation)
even_parity = [x for x in comb_results if bin(x).count('1') % 2 == 0]

# Step 4: Compute variance of filtered results
var_value = variance(even_parity) if len(even_parity) > 1 else 0

# Step 5: Apply ternary operation based on variance
processed = var_value > 10 and math.floor(var_value) or math.ceil(var_value)

# Step 6: Final signature calculation using modular arithmetic
wave_signature = (int(processed) * 0b1011 + sum(mod_samples)) % 31

print(f"Result: {wave_signature}")