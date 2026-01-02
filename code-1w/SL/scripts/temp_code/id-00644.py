def process_entry(entry):
    # Splits name and computes length-based score
    parts = entry['name'].split(' ')
    first_len = len(parts[0])
    last_len = len(parts[-1]) if len(parts) > 1 else 0
    
    # Irrelevant computation: character frequency map (not used in final score)
    char_freq = {}
    for c in entry['name']:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    base_score = first_len * 3 - last_len * 2
    return base_score

# Lambda to filter valid records
data_filter = lambda x: x['active']

# Sample dataset with mixed statuses
data_entries = [
    {'name': 'Alice Johnson', 'active': True, 'level': 5},
    {'name': 'Bob', 'active': False, 'level': 2},
    {'name': 'Charlie Brown', 'active': True, 'level': 7},
    {'name': 'Diana Prince', 'active': True, 'level': 4},
    {'name': 'Eve', 'active': False, 'level': 3}
]

# Misleading preprocessing: counts total characters (unused)
total_chars = sum(len(entry['name'].replace(' ', '')) for entry in data_entries)
invalid_count = len([e for e in data_entries if not e['active']])

# Filter active entries using lambda and list comprehension
filtered_data = [e for e in data_entries if data_filter(e)]

# Extract levels for secondary check (distractor)
levels = [entry['level'] for entry in filtered_data]

# Core logic: compute weighted contribution from processed names and levels
processed_scores = []
for entry in filtered_data:
    name_score = process_entry(entry)
    level_bonus = entry['level'] * 0.5
    combined = name_score + level_bonus
    processed_scores.append(combined)

# Secondary path: XOR of level bits (semi-relevant but only one value used)
level_xor = 0
for lvl in levels:
    level_xor ^= lvl
auxiliary_flag = level_xor & 1  # Used in conditional below

# Final calculation with conditional offset
def calculate_final_score(data):
    raw_sum = sum(processed_scores)
    adjustment = 0
    if auxiliary_flag:
        adjustment = len(filtered_data) * 1.5
    else:
        temp_val = 0
        for s in processed_scores:
            temp_val += s ** 0.5  # Dead code path, never used
    return raw_sum + adjustment

# Execution point
final_score = calculate_final_score(filtered_data)
print(f"Result: {final_score}")