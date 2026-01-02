from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data stream with noise and redundancy
def generate_noisy_stream():
    base_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
    repeated_stream = (x for _ in range(15) for x in base_sequence)
    return list(islice(repeated_stream, 200))

data_stream = generate_noisy_stream()

# Irrelevant transformation: time dilation mockup (distractor)
time_dilation_map = {}
for idx in range(len(data_stream)):
    time_dilation_map[idx] = data_stream[idx] * 0.97 + (idx % 7)

# Red herring computation: entropy approximation (unused)
entropy_accum = 0.0
freq_count = defaultdict(int)
for val in data_stream:
    freq_count[val] += 1
for count in freq_count.values():
    if count > 0:
        entropy_accum -= (count / len(data_stream)) * (count / len(data_stream))

# Decoy function: looks important but never called
def compute_checksum(sequence):
    checksum = 0
    for i, x in enumerate(sequence):
        checksum ^= (x + i) * 3
    return checksum % 256

# Unused recursive smoothing (dead code path)
def smooth_recursive(seq, depth=0):
    if depth >= 3 or len(seq) < 2:
        return seq
    smoothed = [(seq[i] + seq[i+1]) // 2 for i in range(len(seq)-1)]
    return smooth_recursive(smoothed, depth + 1)

# Actual signal extraction: isolate repeating core pattern
def extract_core_pattern(stream):
    counts = Counter(stream)
    most_common_vals = counts.most_common(4)
    sorted_vals = sorted([v[0] for v in most_common_vals])
    return sorted_vals  # Returns [1, 2, 3, 4]

# Transform data by mapping to positional residue
def transform_signal(pattern):
    mapping = {val: (i * 2 + 1) for i, val in enumerate(pattern)}
    return [mapping.get(x, 0) for x in data_stream if x in mapping]

core_pattern = extract_core_pattern(data_stream)
transformed_data = transform_signal(core_pattern)

# Spurious intermediate: frequency shift analysis (irrelevant)
frequency_shift = defaultdict(list)
for i, x in enumerate(transformed_data):
    frequency_shift[i % 5].append(x % 4)

# Mock AI confidence simulation (distractor variables)
confidence_metrics = []
for chunk in [transformed_data[i:i+10] for i in range(0, len(transformed_data), 10)]:
    local_var = sum(chunk) / len(chunk)
    adjusted_score = abs(local_var - 2.5) * 10
    confidence_metrics.append(adjusted_score)

# Real diagnostic logic: count occurrences of key transformed value
def analyze_pattern(processed):
    # Key insight: only odd-indexed elements matter
    relevant_elements = [x for i, x in enumerate(processed) if i % 2 == 1]
    # Count how many are greater than 3
    count_above_threshold = sum(1 for x in relevant_elements if x > 3)
    # Apply correction based on cycle length
    cycle_iter = cycle([2, 3])
    adjustment = sum(next(cycle_iter) for _ in range(len(relevant_elements) // 10))
    return count_above_threshold * 2 - adjustment

final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")