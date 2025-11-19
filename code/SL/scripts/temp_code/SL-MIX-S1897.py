from collections import Counter

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

text_fragments = [
    "ABRACADABRA",
    "ALAKAZAM",
    "BIBBIDYBOBBIDYBOO",
    "HALLELUJAH"
]

# Get first 30 Fibonacci numbers
fib_numbers = fibonacci_sequence(30)

# Find indices that are prime numbers
prime_indices = [i for i in range(len(fib_numbers)) if is_prime(i)]

# Get Fibonacci numbers at prime indices
prime_indexed_fibs = [fib_numbers[i] for i in prime_indices]

# Count characters across all fragments
char_counter = Counter()
for fragment in text_fragments:
    char_counter.update(fragment)

# Calculate cryptographic checksum
cryptographic_checksum = 0
for char, count in char_counter.items():
    # Get ASCII value of character
    ascii_val = ord(char)
    # Find character's position in alphabet (A=1, B=2, ...)
    if 'A' <= char <= 'Z':
        alpha_pos = ord(char) - ord('A') + 1
    elif 'a' <= char <= 'z':
        alpha_pos = ord(char) - ord('a') + 1
    else:
        alpha_pos = 0
    
    # Use character count and alphabet position
    if alpha_pos > 0 and alpha_pos <= len(prime_indexed_fibs):
        fib_value = prime_indexed_fibs[alpha_pos - 1]
        contribution = (count * fib_value * ascii_val) % 10007
        cryptographic_checksum = (cryptographic_checksum + contribution) % 10007

print(f"Result: {cryptographic_checksum}")