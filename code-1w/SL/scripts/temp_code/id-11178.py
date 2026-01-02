def analyze_telemetry(data, mode):
    baseline = sum(data) / len(data)
    variance = sum((x - baseline) ** 2 for x in data) / len(data)
    normalized = [x / baseline for x in data]

    # Distractor: irrelevant transformation
    inverted = [1 / (1 + x) for x in data if x != 0]
    temp_sum = sum(inverted[:3]) if len(inverted) >= 3 else 0

    adjusted_metrics = []
    for val in normalized:
        if val > 1.1:
            adjusted_metrics.append(val * 0.9)
        elif val < 0.9:
            adjusted_metrics.append(val * 1.1)
        else:
            adjusted_metrics.append(val)

    # Distractor: dead computation path
    outlier_count = 0
    if mode == 'strict':
        outlier_count = sum(1 for x in data if abs(x - baseline) > 2 * variance ** 0.5)

    return adjusted_metrics


def compute_weighting(size):
    weights = [0] * size
    for i in range(size):
        weights[i] = (i + 1) / size
    scaling_factor = sum(weights)
    return [w / scaling_factor for w in weights]


def process_performance(raw_metrics, limit):
    processed = [x for x in raw_metrics if x <= limit]
    
    # Semi-relevant: modifies flow but not final answer directly
    if len(processed) == 0:
        return -1
    
    # Key logic step 1: apply decay
    decayed = [processed[i] * (0.95 ** i) for i in range(len(processed))]
    
    # Distractor: unused helper calculation
    peak_index = 0
    peak_value = decayed[0]
    for i in range(1, len(decayed)):
        if decayed[i] > peak_value:
            peak_value = decayed[i]
            peak_index = i

    # Key logic step 2: aggregate with exponential smoothing
    alpha = 0.3
    smoothed = decayed[0]
    for i in range(1, len(decayed)):
        smoothed = alpha * decayed[i] + (1 - alpha) * smoothed
    
    # Key logic step 3: finalize score
    adjustment = 1.0
    if smoothed > 0.8:
        adjustment = 0.9
    elif smoothed < 0.4:
        adjustment = 1.1
    
    final_score = int(smoothed * adjustment * 100)
    
    # Irrelevant string manipulation (case conversion)
    status_code = 'PERF_' + ('HIGH' if final_score > 70 else 'LOW')
    status_code = status_code.lower()
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == '__main__':
    telemetry_data = [120, 135, 110, 150, 90, 140, 105]
    config_mode = 'normal'
    
    # Distractor: extra function call with unused result
    noise_levels = [abs(x - 100) for x in telemetry_data]
    avg_noise = sum(noise_levels) / len(noise_levels)
    
    metrics = analyze_telemetry(telemetry_data, config_mode)
    weights = compute_weighting(len(metrics))
    
    # Apply weighting (semi-relevant, but not affecting final_score directly)
    weighted_metrics = [metrics[i] * weights[i] for i in range(len(metrics))]
    
    threshold = 1.05
    final_score = process_performance(metrics, threshold)