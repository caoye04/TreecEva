import itertools

# Simulated sensor data with noise and metadata
data_stream = [107, 214, 153, 92, 188, 251, 134, 89, 201, 166]
noise_floor = 85
calibration_offset = 12

# Irrelevant auxiliary variables (distractors)
temp_buffer = [x + calibration_offset for x in data_stream if x % 2 == 0]
status_flags = {i: 'OK' if x > 100 else 'LOW' for i, x in enumerate(data_stream)}
checksum = sum(temp_buffer) % 256

# Simulate historical thresholds (unused but plausible)
historical_avgs = []
for window_size in range(3, 6):
    averages = [sum(data_stream[i:i+window_size]) / window_size 
                for i in range(len(data_stream) - window_size + 1)]
    historical_avgs.extend(averages)

# Primary signal processing chain
raw_signals = (x - calibration_offset for x in data_stream)
valid_signals = [x for x in raw_signals if x > noise_floor]

# Bit manipulation red herring (irrelevant to final result)
bit_score = 0
for val in valid_signals:
    rotated = ((val << 3) & 0xFF) | ((val >> 5) & 0xFF)
    bit_score += bin(rotated ^ 0xAA).count('1')

# Logical filtering with misleading short-circuit pattern
threshold_mask = [(x > 100) and (True or x < 50) for x in valid_signals]  # 'or x < 50' is dead logic
masked_values = [x for x, mask in zip(valid_signals, threshold_mask) if mask]

# Decoy transformation using itertools (never used)
decoys = list(itertools.accumulate(valid_signals, lambda a, b: a + (b % 17)))
decoys = [x for x in decoys if x % 19 == 0]  # Unused filtered decoys

# Actual computation path
squared_valid = [x * x for x in valid_signals]
mod_filtered = [x % 103 for x in squared_valid]
filtered_results = [x for x in mod_filtered if x % 2 == 1]  # Only odd remainders
filtered_sum = sum(filtered_results)

# Output target result
print(f"Result: {filtered_sum}")