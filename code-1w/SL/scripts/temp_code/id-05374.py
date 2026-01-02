def analyze_trend(data, threshold):
    trend = 0
    fluctuations = []
    decoy_sum = 0
    for i in range(len(data)):
        if data[i] > threshold:
            trend += 1
            fluctuations.append(i)
        else:
            decoy_sum += data[i] * 2  # Irrelevant computation
    adjustment = len(fluctuations) // 2
    return trend - adjustment


def normalize_values(entries):
    total = sum(entries)
    normalized = [round(x / total * 100, 2) for x in entries]
    inverted = [100 - val for val in normalized]  # Distractor list
    return normalized


def filter_outliers(sequence, limit=50):
    filtered = [x for x in sequence if x < limit]
    discarded = [x for x in sequence if x >= limit]  # Dead path
    return filtered


def compute_stability(ratio, weight="medium"):
    if weight == "low":
        factor = 0.5
    elif weight == "high":
        factor = 1.2
    else:
        factor = 0.8
    stability = (ratio * 1.78 + 12) * factor
    temp_result = stability ** 0.5  # Misleading intermediate
    return int(stability)


def evaluate_performance(metrics, base):
    score = 0
    
    # Red herring: string processing unrelated to final result
    tag = "PERF-ANALYSIS"
    tag_lower = tag.lower()
    tag_parts = tag_lower.split('-')
    prefix = tag_parts[0].strip()  # Unused
    suffix = tag_parts[1].strip()  # Unused

    # Relevant logic begins
    primary_metric = metrics['throughput']
    secondary_metric = metrics['latency']
    
    throughput_adjusted = primary_metric // 100
    latency_normalized = 1000 // secondary_metric if secondary_metric > 0 else 0
    
    # Bit manipulation distraction
    xor_key = 0b1010
    masked_latency = latency_normalized ^ xor_key | 0b1100  # Partially used

    # Boolean logic with short-circuiting red herring
    is_optimal = (primary_metric > base['throughput']) and (secondary_metric < base['latency']) or False
    performance_ratio = throughput_adjusted / (secondary_metric + 1)
    
    # Call to irrelevant function
    dummy_data = [12, 45, 67, 89, 23]
    _ = normalize_values(dummy_data)
    
    # Core calculation chain
    base_score = analyze_trend([88, 92, 95, 87, 90], 90)
    bonus = compute_stability(performance_ratio, "medium")
    penalty = 0
    
    if masked_latency > 200:
        penalty = 10
    elif masked_latency > 150:
        penalty = 5
    
    score += base_score * 15
    score += bonus
    score -= penalty
    
    # Final adjustment using integer division
    final_score = score // 1  # Critical statement
    
    # Dead-end conditional
    if len(tag_parts) > 3:
        final_score += 100  # Never reached
    
    return final_score

# Main execution
metrics = {
    'throughput': 850,
    'latency': 14
}
baseline = {
    'throughput': 800,
    'latency': 15
}

result_cache = []
for _ in range(1):  # Simulated single run
    final_score = evaluate_performance(metrics, baseline)

print(f"Target result: {final_score}")