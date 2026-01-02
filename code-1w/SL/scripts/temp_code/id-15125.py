import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return x ** 3 + 2 * x - 1

# Distractor computation with misleading intermediate
buffer_cache = [i ** 2 for i in range(15) if i % 3 != 0]
shadow_index = sum(buffer_cache) // 100  # Misleading value, not used later

# Simulated sensor data with noise
raw_readings = [0.7, 1.3, 4.1, 2.8, 3.6]

def apply_filter(signal, threshold=lambda t: t > 2.0):
    return [s for s in signal if threshold(s)]

# Noise reduction pass
filtered_data = apply_filter(raw_readings)

# Secondary distractor: decoy statistical analysis
mean_guess = sum(filtered_data) / len(filtered_data) if filtered_data else 0
variance_proxy = sum((x - mean_guess) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0

# Core logic disguised among distractions
scaling_factor = 1.75
offset_correction = -0.4

# Conditional data routing based on arbitrary criterion
data_stream = filtered_data if len(filtered_data) > 2 else [1.0]

# Bit manipulation red herring
bit_fiddling = 0
for i in range(len(data_stream)):
    bit_fiddling ^= int(data_stream[i]) << 1
bit_fiddling = (bit_fiddling & 0xFF) ^ 0xAA  # Decoy result

# Real processing chain starts here
normalization_func = lambda x: round(math.log(x + 1) * scaling_factor + offset_correction, 6)

def enhance_sample(val):
    if val < 2.5:
        return val * 1.2
    elif val < 3.5:
        return val * 1.1
    else:
        return val * 0.95

# Data transformation pipeline
def process_pipeline(stream):
    temp_result = 0.0
    for item in stream:
        processed = normalization_func(item)
        enhanced = enhance_sample(processed)
        # Accumulate weighted contribution
        weight = 1.5 if processed > 1.0 else 0.8
        temp_result += enhanced * weight
    # Final nonlinear adjustment
    if temp_result > 5.0:
        temp_result = math.sqrt(temp_result) * 1.3
    return round(temp_result, 6)

# Unused recursive distraction
def bad_recursion(n):
    return n if n <= 1 else bad_recursion(n-1) + bad_recursion(n-2)

# Unused list of decoy operations
decoys = [
    lambda: shadow_index * variance_proxy,
    lambda: bad_recursion(5),
    lambda: sum(buffer_cache[:5])
]

# Critical execution point
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Result: {final_output}")