import itertools

# Simulated sensor data processing for environmental monitoring station
def collect_readings():
    return [23.4, 25.1, 22.8, 24.6, 26.3, 21.9, 25.7]

def smooth_data(data):
    # Moving average smoothing (window size 3)
    smoothed = []
    for i in range(1, len(data) - 1):
        smoothed.append(round((data[i-1] + data[i] + data[i+1]) / 3, 2))
    return smoothed

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def normalize readings(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def extract_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks

def evaluate_stability(variance, threshold=1.5):
    return 1 if variance < threshold else 0

def compute_trend(data):
    # Linear trend approximation
    n = len(data)
    if n < 2:
        return 0.0
    slope = (data[-1] - data[0]) / (n - 1) if n > 1 else 0.0
    return round(slope, 3)

def filter_outliers(data, z_threshold=1.5):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    if std_dev == 0:
        return data
    return [x for x in data if abs(x - mean) / std_dev <= z_threshold]

def generate_pairs(data):
    # Irrelevant function - dead code path
    return list(itertools.combinations(data, 2))

def calculate_entropy(data):
    # Another irrelevant metric - red herring
    from math import log2
    freqs = {}
    for x in data:
        freqs[x] = freqs.get(x, 0) + 1
    total = len(data)
    return -sum((count/total) * log2(count/total) for count in freqs.values())

def assess_consistency(readings):
    # Returns consistency score based on consecutive similar values
    count = 0
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) < 0.5:
            count += 1
    return count / (len(readings) - 1) if len(readings) > 1 else 1.0

def aggregate_performance(metrics, weights):
    # Only some metrics are actually used
    score = 0.0
    # Relevant components:
    score += metrics['stability'] * weights['stability']           # weight: 0.4
    score += metrics['trend_reliability'] * weights['reliability'] # weight: 0.3
    score += metrics['consistency'] * weights['consistency']       # weight: 0.3
    # Irrelevant components in metrics dict are ignored (distractors)
    return round(score, 4)

def main():
    raw_data = collect_readings()  # Initial sensor values
    
    # Step 1: Smooth the data
    processed_data = smooth_data(raw_data)
    
    # Step 2: Normalize for comparison
    normalized = normalize_readings(processed_data)
    
    # Step 3: Filter outliers (though not used later - distraction)
    clean_data = filter_outliers(normalized)
    
    # Step 4: Extract peaks (not used in final score - misleading)
    peak_values = extract_peaks(processed_data)
    
    # Step 5: Calculate variance for stability assessment
    variance = calculate_variance(processed_data)
    stability_flag = evaluate_stability(variance)
    
    # Step 6: Compute trend
    trend_slope = compute_trend(processed_data)
    trend_abs = abs(trend_slope)
    trend_reliability = 1 - min(trend_abs, 1.0)  # Inverse relationship
    
    # Step 7: Assess consistency
    consistency_score = assess_consistency(processed_data)
    
    # Step 8: Generate unused entropy (red herring)
    entropy = calculate_entropy([int(x*100) for x in processed_data])  # Discretize for entropy
    
    # Step 9: Create irrelevant combinations (dead code)
    pairs = generate_pairs(raw_data)
    pair_count = len(pairs)
    
    # Step 10: Prepare metrics dictionary with several decoys
    metrics = {
        'stability': stability_flag,
        'variance': variance,  # distractor
        'trend': trend_slope,
        'trend_reliability': trend_reliability,
        'peak_count': len(peak_values),  # distractor
        'entropy': entropy,  # distractor
        'consistency': consistency_score,
        'raw_count': len(raw_data),  # distractor
        'pair_count': pair_count   # distractor
    }
    
    # Step 11: Define weighting scheme
    weights = {
        'stability': 0.4,
        'reliability': 0.3,  # matches trend_reliability
        'consistency': 0.3
        # Other keys missing intentionally to ignore other metrics
    }
    
    # Step 12: Aggregate final performance score
    final_score = aggregate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")

if __name__ == "__main__":
    main()