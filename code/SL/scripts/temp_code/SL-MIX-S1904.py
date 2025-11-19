import math
from functools import reduce
from statistics import harmonic_mean

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def gcd_of_list(lst):
    return reduce(math.gcd, lst)

def lcm_of_list(lst):
    return reduce(lambda a, b: abs(a*b) // math.gcd(a, b), lst)

# Raw signal data from deep space observation
signal_amplitudes = [24, 36, 48, 60, 72]

# Step 1: Calculate prime factorization weights
prime_weights = list(map(lambda x: len(prime_factors(x)), signal_amplitudes))

# Step 2: Apply custom encryption scoring function
encryption_scores = {amp: sum(int(digit) for digit in str(amp)) for amp in signal_amplitudes}

# Step 3: Normalize scores using harmonic mean of prime weights
normalized_scores = {k: v / harmonic_mean(prime_weights) for k, v in encryption_scores.items()}

# Step 4: Calculate signal coherence using GCD and LCM
coherence_base = gcd_of_list(signal_amplitudes)
resonance_factor = lcm_of_list(signal_amplitudes)

# Step 5: Compute pattern recognition metric
pattern_strength = resonance_factor // coherence_base

# Step 6: Calculate extraterrestrial confidence score
signal_integrity = sum(normalized_scores.values())
extraterrestrial_confidence_score = int((signal_integrity * pattern_strength) ** 0.5) // 2

print(f"Result: {extraterrestrial_confidence_score}")