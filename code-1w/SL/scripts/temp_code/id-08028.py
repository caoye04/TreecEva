from itertools import combinations

def preprocess_records(raw_entries):
    processed = []
    offset = 17
    for entry in raw_entries:
        temp_val = (entry[1] + entry[2]) * 2.5 - offset
        if temp_val > 100:
            temp_val = 100 + (100 / (temp_val - 99))  # damping function
        processed.append((entry[0], round(temp_val, 3)))
    return processed

def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log2(prob)
    return round(entropy, 4)

def generate_diagnostic_pairs(data_list):
    pairs = list(combinations(data_list, 2))
    diagnostic_sum = 0
    for p in pairs[:10]:  # arbitrary limit for distraction
        diagnostic_sum += abs(p[0][1] - p[1][1])
    return diagnostic_sum  # unused but looks important

def normalize_readings(raw_data):
    flat_vals = [x[1] for x in raw_data]
    min_val, max_val = min(flat_vals), max(flat_vals)
    range_val = max_val - min_val or 1
    return [(item[0], (item[1] - min_val) / range_val) for item in raw_data]

def evaluate_performance(weights, dataset):
    base = 0
    multiplier = 1.0
    for i, record in enumerate(dataset):
        contribution = record[1] * weights.get(i % 4, 0.5)
        if i % 5 == 0:
            multiplier *= 1.1  # slight boost
        base += contribution
    return int(base * multiplier)

# Main execution flow
raw_employee_data = [
    ('Alice', 88, 45),
    ('Bob', 76, 50),
    ('Charlie', 92, 38),
    ('Diana', 81, 55),
    ('Eve', 95, 42),
    ('Frank', 70, 60)
]

# Step 1: Preprocess to adjust raw metrics
processed_metrics = preprocess_records(raw_employee_data)

# Step 2: Calculate entropy of performance spread (distractor analysis)
entropy_measure = calculate_entropy([x[1] for x in processed_metrics])

# Step 3: Generate diagnostic comparison pairs (unused but plausible)
diag_pairs_value = generate_diagnostic_pairs(processed_metrics)

# Step 4: Normalize data for scoring consistency
normalized_data = normalize_readings(processed_metrics)

# Step 5: Define metric importance weights
metric_weights = {0: 0.8, 1: 1.2, 2: 0.9, 3: 1.1}

# Step 6: Evaluate final performance score
final_score = evaluate_performance(metric_weights, normalized_data)

# Output result
print(f"Result: {final_score}")