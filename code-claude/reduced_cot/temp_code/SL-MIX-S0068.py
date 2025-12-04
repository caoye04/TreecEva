from collections import Counter, defaultdict
import math

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

def generate_sequence(start, end, step):
    # Generate a sequence for cryptographic analysis
    return [x for x in range(start, end, step)]

def analyze_distribution(values):
    # Analyze frequency distribution (distractor function)
    frequencies = Counter(values)
    entropy = sum([-count/len(values) * math.log2(count/len(values)) for count in frequencies.values()])
    return entropy, frequencies.most_common(3)

def calculate_strength(prime_factors):
    # Calculate encryption strength based on prime factors
    if not prime_factors:
        return 0
    
    bit_strength = 0
    for prime in prime_factors:
        # Each prime contributes to bit strength based on its value
        bit_strength += math.log2(prime)
    
    # Adjust for redundancy
    return int(bit_strength)

# Initialize cryptographic parameters
base_range = [10, 20, 30, 40, 50, 60]
modifier = 7
key_length = 256
security_threshold = 128

# Generate potential prime candidates
candidates = generate_sequence(11, 100, 2)
candidates_backup = [x for x in range(20, 80) if x % 3 == 1]  # Backup candidates (distractor)

# Track various metrics for analysis
metrics = defaultdict(int)
for c in candidates:
    metrics[c % 10] += 1

# Filter for prime numbers
primes = []
composite_count = 0
for num in candidates:
    if is_prime(num):
        primes.append(num)
    else:
        composite_count += 1

# Apply security filters based on bit patterns
bit_patterns = [bin(p)[2:].count('1') for p in primes]  # Count set bits
pattern_entropy, common_patterns = analyze_distribution(bit_patterns)

# Filter primes based on security requirements
security_coefficient = (pattern_entropy * 10) // 3  # Distractor calculation
filtered_primes = [p for p in primes if p > 30 and p < 80]

# Calculate final encryption strength
raw_strength = sum(filtered_primes) / len(filtered_primes)  # Distractor calculation
encryption_strength = calculate_strength(filtered_primes)

# Apply additional security adjustments (distractors)
adjusted_strength = encryption_strength * (1 + pattern_entropy / 10)
if security_coefficient > 5:
    adjusted_strength += security_coefficient

# Final security assessment
security_rating = "HIGH" if encryption_strength > security_threshold else "MODERATE"
print(f"Result: {encryption_strength}")