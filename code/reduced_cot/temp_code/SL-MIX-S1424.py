from math import gcd
from itertools import combinations

def compute_wavelet_coefficients(samples):
    n = len(samples)
    coefficients = []
    for i in range(n-1):
        diff = samples[i+1] - samples[i]
        coefficients.append(diff * 2 if diff > 0 else diff // 2)
    return coefficients

def aggregate_signature(coeffs):
    xor_accum = 0
    for c in coeffs:
        if c == 0:
            continue
        elif c > 0:
            xor_accum ^= c
        else:
            xor_accum &= (c + 256)  # Ensure positive bitwise op
    return xor_accum

# Simulated input signal samples
raw_samples = [13, 22, 18, 30, 26, 32, 28, 36]
filtered_samples = [s for s in raw_samples if s % 2 == 0]
wavelet_coeffs = compute_wavelet_coefficients(filtered_samples)
signature = aggregate_signature(wavelet_coeffs)

# Compute processed signal strength using number theory
processed_signal_strength = 0
for i in range(1, min(signature, 20)):
    if signature & (1 << i):  # Bit check
        lcm_val = (signature * i) // gcd(signature, i)
        processed_signal_strength += lcm_val if lcm_val < 100 else 0

print(f"Result: {processed_signal_strength}")