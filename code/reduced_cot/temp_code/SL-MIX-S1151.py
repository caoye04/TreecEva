from collections import Counter
import hashlib

def custom_base_decode(s, base_chars):
    base = len(base_chars)
    decoded = 0
    for char in s:
        decoded = decoded * base + base_chars.index(char)
    return decoded

def hash_segment(segment):
    return int(hashlib.sha256(str(segment).encode()).hexdigest(), 16) % 1000000

# Encoded suspicious IP segments using custom base-5 encoding with characters 'abcde'
encoded_segments = ['aab', 'bac', 'cab', 'dac', 'ead', 'bba', 'ccd', 'dee']
base_chars = 'abcde'

# Step 1: Decode segments
ip_segments = [custom_base_decode(seg, base_chars) for seg in encoded_segments]

# Step 2: Filter out segments less than 10
filtered_segments = list(filter(lambda x: x >= 10, ip_segments))

# Step 3: Hash each segment and count frequencies
hashed_segments = [hash_segment(seg) for seg in filtered_segments]
frequency_counter = Counter(hashed_segments)

# Step 4: Find segments with frequency > 1
repeated_hashes = [h for h, count in frequency_counter.items() if count > 1]

# Step 5: Apply scoring algorithm
suspicious_score = sum(map(lambda x: x * 3 - 7, repeated_hashes)) if repeated_hashes else 0

print(f"Result: {suspicious_score}")