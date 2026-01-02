def analyze_component(x, threshold=5.0):
    return x > threshold

# Simulate sensor data processing with filtering and scoring
data_points = [3.2, 6.1, 4.8, 7.3, 5.5]
weights = [0.8, 1.2, 0.9, 1.5, 1.1]
labels = ['A', 'B', 'C', 'D', 'E']

# Irrelevant transformation (distractor)
transformed_labels = [label.lower().replace('a', 'x') for label in labels]

# Accumulate weighted values above threshold
aggregate = 0.0
valid_count = 0
for i, value in enumerate(data_points):
    if analyze_component(value):
        aggregate += value * weights[i]
        valid_count += 1

# Secondary computation with string-based logic (semi-relevant)
bonus_factor = len([l for l in labels if l in 'BCDE']) * 0.1

# Simulated normalization step (distractor)
normalized = [round((x - min(data_points)) / (max(data_points) - min(data_points)), 3) for x in data_points]

# Build benchmark structure using tuples and dictionaries
benchmark_data = [
    {'id': 'S1', 'value': data_points[0], 'meta': ('type1', 100)},
    {'id': 'S2', 'value': data_points[1], 'meta': ('type2', 200)},
    {'id': 'S3', 'value': data_points[2], 'meta': ('type1', 150)},
    {'id': 'S4', 'value': data_points[3], 'meta': ('type3', 300)},
    {'id': 'S5', 'value': data_points[4], 'meta': ('type2', 250)}
]

# Dead code path (distractor)
def unused_helper(data):
    return sum(len(str(d)) for d in data)

# Core calculation function with conditional expression
def calculate_performance(logs):
    base_total = 0
    type_counts = {}
    for entry in logs:
        val = entry['value']
        category = entry['meta'][0]
        
        # Conditional expression usage (core logic)
        adjustment = 1.1 if 'S' in entry['id'] and val >= 5.0 else 0.95
        
        base_total += val * adjustment
        
        # Track type frequency (semi-relevant)
        if category not in type_counts:
            type_counts[category] = 0
        type_counts[category] += 1
    
    # Summation over dictionary values (semi-relevant to distraction)
    type_penalty = sum(v ** 0.5 for v in type_counts.values())
    
    # Final performance score with bonus factor from earlier
    return int(base_total - type_penalty + bonus_factor)

# Execute main logic
interim_result = aggregate * valid_count  # Distractor variable
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")