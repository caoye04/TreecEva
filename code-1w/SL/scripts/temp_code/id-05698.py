from itertools import cycle, islice

# Irrelevant helper function (decoy)
def normalize_vector(v):
    magnitude = sum(x ** 2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

# Another decoy: unused transformation
def reflect_across_axis(points, axis=0):
    return [(p[0], -p[1]) if axis == 1 else (-p[0], p[1]) for p in points]

# Misleading entropy simulation with red herring computations
def generate_entropy_stream(length):
    stream = []
    seed = 7
    for i in range(length):
        seed = (seed * 97 + 13) % 1000
        noise = (seed % 17) / 100.0
        # Distractor computation
        temp_offset = (i * noise) % 3.5
        jitter = temp_offset * 0.1
        stream.append(noise + jitter)
    return stream

# Unused recursive variant (dead code path)
def recursive_sum(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx] + recursive_sum(lst, idx + 1)

# Key data transformation function
def transform_sequence(seq, factor=2.5):
    result = []
    for i, val in enumerate(seq):
        # Relevant but disguised calculation
        adjusted = val * factor + (i % 4) * 0.1
        if i % 3 == 0:
            adjusted -= 0.05
        result.append(round(adjusted, 6))
    return result

# Core logic hidden among distractions
def detect_coherence_pattern(buffer):
    coherence = 0
    for i in range(1, len(buffer)):
        diff = buffer[i] - buffer[i-1]
        if abs(diff) < 0.25:
            coherence += int(abs(diff) * 100)
    return coherence * 3

# Primary calculation with meaningful logic
entropy_pool = generate_entropy_stream(12)

# Irrelevant tuple unpacking (distractor)
init_x, init_y, *_ = [1.1, 2.2, 3.3, 4.4, 5.5]

# Use of itertools: cycle over a small segment
rotated_view = list(islice(cycle([0.1, 0.2]), 0, len(entropy_pool)))

# Apply actual transformation needed for final result
tuned_buffer = transform_sequence(entropy_pool, factor=3.1)

# Fake aggregation (misleading intermediate)
cumulative_drift = sum(tuned_buffer[i+1] - tuned_buffer[i] for i in range(len(tuned_buffer)-1) if i % 2 == 0)

# Real signal extraction
signal_hint = sum(1 for x in tuned_buffer if x > 0.5)

# Hidden key operation: pattern-based adjustment
coherence_score = detect_coherence_pattern(tuned_buffer)

# Decoy list comprehension with no effect
_ = [x * 2 for x in rotated_view if x < 0.15]

# Conditional expression used idiomatically (required feature)
scaling_factor = 1.75 if signal_hint > 5 else 0.85

# Final relevant assignment — the answer depends on this
thermal_capacity = calculate_thermal_output(entropy_pool) if 'coherence_score' in locals() and coherence_score > 0 else 0

# Actual definition of the required function (was referenced above)
def calculate_thermal_output(data):
    base = sum(x * 100 for x in data[:8])
    bonus = len([x for x in data if x > 0.6]) * 12
    penalty = (data.index(min(data)) % 7) * 5
    return int(base) + bonus - penalty

# Print target result
print(f"Target result: {thermal_capacity}")