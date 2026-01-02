def analyze_data(records):
    # Irrelevant data transformation (dead path)
    transformed = []
    for r in records:
        if r['status'] == 'active':
            transformed.append({k: v * 2 for k, v in r.items() if isinstance(v, int)})
    
    # Distractor aggregation
    total_temp = sum(r.get('temp', 0) for r in records)
    avg_temp = total_temp / len(records) if records else 0

    # Real metric extraction (buried in noise)
    counts = {'success': 0, 'warning': 0, 'error': 0}
    durations = []
    for entry in records:
        outcome = entry.get('result')
        if outcome in counts:
            counts[outcome] += 1
        if 'duration' in entry:
            durations.append(entry['duration'])

    # Compute median duration (used later)
    sorted_durations = sorted(durations)
    n = len(sorted_durations)
    if n == 0:
        median_duration = 0
    elif n % 2 == 1:
        median_duration = sorted_durations[n // 2]
    else:
        median_duration = (sorted_durations[n // 2 - 1] + sorted_durations[n // 2]) / 2

    # Irrelevant frequency map (decoy)
    freq_map = {}
    for r in records:
        category = r.get('category', 'unknown')
        freq_map[category] = freq_map.get(category, 0) + 1

    # Return only relevant metrics
    return {
        'success_rate': counts['success'] / len(records) * 100 if records else 0,
        'median_duration': median_duration,
        'stability_index': counts['warning'] - counts['error'],
        'peak_load': max((r['load'] for r in records if 'load' in r), default=0)
    }


def normalize_values(data_dict):
    # Misleading normalization function (not actually used)
    result = {}
    max_val = max(data_dict.values()) if data_dict.values() else 1
    for k, v in data_dict.items():
        result[k] = round(v / max_val, 3)
    return result


def calculate_entropy(values):
    # Dead-end mathematical distraction
    from math import log2
    total = sum(values)
    if total == 0:
        return 0
    entropy = 0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 4)


def adjust_for_latency(metric, latencies):
    # Unused adjustment logic (red herring)
    base = metric * (1 + sum(latencies) / 1000)
    return int(base) if base > 10 else round(base, 2)


def evaluate_performance(metrics, weights):
    # Core calculation buried in distractions
    score = 0.0
    
    # Key components
    if metrics['success_rate'] >= 90:
        score += 40
    elif metrics['success_rate'] >= 75:
        score += 25
    else:
        score += 10
    
    # Median duration impact
    if metrics['median_duration'] < 50:
        score += 30
    elif metrics['median_duration'] < 100:
        score += 20
    else:
        score += 5
    
    # Stability bonus
    if metrics['stability_index'] > 0:
        score += 15
    elif metrics['stability_index'] == 0:
        score += 5
    else:
        score += -10
    
    # Peak load penalty
    if metrics['peak_load'] > 800:
        score -= 20
    elif metrics['peak_load'] > 500:
        score -= 10

    # Weighted adjustment (weights are passed but mostly ignored except one)
    final_weights = {}
    for k in weights:
        if k == 'critical':
            final_weights[k] = weights[k] * 1.2
        else:
            final_weights[k] = weights[k]  # unused in actual logic
    
    # Only 'critical' weight is actually applied
    if 'critical' in weights and weights['critical'] > 0.7:
        score *= 1.15
    
    return int(round(score))

# Main execution with decoy variables
raw_records = [
    {'result': 'success', 'duration': 45, 'status': 'active', 'load': 700, 'temp': 68},
    {'result': 'success', 'duration': 55, 'status': 'inactive', 'load': 400, 'temp': 70},
    {'result': 'warning', 'duration': 40, 'status': 'active', 'load': 300, 'temp': 65},
    {'result': 'success', 'duration': 60, 'status': 'active', 'load': 900, 'temp': 72},
    {'result': 'error', 'duration': 120, 'status': 'active', 'load': 550, 'temp': 69},
    {'result': 'success', 'duration': 30, 'status': 'inactive', 'load': 200, 'temp': 66},
    {'result': 'success', 'duration': 40, 'status': 'active', 'load': 850, 'temp': 71}
]

# Irrelevant preprocessing
processed = [{k: v for k, v in item.items() if k != 'temp'} for item in raw_records]
category_stats = {}
for item in processed:
    cat = item.get('status', 'unknown')
    category_stats[cat] = category_stats.get(cat, 0) + 1

# Actual pipeline
metrics = analyze_data(raw_records)

# Distractor weight variations
weights_full = {'primary': 0.8, 'secondary': 0.6, 'critical': 0.85, 'aux': 0.3}
weights_partial = {'primary': 0.5, 'critical': 0.6}

# Final computation
final_score = evaluate_performance(metrics, weights_full)

# Print result as required
print(f"Target result: {final_score}")