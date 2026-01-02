from collections import defaultdict

def calculate_performance(base, metrics):
    adjustments = defaultdict(float)
    adjustments['gain'] = base * 0.1
    adjustments['decay'] = metrics['stability'] * 0.05
    
    if metrics['consistency'] > 0.7:
        adjustments['bonus'] = base * 0.08
    else:
        adjustments['penalty'] = -base * 0.06

    total_adjustment = sum(adjustments.values())
    return base + total_adjustment

# Simulate system performance evaluation
baseline = 850
metrics = {
    'stability': 0.82,
    'consistency': 0.75,
    'latency': 45  # Irrelevant metric (distractor)
}

final_score = calculate_performance(baseline, metrics)
print(f"Target result: {final_score}")