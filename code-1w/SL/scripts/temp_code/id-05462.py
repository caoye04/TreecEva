from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == 'A' and i % 2 == 0:
            count += 1
    return count

def validate_entry(entry):
    # Irrelevant validation logic (not used in final computation)
    if not entry.get('active'):
        return False
    if len(entry['name']) < 3:
        return False
    return True

data = [
    {'name': 'Alice', 'values': [3, 7, 2], 'active': True, 'tag': 'X'},
    {'name': 'Bob', 'values': [5, 1, 9], 'active': True, 'tag': 'Y'},
    {'name': 'Charlie', 'values': [4, 6, 3], 'active': False, 'tag': 'X'},
    {'name': 'Diana', 'values': [2, 8, 5], 'active': True, 'tag': 'Z'}
]

# Preprocessing: extract names and compute string-based metrics
names = [entry['name'] for entry in data]
name_lengths = [len(name) for name in names]
avg_length = sum(name_lengths) / len(name_lengths)

# Extract active entries (only True entries are processed further)
active_entries = [e for e in data if e['active']]

# Compute product of values for each active entry
products = []
for entry in active_entries:
    prod = 1
    for v in entry['values']:
        prod *= v
    products.append(prod)

# Misleading intermediate calculation (not used later)
max_product = max(products) if products else 0
placeholder_result = max_product * 0.85

# Use lambda to filter high-product entries
high_performer = list(filter(lambda x: x > 100, products))

# Simulate pattern analysis on encoded tag string
encoded_tags = ''.join([e['tag'] for e in active_entries])
analyzed_count = analyze_pattern('A' + encoded_tags + 'A')  # Extra 'A's added

# Combine results using weighted logic
base_score = sum(high_performer) // len(high_performer) if high_performer else 0
bonus = analyzed_count * 5

# Final processing step with distraction
processed_data = {
    'base': base_score,
    'extra': placeholder_result,  # unused field
    'adjustment': bonus,
    'flags': [False, True, False]  # red herring
}

def calculate_final_score(data_dict):
    score = data_dict['base']
    # Apply adjustment only if certain condition met (always true here)
    tags_str = "XY"
    if 'X' in tags_str:
        score += data_dict['adjustment']
    return int(score)

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")