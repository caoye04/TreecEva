def analyze_system_metrics(raw_data, thresholds):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = []
    for entry in raw_data:
        if isinstance(entry, dict) and 'temp' in entry:
            temp_buffer.append(entry['temp'] * 1.8 + 32)

    # Distractor: unused transformation
    adjusted_data = [x.get('value', 0) * 0.95 for x in raw_data if isinstance(x, dict)]

    # Core data extraction
    extracted = []
    for i, item in enumerate(raw_data):
        if i % 2 == 0 and isinstance(item, dict):
            if 'metric_a' in item:
                extracted.append(item['metric_a'])
            elif 'score' in item:
                extracted.append(item['score'] * 2)

    # Normalization using min-max scaling
    if extracted:
        min_val, max_val = min(extracted), max(extracted)
        range_val = max_val - min_val if max_val != min_val else 1
        normalized = [(x - min_val) / range_val for x in extracted]
    else:
        normalized = [0]

    # Misleading secondary normalization (not used in final path)
    z_scores = [(x - sum(normalized)/len(normalized)) for x in normalized] if len(normalized) > 1 else [0]

    # Weight assignment with zip and enumerate
    categories = ['latency', 'throughput', 'stability', 'error_rate']
    base_weights = [0.4, 0.3, 0.2, 0.1]
    metric_weights = {cat: weight for cat, weight in zip(categories, base_weights)}

    # Simulated threshold comparison (distractor)
    compliance = {}
    for k, v in thresholds.items():
        compliance[k] = sum(1 for x in extracted if x >= v)

    # Real processing begins: reconstructing results from pattern
    patterned_results = []
    for idx, val in enumerate(normalized):
        shifted = val * (idx + 1) ** 0.5
        patterned_results.append(shifted if shifted < 1.0 else 1.0)

    # Final aggregation structure
    normalized_results = {}
    for j, res in enumerate(patterned_results):
        key = categories[j % len(categories)]
        if key in normalized_results:
            normalized_results[key].append(res)
        else:
            normalized_results[key] = [res]

    # Reduce dictionary values to single scores
    for k in normalized_results:
        lst = normalized_results[k]
        normalized_results[k] = sum(lst) / len(lst)

    # Critical statement
    final_score = evaluate_performance(metric_weights, normalized_results)
    return final_score


def evaluate_performance(weights, results):
    # Simple weighted sum despite complex setup
    total = 0.0
    for metric, weight in weights.items():
        total += results.get(metric, 0) * weight
    return round(total * 1000)  # Amplify for integer output

# Simulated input data
input_data = [
    {'metric_a': 120, 'temp': 45},
    {'score': 60},
    {'metric_a': 180},
    {'metric_a': 90, 'flag': True},
    {'score': 75},
    {'metric_a': 210}
]

thresholds_config = {
    'critical': 200,
    'warning': 150
}

# Unused recursive function (red herring)
def calculate_depth(node, acc=0):
    if not node or 'child' not in node:
        return acc
    return calculate_depth(node['child'], acc + 1)

# Trigger execution
result_dict = {'raw': input_data}
processed = analyze_system_metrics(result_dict['raw'], thresholds_config)

# Key assignment
final_score = processed
print(f"Result: {final_score}")