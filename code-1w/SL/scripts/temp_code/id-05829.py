from itertools import cycle

# Simulate a data transmission chain with noise and correction mapping
def generate_noisy_chain(base_sequence, noise_factor):
    return [x ^ (i * noise_factor % 256) for i, x in enumerate(base_sequence)]

# Apply transformation using a shifting mask
def apply_mask(sequence, mask):
    masked = []
    for val, m in zip(sequence, cycle(mask)):
        masked.append((val & m) ^ (m >> 2))
    return masked

# Dummy entropy calculation (not used in final result but adds distraction)
def calculate_entropy(data):
    from math import log
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Core signal processing function
def process_transmission(chain, corrections):
    temp_state = [x % 128 for x in chain]
    adjusted = []
    
    # Primary transformation loop
    for i, val in enumerate(temp_state):
        key = i % len(corrections)
        adjusted.append(val ^ corrections[key])
    
    # Introduce distractor: unused intermediate smoothing
    smoothed = []
    for j in range(len(adjusted)):
        prev = adjusted[j-1] if j > 0 else adjusted[-1]
        next_val = adjusted[(j+1) % len(adjusted)]
        smoothed.append((prev + adjusted[j] + next_val) // 3)
    
    # Actual computation path
    checksum = 0
    for x in adjusted:
        if x % 2 == 0:
            checksum += x * 2
        else:
            checksum -= x
    
    # Final non-linear transformation
    final_value = (checksum ^ 0x5F) & 0x7FFF
    return final_value

# Setup transmission parameters
base_data = [104, 97, 115, 104, 32, 107, 101, 121]
noise_level = 17
signal_chain = generate_noisy_chain(base_data, noise_level)

# Correction map based on cyclic redundancy concept (simplified)
correction_map = [5, 12, 9, 14, 6]

# Apply physical layer masking (distraction step - not used later)
masked_signal = apply_mask(signal_chain, [0xFF, 0xAA, 0x55])

# Calculate dummy metrics for system logging (dead code path)
signal_entropy = calculate_entropy(signal_chain)
drift_estimate = sum(signal_chain[i+1] - signal_chain[i] for i in range(len(signal_chain)-1)) // len(signal_chain)

# Main processing step
final_signal = process_transmission(signal_chain, correction_map)

# Output result
print(f"Result: {final_signal}")