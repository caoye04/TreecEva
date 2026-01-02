from collections import defaultdict, Counter
import math

# Simulated sensor readings with noise and redundant data
data_stream = [14, 19, 14, 22, 25, 14, 19, 30, 31, 30, 22, 25, 28, 29, 30, 14, 19, 22]

# Irrelevant frequency analysis (distraction)
freq_map = defaultdict(int)
for val in data_stream:
    freq_map[val] += 1

# Misleading peak detection (dead path)
peaks = []
for i in range(1, len(data_stream) - 1):
    if data_stream[i] > data_stream[i-1] and data_stream[i] > data_stream[i+1]:
        peaks.append(i)

# Noise threshold for filtering (relevant)
base_threshold = sum(data_stream) / len(data_stream)

# Decoy transformation: bit manipulation on indices (irrelevant)
index_signature = 0
for i in range(len(data_stream)):
    if i % 3 == 0:
        index_signature ^= (i << 2)
    elif i % 5 == 0:
        index_signature |= (i + 1)

# Data smoothing via moving average (distractor)
smoothed = []
window_size = 3
for i in range(len(data_stream) - window_size + 1):
    window = data_stream[i:i + window_size]
    smoothed.append(sum(window) // len(window))

# Actual relevant path begins: filter values above dynamic threshold
dynamic_factor = math.log(max(data_stream))
threshold = int(base_threshold * (1 + (dynamic_factor / 25)))

filtered_data = [x for x in data_stream if x > threshold]

# Further reduction using modulo pattern (relevant but non-obvious)
filtered_data = [x for x in filtered_data if x % 5 != 3]

# Count occurrences (partially relevant)
counts = Counter(filtered_data)

# Secondary filter: remove values with frequency > 1 (subtle but important)
unique_only = [x for x in filtered_data if counts[x] == 1]

# Tertiary operation: apply exponential decay weighting (irrelevant to final result)
decay_weights = []
for i, val in enumerate(unique_only):
    weight = val * math.exp(-0.1 * i)
    decay_weights.append(weight)

# Core logic: process signal based on arithmetic-boolean hybrid rule
def process_signals(signal_list, thresh):
    if not signal_list:
        return -1
    
    # Conditional expression with nested checks
    adjusted = [x for x in signal_list if (x > thresh) and ((x & (x - 1)) == 0)]  # Power of two check
    
    # Final computation: sum with positional scaling
    total = 0
    for idx, val in enumerate(adjusted):
        total += val * (idx + 1)  # Weight by position
    
    # Bitwise obfuscation (neutralized later)
    masked = total ^ 0xFF
    unmasked = masked ^ 0xFF  # Restore original
    
    # Final adjustment: integer division rounding
    return (unmasked + 4) // 5 * 5  # Round up to nearest 5

# Execution point of interest
final_output = process_signals(filtered_data, threshold)

# Print result as required
print(f"Result: {final_output}")