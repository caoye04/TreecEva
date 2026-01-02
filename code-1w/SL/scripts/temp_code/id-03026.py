def process_entries(entries):
    filtered = [e for e in entries if len(e['name']) > 3]
    transformed = list(map(lambda x: {**x, 'name': x['name'].upper()}, filtered))
    return transformed

# Irrelevant helper that isn't used
def dummy_analysis(seq):
    return sum(len(s) for s in seq) // len(seq) if seq else 0

# Distractor variables
total_checks = 0
redundant_sum = 0

raw_data = [
    {'name': 'alice', 'value': 12, 'flag': True},
    {'name': 'bob', 'value': 8, 'flag': False},
    {'name': 'carol', 'value': 15, 'flag': True},
    {'name': 'dave', 'value': 5, 'flag': True},
    {'name': 'eve', 'value': 20, 'flag': False}
]

processed_data = process_entries(raw_data)

# Extra computation on unused path
lengths_list = [len(item['name']) for item in raw_data]
avg_length = sum(lengths_list) / len(lengths_list)

# More distraction: string manipulation with no impact
status_tags = ['valid' if 'A' in name.upper() else 'other' for name in [d['name'] for d in processed_data]]

# Actual logic begins here
valid_count = 0
accumulated = 0
for record in processed_data:
    total_checks += 1  # distractor counter
    if record['flag']:
        accumulated += record['value'] * 2
        valid_count += 1

# Simulate weighting
weight_factor = 1.5 if valid_count > 2 else 1.0
weighted_accum = accumulated * weight_factor

# Secondary loop – partially redundant
intermediate_scores = []
for record in processed_data:
    base = record['value']
    bonus = 5 if record['name'].startswith('C') else 0
    intermediate_scores.append(base + bonus)

# This function uses lambda and string methods as required
calculate_final_score = lambda data: len("".join([d['name'] for d in data])) + sum(d['value'] for d in data)

# Final assignment
final_score = calculate_final_score(processed_data)

# Print result as required
print(f"Result: {final_score}")