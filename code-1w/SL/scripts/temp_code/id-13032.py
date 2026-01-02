def calculate_performance(results):
    base_score = results['accuracy'] * 100
    penalty = 0
    if results['latency'] > 50:
        penalty += (results['latency'] - 50) * 0.1
    if results['memory_usage'] > 80:
        penalty += (results['memory_usage'] - 80) * 0.2
    
    adjustment = 5 if results['stability'] else -10
    
    return base_score - penalty + adjustment

# Simulated benchmark data
test_data = {
    'accuracy': 0.92,
    'latency': 65,
    'memory_usage': 85,
    'stability': True
}

intermediate = test_data['accuracy'] * test_data['latency']
bonus = 3  # Irrelevant distractor variable
final_score = calculate_performance(test_data)
print(f"Result: {final_score}")