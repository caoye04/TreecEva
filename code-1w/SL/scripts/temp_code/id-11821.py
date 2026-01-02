from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 92, 64, 85, 90, 77, 88, 61, 95, 83]
    metrics = defaultdict(int)
    
    # Irrelevant aggregation
    temp_aggr = 0
    for val in raw_data:
        temp_aggr += val % 10
    
    # Relevant metric calculations
    total = sum(raw_data)
    count = len(raw_data)
    avg = total / count
    above_80 = len([x for x in raw_data if x > 80])
    peak = max(raw_data)
    
    # Populate metrics with useful and misleading keys
    metrics['average'] = avg
    metrics['high_performers'] = above_80
    metrics['peak_value'] = peak
    metrics['temp_noise'] = temp_aggr * 2  # unused distraction
    metrics['stdev_guess'] = (max(raw_data) - min(raw_data)) / 4
    
    return metrics

# Determine adaptive thresholds based on external factors
def compute_thresholds(security_mode=True):
    base_thresholds = {
        'min_avg': 75,
        'target_high': 3,
        'bonus_trigger': 90
    }
    
    # Complex but irrelevant computation
    dummy_calc = 0
    for i in range(1, 10):
        for j in range(1, 6):
            if i % j == 0:
                dummy_calc += j
    
    # Modify thresholds based on mode
    if security_mode:
        base_thresholds['min_avg'] += 5
        base_thresholds['adjustment_factor'] = 1.1
    else:
        base_thresholds['adjustment_factor'] = 0.9
    
    # Unused field - red herring
    base_thresholds['dummy_total'] = dummy_calc
    
    return base_thresholds

# Evaluate final performance score
def evaluate_performance(metrics, thresholds):
    score = 0
    
    # Core logic steps
    if metrics['average'] >= thresholds['min_avg']:
        score += 40
    
    if metrics['high_performers'] >= 4:
        score += 30
    
    bonus_awarded = False
    if metrics['peak_value'] >= thresholds['bonus_trigger']:
        bonus_awarded = True
        score *= thresholds['adjustment_factor']  # increases score
    
    # Distractor branch - never reached due to logic above
    fallback_value = 0
    if not bonus_awarded and metrics['stdev_guess'] < 5:
        fallback_value = 25
    
    # Final adjustment
    penalty = 0
    if metrics['temp_noise'] > 50:
        penalty = 5  # minor penalty
    
    score -= penalty
    rounded_score = round(score)
    
    # Key assignment: final answer determined here
    final_score = int(rounded_score)
    return final_score

# Main execution flow
data_metrics = collect_metrics()
security_thresholds = compute_thresholds(security_mode=True)
final_score = evaluate_performance(data_metrics, security_thresholds)

print(f"Result: {final_score}")