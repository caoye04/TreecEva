import math

# Simulated sensor data processing with diagnostic evaluation
data_stream = [142, 98, 111, 105, 99, 108, 101, 32, 116, 114, 97, 110, 115, 108, 97, 116, 101, 100]

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 256
DEFAULT_TIMEOUT = 15.5
DEVICE_ID = 'XJ-42'
VERSION_CODE = 3.14159

# Decoy transformation functions
def decoy_transform_a(x):
    return (x ** 2 + 3 * x + 1) % 256

def decoy_transform_b(data):
    return [((val << 2) ^ 0x55) & 0xFF for val in data]

def unused_hash_sequence(seq):
    prime_sum = 0
    for i, v in enumerate(seq):
        prime_sum += v * (i + 1) * (i + 2)
    return prime_sum % 10007

# Real transformation: interpret as ASCII and filter control characters
def ascii_decode(stream):
    decoded = ''.join(chr(b) for b in stream if 32 <= b <= 126)
    return decoded

# Further processing pipeline
decoded_message = ascii_decode(data_stream)

# Spurious checksum calculation (dead code path)
spurious_checksum = sum(ord(c) * (i + 1) for i, c in enumerate(decoded_message)) % 997

# Actual data transformation chain
tokenized = list(map(ord, decoded_message))  # Convert back to ASCII values

# Introduce lambda-based filtering and transformation
noise_filter = lambda x: x if 100 <= x <= 115 else x - 10  # subtle shift logic
filtered_tokens = [noise_filter(t) for t in tokenized]

# Red herring: complex but unused frequency analysis
char_freq = {}
for c in decoded_message:
    char_freq[c] = char_freq.get(c, 0) + 1
frequency_entropy = -sum((count / len(decoded_message)) * math.log2(count / len(decoded_message))
                      for count in char_freq.values())

# Modular arithmetic manipulation
mod_shift = 19
transformed_data = [(t + mod_shift) % 127 for t in filtered_tokens]

# Misleading intermediate result
apparent_pattern = sum(1 for t in transformed_data if t % 7 == 0)

# Threshold function using lambda and set operations
critical_values = {102, 108, 111, 119}
threshold_func = lambda x: x > 105 or x in critical_values

# Decoy state tracker (unused)
current_state = {
    'active': True,
    'mode': 'diagnostic',
    'sequence_index': 0,
    'last_update': 1625097600
}

# Core analysis function with nested logic
def analyze_pattern(data, threshold):
    if not data:
        return -1
    
    # Step 1: collect indices passing threshold
    hotspots = [i for i, val in enumerate(data) if threshold(val)]
    
    # Step 2: compute gap statistics
    if len(hotspots) < 2:
        gap_metric = 0
    else:
        gaps = [hotspots[i+1] - hotspots[i] for i in range(len(hotspots)-1)]
        gap_metric = int(sum(gaps) / len(gaps))
    
    # Step 3: apply bit manipulation on aggregate
    aggregated = sum(data) & 0xFFFF  # Keep lower 16 bits
    
    # Step 4: conditional adjustment based on modular pattern
    if len(data) % 4 == 0:
        aggregated ^= 0xAA
    
    # Step 5: combine with gap metric using XOR and rotation
    rotated = ((aggregated << 3) & 0xFFFF) | (aggregated >> 13)
    combined = rotated ^ gap_metric
    
    # Step 6: final adjustment using set intersection count
    data_set = set(data)
    overlap = len(data_set.intersection(critical_values))
    
    # Step 7: apply logarithmic dampening if overlap exists
    if overlap > 0:
        combined = int(combined / (math.log2(overlap + 1)))
    
    # Step 8: final bounds check
    final_score = max(-1000000, min(combined, 1000000))
    
    return final_score

# Execute main analysis
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

# Print result as required
print(f"Target result: {final_diagnostic}")