from collections import defaultdict, Counter
import math

# Simulate sensor data processing for environmental monitoring system
def collect_readings():
    readings = [23.4, 24.1, 19.5, 25.0, 30.2, 27.8, 26.1, 24.3, 22.7]
    return readings

def calculate_baseline(readings):
    # Irrelevant computation: computes average but not used in final path
    total = sum(readings)
    count = len(readings)
    avg = total / count
    baseline = avg - 0.5  # Distractor adjustment
    return baseline

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered  # Used later, but with red herring logic around it

def compute_variability(signal):
    sorted_signal = sorted(signal)
    diff_sequence = [sorted_signal[i+1] - sorted_signal[i] for i in range(len(sorted_signal)-1)]
    variability = sum(d ** 2 for d in diff_sequence) / len(diff_sequence)
    return variability

def generate_diagnostic_report(raw, clean):
    report = defaultdict(int)
    report['raw_count'] = len(raw)
    report['clean_count'] = len(clean)
    report['data_loss'] = len(raw) - len(clean)
    report['status_code'] = 0x200  # HTTP 200 analog, irrelevant to result
    return report  # Dead-end function, distractor

def evaluate_stability(variance, tolerance=1.5):
    if variance < tolerance:
        return "stable"
    elif variance < tolerance * 2:
        return "caution"
    else:
        return "unstable"

def assess_complexity(sequence):
    entropy = 0.0
    freq = Counter(sequence)
    for k in freq:
        p = freq[k] / len(sequence)
        if p > 0:
            entropy -= p * math.log2(p)
    # This function is called but its return value is ignored
    return round(entropy, 3)

def normalize_scores(vals):
    min_val, max_val = min(vals), max(vals)
    if max_val == min_val:
        return [0.5] * len(vals)
    return [(v - min_val) / (max_val - min_val) for v in vals]

def aggregate_performance(metrix, weights):
    # Note: intentional typo in arg name to simulate noise
    adjusted = []
    for i, val in enumerate(metrix):
        if i < len(weights):
            adjusted.append(val * weights[i])
    raw_sum = sum(adjusted)
    penalty = 0.1 * len([x for x in metrix if x < 0.3])  # small correction
    final_score = raw_sum - penalty
    return int(round(final_score * 100))  # Scale up to integer

def main():
    # Step 1: Collect sensor readings
    raw_readings = collect_readings()
    
    # Step 2: Calculate baseline (irrelevant, never used)
    base_ref = calculate_baseline(raw_readings)
    
    # Step 3: Filter outliers
    cleaned = filter_outliers(raw_readings, threshold=1.8)
    
    # Step 4: Generate diagnostic report (distractor)
    report = generate_diagnostic_report(raw_readings, cleaned)
    
    # Step 5: Compute signal variability
    variation_metric = compute_variability(cleaned)
    
    # Step 6: Assess stability
    stability_status = evaluate_stability(variation_metric)
    
    # Step 7: Assess complexity (called but result ignored)
    _ = assess_complexity(cleaned)
    
    # Step 8: Normalize readings for scoring
    normalized_data = normalize_scores(cleaned)
    
    # Step 9: Extract specific metrics for performance
    metrics = [
        normalized_data[0],                    # first reading weight
        sum(normalized_data) / len(normalized_data),  # average
        1.0 - (variation_metric / 10.0),         # adjusted stability score
        len(normalized_data) / 10.0              # completion ratio
    ]
    
    # Step 10: Define weights (some are misleadingly named)
    weights = [0.4, 0.3, 0.2, 0.1]  # Standard weighting scheme
    
    # Step 11: Aggregate performance - KEY STATEMENT
    final_score = aggregate_performance(metrics, weights)
    
    # Step 12: Print result
    print(f"Result: {final_score}")
    return final_score

if __name__ == '__main__':
    main()