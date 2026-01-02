def analyze_signal(noise_floor, samples):
    filtered = [s for s in samples if abs(s) > noise_floor]
    return sum(filtered) // len(filtered) if filtered else 0

thresholds = {"low": 5, "medium": 12, "high": 25}
diagnostics = [(8, 14), (13, 17), (21, 9), (5, 3)]

# Irrelevant helper function (decoy)
def validate_entry(record):
    return isinstance(record, tuple) and len(record) == 2

# Misleading preprocessing path (dead code)
temp_logs = []
for entry in diagnostics:
    if entry[0] > 10:
        temp_logs.append(entry[1] * 2)

# Unused transformation chain
transform = lambda x: x ** 2 - x
mapped_diagnostics = set()
for a, b in diagnostics:
    mapped_diagnostics.add(transform(a + b))

# Core logic buried in distractions
baseline = 3
offsets = [analyze_signal(baseline, [d[0]*2 for d in diagnostics[:i+1]]) for i in range(len(diagnostics))]

# Complex data transformation with red herring operations
aggregate = 0
for idx, (x, y) in enumerate(diagnostics):
    if x > y:
        aggregate += x ^ (idx + 1)
    else:
        aggregate -= y | idx

# Set operations used meaningfully but with irrelevant extensions
critical_set = {d[0] for d in diagnostics if d[0] > thresholds["low"]}
unused_complement = {i for i in range(30) if i not in critical_set}

# Key computation hidden among multiple layers
intermediate_scores = []
for p in diagnostics:
    raw_score = p[0] * 2 + p[1]
    adjustment = len(critical_set.intersection({p[0], p[1]})) * 3
    intermediate_scores.append(raw_score + adjustment)

# Final processing with distractor variables
rolling_window = []
for s in intermediate_scores:
    rolling_window.append(s % 7)

# Decoy statistical calculation
mean_irrelevant = sum(rolling_window) / len(rolling_window) if rolling_window else 0

# Core answer path
flagged = list(filter(lambda x: x > thresholds["medium"], intermediate_scores))
activation_sequence = [a ^ b for a, b in zip(flagged, offsets[:len(flagged)])]

# Final diagnostic depends on conditional nesting and prior state
final_diagnostic = 0
if len(flagged) >= 2:
    for i, val in enumerate(activation_sequence):
        if i % 2 == 0:
            final_diagnostic += val * baseline
        else:
            final_diagnostic -= val // (i + 1)
else:
    final_diagnostic = -999

# Output the target result
Target result: {final_diagnostic}