def analyze_metrics(data, threshold=50):
    # Irrelevant preprocessing: counts digits (not used in final result)
    digit_count = 0
    temp_value = threshold
    while temp_value:
        digit_count += 1
        temp_value //= 10

    # Relevant transformation: map each value above threshold to its square root, others to zero
    processed = [round(v ** 0.5, 2) if v > threshold else 0 for v in data]

    # Distractor: unused statistical calculation
    mean_val = sum(data) / len(data) if data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0

    return processed


# Simulate performance assessments across modules
assessments = [45, 67, 89, 34, 78, 91, 50, 46]

# Apply non-linear correction using lambda for dynamic filtering
filter_correction = lambda x: x * 1.2 if x < 70 else x * 0.95
adjusted_scores = [filter_correction(score) for score in assessments]

# Secondary irrelevant transformation
noisy_adjustments = []
for s in adjusted_scores:
    if s % 2 == 0:
        noisy_adjustments.append(s + 3.1)
    else:
        noisy_adjustments.append(s - 1.7)

# Core logic: scale based on cohort performance
baseline = sum(assessments) / len(assessments)
scaling_factor = 1.5 if baseline >= 60 else 1.2

# Aggregation function with embedded logic
def aggregate_performance(metrics, scale):
    # Step 1: boost all metrics by scale
    boosted = [m * scale for m in metrics]
    
    # Step 2: apply tiered bonus (only for values above 75 after boost)
    extended_bonus = 0
    for val in boosted:
        if val > 75:
            extended_bonus += val * 0.05  # small incremental bonus

    # Step 3: compute base total and add bonus
    raw_total = sum(boosted)
    final_total = raw_total + extended_bonus
    
    # Step 4: apply modular reduction for normalization
    normalized = final_total % 9997
    
    # Step 5: floor to nearest integer
    final_score = int(normalized)
    
    # Distractor: extra floating point operation (dead code)
    precision_artifact = normalized - final_score
    adjustment_log = []
    if precision_artifact > 0.5:
        adjustment_log.append('High fractional')
    else:
        adjustment_log.append('Low fractional')
    
    return final_score

# Execute main computation
processed_data = analyze_metrics(assessments, threshold=40)
final_score = aggregate_performance(assessments, scaling_factor)
print(f"Result: {final_score}")