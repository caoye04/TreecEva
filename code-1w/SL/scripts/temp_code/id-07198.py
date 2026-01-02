from itertools import combinations

def analyze_trends(data, threshold):
    trend_count = 0
    volatility = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if abs(diff) > threshold:
            trend_count += 1
        volatility += abs(diff)
    adjusted_volatility = volatility / len(data) if data else 0
    return trend_count, adjusted_volatility

def calculate_efficiency(runs):
    total_ops = 0
    metadata_log = []
    for run in runs:
        ops = 0
        temp = run
        while temp > 1:
            if temp % 2 == 0:
                temp //= 2
            else:
                temp = 3 * temp + 1
            ops += 1
        total_ops += ops
        metadata_log.append(ops)
    efficiency = len(runs) / (total_ops + 1)
    return efficiency

def evaluate_performance(metrics, base):
    score = 0
    bonus_tracker = {}
    
    # Relevant logic: assess deviation from baseline
    deviations = {k: abs(metrics[k] - base[k]) for k in base}
    
    # Distractor: complex combination analysis not used in final score
    keys = list(deviations.keys())
    unused_combinations = []
    for r in range(2, min(4, len(keys)+1)):
        for combo in combinations(keys, r):
            unused_combinations.append(combo)
    
    # Irrelevant statistical tracking
    avg_dev = sum(deviations.values()) / len(deviations)
    high_dev = sum(1 for d in deviations.values() if d > avg_dev)
    
    # Actual scoring logic
    for k in deviations:
        if deviations[k] < 5:
            score += 10
        elif deviations[k] < 10:
            score += 5
        else:
            score -= 2
        
        # Bonus rule: specific condition on key length
        if len(k) % 2 == 0:
            bonus_tracker[k] = True
    
    # Final adjustment based on bonus conditions (only even-length keys contribute)
    extra = sum(1 for bk in bonus_tracker if metrics.get(bk, 0) > 0)
    score += extra * 3
    
    return score

# Main execution
if __name__ == "__main__":
    # Simulated system metrics
    system_metrics = {
        'latency': 8,
        'throughput': 12,
        'reliability': 6,
        'bandwidth': 15,
        'scalability': 9
    }
    
    baseline_profile = {
        'latency': 5,
        'throughput': 10,
        'reliability': 5,
        'bandwidth': 10,
        'scalability': 7
    }
    
    # Dummy data for other functions (not affecting final_score)
    time_series_data = [100, 103, 98, 110, 108, 101, 95]
    performance_runs = [7, 5, 9]
    
    # Unused but plausible computation
    trends, vol = analyze_trends(time_series_data, threshold=4)
    eff = calculate_efficiency(performance_runs)
    
    # Key statement
    final_score = evaluate_performance(system_metrics, baseline_profile)
    
    print(f"Result: {final_score}")