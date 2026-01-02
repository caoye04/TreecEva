def calculate_performance(base, metrics_dict):
    adjustment = 0
    if metrics_dict['accuracy'] > 0.8:
        adjustment += base * 0.2
    if metrics_dict['stability'] < 50:
        adjustment -= base * 0.1
    
    # Irrelevant utility calculation (minor distraction)
    peak_utilization = max(metrics_dict['load_history'])
    avg_load = sum(metrics_dict['load_history']) / len(metrics_dict['load_history'])
    
    return int(base + adjustment)

# Main execution
baseline = 100
config = {'version': '2.1', 'mode': 'production'}
metrics = {
    'accuracy': 0.85,
    'stability': 45,
    'load_history': [20, 35, 40, 55, 48]
}

# Key computation
final_score = calculate_performance(baseline, metrics)

Result: final_score