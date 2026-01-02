def calculate_performance(results):
    base_score = results['initial']
    bonus = 0
    if results['cycles'] > 3:
        bonus += results['efficiency'] * 2
    if results['stability'] and not results['overheating']:
        bonus += 15
    total = base_score + bonus
    penalty = max(0, 5 - results['cooling_factor']) * 3
    return total - penalty

# Benchmark configuration
test_config = {
    'initial': 78,
    'cycles': 4,
    'efficiency': 12,
    'stability': True,
    'overheating': False,
    'cooling_factor': 7,
    'timestamp': 1712345678,
    'version': '2.1.3'
}

# Irrelevant utility (minimal distraction)
def log_event(msg):
    pass

log_event("Starting performance evaluation")

# Key computation
final_score = calculate_performance(test_config)
print(f"Result: {final_score}")