from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant channels
data_stream = [
    [1, 1, 2, 3, 5, 8, 13],
    [2, 3, 5, 7, 11, 13, 17],
    [1, 4, 9, 16, 25, 36, 49],
    [0, 1, 1, 2, 3, 5, 8],
    [1, 2, 4, 8, 16, 32, 64]
]

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'min_val': 0,
    'max_val': 100,
    'threshold': 42
}

# Noise filter mask (partially used, misleading)
noise_mask = [0.98, 1.02, 0.99, 1.01, 0.97, 1.03, 0.96]

# Apply noise correction (only first two rows actually matter)
corrected_data = []
for i, row in enumerate(data_stream):
    corrected_row = []
    for j, val in enumerate(row):
        if i < 2:  # Only first two rows are relevant
            corrected_row.append(val * noise_mask[j])
        else:
            corrected_row.append(val)  # No correction for others (but looks like there is)
    corrected_data.append(corrected_row)

# Extract prime sequence from second row (actual signal path)
prime_sequence = data_stream[1][:]

# Misleading transformation: frequency analysis on irrelevant data
value_frequency = defaultdict(int)
for row in data_stream[2:]:
    for v in row:
        value_frequency[v] += 1

# Real processing begins: detect Fibonacci pattern in first row
def is_fibonacci_triplet(a, b, c):
    return a + b == c

fib_detections = 0
first_row = corrected_data[0]
for k in range(len(first_row) - 2):
    if is_fibonacci_triplet(first_row[k], first_row[k+1], first_row[k+2]):
        fib_detections += 1

# Hidden logic: count how many primes are also perfect squares (always 0, red herring)
square_primes = [p for p in prime_sequence if round(p**0.5)**2 == p]

# Critical signal aggregation: use only fib_detections and prime gaps
prime_gaps = [prime_sequence[i+1] - prime_sequence[i] for i in range(len(prime_sequence)-1)]
gap_variance = sum((g - sum(prime_gaps)/len(prime_gaps))**2 for g in prime_gaps) / len(prime_gaps)

# Decoy statistical analysis
zipped_analysis = list(zip(prime_sequence[::2], prime_sequence[1::2]))
pair_products = [x * y for x, y in zipped_analysis]

# Core diagnostic computation (depends only on fib_detections and gap_variance)
aggregate_score = 0
for idx, (a, b) in enumerate(zip(prime_sequence, reversed(prime_sequence))):
    if idx % 2 == 0 and a > b:
        aggregate_score += a - b

# This normalization is critical but obscured by distractions
normalization_factor = len([g for g in prime_gaps if g == 2])  # Count twin-like prime gaps
if normalization_factor > 0:
    aggregate_score = aggregate_score / normalization_factor
else:
    aggregate_score = aggregate_score / 1

# Final correction using fib_detections as weight
correction_factor = fib_detections * 1.5

# Offset based on length of constant sequences (irrelevant but looks important)
constant_run_detector = []
for row in corrected_data:
    run_length = 1
    max_run = 1
    for pos in range(1, len(row)):
        if abs(row[pos] - row[pos-1]) < 0.01:
            run_length += 1
        else:
            max_run = max(max_run, run_length)
            run_length = 1
    constant_run_detector.append(max_run)

# Actual offset is fixed but hidden in logic
offset_candidates = [17, 23, 42]
if any(cr > 4 for cr in constant_run_detector):
    offset_value = offset_candidates[0]
else:
    offset_value = 19  # Truth: no run exceeds 1 due to data structure

# Key statement — final_diagnostic combines all processed signals
final_diagnostic = aggregate_score * correction_factor + offset_value

print(f"Result: {final_diagnostic}")