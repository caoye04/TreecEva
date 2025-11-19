import math
import itertools

def transform_sequence(value, operations):
    result = value
    for op in operations:
        if op == 'exp':
            result = math.exp(result) if result < 10 else result
        elif op == 'log':
            result = math.log(result) if result > 0 else result + 1
        elif op == 'xor':
            result = int(result) ^ 0xF0
        elif op == 'shift':
            result = int(result) << 2 if int(result) < 100 else int(result) >> 1
    return result

def generate_verification_key(seed_values, transform_ops):
    active_transformations = []
    verification_components = set()
    
    # Process seed values with conditional transformations
    for i, seed in enumerate(seed_values):
        if seed > 0 and (i < len(transform_ops) and transform_ops[i] != 'skip'):
            transformed = transform_sequence(seed, [transform_ops[i]])
            active_transformations.append(transformed)
            verification_components.add(int(transformed))
    
    # Apply combinatorial mixing using itertools
    mixed_values = []
    for combo in itertools.combinations(active_transformations, min(2, len(active_transformations))):
        combo_result = combo[0]
        for val in combo[1:]:
            combo_result = combo_result + val if combo_result * val < 1000 else combo_result - val
        mixed_values.append(combo_result)
    
    # Final key derivation with short-circuit evaluation
    final_sum = sum(mixed_values)
    verification_key = 0
    
    if final_sum > 0 and (len(verification_components) > 1 or len(mixed_values) == 0):
        component_factor = len(verification_components) if len(verification_components) > 0 else 1
        verification_key = int(final_sum * math.log(component_factor)) if component_factor > 1 else final_sum
    else:
        verification_key = -1
    
    return verification_key

# Initial system parameters
initial_seeds = [2.5, 3.0, -1.0, 5.5]
operation_sequence = ['exp', 'log', 'skip', 'xor']

# Generate the verification key
verification_key = generate_verification_key(initial_seeds, operation_sequence)
print(f"Result: {verification_key}")