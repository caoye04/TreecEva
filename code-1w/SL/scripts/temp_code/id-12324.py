def generate_sequence(seed, length):
    seq = [seed]
    for i in range(1, length):
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)
    return seq

# Irrelevant transformation - distractor
def transform_data(data):
    return [x * 2 + 1 for x in data if x < 50]

# Unused function - dead code path
def deprecated_filter(arr, limit):
    result = []
    for val in arr:
        if val > limit:
            result.append(val // 3)
    return result

# Misleading statistical function with decoy output
def compute_bias_metric(seq):
    evens = sum(1 for x in seq if x % 2 == 0)
    odds = len(seq) - evens
    if odds == 0:
        return float('inf')
    return round(evens / odds, 4)

# Core analysis function with critical logic
def analyze_pattern(seq, thresh):
    count = 0
    segment_sum = 0
    segments = []
    
    # Slice into overlapping windows - relevant use of slicing
    for i in range(len(seq) - 3):
        window = seq[i:i+4]
        if sum(window) > thresh:
            count += 1
            segment_sum += sum(window)
            segments.append(sum(window))
    
    # Red herring: unused list comprehension
    weighted_values = [seg * (i+1) for i, seg in enumerate(segments)]
    
    # Decoy variable that looks important
    normalization_factor = max(segment_sum, 1)
    
    # Actual answer derivation through filtering logic
    filtered_segments = [s for s in segments if s % 4 == 0]  # Only multiples of 4
    
    # Critical line: this determines the final answer
    filtration_score = len(filtered_segments) * segment_sum // (count + 1) if count > 0 else 0
    
    return filtration_score

# Irrelevant global constants
MAX_ITERATIONS = 1000
DEFAULT_BUFFER_SIZE = 256

# Setup sequence generation
initial_seed = 27
sequence_length = 15
threshold = 100

# Generate main sequence
sequence = generate_sequence(initial_seed, sequence_length)

# Distraction: unused transformation
transformed_seq = transform_data(sequence)

# Compute misleading metric
bias_metric = compute_bias_metric(sequence)

# Key execution point
filtration_score = analyze_pattern(sequence, threshold)

# Print target result
print(f"Result: {filtration_score}")