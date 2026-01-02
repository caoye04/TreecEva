def analyze_metrics(raw_values, config):
    # Irrelevant preprocessing (red herring)
    temp_buffer = [x ** 0.5 for x in raw_values if x > 10]
    normalized = [x / sum(raw_values) for x in raw_values]

    # Decoy transformation with no downstream effect
    decoy_map = {}
    for i, val in enumerate(normalized):
        decoy_map[f'item_{i}'] = round(val * 100, 2)

    # Real computation begins: filter and scale
    filtered = [x for x in raw_values if x % 2 == 1]  # Only odd values matter
    scaling_factor = len(raw_values) / (len(filtered) or 1)

    # Dictionary-based weight assignment (actual relevant logic)
    weights = {k: v + 1 for k, v in config.items()}
    weighted_sum = sum(weights.get(i, 1) * val for i, val in enumerate(filtered))

    return weighted_sum * scaling_factor


def calculate_baseline(ref_data):
    # Dead function: never called but looks important
    cumulative = 0
    for x in ref_data:
        if x < 0:
            cumulative -= x ** 2
        else:
            cumulative += x ** 3
    return cumulative

def validate_integrity(checksum, metadata):
    # Unused validation logic (distractor)
    if not metadata:
        return False
    keyscore = sum(len(k) for k in metadata.keys())
    return (checksum + keyscore) % 7 == 0

# Main execution flow
if __name__ == "__main__":
    # Input data with mixed relevance
    readings = [15, 22, 33, 44, 55, 66, 77]
    settings = {0: 2, 1: 1, 2: 3, 4: 2}  # Note missing key 3

    # Step 1: Process metrics through analysis
    metric_data = analyze_metrics(readings, settings)

    # Step 2: Apply transformation chain
    transformed = metric_data * 1.5
    transformed -= 10
    transformed = abs(transformed)  # Defensive adjustment

    # Step 3: Conditional override (never triggers - red herring)
    if transformed > 1000:
        transformed = 999
    elif transformed < 0:
        transformed = 0

    # Step 4: Bit manipulation for "stability check" (irrelevant)
    stability_flag = int(transformed) ^ 255
    flag_check = (stability_flag & 15) >> 2

    # Step 5: Real threshold logic
    base_threshold = 40
    adjustment = 0

    # Complex conditional scoring
    if metric_data > 50:
        adjustment += 5
    elif metric_data > 30:
        adjustment += 3
    else:
        adjustment += 1

    if len(readings) >= 5:
        adjustment *= 2

    # Final performance evaluation (key statement)
    final_score = evaluate_performance(metric_data, base_threshold)

    # Print result for extraction
    print(f"Target result: {final_score}")

# Critical function definition moved after main block (style distraction)
def evaluate_performance(data_point, threshold):
    # Core logic hidden in later-defined function
    deviation = abs(data_point - threshold)
    penalty = deviation // 5
    score = 100 - penalty

    # Dictionary-based bonus system (actual impact)
    bonuses = {0: 10, 1: 5, 2: 3, 3: 0}
    bonus_key = min(int(deviation % 4), 3)
    score += bonuses.get(bonus_key, 0)

    # Extra conditionals that don't trigger (misleading paths)
    if data_point == 0:
        score = 0
    elif data_point < 0:
        score -= 20

    return score
