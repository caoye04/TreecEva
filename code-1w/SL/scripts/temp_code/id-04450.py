import itertools

def analyze_signal(pattern):
    # Irrelevant signal analysis with decoy logic
    if len(pattern) < 5:
        return sum([p ** 2 for p in pattern])
    else:
        return sum([p % 3 for p in pattern]) // 2


def process_metrics(raw):
    # Distractor function: looks important but unused in final path
    temp_vals = [x * 1.5 for x in raw if x > 0]
    return [round(v, 2) for v in temp_vals]


def filter_outliers(data_stream):
    # Real preprocessing step embedded in noise
    threshold = sum(data_stream) / len(data_stream)
    cleaned = [d for d in data_stream if abs(d - threshold) < threshold * 0.6]
    return cleaned if len(cleaned) > 0 else data_stream


def transform_sequence(seq):
    # Bit manipulation red herring
    shifted = [(s << 1) ^ 0x5 for s in seq]
    reversed_seq = list(reversed(shifted))
    return [r % 100 for r in reversed_seq]


def compute_entropy(values):
    # Unused mathematical distraction
    from math import log2
    counts = {v: values.count(v) for v in set(values)}
    total = len(values)
    entropy = sum(-(count/total) * log2(count/total) for count in counts.values())
    return round(entropy, 4)


def evaluate_stage_score(stage_data, weights):
    # Mix of real and fake operations
    weighted_sum = 0
    for i, val in enumerate(stage_data):
        if i % 2 == 0:
            weighted_sum += val * weights.get('even', 1.1)
        else:
            weighted_sum += val * weights.get('odd', 0.9)
    adjustment = len(stage_data) > 3 and stage_data[0] > 20
    bonus = 10 if adjustment else 0
    return weighted_sum + bonus  # Actual contributor to final result


def evaluate_performance(metrics):
    # Core logic buried in distractions
    base_metrics = filter_outliers(metrics)
    
    # Decoy transformations
    _ = transform_sequence(base_metrics)
    _ = analyze_signal(base_metrics)
    
    # Conditional expression used meaningfully
    scale_factor = 1.75 if any(m > 25 for m in base_metrics) else 1.2
    
    scaled_metrics = [m * scale_factor for m in base_metrics]
    
    # Real evaluation happens here
    config = {'even': 1.3, 'odd': 0.8}
    stage_score = evaluate_stage_score(scaled_metrics, config)
    
    # String method as subtle distractor
    flag_check = "performance_ok".upper().replace("_", " ").split()[0]
    
    # Critical branching with early return avoided
    penalty = 0
    if len(scaled_metrics) >= 4:
        gap = max(scaled_metrics) - min(scaled_metrics)
        if gap > 30:
            penalty = gap * 0.3
    
    # Final computation
    raw_final = stage_score - penalty
    
    # Conditional expression determining final adjustment
    final_modifier = 1.1 if all(x % 2 == 1 for x in map(int, scaled_metrics)) else 0.95
    
    # Answer-determining assignment
    final_score = int(raw_final * final_modifier)
    
    # Dead code path - misleading continuation
    if False:
        fallback = compute_entropy(scaled_metrics)
        final_score = int(fallback * 100)
    
    return final_score

# Irrelevant dataset generation (distractor)
data_log = [12, 18, 22, 31, 45]
_ = process_metrics(data_log)

# Primary input with significance
metric_data = [15, 23, 19, 27]

# Key execution point
final_score = evaluate_performance(metric_data)

# Output result as required
print(f"Result: {final_score}")