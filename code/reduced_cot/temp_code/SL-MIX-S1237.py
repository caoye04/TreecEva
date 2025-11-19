import math

def process_token_sequence(tokens):
    # Parse and tokenize input
    parsed_tokens = [token.strip().lower() for token in tokens.split(',')]
    
    # Apply string transformations
    transformed_tokens = [
        ''.join(chr((ord(c) * 3 + 5) % 256) for c in token)
        for token in parsed_tokens
    ]
    
    # Convert to numeric values using polynomial hashing
    hash_values = [
        sum(ord(c) * (31 ** i) for i, c in enumerate(token))
        for token in transformed_tokens
    ]
    
    # Apply modular arithmetic with prime modulus
    prime_modulus = 97
    mod_hash_values = [
        (hash_val * 17 + 23) % prime_modulus
        for hash_val in hash_values
    ]
    
    # Compute floating point weighted average
    weights = [math.log(i + 2) for i in range(len(mod_hash_values))]
    if sum(weights) == 0:
        weighted_avg = 0.0
    else:
        weighted_avg = sum(val * weight for val, weight in zip(mod_hash_values, weights)) / sum(weights)
    
    # Final verification code calculation
    verification_code = int(round(weighted_avg * 13.7) % 1000)
    return verification_code

# Input sequence
input_sequence = "Alpha,Beta,Gamma,Delta,Epsilon"
verification_code = process_token_sequence(input_sequence)
print(f"Result: {verification_code}")