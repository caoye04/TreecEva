def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes_less_than(n):
    return sum(1 for i in range(2, n) if is_prime(i))

def sum_of_divisors(n):
    return sum(i for i in range(1, n+1) if n % i == 0)

# Compute base scores using dictionary comprehension
node_base_scores = {
    n: sum_of_divisors(n) if not is_prime(n) else count_primes_less_than(n)
    for n in range(2, 11)
}

# Adjust scores using ternary-like logic
adjusted_scores = [
    score * 2 if score % 3 == 0 else
    score + 5 if score % 3 == 1 else
    score
    for score in node_base_scores.values()
]

# Apply lambda filter and aggregate
filter_and_sum = lambda scores: sum(s for s in scores if s > 10)
aggregated_trust_score = filter_and_sum(adjusted_scores)

print(f"Result: {aggregated_trust_score}")