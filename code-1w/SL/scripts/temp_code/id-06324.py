import itertools

# Simulated sensor data with noise and metadata
data_stream = [15, 23, -7, 42, 8, 19, 4, -13, 31, 11, 5, 99, 44, 27]
metadata_tags = ['A', 'B', 'C', 'X', 'D', 'E', 'F', 'Y', 'G', 'H', 'I', 'J', 'K', 'L']

timestamps = [1623456780 + i*60 for i in range(len(data_stream))]
noise_floor = 10
amplification_factor = 2.5

# Irrelevant transformation: frequency domain mock-up (distractor)
freq_weights = [0.1 * (x % 7) for x in range(14)]
distorted_spectrum = [d * w for d, w in zip(data_stream, freq_weights)]

# Decoy function: looks important but unused
def analyze_pattern(seq):
    return [seq[i] - seq[i-1] for i in range(1, len(seq))]

# Real processing begins: extract high-value readings above noise
strong_signals = [x for x in data_stream if abs(x) > noise_floor]

# Tag association (red herring: only some tags matter)
tagged_pairs = list(zip(strong_signals, metadata_tags[:len(strong_signals)]))

# Filter out entries with 'suspicious' tags (X, Y) - actual relevance
cleaned_pairs = [p for p in tagged_pairs if p[1] not in {'X', 'Y'}]
cleaned_signals = [p[0] for p in cleaned_pairs]

# Apply amplification only to positive signals (important detail)
amplified_signals = [
    s * amplification_factor if s > 0 else s
    for s in cleaned_signals
]

# Generate rolling windows of size 3 for stability check (partially relevant)
windows = list(itertools.windowsover(amplified_signals, 3)) if len(amplified_signals) >= 3 else []

# Misleading comment: "Stability metric reduces fluctuating values"
stability_mask = [
    abs(w[0] - w[2]) < 15 for w in windows
]

# Another distractor: time-based filter (unused path)
valid_times = [t for t, d in zip(timestamps, data_stream) if d in strong_signals and d > 0]

# Critical operation: use set logic to find unique magnitude patterns
unique_magnitudes = set(abs(int(s)) for s in amplified_signals)
reference_set = {23, 42, 19, 31, 27}
common_elements = unique_magnitudes & reference_set

# Further distraction: mock ML threshold prediction
ml_confidence = sum(1 for m in common_elements if m % 3 == 1) * 0.7

# Core logic chain resumes: map magnitudes back to original amplified values
# Only include amplified values whose floored magnitude is in common_elements
candidate_values = []
for val in amplified_signals:
    if int(abs(val)) in common_elements:
        candidate_values.append(val)

# Apply secondary filter: must have appeared in a stable window (if windows exist)
if windows:
    stable_indices = {i for i, m in enumerate(stability_mask) if m}
    # Map window indices to element indices (center element)
    valid_centers = {w_idx + 1 for w_idx in stable_indices}
    # amplified_signals has same index as cleaned_signals
    filtered_candidates = [
        v for i, v in enumerate(candidate_values)
        if (cleaned_signals.index(int(v // amplification_factor)) if v > 0 else cleaned_signals.index(v)) + 1 in valid_centers
    ]
else:
    filtered_candidates = candidate_values

# Final processing: apply logarithmic correction to reduce large values
log_adjusted = [round(v - 0.1 * abs(v), 4) for v in filtered_candidates]

# Key computation step
filtered_sum = sum(log_adjusted)

# Output result as required
print(f"Result: {filtered_sum}")