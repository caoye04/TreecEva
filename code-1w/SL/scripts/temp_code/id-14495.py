import math

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    return sum(-p * math.log2(p) for p in data if p > 0)

# Misleading data initialization
temp_readings = [23.5, 24.1, 22.9, 25.0, 26.3, 21.7]
offset_adjustment = sum(temp_readings) / len(temp_readings)
entropy_proxy = offset_adjustment * 0.87

# Core logic disguised among distractors
sequence_limit = 100
even_candidates = {n for n in range(2, sequence_limit) if n % 2 == 0}
odd_shifted = {n + 1 for n in even_candidates}
fibonacci_cache = [0, 1]

# Generate Fibonacci numbers up to limit (partially relevant)
while fibonacci_cache[-1] + fibonacci_cache[-2] < sequence_limit:
    next_fib = fibonacci_cache[-1] + fibonacci_cache[-2]
    fibonacci_cache.append(next_fib)

# Build irrelevant transformation map
transform_map = {}
for idx, val in enumerate(fibonacci_cache):
    transform_map[idx] = val ** 2 - idx

# Prime number generation (critical component)
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return set(i for i, is_prime in enumerate(sieve) if is_prime)

prime_pool = generate_primes(sequence_limit)

# Complex filtering with red herring conditions
validity_flags = []
for num in range(10, 85):
    condition_a = (num in fibonacci_cache)
    condition_b = (num % 7 != 0)
    condition_c = (sum(int(d) for d in str(num)) < 13)
    validity_flags.append(condition_a and condition_b and condition_c)

# Actual qualification criteria (non-obvious)
qualified_set = {n for n in range(10, 90) if n % 6 == 0 and (n + 5) in prime_pool}

# Secondary decoy set using set operations (irrelevant)
decoys = {x for x in odd_shifted if x % 5 == 0}
shadow_filter = decoys | {x*2 for x in fibonacci_cache if x > 10}
overlap_score = len(shadow_filter & even_candidates)  # misleading metric

# Key computational step
filtration_score = len(qualified_set & prime_pool)

# Final output
print(f"Result: {filtration_score}")