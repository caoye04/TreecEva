import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum([x ** 2 for x in data if x > 0]) // (len(data) or 1)

# Misleading pre-processing chain
def false_normalization(arr):
    factor = 1.75 if sum(arr) > 100 else 0.95
    return [a * factor + 2 for a in arr]

# Distractor: complex but unused transformation
class SignalMask:
    def __init__(self, key):
        self.key = key
        self.shift = (key * 3) % 7
    
    def scramble(self, val):
        return (val ^ self.shift) + self.key

# Real processing function with conditional logic and lambda use
def process_signal(data, limit):
    # Step 1: Filter values above threshold
    filtered = [x for x in data if x > limit]
    
    # Step 2: Apply adaptive gain using conditional expression
    base_gain = 1.5 if len(filtered) > 3 else 0.8
    amplified = list(map(lambda x: x * base_gain, filtered))
    
    # Step 3: Rectify negative drift (no effect here, but adds confusion)
    rectified = [abs(x) if x < 0 else x for x in amplified]
    
    # Step 4: Accumulate with decay factor
    decay = 0.9
    accumulated = 0
    for val in rectified:
        accumulated = accumulated * decay + val
    
    # Step 5: Apply nonlinear compression if needed
    if accumulated > 50:
        accumulated = math.log(accumulated) * 10
    
    return int(accumulated)

# Secondary distractor function
def legacy_calibrate(seq):
    return [seq[i] + seq[i-1] for i in range(1, len(seq))] + [0]

# Simulated sensor readings (irrelevant computation)
sensor_log = [12, 15, 8, 23, 19, 31, 14]
baseline = sum(sensor_log) / len(sensor_log)
adjusted_log = [x - baseline + 3 for x in sensor_log]

# Unused transformation pipeline
dummy_mask = SignalMask(key=5)
masked_data = [dummy_mask.scramble(int(x)) for x in adjusted_log]

# Core signal data (obfuscated initialization)
raw_data = [i * 2 + (i % 3) for i in range(1, 9)]  # Generates: [3,6,7,10,13,14,17,20]

# Transform via irrelevant normalization
transformed_data = false_normalization(raw_data)

# Threshold derived from misleading statistics
median_val = sorted(raw_data)[len(raw_data)//2]
thresh_proxy = median_val * 0.75
threshold = 8 if thresh_proxy < 10 else 12

# Critical execution point
final_output = process_signal(transformed_data, threshold)

# Print target result
print(f"Target result: {final_output}")