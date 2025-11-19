from math import gcd, sqrt
from statistics import mean, variance

def compute_detection_score(frequencies):
    # Step 1: Filter valid frequencies using lambda and statistical analysis
    avg_freq = mean(frequencies)
    var_freq = variance(frequencies)
    threshold = avg_freq + sqrt(var_freq)
    
    valid_freqs = list(filter(lambda x: x > threshold, frequencies))
    
    # Step 2: Calculate harmonic relationships using number theory
    if len(valid_freqs) < 2:
        return 0
    
    harmonic_sum = 0
    for i in range(len(valid_freqs)-1):
        for j in range(i+1, len(valid_freqs)):
            g = gcd(int(valid_freqs[i]), int(valid_freqs[j]))
            if g > 1:
                harmonic_sum += g
    
    # Step 3: Apply noise reduction based on set operations
    noise_profile = {2, 3, 5, 7, 11, 13}
    freq_primes = frozenset({f for f in valid_freqs if f == int(f) and is_prime(int(f))})
    
    # Step 4: Compute interference factor
    interference = len(noise_profile & freq_primes)
    
    # Step 5: Switch-based signal classification
    signal_class = classify_signal(harmonic_sum)
    
    # Step 6: Calculate final score with early returns
    if signal_class == 'weak':
        return harmonic_sum // 2 - interference
    elif signal_class == 'moderate':
        return harmonic_sum - interference * 2
    else:  # strong
        return harmonic_sum * 2 - interference

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def classify_signal(value):
    if value < 50:
        return 'weak'
    elif value < 150:
        return 'moderate'
    else:
        return 'strong'

# Main execution
sensor_readings = [23.5, 45.2, 67.8, 89.1, 101.3, 127.9, 131.7, 149.2, 157.6, 173.4]
final_score = compute_detection_score(sensor_readings)
print(f"Result: {final_score}")