def generate_fibonacci(limit):
    fib_seq = [1, 1]
    while fib_seq[-1] + fib_seq[-2] <= limit:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

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

def get_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors

# Analyzing molecular weights in chemistry experiment
base_elements = {"H": 1, "C": 12, "N": 14, "O": 16, "P": 31, "S": 32}
element_counts = {"H": 12, "C": 22, "N": 2, "O": 4, "P": 0, "S": 1}

# Calculate molecular weight (distraction)
molecular_weight = sum(base_elements[e] * element_counts[e] for e in element_counts)

# Analyze numerical properties
target_number = 120
factors = []
for i in range(1, target_number + 1):
    if target_number % i == 0:
        factors.append(i)

prime_candidates = [x for x in range(2, 50)]
prime_numbers = [x for x in prime_candidates if is_prime(x)]

# Distraction calculations
sum_of_primes = sum(prime_numbers)
product_of_first_five = 1
for i in range(min(5, len(prime_numbers))):
    product_of_first_five *= prime_numbers[i]

# Main logic for analysis
prime_factors = get_prime_factors(target_number)
fibonacci_sequence = generate_fibonacci(40)

# Distraction set operations
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
odd_primes = {p for p in prime_numbers if p > 2}
distraction_set = even_numbers ^ odd_primes

# Critical calculation
unique_elements = len(set(prime_factors) & set(fibonacci_sequence))

# More distractions
combined_sequence = sorted(list(set(prime_factors).union(set(fibonacci_sequence))))
ratio = sum(combined_sequence) / len(combined_sequence) if combined_sequence else 0

# Misleading calculation with similar variable name
unique_element_pairs = [(x, y) for x in prime_factors for y in fibonacci_sequence if x < y]
unique_element_count = len(unique_element_pairs)

# Alternative calculation to confuse
potential_result = len(set(prime_factors).symmetric_difference(set(fibonacci_sequence)))

print(f"Target result: {unique_elements}")
