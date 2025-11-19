import hashlib
import itertools

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def encode_with_fibonacci_mask(text):
    fib_values = list(fibonacci_sequence(len(text)))
    encoded = []
    for i, char in enumerate(text):
        char_code = ord(char)
        masked_code = char_code ^ fib_values[i]  # XOR with Fibonacci number
        encoded.append(masked_code)
    return encoded

def generate_permutation_hash(numbers):
    # Generate all permutations of the first 3 numbers
    perms = list(itertools.permutations(numbers[:3]))
    hash_sum = 0
    for perm in perms:
        product = 1
        for num in perm:
            product *= num
        hash_sum += product
    return hash_sum

def custom_hash_function(transaction_id):
    # Step 1: Encode the transaction ID with Fibonacci mask
    encoded_chars = encode_with_fibonacci_mask(transaction_id)
    
    # Step 2: Generate a permutation-based hash from the first 4 encoded values
    perm_hash = generate_permutation_hash(encoded_chars[:4])
    
    # Step 3: Apply bitwise operations
    shifted_hash = perm_hash << 2  # Left shift by 2
    masked_hash = shifted_hash & 0xFFFF  # Apply 16-bit mask
    
    # Step 4: Incorporate string hash of the original transaction ID
    string_hash = hash(transaction_id) & 0xFF  # Lower 8 bits of Python's hash
    
    # Step 5: Combine all components
    final_hash_code = masked_hash ^ string_hash
    
    return final_hash_code

# Main execution
transaction_identifier = "TX-9A2F"
final_hash_code = custom_hash_function(transaction_identifier)
print(f"Result: {final_hash_code}")