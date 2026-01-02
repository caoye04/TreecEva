import itertools

# Simulated sensor data processing with performance evaluation
def collect_diagnostics():
    return [0.85, 0.92, 0.78, 0.96, 0.88]

def normalize_readings(readings):
    max_val = max(readings)
    return [round(x / max_val, 4) for x in readings]

def compute_reliability_index(readings):
    # Irrelevant computation: used as distraction
    cumulative = 0
    for val in readings:
        if val > 0.9:
            cumulative += val * 1.2
        else:
            cumulative += val * 0.8
    return round(cumulative, 4)

def generate_combinations(data):
    # Distractor function: creates unused combinations
    combos = list(itertools.combinations(data, 3))
    return len(combos)  # Unused result

def filter_outliers(values, threshold=0.75):
    # Another distractor: this modifies a copy, not original
    filtered = [v for v in values if v >= threshold]
    return filtered

def calculate_baseline_deviation(metrics):
    mean = sum(metrics) / len(metrics)
    variance = sum((x - mean) ** 2 for x in metrics) / len(metrics)
    return round(variance ** 0.5, 4)

def adjust_for_bias(metrics, factor=0.95):
    # This function is called but its result is not directly used
    return [round(m * factor, 4) for m in metrics]

def evaluate_integrity_score(seq):
    # Decoy scoring logic that looks important but isn't final
    score = 0
    for i in range(1, len(seq)):
        if seq[i] >= seq[i-1]:
            score += 1
    return score * 10

def detect_anomalies(patterns):
    # Dead code path: never actually used
    anomalies = []
    for p in patterns:
        if p < 0.8:
            anomalies.append(True)
    return len(anomalies)

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    total_weight = sum(weights)
    
    # Core logic: dot product of normalized metrics and weights
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    
    # Final score is normalized by total weight
    final = weighted_sum / total_weight
    
    # Secondary adjustment based on trend (increasing or decreasing)
    increasing_trend = 0
    for j in range(1, len(metrics)):
        if metrics[j] > metrics[j-1]:
            increasing_trend += 1
    
    trend_bonus = (increasing_trend / (len(metrics) - 1)) * 0.05 if len(metrics) > 1 else 0
    final += trend_bonus
    
    return round(final, 6)

# Main execution block
if __name__ == "__main__":
    # Step 1: Collect raw diagnostics
    raw_metrics = collect_diagnostics()
    
    # Step 2: Normalize readings (this modifies the data meaningfully)
    processed_metrics = normalize_readings(raw_metrics)
    
    # Step 3: Compute various irrelevant metrics (distractions)
    reliability = compute_reliability_index(processed_metrics)
    combo_count = generate_combinations(processed_metrics)
    deviation = calculate_baseline_deviation(processed_metrics)
    adjusted_metrics = adjust_for_bias(processed_metrics)  # Computed but not used
    integrity = evaluate_integrity_score(processed_metrics)
    anomalies_detected = detect_anomalies(processed_metrics)
    
    # Step 4: Filter outliers — result ignored to mislead
    clean_data = filter_outliers(processed_metrics, threshold=0.82)
    
    # Step 5: Define weighting scheme for final evaluation
    weights = [0.1, 0.2, 0.15, 0.25, 0.3]
    
    # Step 6: Evaluate final performance score — THIS IS THE KEY STATEMENT
    final_score = evaluate_performance(processed_metrics, weights)
    
    # Print result
    print(f"Result: {final_score}")