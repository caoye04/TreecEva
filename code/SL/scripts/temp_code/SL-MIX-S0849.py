def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 12 Fibonacci numbers
fib_gen = fibonacci_sequence(12)
fib_numbers = [next(fib_gen) for _ in range(12)]

# Convert each to hexadecimal (without '0x' prefix)
hex_strings = [hex(num)[2:] for num in fib_numbers]

# Concatenate all hex strings
concatenated_hex = ''.join(hex_strings)

# Reverse the concatenated string
reversed_hex = concatenated_hex[::-1]

# Count numeric characters in reversed string
numeric_count = sum(1 for char in reversed_hex if char.isdigit())

print(f"Target result: {numeric_count}")