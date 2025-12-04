def generate_primes(limit):
    """Generate prime numbers up to limit using Sieve of Eratosthenes"""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(limit + 1) if sieve[i]]

def generate_fibonacci(count):
    """Generate first count Fibonacci numbers"""
    fib = [0, 1]
    for i in range(2, count):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Generate data sets
max_value = 100
fibonacci_count = 15

primes = generate_primes(max_value)
fibonacci = generate_fibonacci(fibonacci_count)

# Create distractor sets
even_numbers = set(range(0, max_value + 1, 2))
odd_numbers = set(range(1, max_value + 1, 2))
multiples_of_three = set(range(0, max_value + 1, 3))

# Apply filters (distractors)
divisible_by_seven = set([x for x in range(1, max_value + 1) if x % 7 == 0])
square_numbers = set([x*x for x in range(1, int(max_value**0.5) + 1)])

# Filter prime numbers - only keep those that satisfy the condition
filter_condition = lambda x: (x % 4 == 1 or x % 4 == 3) and x > 10
filtered_primes = [p for p in primes if filter_condition(p)]

# Process Fibonacci numbers (more distractors)
fib_squared = [f**2 for f in fibonacci]
fib_plus_one = [f+1 for f in fibonacci]

# Apply complex transformations to fibonacci (mostly distractors)
transformed_fib = []
for f in fibonacci:
    if f % 2 == 0:
        transformed_fib.append(f + 3)
    else:
        transformed_fib.append(f * 2)

# Misleading calculation (distractor)
potential_intersection = set(primes).intersection(set(fibonacci))
false_result = len(potential_intersection) * 5

# Apply another filter to fibonacci
filtered_fibonacci = [f for f in fibonacci if f > 5 and f < 60]

# Create misleading set operations (distractors)
union_set = even_numbers.union(multiples_of_three)
intersection_distractor = odd_numbers.intersection(square_numbers)
symmetric_diff = divisible_by_seven.symmetric_difference(square_numbers)

# The key calculation
common_elements = set(filtered_primes).intersection(filtered_fibonacci)

# More distractors after the key calculation
final_result = len(common_elements) + len(symmetric_diff)
complex_formula = sum(filtered_primes) - sum(filtered_fibonacci)
weighted_average = (sum(filtered_primes) * 0.7 + sum(filtered_fibonacci) * 0.3) / (len(filtered_primes) + len(filtered_fibonacci))

# Print results
print(f"Filtered primes: {filtered_primes}")
print(f"Filtered fibonacci: {filtered_fibonacci}")
print(f"Common elements: {common_elements}")
print(f"Result: {len(common_elements)}")