import math
import itertools

def process_signals(base_freq, harmonics):
    # Compute log base 2 of base_freq and raise 2 to that power
    log_val = math.log2(base_freq)
    reconstructed = 2 ** int(log_val)
    
    # Bitwise operations on harmonics
    harmonic_mask = 0
    for h in harmonics:
        harmonic_mask |= h
    
    # Apply mask using XOR and shift
    masked_value = (reconstructed ^ harmonic_mask) << 2
    
    # String transformation and hashing
    signal_str = f"signal_{masked_value}"
    hash_val = hash(signal_str) & 0xFF  # Take lower 8 bits
    
    # Ternary operation based on comparison
    encoded_signal = hash_val if hash_val > 128 else (hash_val + 100)
    
    return encoded_signal

# Input parameters
base_frequency = 32
harmonic_list = [1, 2, 4, 8]

# Execute processing
encoded_signal = process_signals(base_frequency, harmonic_list)
print(f"Result: {encoded_signal}")