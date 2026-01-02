import math

# Simulate cognitive load in a multi-stage logic processor
def analyze_pattern(sequence, threshold_func):
    accumulated = 0
    for val in sequence:
        if threshold_func(val):
            accumulated += int(math.sqrt(abs(val))) * 2
    return accumulated

# Irrelevant helper: computes signal decay (not used in final result)
def compute_decay(age):
    return round(math.exp(-0.1 * age), 4)

# Core evaluation function with embedded lambda
evaluate_stability = lambda segments: sum(
    [analyze_pattern(seg, lambda x: x % 3 == 0 and x > 0) for seg in segments]
)

# Initialize system diagnostics (some are red herrings)
diagnostic_codes = [101, 205, 303, 404, 505]
signal_strength = sum([d % 2 for d in diagnostic_codes])  # distractor
baseline_offset = math.ceil(math.log(signal_strength + 1))  # semi-relevant but unused

# Define logic segments representing neural activation patterns
segment_A = [9, -6, 12, 15, 3]
segment_B = [6, 0, -3, 18]
segment_C = [21, 14, 9, 12, 6, 3]
logic_segments = [segment_A, segment_B, segment_C]

# Secondary analysis: stability margin (unused in main path)
stability_margin = 0
for s in logic_segments:
    non_zero_count = len([x for x in s if x != 0])
    stability_margin += non_zero_count // 2

# Noise filter simulation (dead code path)
noise_floor = 0.05
filtered_segments = []
for seg in logic_segments:
    cleaned = [x for x in seg if abs(x) > noise_floor]
    filtered_segments.append(cleaned)

# Primary computation path
raw_energy = sum([sum(seg) for seg in logic_segments])  # irrelevant aggregate
normalization_factor = len(logic_segments)  # distractor

# Key statement
equilibrium_score = evaluate_stability(logic_segments)

# Print result as required
print(f"Result: {equilibrium_score}")