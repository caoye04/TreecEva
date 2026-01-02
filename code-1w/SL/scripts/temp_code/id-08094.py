def calculate_final_score(entries):
    total = 0
    bonus = 0
    penalties = []
    temp_buffer = []

    for i, entry in enumerate(entries):
        if i % 2 == 0:
            total += entry['value']
        else:
            temp_buffer.append(entry['value'])

    for val in temp_buffer:
        if val > 50:
            bonus += 5

    flags = [1, 0, 1]
    mask = 3
    masked_flags = [f & mask for f in flags]

    active_count = sum(masked_flags)
    final_score = total + bonus - active_count

    metadata_log = "Processed {} entries with {} bonuses applied".format(len(entries), bonus)
    print(metadata_log)

    return final_score

# Simulated data input
data_entries = [
    {'id': 'A01', 'value': 45, 'valid': True},
    {'id': 'A02', 'value': 60, 'valid': True},
    {'id': 'A03', 'value': 30, 'valid': False},
    {'id': 'A04', 'value': 70, 'valid': True},
    {'id': 'A05', 'value': 25, 'valid': True}
]

intermediate_result = [d['value'] for d in data_entries if d['valid']]
entry_count = len(intermediate_result)
sorted_values = sorted(intermediate_result)
median_val = sorted_values[len(sorted_values)//2] if sorted_values else 0

result = calculate_final_score(data_entries)
print("Result: {}".format(result))