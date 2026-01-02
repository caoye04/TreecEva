from collections import defaultdict, Counter

# Simulated sensor data ingestion with noise
raw_signals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
noise_floor = 2
cleaned_signals = [x for x in raw_signals if x > noise_floor]

# Irrelevant transformation: frequency analysis (dead end)
freq_map = {}
for val in raw_signals:
    freq_map[val] = freq_map.get(val, 0) + 1
sorted_freq = sorted(freq_map.items(), key=lambda x: -x[1])
dominant_value = sorted_freq[0][0]  # Misleading: not used later

# Data windowing and chunking
window_size = 4
time_windows = [cleaned_signals[i:i+window_size] for i in range(0, len(cleaned_signals), window_size)]

# Apply non-linear transformation: square root of product per window
import math
transformed_data = []
for window in time_windows:
    if len(window) == window_size:
        product = 1
        for w in window:
            product *= w
        transformed_data.append(int(math.sqrt(product)))
    else:
        # Padding with checksum (distractor logic)
        padded = window + [sum(window) % 7] * (window_size - len(window))
        fake_product = 1
        for p in padded:
            fake_product *= (p + 1)
        transformed_data.append(fake_product % 100)

# Configuration profile with red herrings
class Config:
    def __init__(self):
        self.threshold = 15
        self.mode = 'diagnostic'
        self.debug_level = 99  # Unused field
        self.trace_enabled = True
        self.cache_ttl = 3600  # Distractor: looks important but isn't
config = Config()

# Decoy function that's defined but never called
def legacy_calibrate(data):
    """Outdated calibration method - irrelevant."""
    return [x ^ 3 for x in data if x % 2 == 0]

# Real processing pipeline
def compress_sequence(seq):
    """Run-length encode the sequence."""
    if not seq:
        return []
    compressed = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            compressed.append((seq[i-1], count))
            count = 1
    compressed.append((seq[-1], count))
    return compressed

# Secondary distractor: analyze stability (never invoked)
stability_log = []
for entry in transformed_data:
    binary_rep = bin(entry)[2:]
    ones_ratio = binary_rep.count('1') / len(binary_rep)
    stability_log.append('stable' if 0.4 <= ones_ratio <= 0.6 else 'volatile')

# Core analysis function
def analyze_pattern(data, cfg):
    rle_data = compress_sequence(data)
    
    # Extract even-positioned values from RLE (algorithmic nuance)
    filtered_pairs = [pair for idx, pair in enumerate(rle_data) if idx % 2 == 0]
    
    # Compute weighted diagnostic score
    total_score = 0
    for value, run in filtered_pairs:
        # Complex weighting: combines bitwise, arithmetic, and logical ops
        contribution = (value & 7) * run  # Bitwise mask with multiplier
        if value > cfg.threshold:
            contribution *= 2
        parity_flag = (bin(value).count('1') % 2 == 0)  # Even popcount?
        modifier = 1.5 if parity_flag else 0.8
        total_score += contribution * modifier
    
    # Final adjustment based on string representation properties
    str_repr = ''.join(map(str, data))
    digit_counter = Counter(str_repr)
    most_common_digit = digit_counter.most_common(1)[0]
    if int(most_common_digit[0]) % 2 == 1:
        total_score -= 10
    else:
        total_score += 5
    
    # Normalize by number of windows (actual result)
    normalized = total_score / len(data)
    return int(round(normalized))

# Trigger point: critical execution step
final_diagnostic = analyze_pattern(transformed_data, config)

# Print result as required
print(f"Result: {final_diagnostic}")