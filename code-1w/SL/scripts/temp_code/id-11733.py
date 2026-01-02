def process_entry(entry):
    # Irrelevant transformation
    temp_adjustment = (entry['value'] ** 0.5) * 0.1
    category_bonus = 0
    if entry['category'] == 'A':
        category_bonus = 10
    elif entry['category'] == 'B':
        category_bonus = 5
    
    # Distractor: unused computation
    shadow_weight = entry['value'] % 7 * 2.3
    
    base_score = entry['value'] * 0.8 + category_bonus
    return base_score

# Helper lambda for string-based filtering (partially relevant)
valid_category = lambda cat: cat in ['A', 'B', 'C']

# Simulated data entries with mixed content
data_entries = [
    {'id': '001', 'value': 50, 'category': 'A', 'tag': 'alpha'},
    {'id': '002', 'value': 30, 'category': 'B', 'tag': 'beta'},
    {'id': '003', 'value': 40, 'category': 'C', 'tag': 'gamma'},
    {'id': '004', 'value': 60, 'category': 'A', 'tag': 'delta'}
]

# Preprocessing: filter by valid categories using lambda and string method
filtered_entries = [e for e in data_entries if valid_category(e['category']) and e['tag'].startswith('d') or 'a' in e['tag']]

# Secondary distractor: counting irrelevant attributes
tag_count = {}
for entry in data_entries:
    first_char = entry['tag'][0]
    tag_count[first_char] = tag_count.get(first_char, 0) + 1

# Another red herring: dictionary manipulation with no impact
summary_stats = {
    'max_value': max(e['value'] for e in data_entries),
    'avg_value': sum(e['value'] for e in data_entries) / len(data_entries),
    'total_tags': len(tag_count)
}

# Actual processing chain
def calculate_final_score(entries):
    raw_scores = []
    for e in entries:
        score = process_entry(e)
        raw_scores.append(score)
    
    # Aggregation with rounding
    total = sum(raw_scores)
    adjustment_factor = 0.9 if len(raw_scores) > 3 else 1.0
    intermediate = total * adjustment_factor
    
    # Final scaling with truncation
    final = int(intermediate + 0.5)  # Simulate round-to-nearest
    return final

# Execute main logic
final_score = calculate_final_score(filtered_entries)

# Print result as required
print(f"Result: {final_score}")