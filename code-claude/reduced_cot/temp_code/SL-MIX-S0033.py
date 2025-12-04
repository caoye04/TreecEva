import itertools

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

def generate_fibonacci(limit):
    """Generate Fibonacci sequence up to limit"""
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def calculate_product_of_filtered_primes(numbers):
    """Calculate product of prime numbers that meet certain criteria"""
    # Generate some Fibonacci numbers for distraction
    fibonacci = generate_fibonacci(100)
    
    # Filter operation that seems important but isn't used
    filtered_fibonacci = [f for f in fibonacci if f % 3 != 0]
    
    # Create sets for efficient lookups (distraction)
    number_set = set(numbers)
    fib_set = set(fibonacci)
    common_elements = number_set.intersection(fib_set)
    
    # This looks important but is unused
    bitwise_sum = 0
    for num in common_elements:
        bitwise_sum |= num
    
    # The actual filtering we care about
    primes = [num for num in numbers if is_prime(num)]
    
    # More distraction with itertools
    pairs = list(itertools.combinations(primes, 2))
    max_pair_sum = 0
    if pairs:
        max_pair_sum = max(sum(pair) for pair in pairs)
    
    # Distraction: calculate factors of a number
    factors_of_30 = [i for i in range(1, 31) if 30 % i == 0]
    
    # Misleading intermediate calculation
    if len(primes) >= 3:
        potential_result = primes[0] * primes[2]
    else:
        potential_result = 1
    
    # The actual calculation we care about
    result = 1
    for prime in primes:
        if prime > 10 and prime < 50:
            result *= prime
    
    # More distraction
    for i in range(min(3, len(primes))):
        if i % 2 == 0 and primes[i] < 20:
            # This branch is never taken for our input
            if primes[i] == 17:
                result = result * 2
                break
    
    return result

# Main execution
numbers = [4, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51, 53]

# Distraction: calculate digit sums
digit_sums = {}
for num in numbers:
    digit_sum = sum(int(digit) for digit in str(num))
    digit_sums[num] = digit_sum

# Distraction: find numbers with specific properties
special_nums = [num for num in numbers if num % 10 == 3 or num % 10 == 7]

# Calculate prime product - this is what we care about
prime_product = calculate_product_of_filtered_primes(numbers)

# More distraction after the target calculation
bit_counts = {}
for num in numbers:
    bit_counts[num] = bin(num).count('1')

# Final distracting calculation that seems important
final_sum = sum(num for num in numbers if bit_counts[num] > 2)

print(f"Result: {prime_product}")