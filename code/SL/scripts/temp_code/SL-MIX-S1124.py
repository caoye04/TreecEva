import statistics
from collections import deque

def process_underwater_signal(acoustic_samples):
    # Initialize modified Fibonacci sequence with first two terms
    fib_mod_seq = deque([acoustic_samples[0] % 17, acoustic_samples[1] % 17], maxlen=2)
    
    # Calculate noise factor from sample statistics
    sample_mean = statistics.mean(acoustic_samples)
    sample_variance = statistics.variance(acoustic_samples) if len(acoustic_samples) > 1 else 0
    noise_factor = int((sample_mean + sample_variance) * 1.73) % 13
    
    # Process remaining samples to build sequence
    for i in range(2, len(acoustic_samples)):
        # Modified Fibonacci: next = (prev1 + prev2 + noise) mod 17
        next_term = (fib_mod_seq[0] + fib_mod_seq[1] + noise_factor) % 17
        fib_mod_seq.append(next_term)
    
    # Detection algorithm: pattern score is last term adjusted by sequence properties
    pattern_score = (fib_mod_seq[-1] * len(acoustic_samples) - sum(fib_mod_seq)) % 19
    return pattern_score

# Underwater acoustic monitoring data (amplitude measurements)
technical_readings = [23.7, 18.2, 31.5, 12.8, 45.1, 27.3, 19.9, 38.6]

detected_pattern = process_underwater_signal(technical_readings)
print(f"Result: {detected_pattern}")