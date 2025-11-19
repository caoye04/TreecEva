from collections import defaultdict
import math

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# Generate prime coefficients for filter
prime_coeffs = generate_primes(30)[:8]

# Initialize filter state
filter_state = defaultdict(lambda: 0)

# Audio sample processing pipeline
audio_samples = [12, 25, 8, 33, 19, 42, 7, 28]
processed_signal = 0
mask_register = 0xF0

# Recursive filter function
filter_func = lambda x, n: (x * prime_coeffs[n % len(prime_coeffs)]) ^ filter_state[n-1] if n > 0 else x

for idx, sample in enumerate(audio_samples):
    # Apply bit masking
    masked_sample = sample & mask_register
    
    # Calculate log-weighted contribution
    if masked_sample > 0:
        weight = int(math.log2(masked_sample))
    else:
        weight = 1
    
    # Apply recursive filter
    filtered_value = filter_func(masked_sample, idx)
    
    # Update filter state with XOR combination
    filter_state[idx] = filtered_value ^ (weight << 2)
    
    # Accumulate processed signal with exponential scaling
    processed_signal += filtered_value * (2 ** (idx // 3))

# Final adjustment using GCD
final_adjustment = math.gcd(audio_samples[0], audio_samples[-1])
processed_signal = processed_signal >> final_adjustment

print(f"Result: {processed_signal}")