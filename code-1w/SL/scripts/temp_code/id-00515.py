def analyze_user_behavior(data_stream, threshold):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in data_stream if x > 0]
    filtered = [x for x in normalized if x < 1000]
    stats = {'max_val': max(filtered), 'min_val': min(filtered)}
    
    # Misleading transformation chain
    transformed = []
    for val in filtered:
        if val > threshold * 1.2:
            transformed.append(val ** 0.5)
        elif val < threshold * 0.8:
            transformed.append(val * 0.1)
        else:
            transformed.append(val)  # Neutral zone

    # Dead code path (never executed due to logic)
    if len(transformed) > 10000:
        smoothed = [sum(transformed[i:i+5])/5 for i in range(0, len(transformed), 5)]
    else:
        smoothed = transformed[:]  # Copy, not smoothing

    return transformed


def compute_risk_factor(entries):
    # Complex but irrelevant risk calculation (red herring)
    base_risk = 0
    for e in entries:
        if e % 7 == 0:
            base_risk += 1
        if e > 500:
            base_risk += 0.5
    adjusted_risk = base_risk * 1.3
    
    # Decoy return path (not actually used in final logic)
    if adjusted_risk > 10:
        return adjusted_risk / 2
    return adjusted_risk

# Simulated log processing with slicing and distractors
def extract_critical_segments(full_log):
    segment_a = full_log[5:15]
    segment_b = full_log[20:30]
    combined = segment_a + segment_b
    
    # Real computation buried in noise
    mid_values = [x for x in combined if 100 <= x <= 400]
    high_impact = [x for x in combined if x > 400]
    
    # Actual relevant metric (obscured)
    signal_strength = sum(mid_values) / len(mid_values) if mid_values else 0
    
    # Distractor: unused aggregation
    noise_ratio = len(high_impact) / len(combined) if combined else 0
    
    return signal_strength

# Core logic hidden among decoys
def aggregate_performance(log_entries, user_threshold):
    # Real signal extraction
    primary_signal = extract_critical_segments(log_entries)
    
    # Irrelevant side computation (looks important)
    outlier_count = sum(1 for x in log_entries if x > user_threshold * 2)
    suppression_factor = 1.0
    if outlier_count > 5:
        suppression_factor = 0.9
    
    # Real logic: performance based on signal and threshold alignment
    aligned_points = [x for x in log_entries if abs(x - user_threshold) <= 50]
    alignment_score = len(aligned_points) * 10
    
    # Secondary metric from signal strength
    stability_bonus = int(primary_signal // 10)
    
    # Early termination red herring (never triggered in this input)
    if primary_signal < 0:
        return -999
    
    # Final score computation (key statement)
    final_score = alignment_score + stability_bonus
    
    # Unused alternate scoring method (decoy)
    if user_threshold > 300:
        alternative = sum(log_entries[:10]) // 5
        final_score = max(final_score, alternative)
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Simulated telemetry log (deterministic input)
    raw_telemetry = [
        85, 92, 101, 150, 160, 180, 200, 220, 240, 260,
        280, 300, 310, 320, 330, 120, 130, 140, 150, 160,
        410, 420, 430, 440, 450, 190, 210, 230, 250, 270
    ]
    
    # Irrelevant initialization (distraction)
    baseline_metrics = {'start': 100, 'end': 350, 'step': 10}
    temp_buffer = [x // 2 for x in raw_telemetry if x % 2 == 0]
    
    config_threshold = 200
    
    # Real function call
    behavior_profile = analyze_user_behavior(raw_telemetry, config_threshold)
    risk_level = compute_risk_factor(raw_telemetry)  # Computed but unused
    
    # Key statement
    final_score = aggregate_performance(raw_telemetry, config_threshold)
    
    print(f"Result: {final_score}")