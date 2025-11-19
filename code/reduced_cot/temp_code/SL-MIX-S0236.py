import math
from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def compute_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Character codes for a cryptographic key seed
seed_chars = [65, 66, 67, 68, 69]  # A, B, C, D, E

# Step 1: Generate all 3-character combinations
char_combinations = list(combinations(seed_chars, 3))

# Step 2: For each combination, compute a score based on number theory
combination_scores = []
for combo in char_combinations:
    a, b, c = combo
    # Compute LCM of first two
    lcm_ab = compute_lcm(a, b)
    # Compute GCD of result with third
    gcd_result = math.gcd(lcm_ab, c)
    # If the GCD is prime, square it; otherwise take log base 2
    if is_prime(gcd_result):
        score = gcd_result ** 2
    else:
        score = math.log2(gcd_result) if gcd_result > 0 else 0
    combination_scores.append(score)

# Step 3: Apply floating point operations to normalize scores
normalized_scores = [score / max(combination_scores) for score in combination_scores]

# Step 4: Use list comprehension to filter scores above threshold
threshold = 0.5
filtered_scores = [score for score in normalized_scores if score > threshold]

# Step 5: Compute final cipher strength using exponentiation
cipherStrength = 0
for i, score in enumerate(filtered_scores):
    cipherStrength += score * (2 ** i)

# Apply final transformation
cipherStrength = int(math.floor(cipherStrength * 1000))

print(f"Result: {cipherStrength}")