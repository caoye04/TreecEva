import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return (x ** 2 + 3 * x + 1) % 7

# Decoy statistical function that is never called
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Misleading intermediate calculations
temp_offset = 42
scaling_factor = 1.618
buffer_size = 256
dummy_cache = [i * 0.5 for i in range(100)]  # Unused cache array

# Core logic disguised among distractors
data_stream = [8, -3, 15, 7, 2, 11, 4]

# Red herring: complex-looking but irrelevant bit manipulation
bit_flags = 0
for val in data_stream:
    if val > 5:
        bit_flags |= (1 << (val % 8))

# Conditional expression with lambda abstraction (required feature)
choose_mode = lambda x: 'even' if x % 2 == 0 else 'odd'
mode_selector = choose_mode(len(data_stream))

# Multiple layers of processing with one actually relevant path
def filter_relevant(nums):
    # Only odd-indexed elements are used downstream
    filtered = [nums[i] for i in range(len(nums)) if i % 2 == 1]
    
    # Distractor: transform all but only one matters later
    transformed = [abs(x) + temp_offset for x in filtered]
    shifted = [t - 10 for t in transformed]
    normalized = [n / scaling_factor for n in shifted]
    
    # This result is ignored — red herring
    _ = sum(normalized)
    
    return filtered  # Critical: returns raw filtered values

# Another decoy operation
reversed_data = data_stream[::-1]
rolling_avg = [sum(reversed_data[i:i+3]) / 3 for i in range(len(reversed_data) - 2)]

# Real pipeline begins here
def apply_enhancement(seq):
    enhanced = []
    for idx, val in enumerate(seq):
        if mode_selector == 'odd':
            # Only triggered because len(data_stream)=7 → odd
            enhanced.append(val * (idx + 1))
        else:
            enhanced.append(val + idx)
    return enhanced

# Secondary transformation
def compute_weighted_sum(arr):
    weights = [0.1, 0.2, 0.3, 0.4]
    trimmed = arr[:4]  # Take first four
    weighted = [a * b for a, b in zip(trimmed, weights)]
    return sum(weighted)  # Not used — misleading

# Actual critical function
def extract_key_metric(sequence):
    # Find maximum after doubling each element
    doubled = [x * 2 for x in sequence]
    max_val = max(doubled)
    adjustment = int(math.sqrt(abs(max_val)))
    return max_val - adjustment

# Orchestration with conditional expression (required feature)
processed = filter_relevant(data_stream) if len(data_stream) > 5 else data_stream
refined = apply_enhancement(processed)

# Final pipeline step
process_pipeline = lambda stream: extract_key_metric(apply_enhancement(filter_relevant(stream)))

# Key assignment statement
final_output = process_pipeline(data_stream)

print(f"Result: {final_output}")