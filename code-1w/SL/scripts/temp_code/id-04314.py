def preprocess_records(raw_entries):
    filtered = [e for e in raw_entries if e['status'] == 'active']
    sorted_by_id = sorted(filtered, key=lambda x: x['id'])
    return sorted_by_id

raw_data = [
    {'id': 5, 'status': 'inactive', 'load': 20},
    {'id': 1, 'status': 'active', 'load': 15},
    {'id': 3, 'status': 'active', 'load': 10},
    {'id': 4, 'status': 'inactive', 'load': 5},
    {'id': 2, 'status': 'active', 'load': 30}
]

# Irrelevant transformation - distractor
transformed = [{**item, 'flag': item['load'] > 10} for item in raw_data]
duplicate_check = {item['id']: item for item in transformed}

processed_data = preprocess_records(raw_data)

# Secondary helper with misleading intermediate
redundant_aggregate = sum(item['load'] for item in raw_data if item['status'] == 'active')
baseline = len([x for x in raw_data if x['status'] == 'active'])

scaling_factor = 2.5
adjustment_offset = 0.7

# Real computation begins
loads = [record['load'] for record in processed_data]
total_load = sum(loads)
record_count = len(processed_data)

if record_count > 0:
    average_load = total_load / record_count
else:
    average_load = 0

# Dummy branching - does not affect result
if average_load > 25:
    efficiency_class = 'high'
elif average_load > 15:
    efficiency_class = 'medium'
else:
    efficiency_class = 'low'

# Actual final calculation
normalization_constant = 100

# Misleading complexity with unused formula
theoretical_max = record_count * max(loads) if loads else 1
utilization_ratio = total_load / theoretical_max if theoretical_max != 0 else 0

# Core logic hidden among distractions
weighted_sum = sum(load * (i + 1) for i, load in enumerate(loads))

# Final function call


def calculate_efficiency(data):
    base = sum(entry['load'] for entry in data)
    penalty = len(data) ** 2
    return int((base * scaling_factor) - penalty + adjustment_offset)

# Key assignment point
efficiency_score = calculate_efficiency(processed_data)

print(f"Result: {efficiency_score}")