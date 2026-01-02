import math

# Simulated sensor data with noise and metadata
data_stream = [
    (1.2, 'A', 100), (3.4, 'B', 105), (2.1, 'A', 102), 
    (5.6, 'C', 101), (4.3, 'B', 108), (6.7, 'A', 103),
    (8.9, 'D', 107), (7.2, 'C', 104), (9.1, 'B', 106)
]

# Irrelevant mapping table for device types (distractor)
device_map = {'A': 'SensorX', 'B': 'SensorY', 'C': 'SensorZ', 'D': 'SensorW'}

timestamp_log = [100, 101, 102, 103, 104, 105, 106, 107, 108]

# Decoy function that calculates average but is never used
def calculate_average(signal_list):
    return sum(signal_list) / len(signal_list)

# Unused recursive function to mislead about complexity
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Misleading intermediate transformation (not part of main logic)
raw_magnitudes = [abs(math.sin(x[0]) * x[2]) for x in data_stream]

# Filter data by type 'A' and 'C' — only this subset is relevant
criteria_types = ['A', 'C']
filtered_data = [entry for entry in data_stream if entry[1] in criteria_types]

# Red herring: string processing on irrelevant labels
label_string = ''.join([t[1] for t in data_stream])
label_counts = {char: label_string.count(char) for char in set(label_string)}

# Distractor: complex bit manipulation with timestamps (unused later)
shifted_times = []
for t in timestamp_log:
    shifted = (t << 2) ^ 0xFF
    if shifted > 200:
        shifted_times.append(shifted)

# Real processing begins here — extract values for 'A' and 'C'
signal_values = [x[0] for x in filtered_data]

# Apply non-linear transformation: log(1 + exp(x)) for robustness (real computation)
transformed = [math.log(1 + math.exp(val)) for val in signal_values]

# Weighted contribution based on position in filtered list (enumerate usage)
weighted_sum = 0.0
for i, value in enumerate(transformed):
    weight = 1 / (i + 1)  # Higher weight for earlier entries
    weighted_sum += weight * value

# Additional logic: count how many original entries had magnitude > 5.0
high_magnitude_count = len([x for x in data_stream if x[0] > 5.0])

# Another decoy: zipping unrelated sequences
zipped_dummies = list(zip(raw_magnitudes[::2], shifted_times[:len(raw_magnitudes[::2])]))

# Real final step: combine weighted_sum with count in non-obvious way
temp_offset = math.ceil(high_magnitude_count * 1.5)

# Critical statement
final_output = int(weighted_sum * temp_offset)

print(f"Result: {final_output}")