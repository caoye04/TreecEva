from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring with noise filtering
def preprocess_data(raw):
    processed = []
    noise_counter = 0
    for val in raw:
        if isinstance(val, str) and 'ERR' in val:
            noise_counter += 1
            continue
        if isinstance(val, (int, float)) and val >= 0:
            processed.append(float(val))
    return processed, noise_counter

def compute_moving_average(series, window=3):
    if len(series) < window:
        return [sum(series)/len(series)] if series else [0]
    averages = []
    for i in range(len(series) - window + 1):
        averages.append(sum(series[i:i+window]) / window)
    return averages

def calculate_outlier_penalty(values):
    if not values:
        return 0.0
    mean_val = sum(values) / len(values)
    squared_diffs = [(v - mean_val)**2 for v in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    return round(variance * 0.1, 4)

def calculate_final_score(raw_data, importance_weights):
    # Step 1: Clean and validate input
    cleaned, dropped = preprocess_data(raw_data)
    
    # Irrelevant distraction: string analysis on metadata
    metadata_summary = "sensor_readings_v2"
    char_freq = defaultdict(int)
    for c in metadata_summary:
        char_freq[c] += 1
    vowel_count = sum(char_freq[c] for c in 'aeiou')  # Unused metric
    
    # Step 2: Apply dynamic filtering based on length
    if len(cleaned) > 5:
        recent_segment = cleaned[-5:]
    else:
        recent_segment = cleaned[:]
    
    # Step 3: Compute temporal patterns
    moving_avgs = compute_moving_average(recent_segment, window=2)
    trend_adjustment = 0.0
    if len(moving_avgs) >= 2:
        trend = moving_avgs[-1] - moving_avgs[0]
        trend_adjustment = trend * 0.2
    
    # Step 4: Weighted contribution from different factors
    base_score = sum(x * w for x, w in zip(recent_segment, importance_weights[:len(recent_segment)]))
    
    # Step 5: Apply penalty for instability
    outlier_penalty = calculate_outlier_penalty(recent_segment)
    
    # Step 6: Conditional boost for consistency
    consistency_boost = 0.0
    if len(recent_segment) >= 3:
        deviations = [abs(recent_segment[i] - recent_segment[i-1]) for i in range(1, len(recent_segment))]
        avg_deviation = sum(deviations) / len(deviations)
        if avg_deviation < 2.0:
            consistency_boost = 8.5  # Reward stable readings
    
    # Step 7: Final computation chain
    intermediate_total = base_score + trend_adjustment + consistency_boost
    final_score = intermediate_total - outlier_penalty
    
    # Dead code path: simulation of alternate scoring (never used)
    if False:
        backup_score = sum(cleaned) * 0.9
        final_score = max(final_score, backup_score)
    
    return round(final_score, 4)

# Input data with mixed types and noise
data = [10.0, 12.5, "ERR_NA", 11.0, 13.2, 12.8, "ERR_TIMEOUT", 14.1, 13.9]
weights = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7, 1.0, 0.6, 1.3]

# Execute main logic
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")