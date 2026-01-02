import math

# Simulated sensor data with noise and metadata
data_stream = [15, -8, 23, 42, -17, 9, 0, 64, 12, -99, 50, 22]
metadata_tags = ['A', 'B', 'C', 'D', 'E', 'F']

# Irrelevant transformation: string padding for fake analysis
tagged_data = [tag.ljust(5, '.') for tag in metadata_tags]
expanded_tags = [t.upper() + t.lower() for t in tagged_data if len(t) > 3]

# Decoy statistical calculation
mean_value = sum(data_stream) / len(data_stream)
variance_proxy = sum([(x - mean_value) ** 2 for x in data_stream]) / len(data_stream)
standard_deviation = math.sqrt(variance_proxy)

# Fake filter based on irrelevant criteria
decoys = [x for x in data_stream if x % 7 == 0]

# Real processing path begins: extract positive even numbers
even_positive = []
for val in data_stream:
    if val > 0 and val % 2 == 0:
        even_positive.append(val)

# Secondary filter: exclude values greater than 50 (arbitrary domain rule)
cleaned_data = [x for x in even_positive if x <= 50]

# Bit manipulation red herring: simulate checksum
checksum = 0
for x in data_stream:
    checksum ^= x  # Unused beyond this point

# String-based masking logic (distractor)
mask_pattern = '101'
dynamic_mask = int(mask_pattern * 3, 2)  # Creates a large unused integer

# Conditional mutation based on length (irrelevant)
if len(expanded_tags) > 10:
    cleaned_data = [x + 10 for x in cleaned_data]

# Core logic: apply logarithmic scaling only to values >= 10
scaled_data = []
for x in cleaned_data:
    if x >= 10:
        scaled_data.append(math.log(x, 2))
    else:
        scaled_data.append(x)

# Round scaled values to 3 decimal places
rounded_data = [round(x, 3) for x in scaled_data]

# Another decoy: attempt to reverse list but don't assign
list(reversed(rounded_data))

# Convert back using exponent where applicable (simulate decoding)
restored_data = []
for x in rounded_data:
    if x > 4:  # Approximate log2 threshold
        restored_data.append(int(2 ** x))
    else:
        restored_data.append(int(x))

# Final filtering: keep only those present in original even_positive
filtered_data = [x for x in restored_data if x in even_positive]

# Critical execution point
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")