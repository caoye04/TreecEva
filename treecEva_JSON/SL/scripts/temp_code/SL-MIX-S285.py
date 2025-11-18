from collections import deque
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Audio peak frequency data (Hz)
audio_peaks = [261.63, 329.63, 392.00, 523.25, 659.25, 783.99, 1046.50]
window_size = 3
peak_history = deque(maxlen=window_size)
harmonic_accumulator = 0
prime_weight = 0

for idx, freq in enumerate(audio_peaks):
    # Round to nearest integer for processing
    rounded_freq = round(freq)
    peak_history.append(rounded_freq)
    
    # Statistical validation - check if current frequency is above mean of window
    if len(peak_history) == window_size:
        window_mean = sum(peak_history) / len(peak_history)
        is_above_average = freq > window_mean
        
        # Number theory component - weight by prime factors
        prime_factors = sum(1 for i in range(2, rounded_freq + 1) if rounded_freq % i == 0 and is_prime(i))
        
        # Short-circuit evaluation with logical operations
        if is_above_average and not (prime_factors > 3 or rounded_freq < 300):
            # Calculate harmonic relationship with previous peaks
            base_freq = peak_history[0]
            current_lcm = lcm(base_freq, rounded_freq) if base_freq else 0
            harmonic_accumulator += current_lcm % 100
        elif not is_above_average or prime_factors <= 2:
            prime_weight += prime_factors * 10
    
    # Apply modulo to prevent overflow
    harmonic_accumulator %= 1000

# Final signature calculation
harmonic_signature = (harmonic_accumulator * prime_weight) % 997
print(f"Result: {harmonic_signature}")