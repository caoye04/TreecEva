def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == 'A' and sequence[i+1] == 'C':
            count += 1
    return count

sequence = 'AACGTACGTAATCG'
occurrences = analyze_pattern(sequence)

# Irrelevant string transformation (distractor)
transformed = ''.join([s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(sequence)])
dummy_slice = transformed[3:9]

# Data processing with multiple concepts
raw_data = [4, 8, 15, 16, 23, 42]
flags = {"threshold": 15, "offset": 3, "mode": "strict"}

# Misleading intermediate calculation (dead path)
if len(raw_data) > 10:
    adjustment = sum(x ** 0.5 for x in raw_data)
elif flags["mode"] == "relaxed":
    adjustment = 5
else:
    adjustment = 0  # This is unused later but looks relevant

# Actual computation chain (5-8 logic steps)
def filter_and_shift(values, config):
    filtered = [v for v in values if v > config["threshold"]]
    shifted = [v - config["offset"] for v in filtered]
    return shifted

processed = filter_and_shift(raw_data, flags)

# Use of set operations (required python feature)
unique_values = set(processed)
reference_set = {12, 13, 20}
overlap = unique_values & reference_set  # intersection

# Incorporate slicing (required python feature)
segment = processed[1:3]
segment_sum = sum(segment)

# Conditional state tracking
status_flags = []
if len(overlap) > 0:
    status_flags.append('OVR')
if segment_sum >= 25:
    status_flags.append('HIGH')
if occurrences > 2:
    status_flags.append('MULTI')

# Core logic depends on boolean and arithmetic chain
base_metric = len(processed) * 10
adjustment_factor = 2 if 'MULTI' in status_flags else 1
secondary_boost = 5 if segment_sum > 20 else 0

# Final computation
intermediate = base_metric + secondary_boost
final_score = intermediate - len(status_flags) * 3

# Print required output
print(f"Result: {final_score}")