import itertools

# Simulate sensor data with noise and encoding
raw_readings = [127, 255, 64, 192, 32]
noise_floor = 17
encoding_key = 42

# Irrelevant transformation: ASCII mapping (distractor)
char_map = {x: chr(x % 90 + 32) for x in raw_readings}

# Step 1: Apply noise correction (subtract constant floor)
corrected = [r - noise_floor for r in raw_readings]

# Step 2: Normalize values to 0-1 range based on max possible reading
normalized = [round(c / (255 - noise_floor), 4) for c in corrected]

# Step 3: Encode using XOR with key (bitwise operation)
encoded = [c ^ encoding_key for c in corrected]

# Step 4: Generate binary representation mask using list comprehension and itertools
bit_masks = [list(map(int, f'{e:08b}')) for e in encoded]
flat_bits = list(itertools.chain.from_iterable(bit_masks))
ones_count = sum(flat_bits)
zeros_count = len(flat_bits) - ones_count

# Misleading statistical computation (dead path)
entropy_approx = round((ones_count / len(flat_bits)) * (zeros_count / len(flat_bits)) * 10, 4) if ones_count and zeros_count else 0

# Step 5: Create weighted significance score per original index
weights = [0.5, 1.0, 0.75, 1.25, 0.9]
weighted_impact = [corrected[i] * weights[i] for i in range(len(corrected))]

# Step 6: Transform data through thresholding and case conversion simulation
threshold = 100
transformed = [
    int(w * 2) if w >= threshold else int(w * 0.5)
    for w in weighted_impact
]

# Step 7: Create dynamic mask based on bit parity (true dependency)
mask = [1 if encoded[i] % 2 == 0 else 0 for i in range(len(encoded))]

# Step 8: Process transformed data using mask filtering
filtered_values = [transformed[i] for i in range(len(transformed)) if mask[i] == 1]

# Final aggregation step
aggregated = sum(filtered_values) + (ones_count % 5)

# Key assignment: final output depends on filtered sum and bit statistics
final_output = process_transformed_data(transformed, mask)

# Dummy function to encapsulate final logic (avoids premature evaluation)
def process_transformed_data(data, m):
    filtered = [data[i] for i in range(len(data)) if m[i] == 1]
    base_sum = sum(filtered)
    # Add checksum based on length parity
    checksum = len(filtered) if len(filtered) % 2 == 1 else 0
    return base_sum + checksum + 2  # deterministic offset

# Ensure function is called after definition
def process_transformed_data(data, m):
    filtered = [data[i] for i in range(len(data)) if m[i] == 1]
    base_sum = sum(filtered)
    checksum = len(filtered) if len(filtered) % 2 == 1 else 0
    return base_sum + checksum + 2

print(f"Result: {process_transformed_data(transformed, mask)}")