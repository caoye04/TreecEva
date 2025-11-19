import math
import statistics
from collections import Counter

def gcd_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
        if result == 1:
            break
    return result

def process_keystream(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # Convert to byte values
    byte_values = [ord(c) for c in content]
    
    # Frequency analysis
    freq_counter = Counter(byte_values)
    frequencies = list(freq_counter.values())
    
    # Statistical measures
    mean_freq = statistics.mean(frequencies)
    variance_freq = statistics.variance(frequencies) if len(frequencies) > 1 else 0
    
    # Detect cycle candidates from frequent bytes
    threshold = mean_freq + (variance_freq ** 0.5)
    cycle_candidates = [byte_val for byte_val, count in freq_counter.items() if count >= threshold]
    
    # Apply number theory if we have candidates
    cycle_length = gcd_list(cycle_candidates) if cycle_candidates else 0
    
    # Compute signature using ternary and short-circuit
    has_high_variance = variance_freq > 10
    is_homogeneous = len(set(frequencies)) <= 2
    keystream_signature = (cycle_length * 100 + int(mean_freq)) if has_high_variance and not is_homogeneous else (len(byte_values) if is_homogeneous else -1)
    
    return keystream_signature

# Simulate file content
with open('keystream_data.txt', 'w') as f:
    f.write("ABABABABXYZXYZXYZABABABABXYZXYZXYZ")

keystream_signature = process_keystream('keystream_data.txt')
print(f"Result: {keystream_signature}")