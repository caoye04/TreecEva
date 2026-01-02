def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function analyzing efficiency (dead code path)."""
    return [x for x in data if x > threshold]

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
data_checksum = 0xDEADBEEF

# Real input data
raw_metrics = [0.82, 0.91, 0.77, 0.65, 0.88]

# Misleading transformation chain (partially unused)
processed = []
for i, val in enumerate(raw_metrics):
    if i % 2 == 0:
        processed.append(round(val ** 2, 3))
    else:
        processed.append(round(val + 0.1, 3))

# Decoy weight vector (not used)
decoy_weights = [0.1, 0.3, 0.2, 0.25, 0.15]

# Actual weights used in calculation
weights = [2, 3, 1, 4, 2]

# Spurious string manipulation (distractor)
status_flags = ['OK', 'OK', 'WARNING', 'CRITICAL', 'OK']
flag_summary = ''.join([s[0] for s in status_flags])
alert_count = flag_summary.count('W') + flag_summary.count('C')

# Fake normalization (never called)
def normalize_vector(v):
    norm = sum(x**2 for x in v) ** 0.5
    return [x/norm for x in v]

# Another red herring: bit manipulation on checksum
shifted = (data_checksum << 3) & 0xFFFFFFFF
inverted = ~shifted & 0xFFFFFFFF

# Real computation begins here
scaling_factor = 100 // len(raw_metrics)  # Integer division
adjusted_metrics = [int(m * scaling_factor * 10) / 10 for m in raw_metrics]

# Weighted scoring logic
weighted_sum = 0
weight_total = 0
for idx, (metric, w) in enumerate(zip(adjusted_metrics, weights)):
    if metric >= 0.7 * scaling_factor:  # Threshold comparison
        contribution = metric * w
        weighted_sum += contribution
    weight_total += w

# Secondary adjustment using list comprehension (real)
corrections = [abs(w - 2) * 0.05 for w in weights]
adjustment = sum(corrections[:3])  # Only first three matter

# Final aggregation
base_score = weighted_sum / weight_total if weight_total > 0 else 0
final_score = round(base_score + adjustment * 10, 2)

# Print result as required
print(f"Target result: {final_score}")