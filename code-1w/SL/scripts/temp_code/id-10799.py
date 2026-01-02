from collections import defaultdict

# Simulate system metrics over time
def collect_metrics():
    raw_data = [45, 70, 58, 82, 63, 77, 91, 64, 55]
    processed = defaultdict(int)
    
    for i, val in enumerate(raw_data):
        if val > 60:
            processed['high'] += 1
        else:
            processed['low'] += 1
            
        # Irrelevant transformation
        temp_offset = (val * 2) % 17
        processed['offset_sum'] += temp_offset

    # Distractor computation
    avg_temp = sum(raw_data) / len(raw_data)
    variance_proxy = sum((x - avg_temp) ** 2 for x in raw_data) / len(raw_data)
    
    # Actual metrics used later
    processed['peak_count'] = sum(1 for x in raw_data if x > 80)
    processed['efficiency_ratio'] = (len(raw_data) - processed['low']) / len(raw_data)
    
    return dict(processed)

def analyze_trend(data_list):
    # Unused helper function (dead code path)
    trend = 'stable'
    if all(data_list[i] <= data_list[i+1] for i in range(len(data_list)-1)):
        trend = 'increasing'
    elif all(data_list[i] >= data_list[i+1] for i in range(len(data_list)-1)):
        trend = 'decreasing'
    return trend

def evaluate_performance(metrics, weights):
    base = metrics['efficiency_ratio'] * weights[0]
    bonus = metrics['peak_count'] * 0.5
    
    # Misleading adjustment based on unused metric
    noise_adjust = metrics.get('offset_sum', 0) * 0.01  # Has minimal impact
    
    score = base + bonus - noise_adjust
    
    # Additional irrelevant logic
    if metrics['high'] > metrics['low']:
        score *= 1.1
    else:
        score *= 0.9
    
    return int(score * 10)  # Scale and discretize

# Main execution
if __name__ == '__main__':
    # Collect performance metrics
    metrics = collect_metrics()
    
    # Weight configuration (only first weight matters)
    weights = [8.5, 3.2, 1.8]  # Last two are not used
    
    # Extraneous list comprehension
    squared_values = [x**2 for x in weights if x > 2]
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")