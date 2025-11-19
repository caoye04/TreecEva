import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def harmonic_stability_window(frequencies):
    n = len(frequencies)
    if n < 2:
        return 0
    
    # Calculate GCD of all frequencies as baseline stability
    base_stability = gcd_list(frequencies)
    
    # Find window with maximum harmonic mean adjusted by variance
    max_stability = 0
    optimal_window = []
    
    # Sliding window approach with divide and conquer concept
    for i in range(n):
        for j in range(i+2, min(i+6, n+1)):  # Limit window size for efficiency
            window = frequencies[i:j]
            harmonic_mean = len(window) / sum(1/x for x in window if x != 0)
            variance = sum((x - harmonic_mean)**2 for x in window) / len(window)
            
            # Stability calculation combines harmonic properties with variance
            window_stability = (harmonic_mean * base_stability) / (1 + variance)
            
            if window_stability > max_stability:
                max_stability = window_stability
                optimal_window = window
    
    # Final adjustment using prime factor analysis
    prime_factors_count = sum(len([i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0]) for x in optimal_window)
    
    return max_stability * (1 + prime_factors_count/len(optimal_window) if optimal_window else 0)

def signal_analysis_protocol(observations):
    # Filter valid signals (non-zero and within detectable range)
    valid_signals = [s for s in observations if 10 <= s <= 10000]
    
    # Apply stability analysis
    raw_stability = harmonic_stability_window(valid_signals)
    
    # Apply correction factors based on signal distribution
    even_count = sum(1 for s in valid_signals if s & 1 == 0)  # Bitwise check for even
    odd_count = len(valid_signals) - even_count
    
    parity_correction = 1.0
    if even_count > 0 and odd_count > 0:
        parity_correction = (even_count / odd_count) if odd_count > even_count else (odd_count / even_count)
    
    return raw_stability * parity_correction

# Deep space observation data
space_observations = [120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200, 1320, 1440]

# Process the observations
stability_index = signal_analysis_protocol(space_observations)

print(f"Result: {int(stability_index)}")