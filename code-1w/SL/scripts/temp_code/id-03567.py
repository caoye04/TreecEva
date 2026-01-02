from collections import defaultdict

# Simulate sensor data aggregation and filtering for performance benchmarking
def collect_metrics(raw_samples):
    aggregated = defaultdict(int)
    noise_floor = 0.05
    sample_count = len(raw_samples)
    
    for idx, value in enumerate(raw_samples):
        if abs(value) < noise_floor:
            continue
        bucket = idx % 4
        aggregated[bucket] += int(abs(value * 100))
    
    return dict(aggregated)

# Transform raw counts into normalized tiers
def categorize_tiers(counts):
    total = sum(counts.values())
    if total == 0:
        return {i: 0 for i in range(4)}
    
    tiers = {}
    for k, v in counts.items():
        normalized = (v / total) * 100
        if normalized > 50:
            tiers[k] = 3
        elif normalized > 25:
            tiers[k] = 2
        else:
            tiers[k] = 1
    return tiers

# Apply weighting based on tier stability across slices
def assess_stability(tier_dict, history_log):
    stability_scores = []
    base_weights = [1.0, 1.2, 1.5]
    
    for _, tier in tier_dict.items():
        weight = base_weights[tier - 1] if tier > 0 else 1.0
        stability_scores.append(weight)
    
    # Irrelevant dead computation - adds distraction
    cumulative_drift = 0.0
    for i in range(len(history_log) - 1):
        cumulative_drift += abs(history_log[i+1] - history_log[i])
    
    avg_stability = sum(stability_scores) / len(stability_scores) if stability_scores else 1.0
    return avg_stability

# Main ranking computation combining multiple metrics
def compute_ranking(data_sequence):
    # Step 1: Filter and aggregate raw signal data
    processed_counts = collect_metrics(data_sequence)
    
    # Step 2: Categorize into performance tiers
    classified_tiers = categorize_tiers(processed_counts)
    
    # Step 3: Evaluate temporal stability (uses irrelevant history below)
    fake_history = [0.88, 0.91, 0.85, 0.87, 0.90]  # Not actually connected to current data
    stability_factor = assess_stability(classified_tiers, fake_history)
    
    # Step 4: Calculate base composite from tier distribution
    tier_sum = sum(classified_tiers.values())
    count_sum = sum(processed_counts.values())
    
    # Step 5: Apply bitwise adjustment based on pattern parity
    adjustment_key = len(processed_counts) ^ count_sum
    if adjustment_key & 1:
        adjustment_key = adjustment_key >> 1
    
    # Step 6: Final score with weighted combination
    raw_score = tier_sum * stability_factor * 10
    final_adjustment = (raw_score + adjustment_key) // 3
    
    # Dead code - misleading but syntactically present
    debug_snapshot = {
        'raw': data_sequence[:5],
        'counts_slice': {k: v for k, v in processed_counts.items() if k < 2},
        'temporal_gap': max(fake_history) - min(fake_history)
    }
    
    final_score = int(final_adjustment + 7)  # Key assignment point
    return final_score

# Input data: simulated precision readings from calibration sequence
data_stream = [
    0.12, -0.03, 0.45, 0.23, 0.01, -0.67, 0.34, -0.02,
    0.55, 0.11, -0.08, 0.76, 0.04, 0.89, -0.15, 0.22
]

# Execute main logic
benchmark_data = data_stream[::2]  # Use every other reading for evaluation
final_score = compute_ranking(benchmark_data)
print(f"Result: {final_score}")