from collections import defaultdict

def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

def compute_volatility(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance ** 0.5

def evaluate_performance(metrics):
    base_score = 0
    adjustment = 0
    volatility_penalty = 0
    
    # Irrelevant tracking (distractor)
    debug_log = defaultdict(int)
    debug_log['entries'] = len(metrics)
    
    for key, values in metrics.items():
        if key == 'latency':
            trend = analyze_trend(values)
            base_score += trend * 2
            adjustment += abs(trend)
        elif key == 'throughput':
            avg_throughput = sum(values) / len(values)
            base_score += min(avg_throughput // 10, 5)
            # Dead computation: not used later
            temp_fluctuation = compute_volatility(values)
            debug_log['high_flux'] = temp_fluctuation > 3
        elif key == 'errors':
            error_rate = sum(values) / sum([max(v, 1) for v in metrics.get('throughput', [1])])
            adjustment -= int(error_rate * 10)
            
    # Secondary path with early return (not taken but adds complexity)
    if base_score < 0:
        return -5
    
    # Real computation
    volatility = compute_volatility(metrics.get('latency', [0]))
    volatility_penalty = int(volatility * 2)
    
    # Key statement
    final_score = base_score + adjustment - volatility_penalty
    
    # Unused variables and misleading calculations
    normalized_score = final_score / (1 + abs(adjustment))
    debug_log['normalized'] = round(normalized_score, 2)
    
    return final_score

def main():
    metric_data = {
        'latency': [120, 110, 95, 90, 85, 88],
        'throughput': [45, 48, 52, 50, 53],
        'errors': [3, 2, 4, 1, 2]
    }
    
    # Distractor variables
    baseline_ref = [100, 50, 3]
    calibration_factor = sum(baseline_ref) / 10
    dummy_result = analyze_trend(baseline_ref)
    
    result = evaluate_performance(metric_data)
    print(f"Target result: {result}")

if __name__ == "__main__":
    main()