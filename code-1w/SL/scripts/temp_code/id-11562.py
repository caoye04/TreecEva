def process_metrics(entries, importance_weights):
    base_offset = 10
    temp_buffer = []
    cumulative_shift = 0

    for i, entry in enumerate(entries):
        adjusted_value = entry['value'] * importance_weights.get(entry['type'], 1.0)
        if entry['active']:
            scaled = adjusted_value ** 0.5
            temp_buffer.append(scaled + base_offset)
            if i % 2 == 0:
                cumulative_shift += int(scaled) & 7
        else:
            placeholder = adjusted_value / 2
            temp_buffer.append(placeholder)  # dead path contribution

    filtered_data = [x for x in temp_buffer if x > 12]
    
    # Irrelevant string manipulation block (distractor)
    status_labels = ['active', 'inactive', 'pending']
    coded = ''.join([label[0].upper() for label in status_labels])
    magic_key = hash(coded) % 50

    # Bitwise interference
    mask = 0
    for j in range(len(filtered_data)):
        mask ^= int(filtered_data[j]) | (j << 1)
    
    # Real computation starts here
    aggregate = sum(filtered_data)
    correction_factor = len(filtered_data) or 1
    raw_score = aggregate / correction_factor
    
    # Secondary adjustment using lambda and zip
    modifiers = list(map(lambda x: x % 3, [88, 95, 76, 42]))
    pairs = zip(filtered_data, modifiers[:len(filtered_data)])
    bonus = sum([a * (b // 2) for a, b in pairs]) / correction_factor

    # Final computation
    final_score = raw_score + bonus + cumulative_shift - magic_key
    return final_score

# Input setup
data = [
    {'type': 'A', 'value': 25, 'active': True},
    {'type': 'B', 'value': 36, 'active': False},
    {'type': 'A', 'value': 49, 'active': True},
    {'type': 'C', 'value': 64, 'active': True},
    {'type': 'B', 'value': 16, 'active': True}
]
weights = {'A': 1.2, 'B': 0.8, 'C': 1.5}

interim_result = 0
for item in data:
    interim_result += item['value'] // 4

final_score = process_metrics(data, weights)
print(f"Target result: {final_score}")