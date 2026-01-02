from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_traffic(flow_log):
    stats = defaultdict(int)
    for entry in flow_log:
        stats[entry['source']] += entry['bytes']
    return {k: v for k, v in stats.items() if v > 1000}

# Misleading data transformation
def transform_signal(samples):
    transformed = []
    for s in samples:
        if s < 0:
            transformed.append(abs(s) * 0.5)
        else:
            transformed.append(math.sqrt(s) if s > 0 else 0)
    return [x * 1.5 for x in transformed]

# Unused utility
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core logic disguised among distractors
def filter_outliers(data, limit=50):
    # Heavily nested filtering with red herring conditions
    clean = []
    temp_flags = []
    for item in data:
        flag = True
        if isinstance(item, dict) and 'value' in item:
            val = item['value']
            if val < 0: 
                flag = False
            if val > limit:
                temp_flags.append(True)
                continue  # skip large values
            bits = bin(val).count('1')
            if bits % 3 == 0:  # irrelevant bit check
                temp_flags.append(False)
            clean.append(val)
        else:
            clean.append(1)
    return clean

# Secondary processing with conditional expression distraction
def aggregate_metrics(values):
    summary = defaultdict(float)
    magnitude = sum([v ** 0.5 for v in values]) + 1
    
    for i, v in enumerate(values):
        weight = 1.5 if i % 2 == 0 else 0.75
        adjusted = v * weight * (1.1 if v > 10 else 0.9)
        summary[f'level_{i // 3}'] += adjusted

    # Complex conditional expression
    bonus = 5.0 if len(values) > 4 and sum(values) / len(values) >= 8 else (2.5 if len(set(values)) == len(values) else 1.0)
    
    return dict(summary), bonus

# Main evaluation with multiple concepts
def evaluate_performance(raw_metrics, threshold):
    # Step 1: Filter relevant entries
    filtered = [x for x in raw_metrics if x >= 5]  # ignore values < 5
    
    # Step 2: Apply conditional transformation
    processed = []
    for x in filtered:
        if x > threshold:
            processed.append(x * 0.8)
        else:
            processed.append(x * 1.1)
    
    # Step 3: Aggregate using complex weighting
    groups, extra = aggregate_metrics(processed)
    
    # Step 4: Summarize levels with set operations distraction
    level_keys = set(groups.keys())
    expected_levels = {f'level_{i}' for i in range(5)}
    missing = expected_levels - level_keys
    penalty = len(missing) * 1.5 if missing else 0
    
    # Step 5: Compute base score
    base_score = sum(groups.values())
    
    # Step 6: Apply bonus and penalty
    final = base_score + extra - penalty
    
    # Step 7: Clamp to realistic range (key step)
    final = max(10, min(final, 1000))
    
    # Step 8: Additional adjustment based on parity (red herring)
    total_int = int(sum(processed))
    if bin(total_int).count('1') % 2 == 0:  # even popcount
        final *= 1.05
    else:
        final *= 0.95

    # Final result
    return round(final, 4)

# Irrelevant global computation
dummy_log = [{'source': f'host{i}', 'bytes': i*100} for i in range(1, 15)]
traffic_analysis = analyze_traffic(dummy_log)

# Signal data that goes unused
raw_signal = [16, 25, 0, 36, -4, 49]
processed_signal = transform_signal(raw_signal)

# Actual input data for the task
metric_data = [
    {'value': 12}, {'value': 8}, {'value': 15}, {'value': 6},
    {'value': 20}, {'value': 9}, {'value': 11}
]

# Extract base values for processing
base_values = [item['value'] for item in metric_data]

# Outlier filtering (modifies data)
cleaned = filter_outliers([{"value": v} for v in base_values], limit=18)

# Threshold definition (critical)
base_threshold = 10

# Key statement: this produces the answer
temp_result = [x * 1.1 if x <= base_threshold else x * 0.8 for x in cleaned]
final_score = evaluate_performance(temp_result, base_threshold)

print(f"Result: {final_score}")