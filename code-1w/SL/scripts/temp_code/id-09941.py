import itertools

# Simulated sensor data processing with red herrings and complex logic
raw_signals = [15, 23, 8, 42, 7, 31, 18, 26, 13, 37, 9, 46]
noise_floor = 10
decoy_multiplier = 3.14
dummy_flag = True
useless_offset = 999
irrelevant_matrix = [[1, 2], [3, 4]]

# Distractor: Unused transformation function
def transform_signal(x):
    return (x ** 2 + 5) // 3

# Real processing pipeline
active_mask = list(map(lambda x: x > noise_floor, raw_signals))
filtered_data = [x for x, active in zip(raw_signals, active_mask) if active]

# Decoy list comprehension with no side effects
decoys = [x * decoy_multiplier for x in raw_signals if x < noise_floor]

# Phantom calculation with dead variable
phantom_sum = sum([useless_offset for _ in range(3)]) // 3

# Threshold derived from modular arithmetic and bit manipulation
base_threshold = len(filtered_data) ^ 7
threshold = (base_threshold * 2) % 5 or 1

# Misleading intermediate that looks important but isn't used
aggregated_metric = sum(itertools.accumulate(filtered_data, lambda a, b: (a + b) % 17))

# Auxiliary function with conditional expression
def normalize(val, cap=25):
    return val / cap if val > cap else val

# Another decoy function that's defined but not called
def encrypt_data(data):
    return [d ^ 0xAA for d in data]

# Real processing function with nested logic
def process_signals(data, thresh):
    result = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            # Apply normalization only on even indices
            adjusted = normalize(val)
            # Bitwise twist
            shifted = int(adjusted) << 1
            result += shifted
        else:
            # Conditional expression with modular influence
            contribution = (val % thresh) + (1 if val & 1 else -1)
            result += contribution
    # Final adjustment using conditional expression
    return result + (100 if result < 50 else -10)

# Dead code path guarded by impossible condition
if dummy_flag and not dummy_flag:
    final_output = -9999
else:
    final_output = process_signals(filtered_data, threshold)

# Print result for deterministic output
print(f"Target result: {final_output}")