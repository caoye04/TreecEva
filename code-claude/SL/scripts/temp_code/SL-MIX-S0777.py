import itertools
import math

def is_prime(n):
    """Check if a number is prime"""
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

# Initialize data structures
target_number = 84
digit_sum = sum(int(d) for d in str(target_number))
common_divisors = [i for i in range(1, target_number + 1) if target_number % i == 0]

# Process some letter frequencies in a text (irrelevant operation)
text = "The quick brown fox jumps over the lazy dog"
letter_counts = {}
for char in text.lower():
    if char.isalpha():
        letter_counts[char] = letter_counts.get(char, 0) + 1

# Calculate Fibonacci numbers (distraction)
fib_sequence = [0, 1]
while len(fib_sequence) < 10:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
# Find prime factors (relevant operation)
prime_factors = []
temp_num = target_number
i = 2
while i * i <= temp_num:
    while temp_num % i == 0:
        prime_factors.append(i)
        temp_num //= i
    i += 1
    
# Handle remaining prime factor if exists
if temp_num > 1:
    prime_factors.append(temp_num)

# Process some combinations (distraction)
combos = list(itertools.combinations(range(5), 2))
combo_sums = [sum(combo) for combo in combos]

# Calculate some misleading values
false_result = sum(common_divisors) - sum(prime_factors)
distraction_value = sum(letter_counts.values())

# Create a dictionary with sliding windows (distraction)
windows = {}
for i in range(len(fib_sequence) - 2):
    window = fib_sequence[i:i+3]
    windows[i] = sum(window)

# Perform the key calculation
prime_sum = sum(prime_factors)

# More distractions after the key calculation
reversed_factors = prime_factors[::-1]
shifted_sum = sum([f << 1 for f in prime_factors])

# Misleading final calculations
final_result = false_result if digit_sum > 20 else prime_sum
alternative_result = distraction_value if is_prime(target_number) else prime_sum

print(f"Result: {prime_sum}")