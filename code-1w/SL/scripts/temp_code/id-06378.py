import itertools

def analyze_events(raw_data, filters):
    # Irrelevant preprocessing (distractor)
    cleaned = [x for x in raw_data if x > -1]
    temp_stats = {i: val * 2 for i, val in enumerate(cleaned) if val % 3 == 0}
    return [x for x in cleaned if x in filters]

# Misleading auxiliary function (dead logic path)
def compute_health_score(timestamps, weights=None):
    if weights is None:
        weights = [1] * len(timestamps)
    weighted_sum = sum(t * w for t, w in zip(timestamps, weights))
    return weighted_sum // len(timestamps) if timestamps else 0

# Core data with red herring values
log_entries = [142, 177, 205, 138, 191, 220, 153, 168]
system_flags = {k: v > 150 for k, v in enumerate(log_entries)}
offset_table = list(itertools.accumulate([3, -1, 2, -2, 4], lambda a, b: a + b))

# Decoy transformation chain
mapped_diagnostics = []
for idx, entry in enumerate(log_entries):
    shifted = entry + offset_table[idx % len(offset_table)]
    if shifted % 2 == 0:
        mapped_diagnostics.append(shifted * 1.5)
    else:
        mapped_diagnostics.append(shifted * 0.75)

# Unused but plausible-looking aggregation
aggregated_diags = list(map(lambda x: int(x // 1), mapped_diagnostics))
duplicate_mask = [item in aggregated_diags[:-1] for item in aggregated_diags]

# Real processing begins here — heavily buried
reference_sequence = [140, 160, 180, 200, 220]
active_indices = [i for i, x in enumerate(log_entries) if x >= 150]

# Conditional expression with modular arithmetic distraction
threshold_map = {i: ref + (i % 3) * 5 for i, ref in enumerate(reference_sequence)}
system_thresholds = [threshold_map[i] for i in range(len(log_entries))]

# Key logic embedded in complex comprehension with enumerate and zip
adjusted_scores = []
for i, (entry, threshold) in enumerate(zip(log_entries, system_thresholds)):
    if i not in active_indices:
        continue
    diff = abs(entry - threshold)
    penalty = diff // 4 if diff > 8 else 0
    score = entry - penalty
    adjusted_scores.append(score)

# Secondary filtering based on character count in hex representation (string manipulation red herring)
hex_lengths = [len(hex(score)) for score in adjusted_scores]
valid_scores = [s for s, h in zip(adjusted_scores, hex_lengths) if h == 3]

# Final computation using tuple unpacking and set intersection
baseline_set = set(range(150, 181))
overlap = list(set(valid_scores) & baseline_set)

# Destructuring assignment with dummy variables
primary, *rest = sorted(overlap, reverse=True) if overlap else [0], []

# Critical statement containing the answer
final_diagnostic = primary * 2 - len(rest)

Result: final_diagnostic