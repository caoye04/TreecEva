def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant data processing (red herring)
def compute_entropy(data):
    from math import log
    freq_map = {}
    total = len(data)
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0.0
    for v in freq_map.values():
        p = v / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Unused helper function (dead code path)
def normalize_vector(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Misleading transformation chain
text_data = "87,65,92,44,73,81,56"
raw_str_list = text_data.split(',')
str_processed = [s.strip() for s in raw_str_list]
decoy_array = [int(s) for s in str_processed if s.isdigit()]

# Distractor: complex but unused bitwise logic
temp_value = 0
for x in decoy_array:
    temp_value ^= x << 2
    temp_value |= (x + 1) & 7

# Another red herring: frequency analysis of digits
all_digits = ''.join(str(x) for x in decoy_array)
digit_freq = {d: all_digits.count(d) for d in '0123456789' if all_digits.count(d) > 0}

# Real computation begins here — deeply nested and obscured
baseline = [70, 75, 80, 85, 90]
metric_data = [68, 77, 85, 82, 88]

# Conditional manipulation with early exit red herring
if sum(baseline) // len(baseline) >= 75:
    adjusted_metrics = []
    for val in metric_data:
        if val < 70:
            adjusted_val = val + 5
        elif val > 85:
            adjusted_val = val + 2
        else:
            adjusted_val = val + 1
        adjusted_metrics.append(adjusted_val)
        
        # Decoy break that doesn't trigger
        if adjusted_val == 100:
            break  # never reached
else:
    adjusted_metrics = metric_data.copy()

# Key recursive filtering function used in evaluation
def filter_outliers(vals, limit=2):
    if limit <= 0 or len(vals) < 5:
        return vals
    avg = sum(vals) / len(vals)
    new_vals = [v for v in vals if abs(v - avg) / avg < 0.15]
    return filter_outliers(new_vals, limit - 1)

# Apply filtering to cleaned data
filtered_metrics = filter_outliers(adjusted_metrics)

# Simulate performance scoring with string-based condition
status_flag = "optimal" if len(filtered_metrics) >= 4 else "review"
score_modifier = 1.0
if status_flag.startswith('opt'):
    score_modifier = 1.1
else:
    score_modifier = 0.9

# Real scoring logic buried in abstraction
def evaluate_performance(metrics, base):
    match_count = sum(1 for m, b in zip(metrics, base) if m >= b)
    base_strength = sum(base) / len(base)
    pattern_bonus = analyze_pattern(metrics)
    raw_score = match_count * 10 + pattern_bonus * 5
    return int(raw_score * score_modifier)

# Secondary adjustment based on irrelevant historical offset
historical_offset = compute_entropy([1,2,2,3,3,3,4,4,5]) * 10  # ~42.14
adjustment = int(historical_offset % 7) if len(digit_freq) % 2 == 1 else 0

# Critical statement — target of query
final_score = evaluate_performance(metric_data, baseline) + adjustment

# Final red herring: unused tuple unpacking
dummy_tuple = (final_score, final_score * 2, final_score // 3)
one, two, three = dummy_tuple

# Output result as required
print(f"Target result: {final_score}")