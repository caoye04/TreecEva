def evaluate_performance(metrics, base):
    # Irrelevant transformation
    temp_data = [x * 1.05 for x in metrics if x > base]
    offset = sum(temp_data) / len(temp_data) if temp_data else 0
    
    # Distractor: complex but unused calculation
    shadow_metrics = list(map(lambda x: (x - base) ** 2 + 3, metrics))
    avg_shadow = sum(shadow_metrics) / len(shadow_metrics)
    derived_threshold = avg_shadow * 0.7

    # Core logic: count how many exceed baseline, then apply decay function
    valid_entries = [m for m in metrics if m >= base]
    excess_values = [m - base for m in valid_entries]
    
    # Real computation path
    raw_count = len(valid_entries)
    bonus_factor = 0
    if raw_count > 3:
        bonus_factor = 10
    elif raw_count == 3:
        bonus_factor = 5

    # Apply exponential decay based on position (simulating diminishing returns)
    decayed_sum = sum(excess_values[i] * (0.8 ** i) for i in range(len(excess_values)))

    # Secondary distractor: character counting in stringified data
    str_repr = ''.join([str(int(x)) for x in metrics])
    digit_count = len(str_repr)
    parity_penalty = digit_count % 7  # Unused but computed

    # Use of set to deduplicate redundant high performers
    unique_high = set(v for v in valid_entries if v > base * 1.2)
    excellence_bonus = len(unique_high) * 3

    # Final score influenced by decayed sum, count logic, and excellence
    final_score = decayed_sum + bonus_factor + excellence_bonus

    # Red herring: another variable that looks important
    normalized_score = (final_score + offset) / (1 + derived_threshold * 0.01)

    return final_score

# Input data
baseline = 50
metrics = [62, 68, 55, 70, 52, 80]

# Key execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")