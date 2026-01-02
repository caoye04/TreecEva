import math

# Simulated data stream with noise and metadata
data_packet = [18, 23, 14, 55, 29, 31, 44, 67, 38, 21]
metadata_tags = ['A', 'B', 'C', 'D', 'E']
noise_floor = 12.5

def apply_filter(sequence, threshold):
    """Filter out values below threshold (irrelevant to final result)"""
    return [x for x in sequence if x > threshold]

def generate_checksum(seq):
    """Generate checksum for integrity (distractor)"""
    return sum(seq) % 100

def extract_subbands(signal):
    """Split signal into high and low frequency bands (partially relevant)"""
    low_band = [x for x in signal if x < 45]
    high_band = [x for x in signal if x >= 45]
    return low_band, high_band

def scramble_order(seq, key):
    """Apply dummy transformation (dead code path)"""
    shifted = []
    for i in range(len(seq)):
        shifted.append(seq[(i + key) % len(seq)])
    return shifted

def derive_key_indices(tag_list):
    """Map tags to indices - used in decoy function"""
    return {tag: idx * 2 for idx, tag in enumerate(tag_list)}

def decode_frame(frame, offset=3):
    """Decode frame using offset - irrelevant computation"""
    return [((x >> 2) ^ offset) + 1 for x in frame]

def compute_entropy(seq):
    """Calculate entropy of distribution (red herring)"""
    total = sum(seq)
    probs = [n / total for n in seq]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def multiplex_channels(data, factors):
    """Simulate channel multiplexing (distractor)"""
    result = []
    for val, factor in zip(data, factors):
        result.append(val * factor % 79)
    return result

def analyze_peaks(values):
    """Find local maxima - unused function"""
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks.append(i)
    return peaks

def shift_cipher(text, shift):
    """String operation unrelated to main logic"""
    return ''.join(chr((ord(c) - ord('A') + shift) % 26 + ord('A')) for c in text)

# Irrelevant string transformation chain
temp_labels = ['X1', 'Y2', 'Z3', 'W4', 'V5']
encoded_labels = [shift_cipher(label[0], int(noise_floor)) for label in temp_labels]

# Decoy variables and computations
checksum = generate_checksum(data_packet)
decoy_factors = [2, 3, 1, 4, 2, 3, 1, 4, 2, 3]
multiplexed = multiplex_channels(data_packet, decoy_factors)
key_mapping = derive_key_indices(metadata_tags)

# Real processing begins here (nested logic with distractors)
filtered_data = apply_filter(data_packet, 15)
low_freq, high_freq = extract_subbands(filtered_data)

# Conditional signal routing (meaningful branching)
if len(high_freq) >= 3:
    active_channel = high_freq
else:
    active_channel = low_freq

# Transform through multiple stages
transformed = []
for index, (val, _) in enumerate(zip(active_channel, metadata_tags * 10)):
    if index % 2 == 0:
        transformed.append(val ^ (index + 3))
    else:
        transformed.append(val + ((index + 1) ** 2))

# Secondary filtering based on dynamic condition
threshold_signal = sum(transformed) / len(transformed)
processed = [x for x in transformed if x > threshold_signal * 0.8]

# Key manipulation matrix (mix of relevant and irrelevant)
keys = [3, 1, 4, 1, 5]
chunks = []
cursor = 0
while cursor < len(processed):
    chunk_size = keys[cursor % len(keys)]
    chunk = processed[cursor:cursor + chunk_size]
    if len(chunk) == chunk_size:
        chunks.append(sum(chunk) // chunk_size)
    else:
        chunks.append(sum(chunk) % 53)
    cursor += chunk_size

# Final processing function with critical computation
def process_transmission(frames, cipher_keys):
    base_acc = 0
    for i, frame in enumerate(frames):
        # Complex conditional update
        if i % 2 == 0:
            base_acc += frame * cipher_keys[i % len(cipher_keys)]
        else:
            base_acc -= int(math.sqrt(frame + 1)) * (i + 1)
    
    # Final adjustment using bit manipulation
    base_acc = (base_acc ^ 0xFF) + (base_acc >> 3)
    
    # Introduce controlled interference
    dummy_sum = sum([k ** 2 for k in cipher_keys if k % 2 == 1])
    scaling_factor = len(cipher_keys) / 5  # Neutral factor
    
    # Critical line: final_signal depends only on base_acc
    final_result = base_acc * 2  # Amplify signal
    
    # Dead code branch (never executed due to structure)
    if False:
        fallback = compute_entropy(frames)
        final_result = fallback * 1000
    
    return int(final_result)

# Execute main pipeline
final_signal = process_transmission(chunks, keys)
print(f"Result: {final_signal}")