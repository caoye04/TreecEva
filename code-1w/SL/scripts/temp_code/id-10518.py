def analyze_productivity(logs):
    total_entries = len(logs)
    valid_entries = [entry for entry in logs if 'status' in entry and entry['status'] == 'completed']
    completion_rate = len(valid_entries) / total_entries if total_entries > 0 else 0
    
    # Irrelevant computation: average character count in descriptions
    desc_lengths = [len(entry.get('description', '')) for entry in logs]
    avg_desc_length = sum(desc_lengths) / len(desc_lengths) if desc_lengths else 0
    
    # Distraction: unused transformation
    lambda_transform = lambda x: x ** 2 + 1
    transformed_rates = [lambda_transform(completion_rate * 100)]

    return completion_rate


def calculate_efficiency(data):
    if not data:
        return 0
    
    # Extract hours and tasks
    hours_worked = [record['hours'] for record in data]
    tasks_completed = [record['tasks'] for record in data]
    
    efficiency_scores = []
    for i in range(len(data)):
        score = tasks_completed[i] / hours_worked[i] if hours_worked[i] > 0 else 0
        efficiency_scores.append(round(score, 3))
    
    # Dead code path: never used later
    outlier_detection = [s for s in efficiency_scores if s > 2.0]
    
    return sum(efficiency_scores) / len(efficiency_scores) if efficiency_scores else 0


def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    max_possible = sum(weights)
    
    for key in metrics:
        if key in weights:
            weighted_sum += metrics[key] * weights[key]
    
    normalized = (weighted_sum / max_possible) * 100 if max_possible > 0 else 0
    return int(round(normalized))

# Main execution
log_data = [
    {'status': 'completed', 'description': 'Fixed bug in auth module'},
    {'status': 'pending', 'description': 'Update documentation'},
    {'status': 'completed', 'description': 'Optimized database query'},
    {'status': 'completed', 'description': 'Implemented user settings'}
]

work_data = [
    {'hours': 4, 'tasks': 3},
    {'hours': 6, 'tasks': 7},
    {'hours': 5, 'tasks': 5}
]

# Compute intermediate metrics
productivity_rate = analyze_productivity(log_data)  # ~0.75
raw_efficiency = calculate_efficiency(work_data)   # ~1.233

# Build metric dictionary
metrics = {
    'completion': productivity_rate * 100,  # 75.0
    'efficiency': raw_efficiency * 10,
    'response_time': 85.0  # placeholder
}

# Weights for scoring
weights = {
    'completion': 0.4,
    'efficiency': 0.5,
    'response_time': 0.1
}

# Key statement
final_score = evaluate_performance(metrics, weights)

# Print result
print(f"Result: {final_score}")