def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Initialize transformation parameters
mask_pattern = 0b1010101
shift_direction = 1
artistic_signature = 0

# Process first 12 Fibonacci numbers
for i, fib_num in enumerate(fibonacci_sequence(12)):
    # Apply bitwise transformation with shifting mask
    if shift_direction:
        transformed = fib_num ^ (mask_pattern << (i % 5))
    else:
        transformed = fib_num ^ (mask_pattern >> (i % 5))
    
    # Update accumulator with XOR combination
    artistic_signature ^= transformed
    
    # Toggle shift direction every 3 steps
    if (i + 1) % 3 == 0:
        shift_direction = 1 - shift_direction

print(f"Result: {artistic_signature}")