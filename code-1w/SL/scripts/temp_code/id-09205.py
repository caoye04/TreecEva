import math

def preprocess_input(raw_series):
    # Normalize input by removing outliers (values beyond 3σ)
    mean_val = sum(raw_series) / len(raw_series)
    std_dev = (sum((x - mean_val) ** 2 for x in raw_series) / len(raw_series)) ** 0.5
    filtered = [x for x in raw_series if abs(x - mean_val) <= 3 * std_dev]
    
    # Distractor: unused transformation
    temp_log_scaled = [math.log(x + 1) for x in raw_series if x > 0]
    temp_squared_sum = sum(x**2 for x in raw_series)  # Dead computation

    return filtered

def evaluate_consistency(metrics):
    trend_consistent = True
    for i in range(1, len(metrics)):
        if metrics[i] < metrics[i-1]:
            trend_consistent = False
            break
    
    # Irrelevant string processing distraction
    status_label = "consistent" if trend_consistent else "inconsistent"
    status_label = status_label.upper()
    status_flag = len(status_label) > 0  # Always true

    return trend_consistent

def calculate_performance(data_log):
    cleaned_data = preprocess_input(data_log)
    
    # Compute moving average for noise reduction
    window_size = 3
    smoothed = []
    for i in range(len(cleaned_data)):
        start = max(0, i - window_size + 1)
        segment = cleaned_data[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    
    # Compute volatility (standard deviation of differences)
    diffs = [smoothed[i] - smoothed[i-1] for i in range(1, len(smoothed))]
    if len(diffs) == 0:
        volatility = 0.0
    else:
        mean_diff = sum(diffs) / len(diffs)
        variance = sum((d - mean_diff) ** 2 for d in diffs) / len(diffs)
        volatility = math.sqrt(variance)
    
    # Distractor: complex string encoding path that isn't used
    encoded_tag = "perf_" + "_".join([str(int(v*10)) for v in smoothed[:3]])
    encoded_tag = ''.join(chr(ord(c)+1) if c.isalpha() else c for c in encoded_tag)  # obfuscate

    base_score = sum(cleaned_data) / len(cleaned_data) if cleaned_data else 0
    consistency_bonus = 10 if evaluate_consistency(smoothed) else 0
    stability_penalty = 5 * min(int(volatility * 2), 10)
    
    # Final calculation
    final_score = base_score + consistency_bonus - stability_penalty
    
    # Additional red herring variables
    debug_snapshot = {"raw_len": len(data_log), "cleaned_len": len(cleaned_data), "volatility": volatility}
    auxiliary_metric = math.exp(-volatility) if volatility > 0 else 1.0
    
    return final_score

# Simulated benchmark data
benchmark_data = [85, 88, 92, 95, 93, 90, 87, 85, 84, 86]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")