def analyze_pattern(sequence):
    # Irrelevant transformation: counts vowels in a string (not used)
    vowel_count = sum(1 for c in sequence if c.lower() in 'aeiou')

    # Semi-relevant: maps characters to positions
    pos_map = {char: idx for idx, char in enumerate(sequence)}

    # Distractor: complex lambda that's never invoked
    transform = lambda x: (x ** 2 + 3) % 7

    return pos_map

# Simulated binary data stream as string
data_stream = "110101101110"

# Extract segments
segment_a = data_stream[2:6]  # '0101'
segment_b = data_stream[6:10] # '1011'

# Mask with bitwise pattern (used later)
mask = 5  # Binary: 101

# Auxiliary calculation: length product (distractor)
length_product = len(segment_a) * len(segment_b)

# Another red herring: unused list comprehension
reversed_segments = [seg[::-1] for seg in [segment_a, segment_b]]

# Helper function with multiple concerns
def process_segment(segment_str, key_mask):
    # Convert binary string to integer
    raw_value = int(segment_str, 2)
    
    # Apply mask using XOR (core operation)
    masked_value = raw_value ^ key_mask
    
    # Extra step: add sum of digits (semi-relevant but cancels out)
    digit_sum = sum(int(b) for b in segment_str)
    
    # Core logic: apply non-linear adjustment
    intermediate = (masked_value * 3) + (digit_sum % 4)
    
    # Final checksum computation
    checksum = (intermediate ^ (intermediate >> 2)) & 0xFF
    
    # Dead code: this branch is never taken
    if len(segment_str) > 20:
        checksum *= 2
        
    return checksum

# Call analysis on unused data (distractor call)
_ = analyze_pattern("hello_world")

# Critical execution point
checksum = process_segment(data, mask)

print(f"Result: {checksum}")