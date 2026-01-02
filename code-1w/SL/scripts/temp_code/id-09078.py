def analyze_trend(data_sequence):
    trend_signal = 0
    for i, value in enumerate(data_sequence):
        if i > 0 and value > data_sequence[i - 1]:
            trend_signal += (value - data_sequence[i - 1]) * (i % 3)
    return trend_signal


def compute_entropy(values):
    """Unrelated distractor function simulating complexity."""
    import math
    total = sum(values)
    entropy = 0.0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * math.log(prob)
    return round(entropy, 4)


def evaluate_performance(weights, outcomes):
    base = 0
    adjustment = 0
    
    # Simulate multi-factor assessment with distractors
    temp_offsets = [0] * len(outcomes)
    for idx, (w, o) in enumerate(zip(weights, outcomes)):
        temp_offsets[idx] = w * o + (idx % 2)  # Minor offset

    # Real logic starts here
    cumulative = 0
    for i in range(len(outcomes)):
        bit_flag = (temp_offsets[i] > 5) << 1
        mod_factor = (i + 1) % 4 or 1
        cumulative += int(temp_offsets[i] // mod_factor)
        
        # Distractor: irrelevant tracking
        if i % 2 == 0:
            adjustment += (cumulative ^ i) & 3  # XOR and bitwise AND, not used later
    
    # Core decision point
    if cumulative > 30:
        base = 88
    else:
        base = 44
    
    # Secondary correction using modular consistency
    consistency_check = 0
    for i in range(len(weights)):
        consistency_check += (weights[i] + outcomes[i]) % 3
    
    if consistency_check % 2 == 1:
        base -= 13
    else:
        base += 7
    
    # Final score computation
    final_score = base + (cumulative % 19)
    
    # Dead code branch — misleading control flow
    if False:
        final_score *= 2
        final_score -= 999
    
    return final_score

# Main execution
metric_weights = [2, 3, 1, 4]
raw_outcomes = [5, 4, 6, 3]

# Unused but plausible-looking analysis
entropy_value = compute_entropy(raw_outcomes)  # Computed but not used
signal_trend = analyze_trend(raw_outcomes)     # Another red herring

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

print(f"Result: {final_score}")