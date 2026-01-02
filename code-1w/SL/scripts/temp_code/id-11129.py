def analyze_pattern(sequence):
    count = 0
    for s in sequence:
        if 'error' in s.lower():
            count += 1
    return count

baseline = [10, 20, 30, 40]
readings = ['Data OK', 'Minor Warning', 'ERROR: threshold exceeded', 'Normal', 'critical ERROR']

# Irrelevant string processing (distractor)
tokenized = [r.split() for r in readings]
flat_tokens = [item for sublist in tokenized for item in sublist]
distinct_words = set(word.lower() for word in flat_tokens)

# Semi-relevant preprocessing
error_count = analyze_pattern(readings)
safe_count = len(readings) - error_count

# Dummy transformation chain (dead computation)
adjusted_baseline = [x * 1.1 for x in baseline]
normalized = [round(a / sum(adjusted_baseline), 3) for a in adjusted_baseline]
entropy_proxy = 0.0
for n in normalized:
    if n > 0:
        entropy_proxy -= n * __import__('math').log(n)

# Core logic embedded within distractions
scaling_factor = 1 + (safe_count / len(readings)) * 0.5
penalty = 0.2 * error_count

# Key state tracking with mixed operations
performance_log = []
for val in baseline:
    temp = val * scaling_factor
    if temp > 25:
        temp -= penalty * 2
    else:
        temp -= penalty
    performance_log.append(round(temp, 3))

# Final aggregation with string-based condition (using string method)
status_flags = ''.join(['P' if p > 20 else 'L' for p in performance_log])

if status_flags.count('L') > 1:
    adjustment = 0.85
else:
    adjustment = 1.05

# Critical statement
final_score = calculate_performance(baseline, readings)

# Helper function defined late (increases cognitive load)
def calculate_performance(base, logs):
    raw_total = sum(base)
    err_count = analyze_pattern(logs)
    modifier = 1 - (err_count * 0.05)
    intermediate = raw_total * modifier
    # Use of string method in non-trivial way
    flag = "_".join(logs[0].split()).isalpha()
    if flag:
        intermediate += 10
    return round(intermediate * adjustment, 2)

print(f"Result: {final_score}")