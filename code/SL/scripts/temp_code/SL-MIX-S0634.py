import re
from collections import deque
from contextlib import contextmanager
class ManuscriptEncoder:
    def __init__(self):
        self.fib_cache = {}
        self.encoded_segments = []
    
    def fib(self, n):
        if n in self.fib_cache:
            return self.fib_cache[n]
        if n <= 1:
            return n
        result = self.fib(n-1) + self.fib(n-2)
        self.fib_cache[n] = result
        return result
    
    def encode_segment(self, text_segment):
        encoded = []
        for i, char in enumerate(text_segment):
            shift = self.fib(i % 12)  # Cycle through first 12 Fibonacci numbers
            encoded.append(ord(char) + shift)
        return encoded

@contextmanager
def manuscript_processor():
    encoder = ManuscriptEncoder()
    try:
        yield encoder
    finally:
        # Cleanup would go here in a real implementation
        pass

def calculate_checksum(segment_data):
    checksum = 0
    for i, value in enumerate(segment_data):
        if i % 2 == 0:
            checksum ^= value
        else:
            checksum += value
    return checksum & 0xFF  # Keep within byte range

def extract_pattern_fragments(manuscript_text):
    # Find all sequences of 3-5 uppercase letters
    pattern = r'[A-Z]{3,5}'
    matches = re.findall(pattern, manuscript_text)
    return matches

# Main processing pipeline
ancient_manuscript = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
verification_code = 0
segment_checksums = []

with manuscript_processor() as encoder:
    fragments = extract_pattern_fragments(ancient_manuscript)
    for fragment in fragments:
        encoded_segment = encoder.encode_segment(fragment)
        encoder.encoded_segments.append(encoded_segment)
        checksum = calculate_checksum(encoded_segment)
        segment_checksums.append(checksum)

# Create a linked list-like structure using deque for checksum processing
checksum_chain = deque(segment_checksums)

# Process the checksum chain with a custom algorithm
while len(checksum_chain) > 1:
    first = checksum_chain.popleft()
    second = checksum_chain.popleft()
    combined = (first * 3) ^ (second * 5)
    checksum_chain.append(combined & 0xFF)

# Final verification calculation
if checksum_chain:
    base_value = checksum_chain[0]
    verification_code = ((base_value << 2) | (base_value >> 2)) & 0xFF

print(f"Result: {verification_code}")