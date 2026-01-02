def calculate_performance(metrics):
    base = metrics['accuracy'] * 100
    penalty = (lambda x: x ** 2 if x > 0.1 else 0)(metrics['error_rate'])
    bonus = 10 if metrics['converged'] else 0
    return base - (penalty * 10) + bonus

# Irrelevant auxiliary data (minor distraction)
data_log = [('epoch', 5), ('batch', 32)]
temp_result = [x for x, _ in data_log]

# Main data input
data_map = {
    'accuracy': 0.92,
    'error_rate': 0.15,
    'converged': True,
    'timestamp': 1712345678
}

# Key computation step
final_score = calculate_performance(data_map)

print(f"Result: {final_score}")