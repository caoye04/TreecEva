from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring with noise filtering
def preprocess_data(raw_data):
    filtered = []
    noise_count = 0
    for val in raw_data:
        if abs(val - 50) > 40:  # Assume values too far from baseline are noise
            noise_count += 1
            continue
        if val % 2 == 0:
            filtered.append(val + 1)  # Slight correction for even values
        else:
            filtered.append(val)
    return filtered, noise_count

def compute_baseline_stats(values):
    stats = defaultdict(int)
    total = 0
    for v in values:
        total += v
        if v > 60:
            stats['high'] += 1
        elif v > 40:
            stats['medium'] += 1
        else:
            stats['low'] += 1
    stats['average'] = total / len(values) if values else 0
    return stats

def apply_weighting(values, weights):
    # weights: list of multiplicative factors, cyclically applied
    weighted = []
    for i, v in enumerate(values):
        factor = weights[i % len(weights)]
        adjusted = v * factor
        weighted.append(adjusted)
    return weighted

def calculate_final_score(data, weights):
    # Step 1: Preprocess to remove noise
    clean_data, dropped = preprocess_data(data)
    
    # Step 2: Compute statistical profile (some values used later)
    profile = compute_baseline_stats(clean_data)
    
    # Step 3: Apply dynamic weighting
    weighted_values = apply_weighting(clean_data, weights)
    
    # Step 4: Compute moving average to smooth
    smoothed = []
    window_size = 3
    for i in range(len(weighted_values)):
        start = max(0, i - window_size + 1)
        segment = weighted_values[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    
    # Step 5: Threshold filtering on smoothed data
    thresholded = [x for x in smoothed if x >= 45.0]
    
    # Step 6: Aggregate final score with penalty for low variance
    if not thresholded:
        base_score = 0
    else:
        base_score = sum(thresholded)
        variance = sum((x - base_score/len(thresholded))**2 for x in thresholded) / len(thresholded)
        penalty = 0
        if variance < 25.0:
            penalty = 15  # Low variance indicates untrustworthy consistency
        base_score -= penalty
    
    # Irrelevant tracking variables (distractors)
    debug_info = {'processed_count': len(clean_data), 'penalty_applied': 'variance' if variance < 25.0 else 'none'}
    temp_snapshot = [int(x) for x in thresholded[::2]]  # Unused summary
    
    # Final adjustment based on original data length (red herring logic)
    legacy_factor = len(data) % 7
    final_score = int(base_score - legacy_factor)
    
    # Another misleading computation
    phantom_score = sum(clean_data) * 0.1
    
    return final_score

# Input data and weights
data = [48, 95, 52, 44, 67, 83, 39, 105, 55, 41, 71, 66, 59]
weights = [0.8, 1.2, 1.0, 0.9]

# Execute main logic
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")