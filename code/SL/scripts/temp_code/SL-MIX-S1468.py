import re
from functools import reduce

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def process_message(msg):
    # Convert characters to ASCII values
    ascii_vals = [ord(c) for c in msg]
    
    # Generate Fibonacci weights for each position
    fib_weights = list(fibonacci_sequence(len(ascii_vals)))
    
    # Apply weighted transformation
    weighted_chars = [
        val * fib_weights[i] if fib_weights[i] > 0 else val
        for i, val in enumerate(ascii_vals)
    ]
    
    # Filter values using regex pattern matching on their string representations
    filtered_values = list(filter(lambda x: re.match(r'^[5-8]', str(x)), weighted_chars))
    
    # Apply ternary transformation
    transformed = [
        x//2 if x % 2 == 0 else (x*3)+1 for x in filtered_values
    ]
    
    # Reduce using a custom lambda function
    result = reduce(lambda acc, curr: acc ^ curr, transformed, 0)
    
    return result

# Main execution
message = "SECURITY"
cryptographic_signature = process_message(message)
print(f"Target result: {cryptographic_signature}")