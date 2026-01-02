from itertools import combinations

# System diagnostics log analysis
raw_logs = ['OK', 'WARN: disk', 'ERR: io', 'OK', 'WARN: mem', 'OK', 'ERR: net', 'WARN: cpu']

efficiency = 0
errors = 0
warnings = 0
temp_flags = []
buffer_size = 4
overhead_counter = 0

# Analyze log sequence
for i, entry in enumerate(raw_logs):
    if entry.startswith('ERR'):
        errors += 1
        efficiency -= 1.5
        temp_flags.append(i)
    elif entry.startswith('WARN'):
        warnings += 1
        efficiency -= 0.7
        if 'disk' in entry:
            overhead_counter += 2
        else:
            overhead_counter += 1
    else:
        efficiency += 1.0

# Simulate buffer processing cycles (distractor loop)
for cycle in range(buffer_size):
    overhead_counter *= 0.95
    if overhead_counter < 1:
        overhead_counter = 1

# Compute redundancy metric from log patterns (semi-relevant)
unique_entries = set(raw_logs)
redundancy_factor = len(raw_logs) - len(unique_entries)
efficiency -= redundancy_factor * 0.3

# Generate all possible warning pairs (uses itertools - required feature)
warning_pairs = list(combinations([log for log in raw_logs if log.startswith('WARN')], 2))
pair_complexity = len(warning_pairs) * 0.1  # Minor efficiency impact

efficiency -= pair_complexity

# Normalize efficiency to 0-10 scale
normalized_efficiency = max(0, min(10, efficiency + 5))  # Shifted normalization

# Final scoring logic
min_error_threshold = 2
penalty_rate = 1.2

if errors >= min_error_threshold:
    base_score = 50
else:
    base_score = 70

adjustment = (normalized_efficiency * 3) - (warnings * 4) - (errors * penalty_rate * 5)

final_score = int(base_score + adjustment)

# Irrelevant string transformation (distractor)
summary = ''.join([s[0] for s in raw_logs if s != 'OK'])
summary_encoded = summary.lower().replace(':', '').upper()

# Print final result as required
print(f"Result: {final_score}")