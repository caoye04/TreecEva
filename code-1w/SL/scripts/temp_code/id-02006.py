def rotate_chunk(segment, shift):
    return segment[-shift:] + segment[:-shift]

# Irrelevant transformation: scrambles data in a reversible way
def scramble(data, factor):
    return [d ^ (factor % 256) for d in data]

def generate_checksum(seq):
    # Dead-end function: looks important but unused
    return sum(seq[i] * i for i in range(len(seq))) % 1000

def extract_peaks(signal):
    # Distractor: finds local maxima but not used in final path
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def decode_segments(chunks):
    # Decoy recursive structure that isn't actually part of critical logic
    if len(chunks) <= 1:
        return chunks[0] if chunks else []
    mid = len(chunks) // 2
    left = decode_segments(chunks[:mid])
    right = decode_segments(chunks[mid:])
    return left + [x + 1 for x in right]

def filter_outliers(data, limit):
    # Seemingly relevant preprocessing that's actually bypassed in execution
    return [x for x in data if abs(x) < limit]

def process_sequence(seq, threshold):
    # Core logic begins
    adjusted = [x - threshold for x in seq]
    squared = [x * x for x in adjusted]
    clipped = [min(x, 255) for x in squared]
    
    # Bit manipulation layer
    processed_bits = []
    for val in clipped:
        bits = (val ^ 42) & 0xFF  # XOR and mask
        bits = ((bits << 3) | (bits >> 5)) & 0xFF  # Rotate left by 3
        processed_bits.append(bits)
    
    # Slicing operation: take every second element starting from index 1
    sampled = processed_bits[1::2]
    
    # Aggregation with modular arithmetic
    total = 0
    for i, v in enumerate(sampled):
        total = (total + v * (i + 1)) % 98765
    
    # Final transformation
    return (total * 2) % 100000

# Main execution flow
base_signal = list(range(100, 120))  # Simulated sensor input

# Apply transformations - only some are actually used
modulated = [x * 2 + 1 for x in base_signal]
distorted = [x + (x % 7) for x in modulated]  # Red herring

# Key branching: distractor conditional that doesn't affect outcome
if sum(distorted) > 5000:
    cleaned = [x for x in distorted if x % 2 == 0]
else:
    cleaned = distorted[:]

# Critical path starts here
key_offset = 17
transformed_data = [((x + key_offset) % 256) for x in modulated]

# Add dummy dictionary mapping - looks like configuration
config_map = {
    'gain': 2.5,
    'offset': 99,
    'active': False,
    'thresholds': [10, 20, 30],
    'mode': 'calibration'
}

key_threshold = len(base_signal) + 5  # evaluates to 25

# Unused data structure - creates false sense of complexity
analysis_grid = [[i * j for j in range(5)] for i in range(5)]

# Another red herring: builds structure but never used
segment_pool = []
for i in range(0, len(transformed_data), 4):
    chunk = transformed_data[i:i+4]
    rotated = rotate_chunk(chunk, 1)
    scrambled = scramble(rotated, 7)
    segment_pool.append(scrambled)

# This call is essential
filtration_score = process_sequence(transformed_data, key_threshold)

# Print result as required
print(f"Result: {filtration_score}")