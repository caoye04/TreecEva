import math

# Simulated sensor data from environmental monitoring stations
data_stream = [143, 271, 331, 199, 233, 449, 353, 467, 181, 283, 379, 409, 157, 263]

# Irrelevant auxiliary constants (distractors)
baseline_offset = 17
scaling_factor = 2.3
noise_floor = 42
max_threshold = 500
min_signal_strength = 100

# Primary processing variables
temp_buffer = []
processed_data = []
prime_seed = 13
rolling_checksum = 0

# Decoy function - looks important but unused in critical path
def validate_signal(sequence):
    return all(x > noise_floor for x in sequence) and len(sequence) % 2 == 1

# Another decoy - simulates calibration but irrelevant
calibration_matrix = [[i * j for j in range(3)] for i in range(3)]

def transform_value(val, key):
    shifted = val ^ (key * 7)
    wrapped = (shifted + baseline_offset) % max_threshold
    return int(math.sqrt(wrapped) * scaling_factor) if wrapped > 100 else wrapped + 10

# Simulate multi-stage signal processing
for reading in data_stream:
    if reading < min_signal_strength:
        continue
    transformed = transform_value(reading, prime_seed)
    temp_buffer.append(transformed)
    rolling_checksum ^= transformed

# Apply filtering mask based on bit patterns (some are red herrings)
mask_filter = lambda x: bin(x).count('1') % 2 == 1
masked_data = list(filter(mask_filter, temp_buffer))

# Core processing begins here — meaningful transformation
for item in masked_data:
    # Non-linear amplification
    amplified = item ** 2 // prime_seed
    # Add to final dataset
    processed_data.append(amplified)

# Dead code path — never executed due to logic above, but looks relevant
duplicate_flag = False
if len(data_stream) > 100:
    processed_data.extend(temp_buffer[:10])
    duplicate_flag = True

# Critical distractor: complex-looking but unused aggregation
def compute_entropy(seq):
    total = sum(seq)
    probs = [s / total for s in seq if s > 0]
    return -sum(p * math.log(p) for p in probs)

unused_entropy = compute_entropy(processed_data) if processed_data else 0.0

# Another decoy function with recursive misdirection
def find_root_cycle(n, depth=0):
    if n <= 1 or depth > 5:
        return n
    return find_root_cycle(sum(int(d)**2 for d in str(n)), depth + 1)

# Unused but plausible-sounding diagnostic
diagnostic_roots = [find_root_cycle(x) for x in processed_data]

# Real computation: define aggregation function used later
aggregate_result = lambda seq: sum(seq) // len(seq) if seq else 0

# Introduce a slicing red herring
historical_slice = processed_data[-10:-5]  # looks like it's used, but isn't
shadow_copy = processed_data[::-1]       # reversed copy — no impact

# Key statement: extract multiples of prime_seed and aggregate
filtration_score = aggregate_result(filter(lambda x: x % prime_seed == 0, processed_data))

# Final output
print(f"Result: {filtration_score}")