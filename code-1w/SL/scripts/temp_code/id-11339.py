from collections import defaultdict, Counter
import math

# Simulated sensor fusion system with noise filtering and scoring
raw_readings = [3.2, 4.1, 2.8, 5.6, 3.9, 4.4, 2.1, 6.7, 3.3, 4.0]

def apply_noise_filter(data):
    # Irrelevant smoothing function (dead path)
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

def generate_frequency_map(data):
    # Distractor: computes frequency but not used in final logic
    freq_map = defaultdict(int)
    for val in data:
        freq_map[round(val)] += 1
    return dict(freq_map)

def extract_outliers(data, threshold=4.0):
    # Misleading outlier detection (not actually used in scoring)
    outliers = [x for x in data if x > threshold]
    temp_result = sum([x**2 for x in outliers]) / len(outliers) if outliers else 0.0
    normalized_peak = math.log(temp_result + 1) if temp_result > 0 else 0.0
    return outliers, normalized_peak

def calculate_entropy(data):
    # Red herring: computes information-theoretic entropy
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def rescale_to_zscore(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return [0 for _ in data]
    return [(x - mean) / std_dev for x in data]

def apply_sigmoid_transform(data):
    # Distractor transformation
    return [1 / (1 + math.exp(-x)) for x in data]

def compute_aggregate(values, limits):
    # Core logic hidden among distractions
    truncated = values[:8]  # Only first 8 values matter
    above_threshold = [v for v in truncated if v > limits['upper']]
    below_floor = [v for v in truncated if v < limits['lower']]
    mid_zone = [v for v in truncated if limits['lower'] <= v <= limits['upper']]
    
    # Real computation path
    primary_sum = sum(mid_zone)
    penalty = len(below_floor) * 1.5
    bonus = len(above_threshold) * 2.0
    adjustment = abs(primary_sum - 10.0) * 0.1
    
    # Dead computations (misleading intermediate values)
    dummy_agg = (sum(above_threshold) if above_threshold else 0) + (sum(below_floor) if below_floor else 0)
    dummy_ratio = dummy_agg / (primary_sum + 1e-8)
    
    result = primary_sum + bonus - penalty - adjustment
    return round(result, 4)

def main():
    # Irrelevant preprocessing steps
    filtered_data = apply_noise_filter(raw_readings)
    freq_analysis = generate_frequency_map(filtered_data)
    outliers, peak_metric = extract_outliers(raw_readings, threshold=5.0)
    signal_entropy = calculate_entropy([int(x) for x in raw_readings])
    
    # Real preprocessing path
    z_scores = rescale_to_zscore(raw_readings)
    sigmoid_mapped = apply_sigmoid_transform(z_scores)
    
    # Key slicing operation (python feature)
    working_slice = sigmoid_mapped[1:9:1]  # Take elements 1 through 8
    
    # Define thresholds (only this part matters)
    config_thresholds = {
        'upper': 0.65,
        'lower': 0.35
    }
    
    # Critical assignment
    scaled_values = working_slice
    
    # This is the key statement
    final_score = compute_aggregate(scaled_values, config_thresholds)
    
    # Print required output
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()