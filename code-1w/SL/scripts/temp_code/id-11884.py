from collections import defaultdict, Counter

# Simulated sensor data processing with noise filtering and scoring
def process_sensor_data(raw_readings):
    filtered_data = [x for x in raw_readings if 10 <= x <= 100]
    
    # Misleading intermediate computations (distractors)
    avg_noise = sum(x for x in raw_readings if x < 10 or x > 100) / max(1, len([x for x in raw_readings if x < 10 or x > 100]))
    peak_spikes = [x for x in raw_readings if x > 95]
    spike_count = len(peak_spikes)
    
    stats = defaultdict(int)
    for val in filtered_data:
        if val >= 90:
            stats['excellent'] += 1
        elif val >= 75:
            stats['good'] += 1
        elif val >= 60:
            stats['acceptable'] += 1
        else:
            stats['poor'] += 1
    
    return filtered_data, stats

# Data transformation with slicing and weighting
def transform_data(sequence, window_size=3):
    transformed = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        weighted_val = (window[0] * 0.2) + (window[1] * 0.3) + (window[2] * 0.5)
        transformed.append(round(weighted_val))
    
    # Dead code path - never used (interference)
    if len(transformed) > 100:
        backup = [x * 0.9 for x in transformed]
        
    return transformed

# Core evaluation logic
def evaluate_performance(metrics, importance_weights):
    base_score = 0
    weight_sum = 0
    
    # Boolean and arithmetic mix
    for category, count in metrics.items():
        weight = importance_weights.get(category, 0.1)
        if weight > 0.2:
            contribution = count * weight * 10
            if count >= 3:
                contribution *= 1.2  # bonus for consistency
            base_score += contribution
            weight_sum += weight
    
    # Normalization step
    final = base_score / (weight_sum if weight_sum != 0 else 1)
    
    # Extra irrelevant calculation (distractor)
    outlier_ratio = len([x for x in metrics.values() if x < 2]) / len(metrics)
    
    return int(final)

# Main execution flow
if __name__ == "__main__":
    # Simulated input data
    raw_input = [15, 88, 92, 76, 81, 94, 67, 105, 89, 73, 12, 91, 79, 85, 96, 54, 200, 82]
    
    # Step 1: Filter and analyze
    cleaned_data, performance_stats = process_sensor_data(raw_input)
    
    # Step 2: Transform using sliding window
    processed_signal = transform_data(cleaned_data)
    
    # Step 3: Extract key slice for evaluation
    data_slice = processed_signal[5:12]  # Critical slice for scoring
    
    # Irrelevant string manipulation (distractor)
    status_tag = "ANALYSIS_" + "VALID" if sum(data_slice) > 500 else "INVALID"
    log_entry = f"Run: {status_tag.lower()}|len={len(data_slice)}"
    
    # Weight configuration (only some are actually used)
    weights = {
        'excellent': 0.5,
        'good': 0.35,
        'acceptable': 0.2,
        'poor': 0.1,
        'unknown': 0.05  # unused
    }
    
    # Bitwise flag check (semi-relevant, adds complexity)
    config_flag = 0b1101
    use_bonus = (config_flag & 0b0100) != 0  # checks third bit
    
    # Final computation
    final_score = evaluate_performance(performance_stats, weights)
    
    # Output result as required
    print(f"Result: {final_score}")