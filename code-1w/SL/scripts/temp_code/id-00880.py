import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum([i ** 2 for i in range(x)])

# Decoy transformation that is never called
def decoy_transform(data):
    return [d * 3 + 7 for d in data if d % 2 == 0]

# Real transformation function used in computation
def apply_filter_and_shift(signal):
    filtered = [x for x in signal if x > 50]  # Only keep strong signals
    shifted = [(x - 50) * 2 for x in filtered]  # Normalize and scale
    return shifted

# Data augmentation with slicing - relevant only in part
def augment_data(raw_sequence):
    mid = len(raw_sequence) // 2
    first_half = raw_sequence[:mid]
    second_half = raw_sequence[mid:]
    # Only second_half is actually used below
    reversed_chunk = second_half[::-1]
    expanded = [x * 2 for x in reversed_chunk]
    return expanded

# Core processing with accumulation and conditional logic
def process_chunk(cleaned):
    accumulator = 0
    for val in cleaned:
        if val < 0:
            accumulator -= int(math.sqrt(abs(val)))
        elif val == 0:
            accumulator += 10
        else:
            # Main arithmetic path
            log_component = math.log(val) if val > 0 else 0
            floor_val = math.floor(log_component * 3)
            accumulator += floor_val
    return accumulator

# Irrelevant constants (distractors)
CALIBRATION_OFFSET = 27.3
MAX_ITERATIONS = 1000
THRESHOLD_LIMIT = 85
DUMMY_MASK = [1, 0, 1, 1, 0]

# Simulated sensor input - real data source
raw_sensor_data = [45, 60, 55, 70, 80, 40, 90, 95, 30, 65]

# Step 1: Filter and shift signal values above threshold
filtered_signal = apply_filter_and_shift(raw_sensor_data)

# Step 2: Augment data using slicing; only second half contributes
augmented_segment = augment_data(filtered_signal)

# Misleading intermediate (not used later)
partial_sum = sum(filtered_signal[:3]) * 0.5

# Step 3: Apply final transformation to get working data
transformed_data = [int(x * 1.5) for x in augmented_segment if x % 2 == 0]

# Step 4: Process chunk to produce final output
final_output = process_chunk(transformed_data)

print(f"Result: {final_output}")