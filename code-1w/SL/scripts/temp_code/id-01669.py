import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3 * x + 1) % 17

# Another decoy: complex but unused calculation
class SignalAnalyzer:
    def __init__(self, samples):
        self.samples = samples
        self.noise_floor = sum(s ** 0.5 for s in samples if s > 0) / len(samples)

    def get_entropy(self):
        return math.log(len(self.samples)) * 0.5

# Unused recursive red herring
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Distractor: irrelevant data processing chain
temp_log = [i * 1.5 for i in range(10)]
shifted_log = [int(x - 5) for x in temp_log if x > 4]
aggregated = sum(shifted_log) * 0.1

# Core logic disguised among noise
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
mask_sequence = [(p % 10) ^ 5 for p in primes]  # Bitwise XOR distraction

# Real signal hidden in list operations
data_stream = [8, 12, 5, 19, 3, 11, 7]

# Lambda-based filtering (key relevant use)
effective_filter = lambda arr: [x for x in arr if x > 6]

# Summation with conditional transforms
partial_results = []
for val in data_stream:
    if val in primes:
        adjusted = val * 2
    else:
        adjusted = val + 1
    partial_results.append(adjusted)

# Red herring: dead code path with misleading comment
# "Optimize using exponential backoff" (never used)
backoff_sequence = [2 ** i for i in range(6) if i % 2 == 0]

# Actual computation chain
transformed = effective_filter(partial_results)

# Accumulation with offset
base_offset = 4
accumulator = base_offset
for num in transformed:
    if num % 2 == 0:
        accumulator += num // 2
    else:
        accumulator += int(math.sqrt(num))

# Decoy dictionary with plausible-sounding metrics
metrics = {
    'peak': max(data_stream),
    'variance': sum((x - 10) ** 2 for x in data_stream) / len(data_stream),
    'coherence': len([x for x in mask_sequence if x < 7]),
    'dummy_flag': True
}

# Key processing pipeline (contains actual answer derivation)
def process_pipeline(signal):
    # Step 1: filter values above threshold
    stage1 = list(filter(lambda x: x != 12, signal))  # Remove magic number
    
    # Step 2: map using conditional logic disguised as calibration
    calibrated = []
    for x in stage1:
        if x > 10:
            calibrated.append(x - 3)
        elif x == 5:
            calibrated.append(x * 4)
        else:
            calibrated.append(x + 2)
    
    # Step 3: reduce using weighted sum
    weight_seq = [1, -1, 1, -1, 1]  # Alternating weights
    weighted_sum = 0
    for i, val in enumerate(calibrated):
        weight = weight_seq[i % len(weight_seq)]
        weighted_sum += val * weight
    
    # Step 4: post-process with offset from earlier accumulator
    result = weighted_sum + accumulator
    
    # Dead return branch (misleading)
    if result < 0:
        return abs(result) * 2
    return result  # Only this path is taken

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output must follow required format
print(f"Target result: {final_output}")