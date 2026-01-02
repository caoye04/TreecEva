from itertools import combinations

def analyze_pattern(sequence):
    trends = []
    for i in range(len(sequence) - 1):
        if sequence[i+1] > sequence[i]:
            trends.append(1)
        elif sequence[i+1] < sequence[i]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def validate_stability(trend):
    changes = 0
    for i in range(len(trend) - 1):
        if trend[i] != trend[i+1]:
            changes += 1
    return changes < 5

def aggregate_performance(records, importance_weights):
    adjusted_scores = []
    temp_buffer = []
    
    # Irrelevant pattern analysis (distractor)
    for record in records:
        pattern = analyze_pattern(record)
        is_stable = validate_stability(pattern)
        temp_buffer.append(is_stable)  # Not used later
    
    # Core logic with distraction from buffer and redundant steps
    total_weight = sum(importance_weights)
    normalized_weights = [w / total_weight for w in importance_weights]
    
    cumulative = 0
    for idx, (record, weight) in enumerate(zip(records, normalized_weights)):
        avg = sum(record) / len(record)
        # Apply non-linear adjustment (relevant)
        adjusted = avg ** 1.2 if avg > 0 else avg
n        cumulative += adjusted * weight
    
    # Red herring: unused combination analysis
    if len(records) >= 3:
        combo_sum = 0
        for combo in combinations(records, 3):
            combo_sum += len(combo)  # Computation with no effect

    scaling_factor = 1.05
    final = int(cumulative * scaling_factor * 100)
    
    return final

# Input data
assessment_data = [
    [85, 90, 88, 87],
    [76, 78, 80, 77],
    [92, 89, 94, 90],
    [81, 83, 80, 82]
]

weights = [0.2, 0.3, 0.4, 0.1]

# Unused preprocessing (dead code path - mild distraction)
processed = []
for i, data in enumerate(assessment_data):
    processed.append([x * 0.95 for x in data if x > 80])

final_score = aggregate_performance(assessment_data, weights)
print(f"Result: {final_score}")