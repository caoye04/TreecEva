from collections import defaultdict, Counter
import math

# Signal processing simulation with frequency analysis
def analyze_signal(raw_data, cutoff=75):
    # Convert string data to numerical values
    signal = [ord(c) % 128 for c in raw_data]
    
    # Calculate signal statistics - not used in core logic
    stats = defaultdict(int)
    for amplitude in signal:
        stats[amplitude] += 1
    
    # Find most common frequencies
    frequency_counter = Counter(signal)
    common_freqs = frequency_counter.most_common(5)
    
    # Filter signal based on cutoff
    filtered = list(filter(lambda x: x < cutoff, signal))
    return filtered, common_freqs

# Generate prime numbers up to limit
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    # Misleading variable - not used in final calculation
    prime_product = 1
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(limit + 1) if sieve[i]]

# Main processing function
def process_signal_data(input_data):
    # Process raw data
    filtered_signal, _ = analyze_signal(input_data)
    
    # Calculate modulation parameters
    base_freq = sum(filtered_signal) // len(filtered_signal)
    
    # This is a distractor calculation
    harmonic_series = [base_freq * (i+1) for i in range(5)]
    
    # Signal modulation - the key calculation path
    modulated_signal = []
    carrier = 42
    for val in filtered_signal[:10]:  # Only first 10 values matter
        # Bitwise operations for signal modulation
        mod_val = (val ^ carrier) & 0xFF
        if mod_val % 2 == 0:
            mod_val = (mod_val // 2) + 3
        else:
            mod_val = (mod_val * 3 + 1) // 2
        modulated_signal.append(mod_val)
    
    # Calculate prime index - key to finding the answer
    primes = generate_primes(50)
    prime_index = primes[3] % len(modulated_signal)  # 4th prime is 7
    
    # Distractor variables and calculations
    max_amplitude = max(modulated_signal)
    min_amplitude = min(modulated_signal)
    avg_amplitude = sum(modulated_signal) / len(modulated_signal)
    
    # This branch is never taken - distractor code
    if max_amplitude > 1000:
        normalized = [x / max_amplitude for x in modulated_signal]
        final_frequency = sum(normalized)
    else:
        # This is the actual path that determines the answer
        final_frequency = modulated_signal[prime_index]
    
    # More distractor variables
    signal_energy = sum(x**2 for x in modulated_signal)
    signal_variance = sum((x - avg_amplitude)**2 for x in modulated_signal) / len(modulated_signal)
    
    return final_frequency

# Input data
input_signal = "HelloWorldSignalProcessing"

# Process data and get result
result = process_signal_data(input_signal)
print(f"Result: {result}")