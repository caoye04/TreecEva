def analyze_metrics(data):
    total = sum(data)
    average = total / len(data) if data else 0
    deviation = sum((x - average) ** 2 for x in data)
    variance = deviation / len(data) if data else 0
    return average, variance

metrics = [0.78, 0.82, 0.88, 0.76, 0.91]

# Irrelevant transformation (distractor)
adjusted_metrics = [round(x * 1.05, 2) for x in metrics]
dropped_values = [x for x in adjusted_metrics if x < 0.80]

avg, var = analyze_metrics(metrics)

# Simulate feedback levels based on thresholds
feedback = []
for val in metrics:
    category = 'high' if val >= 0.85 else 'medium' if val >= 0.75 else 'low'
    confidence = 'high' if var < 0.01 else 'moderate'
    feedback.append({'value': val, 'category': category, 'confidence': confidence})

# Auxiliary function with red herring parameters
def calculate_weighted_risk(feedback_list, adjustment_factor=1.2):
    risk = 0
    for entry in feedback_list:
        if entry['category'] == 'low':
            risk += 0.1 * adjustment_factor
    return risk if risk > 0 else 0.05

risk_level = calculate_weighted_risk(feedback)

baseline = 100 * avg
penalty = int(risk_level * 10) * 2
baseline -= penalty  # Apply artificial penalty

# Unused intermediate calculations (distractors)
theoretical_max = max(metrics) * 100
projection = baseline + (10 if risk_level < 0.06 else 5)

status_flags = ['A' if f['category'] == 'high' else 'B' for f in feedback]
flag_count = len([f for f in status_flags if f == 'A'])

# Core logic embedded within distractions
def evaluate_performance(feedback, target):
    met_target = sum(1 for f in feedback if f['value'] >= target)
    total_entries = len(feedback)
    ratio = met_target / total_entries if total_entries else 0
    multiplier = 1.5 if ratio >= 0.6 else 1.0
    # Conditional expression used here (required Python feature)
    adjustment = 10 if all(f['confidence'] == 'high' for f in feedback) else 5 if flag_count > 1 else 0
    return int((ratio * 100) * multiplier + adjustment)

interim_result = evaluate_performance(feedback, target=0.75)

final_score = evaluate_performance(feedback, target=0.85)

print(f"Result: {final_score}")