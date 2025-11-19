from functools import reduce
from itertools import combinations

def modular_power(base, exp, mod):
    return pow(base, exp, mod)

def compute_coefficients(sequence):
    # Generate all 2-element combinations and compute their products
    combo_products = [a * b for a, b in combinations(sequence, 2)]
    # Apply modular arithmetic to each product
    mod_products = [p % 17 for p in combo_products]
    # Sum all modular products
    return sum(mod_products) % 17

def transform_value(initial, coeffs):
    # Apply a series of transformations using modular arithmetic
    transformed = initial
    for i, coeff in enumerate(coeffs):
        transformed = (transformed * coeff + i) % 19
    return transformed

def cryptographic_hash(initial_value, data_sequence):
    # Step 1: Compute coefficients from data sequence
    coefficients = compute_coefficients(data_sequence)
    
    # Step 2: Generate a secondary transformation sequence
    secondary_seq = [modular_power(x, 3, 13) for x in data_sequence]
    
    # Step 3: Apply transformations
    interim_result = transform_value(initial_value, secondary_seq)
    
    # Step 4: Apply final transformation using coefficients
    final_hash = (interim_result * coefficients + 7) % 23
    
    return final_hash

# Execution
sensor_readings = [4, 7, 2, 9, 5]
baseline_value = 11
final_hash = cryptographic_hash(baseline_value, sensor_readings)
print(f"Result: {final_hash}")