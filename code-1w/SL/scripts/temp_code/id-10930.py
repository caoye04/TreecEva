import math

# Simulated sensor readings with noise
def get_raw_readings():
    return [127, 255, 64, 191, 32, 80, 44, 180, 95]

# Irrelevant transformation - distractor
def transform_signal(x):
    return (x << 2) ^ 0xFF

# Noise filter using threshold logic and bit analysis
def analyze_noise_level(readings):
    high_noise = []
    for val in readings:
        if (val & (val - 1)) == 0:  # power of two check - red herring
            high_noise.append(val)
    return high_noise

# Core logic: extract values above threshold and apply correction
raw_data = get_raw_readings()
threshold = 75

# Decoy list comprehension with unused result
unused_enhanced = [math.sqrt(x) * 1.5 for x in raw_data if x % 2 == 0]

# Misleading intermediate calculation
average = sum(raw_data) / len(raw_data)
deviation_score = sum(abs(x - average) for x in raw_data) / len(raw_data)

# Real processing begins here
significant_values = [x for x in raw_data if x > threshold]

# Apply non-linear correction using lambda (relevant)
corrected = list(map(lambda x: int(math.log2(x) * 10), significant_values))

# Bit manipulation side-path - dead code
shifted_vals = []
for v in corrected:
    if v > 20:
        shifted_vals.append((v << 1) | 1)
    else:
        shifted_vals.append(v >> 1)

# Set operation to remove duplicates - actually used
unique_corrected = list(set(corrected))

# Secondary filtering based on parity - relevant
parity_filtered = [x for x in unique_corrected if x % 2 == 0]

# Another distraction: recursive checksum (never called)
def recursive_checksum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + 2 * recursive_checksum(arr, idx + 1)

# Final filtering based on relation to median
sorted_vals = sorted(parity_filtered)
median = sorted_vals[len(sorted_vals) // 2] if sorted_vals else 0

# Key statement: filter values >= median
filtered_data = [x for x in sorted_vals if x >= median]

# Target result computation
filtered_result = sum(filtered_data)

print(f"Result: {filtered_result}")