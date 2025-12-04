def calculate_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def binary_digits(n):
    # Count the number of 1s in binary representation
    return bin(n).count('1')

def is_relevant(x):
    # Only numbers with an odd number of binary 1s and that are prime
    return binary_digits(x) % 2 == 1 and is_prime(x)

# Main calculation
base_values = [11, 13, 17, 19, 23, 29, 31, 37]
decoy_values = [4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generate Fibonacci numbers - not directly used in final calculation
fib_nums = fibonacci(10)
distractor_sum = sum(fib_nums[2:8])

# Calculate some composite numbers
composite_sum = 0
for i in range(4, 20, 2):
    if not is_prime(i):
        composite_sum += i
        
# Create set operations for distraction
set_a = {2, 3, 5, 7, 11, 13}
set_b = {3, 5, 7, 9, 11}
set_intersection = set_a & set_b
set_union = set_a | set_b
union_product = 1
for num in set_union:
    union_product *= num
    
# More distraction calculations
potential_values = [x**2 for x in range(2, 8)]
transformed = [(x + 2) * 3 - 5 for x in potential_values]

# This looks important but isn't used for final answer
key_value = (union_product % 100) + (composite_sum // 4)
distractor_result = key_value ^ (distractor_sum & 0xFF)

# Generate potential prime numbers for analysis
potential_primes = []
for base in base_values:
    # Add the base value
    potential_primes.append(base)
    
    # Add a transformed version that may not be prime
    if base % 10 == 1 or base % 10 == 9:
        potential_primes.append(base + 4)

# This is the key calculation
filtered_prime_sum = sum([x for x in potential_primes if is_relevant(x)])

# More distraction
final_distractor = 0
if distractor_result > 100:
    final_distractor = distractor_result // 2
else:
    final_distractor = distractor_result * 3
    
# Combine results in a misleading way
false_result = (final_distractor + filtered_prime_sum) % 256

# Print the key result
print(f"Result: {filtered_prime_sum}")