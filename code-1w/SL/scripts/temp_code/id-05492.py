from itertools import combinations

def analyze_trends(data, threshold=3):
    trend_count = 0
    noise_flag = False
    temp_buffer = []

    for i, val in enumerate(data):
        if val > threshold:
            temp_buffer.append(val * 0.9)
            trend_count += 1
        else:
            temp_buffer.append(val + 0.1)

    if len(temp_buffer) > 10:
        noise_flag = True

    adjusted = [round(x, 2) for x in temp_buffer]
    return adjusted, trend_count, noise_flag

def compute_variance(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance

def generate_pairs(elements):
    # Irrelevant function - decoy
    return list(combinations(elements, 2))
def filter_outliers(sequence, limit=2.5):
    filtered = [x for x in sequence if x <= limit]
    discarded = [x for x in sequence if x > limit]  # dead code path
    return filtered

def calculate_entropy(weights):
    # Unused advanced math
    import math
    entropy = 0
    for w in weights:
        if w > 0:
            entropy -= w * math.log(w)
    return entropy

def evaluate_performance(metrics, base):
    score = 0
    penalty = 0

    # Key logic begins
    raw_values = [x * 1.5 for x in metrics if x >= base]

    for idx, val in enumerate(raw_values):
        if idx % 2 == 0:
            score += val
        else:
            score -= val * 0.5

    # Distraction: irrelevant aggregation
    temp_stats = {}
    temp_stats['max'] = max(raw_values) if raw_values else 0
    temp_stats['min'] = min(raw_values) if raw_values else 0
    temp_stats['range'] = temp_stats['max'] - temp_stats['min']

    # More red herrings
    validation_check = any(x > 10 for x in raw_values)
    debug_snapshot = {"stage": "mid", "score_checkpoint": score}

    # Actual decisive computation
    correction_factor = 0.8 if len(raw_values) < 4 else 1.2
    score *= correction_factor

    # Final adjustment based on baseline interaction
    adjustment = (base * 0.6) if base > 5 else (base * 1.1)
    final_score = int(score - adjustment)

    return final_score

# Simulated dataset
metrics_data = [2, 7, 5, 12, 3, 9]
baseline_ref = 6

# Irrelevant preprocessing
processed_metrics, count, flag = analyze_trends(metrics_data, threshold=4)
variance = compute_variance(metrics_data)
outlier_free = filter_outliers(processed_metrics, limit=8.0)
pair_combinations = generate_pairs([1, 2, 3])

# Main execution point
final_score = evaluate_performance(metrics, baseline_ref)
print(f"Result: {final_score}")