from functools import reduce
import itertools

# Audio sample processing pipeline
def process_samples(samples):
    # Step 1: Apply gain (multiply by 2) and offset (-10)
    amplified = [(s * 2) - 10 for s in samples]
    
    # Step 2: Filter out negative values
    filtered = list(filter(lambda x: x >= 0, amplified))
    
    # Step 3: Group into pairs and compute max of each pair
    paired = itertools.batched(filtered, 2)
    max_values = [max(pair) for pair in paired if len(pair) == 2]
    
    # Step 4: Apply modular transformation: (value^2) % 17
    transformed = [(v ** 2) % 17 for v in max_values]
    
    # Step 5: Compute checksum using XOR reduction
    checksum = reduce(lambda a, b: a ^ b, transformed, 0)
    return checksum

# Initial audio samples
audio_samples = [3, 7, 2, 9, 1, 8, 4, 6]

# Process the samples and compute checksum
checksum = process_samples(audio_samples)
print(f"Result: {checksum}")