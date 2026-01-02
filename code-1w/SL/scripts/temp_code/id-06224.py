def analyze_metrics(raw_values, thresholds):
    # Irrelevant transformation (dead path)
    temp_adjusted = [x * 1.05 for x in raw_values if x > 0]
    
    # Distractor: complex but unused filtering
    filtered_caps = list(filter(lambda x: x < max(thresholds), raw_values))
    capped_values = [min(x, 95) for x in raw_values]  # Not used later

    # Real computation begins: normalize using threshold clamping
    normalized = []
    for v in raw_values:
        if v < thresholds[0]:
            normalized.append(50)
        elif v > thresholds[1]:
            normalized.append(90)
        else:
            normalized.append(50 + (v - thresholds[0]) * (40 / (thresholds[1] - thresholds[0])))
    
    # Distractor: fake aggregation (never used)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    high_performers = [n for n in normalized if n >= 85]

    # Hidden relevant logic: count how many are above dynamic midpoint
    mid_threshold = (thresholds[0] + thresholds[1]) / 2
    performance_flags = [1 if x >= mid_threshold else 0 for x in raw_values]
    flag_sum = sum(performance_flags)

    # Return only what's needed for next step
    return normalized, flag_sum


def compute_entropy(data):
    # Unused function – red herring
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log(count/total) for count in freq.values())
    return round(entropy, 3)

def adjust_weights(fidelity, base_weights):
    # Another decoy transformation
    adjusted = [w * (1 + fidelity * 0.1) for w in base_weights]
    return adjusted[::-1]  # Reversed – not used

def integrate_feedback(scores, feedback_mask):
    # Misleading correction system
    corrected = []
    for s, m in zip(scores, feedback_mask):
        if m == 1:
            s = min(s * 1.1, 100)
        else:
            s = max(s * 0.95, 0)
    return corrected  # Never actually called

def evaluate_performance(weights, data):
    # Core calculation buried in noise
    base_score = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            base_score += val * weights[i % len(weights)]
        else:
            base_score += val * (weights[i % len(weights)] * 0.8)  # Weighted odd indices
    
    # Secondary adjustment based on pattern match
    pattern_match = all(data[j] <= data[j+1] for j in range(len(data)-1))
    bonus = 7 if pattern_match else 0
    
    # Final irrelevant smoothing
    smoothed = base_score * 0.98 + bonus
    final = int(round(smoothed + bonus))  # Double-count bonus? No — only one bonus added
    
    return final

# Main execution flow
if __name__ == '__main__':
    # Input data
    readings = [68, 72, 79, 83, 85, 88]
    limits = [60, 80]
    metric_weights = [0.2, 0.3, 0.1, 0.4]

    # Step 1: Normalize metrics
    normalized_data, flag_count = analyze_metrics(readings, limits)

    # Step 2: Compute useless entropy
    _ = compute_entropy(readings)  # Distractor call

    # Step 3: Adjust weights with unused result
    _ = adjust_weights(0.85, metric_weights)

    # Step 4: Evaluate final performance (this is where final_score is set)
    final_score = evaluate_performance(metric_weights, normalized_data)
    
    # Output target result
    print(f"Result: {final_score}")