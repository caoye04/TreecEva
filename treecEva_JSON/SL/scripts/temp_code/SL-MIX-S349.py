import math
import re

def process_tokens(token_list):
    # Step 1: Filter tokens that are purely numeric
    numeric_tokens = list(filter(lambda x: re.match(r'^\d+$', x), token_list))
    
    # Step 2: Convert to integers and apply exponentiation
    powered_values = list(map(lambda x: int(x) ** 2, numeric_tokens))
    
    # Step 3: Apply logarithmic scaling to each powered value
    scaled_values = list(map(lambda x: math.log(x + 1), powered_values))
    
    # Step 4: Convert to integer and perform bitwise XOR with a mask
    mask = 0b1101
    xor_results = list(map(lambda x: int(x) ^ mask, scaled_values))
    
    # Step 5: Sum all XOR results
    aggregated_sum = sum(xor_results)
    
    # Step 6: Apply modulus with a prime number
    prime = 23
    mod_result = aggregated_sum % prime
    
    # Step 7: Final transformation using exponentiation
    final_code = (mod_result ** 3) % 100
    
    return final_code

# Encoded tokens
encoded_tokens = ['abc123', '456def', '789', '12', 'test34', '56']

# Process the tokens
final_code = process_tokens(encoded_tokens)
print(f'Result: {final_code}')