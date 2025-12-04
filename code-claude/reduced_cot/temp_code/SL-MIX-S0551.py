import itertools
from math import gcd

def is_prime(n):
    """Check if a number is prime."""
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
    """Generate first n Fibonacci numbers."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def calculate_lcm(x, y):
    """Calculate the least common multiple of two numbers."""
    return x * y // gcd(x, y)

def calculate_result(numbers):
    """Calculate the product of numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result

# Generate a sequence of numbers for processing
base_numbers = [i for i in range(1, 20)]

# Extract even numbers and calculate their sum
even_numbers = [x for x in base_numbers if x % 2 == 0]
even_sum = sum(even_numbers)

# Generate Fibonacci sequence and find those divisible by 3
fib_sequence = fibonacci(12)
fib_divisible_by_three = [num for num in fib_sequence if num > 0 and num % 3 == 0]
fib_product = calculate_result(fib_divisible_by_three)

# Find prime numbers in the original sequence
prime_candidates = [num for num in base_numbers if num > 1]
prime_numbers = [num for num in prime_candidates if is_prime(num)]

# Create sets for bitwise operations
set_a = set(range(5, 15))
set_b = set(range(10, 20))
set_intersection = set_a & set_b

# Calculate LCM of the first few numbers
lcm_result = 1
for i in range(2, 5):
    lcm_result = calculate_lcm(lcm_result, i)

# Combine different sequences using itertools
combined = list(itertools.chain(prime_numbers, [lcm_result]))

# Perform some misleading calculations
temporary_result = fib_product + even_sum
if temporary_result > 100:
    misleading_value = temporary_result % 7
else:
    misleading_value = temporary_result % 5

# Filter numbers based on complex conditions
filtered_numbers = []
for num in combined:
    if num % 2 == 1:  # Only odd numbers
        if num in set_intersection:
            filtered_numbers.append(num * 2)  # Misleading calculation
        else:
            filtered_numbers.append(num)

# This is where we calculate our target result
prime_product = calculate_result(filtered_numbers)

# Some more calculations to confuse
final_sequence = [x for x in range(misleading_value, misleading_value + 5)]
final_sum = sum(final_sequence)

# Calculate another misleading result
alternate_result = prime_product % final_sum
if alternate_result > prime_product:
    final_output = alternate_result
else:
    final_output = prime_product

print(f"Result: {prime_product}")