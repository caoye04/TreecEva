def analyze_metrics(entries):
    total_entries = len(entries)
    valid_count = 0
    temp_sum = 0
    outlier_threshold = 100
    scaling_factor = 0.9
    adjusted_values = []

    for entry in entries:
        if 'value' not in entry or 'status' not in entry:
            continue
        if entry['status'] != 'active':
            continue
        raw_value = entry['value']
        if raw_value > outlier_threshold:
            raw_value = outlier_threshold  # cap outliers
        adjusted_value = raw_value * scaling_factor
        adjusted_values.append(adjusted_value)
        temp_sum += adjusted_value
        valid_count += 1

    average_adjusted = temp_sum / valid_count if valid_count else 0
    return average_adjusted, valid_count, adjusted_values


def compute_weights(n):
    # Irrelevant helper function (distractor)
    weights = [i ** 0.5 for i in range(1, n+1)]
    normalized = [w / sum(weights) for w in weights]
    return normalized

benchmark_data = [
    {'value': 85, 'status': 'active', 'meta': 'A'},
    {'value': 120, 'status': 'inactive', 'meta': 'B'},
    {'value': 40, 'status': 'active', 'meta': 'C'},
    {'value': 150, 'status': 'active', 'meta': 'D'},
    {'value': 60, 'status': 'active', 'meta': 'E'},
    {'value': 200, 'status': 'active', 'meta': 'F'}
]

# Preprocessing: extract indices and values using enumerate and zip
indices = []
values = []
for i, item in enumerate(benchmark_data):
    indices.append(i)
    values.append(item.get('value', 0))

pairs = list(zip(indices, values))
index_to_value = {idx: val for idx, val in pairs}

# Secondary analysis path (partially irrelevant)
duplicate_tracker = {}
for v in values:
    duplicate_tracker[v] = duplicate_tracker.get(v, 0) + 1

unique_values_count = len(set(values))
sum_of_squares = sum(v ** 2 for v in values)  # Not used later

# Main computation chain
avg_adj, count, adj_vals = analyze_metrics(benchmark_data)

# Simulate data transformation with string operations (semi-relevant)
status_list = [item['status'] for item in benchmark_data]
coded_statuses = [s[0].upper() + str(len(s)) for s in status_list]  # e.g., 'A4' for 'active'

# Weighting logic (only avg_adj matters in the end)
base_score = avg_adj * 1.1
penalty_rate = 0.05
if count < 3:
    base_score -= penalty_rate * 100

# Final aggregation with red herring variables
consistency_bonus = len(coded_statuses) * 0.01
scaling_offset = sum([len(code) for code in coded_statuses]) * 0.005  # unused

final_score = base_score + consistency_bonus

# Output result as required
print(f"Result: {final_score}")