def process_entry(entry):
    # Irrelevant transformation (distractor)
    temp_adjustment = (entry['value'] ** 0.5) * 0.1
    adjusted = entry['value'] + temp_adjustment
    
    # Core logic: classify and weight based on threshold
    if entry['category'] == 'A':
        weight = 1.5
    elif entry['category'] == 'B':
        weight = 0.8
    else:
        weight = 1.0

    return adjusted * weight

# Misleading helper that's not used in final path
def legacy_transform(x):
    return (x * 2) % 7 + 1  # Dead-end computation

# Lambda for dynamic filtering (actually used)
is_relevant = lambda x: x['active'] and x['value'] > 5

# Simulated dataset with mixed categories
raw_data = [
    {'value': 10, 'category': 'A', 'active': True},
    {'value': 15, 'category': 'B', 'active': False},  # filtered out
    {'value': 8, 'category': 'A', 'active': True},
    {'value': 12, 'category': 'C', 'active': True},
    {'value': 20, 'category': 'B', 'active': True},  # included but weighted low
]

# Preprocessing with distraction: unused normalization
max_val = max(d['value'] for d in raw_data)
normalized_data = [{**d, 'norm': d['value'] / max_val} for d in raw_data]

# Actual pipeline
filtered_data = [d for d in raw_data if is_relevant(d)]

# Secondary distraction: accumulation of irrelevant metric
entropy_proxy = 0.0
for d in filtered_data:
    entropy_proxy += (d['value'] / 10) ** 0.3  # Not used later

# Core processing chain
intermediate_scores = []
for entry in filtered_data:
    score = process_entry(entry)
    intermediate_scores.append(score)

# Additional red herring: sorting for no reason
intermediate_scores.sort(reverse=True)

# Final aggregation with modular arithmetic twist
total_mod_sum = sum(int(s) % 7 for s in intermediate_scores)
base_sum = sum(intermediate_scores)

def calculate_final_score(data):
    # Complex but mostly redundant initialization
    initial_guess = len(data) * 10
    penalty = 0
    
    # Use of lambda in reduction (real usage)
    aggregator = lambda acc, x: acc + (x ** 0.25)
    bonus = 0
    for s in intermediate_scores:
        bonus = aggregator(bonus, s)
    
    # Real contribution: base sum + bonus - mod adjustment
    result = base_sum + bonus - total_mod_sum
    
    # Dead code branch (never reached)
    if len(data) > 100:
        fallback = 0
        for i in range(len(data)):
            fallback += data[i]['value'] // (i+1)
        return fallback
    
    return result

# Execute main logic
final_score = calculate_final_score(filtered_data)

# Output target variable
print(f"Result: {final_score}")