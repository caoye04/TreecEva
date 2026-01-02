def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    reverse_scan = sequence[::-1]
    
    for char in reverse_scan:
        if char.lower() in 'aeiou':
            count_vowels += 1
        temp_sum += ord(char) % 17

    adjusted = len(sequence) - count_vowels
    return adjusted, temp_sum


def filter_entries(records):
    valid_items = []
    invalid_count = 0
    
    for record in records:
        if not record.get('active'):
            invalid_count += 1
            continue
        if len(record['name']) < 3:
            continue
        score_hint = sum([ord(c) for c in record['name'][:2]])
        valid_items.append({'name': record['name'], 'score_hint': score_hint})
    
    # Irrelevant transformation
    name_buffer = [item['name'].upper()[::-1] for item in valid_items]
    _ = [n.startswith('A') for n in name_buffer]  # dead computation

    return valid_items


def calculate_final_score(data_chunk):
    base_value = 0
    penalty = 0
    
    for entry in data_chunk:
        name = entry['name']
        hint = entry['score_hint']
        
        # Real contribution to result
        if len(name) % 2 == 0:
            base_value += hint // 10
        else:
            base_value -= hint % 10

        # Distractor block: complex but unused
        reversed_clean = name.lower().replace('e', '').title()
        extra_flag = any(reversed_clean.count(v) > 1 for v in 'aeiou')
        if extra_flag:
            penalty += 1
    
    # This penalty is never applied; red herring
    return base_value  # final logic step


# Main execution flow
raw_sequence = "QuantumEntanglement"
data_set = [
    {'name': 'qubit', 'active': True},
    {'name': 'gate', 'active': True},
    {'name': 'swap', 'active': False},  # filtered out
    {'name': 'alice', 'active': True},
    {'name': 'bob', 'active': True},   # too short
    {'name': 'entangler', 'active': True}
]

# Step 1: Analyze string pattern (partial distractor)
a_pattern_result = analyze_pattern(raw_sequence)
noise_factor = a_pattern_result[1] % 13

# Step 2: Filter and transform data
cleaned_entries = filter_entries(data_set)

# Step 3: Add fake enrichment
for item in cleaned_entries:
    enriched_tag = item['name'].strip().lower().capitalize()
    checksum = sum(map(ord, enriched_tag)) % 100
    item['tag'] = enriched_tag  # stored but not used
    item['check'] = checksum     # irrelevant field

# Key statement: compute final score
final_score = calculate_final_score(cleaned_entries)

print(f"Result: {final_score}")