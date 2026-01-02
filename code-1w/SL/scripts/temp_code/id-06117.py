import math

# Simulated sensor data stream with noise
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Irrelevant transformation: frequency masking (dead code path)
frequency_mask = [math.sin(x * math.pi / 4) for x in range(len(data_stream))]
masked_data = [data_stream[i] * frequency_mask[i] for i in range(len(data_stream))]

# Noise reduction via irrelevant smoothing filter (distractor)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        avg = sum(signal[start:end]) / (end - start)
        smoothed.append(avg)
    return smoothed

filtered_data = smooth_signal(data_stream)  # Unused later

# Core processing: transform data using modular arithmetic and bit shifts
displacement_factor = 7
cyclic_shifted = [(x << 1) % 13 for x in data_stream]
modular_data = [(x + displacement_factor) % 11 for x in cyclic_shifted]

# Secondary distractor: histogram generation (no impact on result)
histogram = {}
for val in modular_data:
    histogram[val] = histogram.get(val, 0) + 1

# Data inversion with slicing and reversal (red herring)
inverted_slice = modular_data[::-1]
offset_corrected = [abs(x - 5) for x in inverted_slice if x != 0]

# Real preprocessing: apply cumulative weighting
weighted_prefix = []
cumulative = 0
for i, val in enumerate(modular_data):
    cumulative += val * (i + 1)
    weighted_prefix.append(cumulative)

# Transform data using combinatorics-inspired expansion
expansion_key = []
for i in range(len(modular_data)):
    combinations = 0
    for j in range(i + 1):
        if j == 0 or j == i:
            combinations += 1
        else:
            combinations += (i // (j + 1))
    expansion_key.append(combinations % 10)

total_weights = sum(expansion_key)
adjusted_weights = [w * total_weights // len(expansion_key) for w in expansion_key]

top_k_indices = sorted(range(len(adjusted_weights)), key=lambda i: adjusted_weights[i], reverse=True)[:5]

# Actual relevant transformation: polynomial transformation
def transform_polynomial(signal, a=2, b=-3, c=1):
    return [a * x * x + b * x + c for x in signal]

transformed_data = transform_polynomial(modular_data)

# Decoy function: looks important but unused
def detect_outliers(data, threshold=2):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    stddev = math.sqrt(variance)
    return [i for i, x in enumerate(data) if abs(x - mean) > threshold * stddev]

# Equilibrium index finder: finds index where left sum equals right sum
def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]
    return -1

# Key statement
equilibrium_index = find_equilibrium_index(transformed_data)

# Distractor: secondary index search with different logic (never executed)
alt_candidates = [i for i, x in enumerate(transformed_data) if x % 4 == 0]
fallback_index = alt_candidates[0] if alt_candidates else -999

# Output the target result
print(f"Result: {equilibrium_index}")