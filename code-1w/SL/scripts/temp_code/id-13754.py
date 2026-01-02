def analyze_text(s):
    vowels = 'aeiou'
    vowel_count = sum(1 for c in s.lower() if c in vowels)
    consonant_count = sum(1 for c in s.lower() if c.isalpha() and c not in vowels)
    special_char_count = len(s) - len(s.replace('@', ''))
    return vowel_count, consonant_count, special_char_count


def transform_values(a, b, c):
    temp1 = a * 2 + 10
    temp2 = b - 3
    temp3 = c * 5 if c > 0 else 0
    normalized = (temp1 + temp2) // max(temp3, 1)
    return normalized


def filter_and_group(data_list):
    grouped = {'A': [], 'B': [], 'C': []}
    totals = {k: 0 for k in grouped.keys()}
    
    for item in data_list:
        key = item['category']
        if key in grouped:
            grouped[key].append(item['value'])
            totals[key] += item['value']
    
    # Irrelevant sorting
    for k in grouped:
        grouped[k].sort(reverse=True)
    
    return totals


def calculate_final_score(metadata_map):
    base = metadata_map['A'] * 3
    bonus = metadata_map['B'] // 2
    penalty = metadata_map['C'] % 7
    adjustment = 5 if penalty < 3 else -2
    
    intermediate = base + bonus - penalty + adjustment
    
    # Distractor computation
    fake_score = (base * bonus) % 1000
    debug_info = f'Score breakdown: {base=}, {bonus=}, {penalty=}'
    
    final = intermediate * 2
    return final

# Main execution
raw_string = "Hello@World@@Programming!!"
vowel_cnt, cons_cnt, special_cnt = analyze_text(raw_string)

processed_value = transform_values(vowel_cnt, cons_cnt, special_cnt)

# Simulated data based on processed value
simulation_seed = processed_value % 4 + 1
data_pool = [
    {'category': 'A', 'value': simulation_seed * 6},
    {'category': 'B', 'value': simulation_seed * 4},
    {'category': 'C', 'value': simulation_seed * 3},
    {'category': 'A', 'value': simulation_seed * 2},
    {'category': 'X', 'value': 999},  # Invalid category (will be ignored)
    {'category': 'B', 'value': 1},
]

aggregated_stats = filter_and_group(data_pool)

# Key statement
final_score = calculate_final_score(aggregated_stats)

# Print result
print(f"Result: {final_score}")