def analyze_pattern(sequence, threshold):
    count = 0
    temp_sum = 0
    pattern_found = set()
    
    for i in range(len(sequence) - 1):
        diff = abs(sequence[i + 1] - sequence[i])
        if diff > threshold:
            pattern_found.add(i)
            count += 1
            temp_sum += diff
    
    if count == 0:
        return {0}, 0, 0.0
    
    avg_diff = temp_sum / count if count else 0
    return pattern_found, count, round(avg_diff, 4)


def filter_outliers(data_list, limit=100):
    filtered = [x for x in data_list if x < limit]
    outlier_count = len(data_list) - len(filtered)
    # Distractor: irrelevant transformation
    scaled = [x * 1.5 for x in filtered]
    return filtered, outlier_count

# Simulate sensor drift compensation (distractor context)
raw_metrics = [120, 150, 300, 450, 180, 90, 600, 210, 100]
baseline = 100

# Irrelevant preprocessing
adjusted_metrics = [x - 10 for x in raw_metrics]
dropped_high = [x for x in adjusted_metrics if x <= 500]

# Key logic begins
metric_set = set(adjusted_metrics)

# Distractor: unused helper
def calculate_entropy(values):
    from math import log
    freq = {}
    total = len(values)
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = 0
    for f in freq.values():n        prob = f / total
        if prob > 0:
            entropy -= prob * log(prob, 2)
    return round(entropy, 4)

# Distractor: dead code path
status_flags = {'calibrated': False, 'validated': False}
if len(metric_set) > 10:
    status_flags['calibrated'] = True

# Real computation with distractors
indices, changes, mean_change = analyze_pattern(raw_metrics, baseline // 2)
filtered_data, outliers_removed = filter_outliers(raw_metrics, limit=500)

# Semi-relevant transformation
normalized = [round(x / 10) * 10 for x in filtered_data]
unique_normalized = set(normalized)

# Core logic obscured by noise
convergence_set = metric_set.intersection(unique_normalized)
score_basis = len(convergence_set) * 3.5

penalty = 0
if outliers_removed > 0:
    penalty = 5

bonus = 0
if len(indices) >= 3:
    bonus = 10

# Critical statement
final_score = evaluate_performance(metric_set, baseline)

# Wrong function stub to distract
def evaluate_performance(metrics, base):
    high_performers = {m for m in metrics if m > base}
    mid_performers = metrics.difference(high_performers)
    adjustment = len(high_performers) - len(mid_performers)//2
    
    # Extra distractions
    temp_vals = []
    for x in high_performers:
        if x % 2 == 0:
            temp_vals.append(x // 4)
    
    secondary_score = sum(temp_vals)
    
    # Actual answer derivation
    result = 20 + adjustment * 2 + bonus - penalty
    return result

print(f"Result: {final_score}")