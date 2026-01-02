def process_entries(entries):
    processed = []
    temp_sum = 0
    for entry in entries:
        if 'valid' in entry and entry['valid']:
            temp_sum += entry['value']
            processed.append(entry['value'] * 2)
    return processed, temp_sum

entries = [
    {'value': 12, 'valid': True, 'meta': 'A'},
    {'value': 8, 'valid': False, 'meta': 'B'},
    {'value': 5, 'valid': True, 'meta': 'C'},
    {'value': 10, 'valid': True, 'meta': 'D'}
]

# Irrelevant transformation
transformed = [x['value'] ** 2 for x in entries if x['value'] > 9]
dummy_flag = len(transformed) > 2
extra_offset = sum(transformed) // 10 if dummy_flag else 0

results, base_total = process_entries(entries)

lookup_table = {i: v for i, v in enumerate(sorted(results))}
offset_key = len(results) % 3
dynamic_shift = lookup_table.get(offset_key, 0)

bonus_multiplier = 3
penalty_factor = 1

# Simulate environmental condition (distraction)
environment_code = 'prod'
if environment_code == 'dev':
    penalty_factor = 2
elif environment_code == 'test':
    penalty_factor = 1.5
else:
    penalty_factor = 1  # neutral

# Complex scoring with dictionary-based weight map
weight_map = {
    'base': 1.0,
    'bonus': bonus_multiplier * 0.5,
    'shift': dynamic_shift * 0.1,
    'offset': extra_offset * 0.05
}

intermediate_score = base_total * weight_map['base']
intermediate_score += sum(results) * weight_map['bonus']
intermediate_score += dynamic_shift * weight_map['shift']
intermediate_score += extra_offset * weight_map['offset']

# Dummy bitwise adjustment (only applied in rare cases)
current_mode = 0b101
adjustment_mask = 0b110
if current_mode & adjustment_mask:
    intermediate_score -= 5  # minor correction

# Final aggregation through helper function
def calculate_final_score(data_map, mult):
    total = 0
    for key, val in data_map.items():
        if 'bonus' in key or 'shift' in key:
            total += val * mult
    return int(intermediate_score + total)

final_score = calculate_final_score(weight_map, bonus_multiplier)
print(f"Result: {final_score}")