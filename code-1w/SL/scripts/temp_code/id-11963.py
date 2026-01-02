import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [18, -5, 22, 4, 7, 13, 0, -11, 9, 6, 14, 3, 8, 1, 10]

# Irrelevant transformation: frequency mapping (distractor)
frequency_map = {x: data_stream.count(x) for x in set(data_stream)}

# Noise threshold simulation (misleading intermediate)
noise_floor = 7
high_noise = [x for x in data_stream if abs(x) > noise_floor]

# Legitimate preprocessing: isolate non-zero values
cleaned_data = [x for x in data_stream if x != 0]

# Apply moving average filter of window size 3 (red herring)
moving_avg = [sum(cleaned_data[i:i+3]) / 3 for i in range(len(cleaned_data) - 2)]

# Bit manipulation decoy: flip bits on first five elements
decoy_bits = [x ^ 0b1111 for x in cleaned_data[:5]]

# Real processing path begins: categorize by parity and magnitude
large_values = list(filter(lambda x: x > 10, cleaned_data))
small_values = list(filter(lambda x: x <= 10, cleaned_data))

even_small = [x for x in small_values if x % 2 == 0]
odd_large = [x for x in large_values if x % 2 == 1]

# Combine using zip_longest to simulate data fusion (complex distractor)
fused_pairs = list(itertools.zip_longest(even_small, odd_large, fillvalue=1))
product_chain = [a * b for a, b in fused_pairs]

# Critical path: select values that appear in both original large and odd-checked sets
intersection_candidate = set(odd_large).intersection(set(data_stream))

# Generate cumulative transforms (dead path)
cumulative = []
temp_sum = 0
for val in intersection_candidate:
    temp_sum += val
    cumulative.append(temp_sum)

cumulative_shifted = [x << 1 for x in cumulative]  # Unused shift

# Key filtering logic: use slice of cleaned data with specific parity and position
sliced_relevant = cleaned_data[1::2]  # Every second element starting from index 1

# Final filter: keep only those divisible by 3 or greater than 8
filtered_data = [x for x in sliced_relevant if x % 3 == 0 or x > 8]

# Target execution point
filtered_sum = sum(filtered_data)

# Output result
print(f"Result: {filtered_sum}")