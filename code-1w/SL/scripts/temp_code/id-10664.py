def process_entries(entry_list):
    processed = {}
    temp_sum = 0
    for entry in entry_list:
        key = entry['id']
        value = entry['value']
        if value < 0:
            value = abs(value)  # Normalize negative values
        temp_sum += value
        processed[key] = value ** 0.5  # Store square root as intermediate metric
    avg_val = temp_sum / len(entry_list)
    return processed, avg_val

entry_data = [
    {'id': 'A', 'value': 25},
    {'id': 'B', 'value': 16},
    {'id': 'C', 'value': 9},
    {'id': 'D', 'value': -4},
    {'id': 'E', 'value': 36}
]

# Irrelevant transformation: string manipulation with no impact
status_labels = ['active', 'inactive', 'pending']
label_caps = [label.upper() for label in status_labels]

# Misleading statistical calculation
mean_value = sum(item['value'] for item in entry_data) / len(entry_data)
adjusted_values = {item['id']: item['value'] * 1.1 for item in entry_data}

# Actual relevant data processing
rank_data, base_average = process_entries(entry_data)

def calculate_correction_factor(avg):
    if avg > 15:
        return 0.9
    else:
        return 1.1

correction = calculate_correction_factor(base_average)

bonus_multiplier = 1
for k, v in rank_data.items():
    if v > 3.0:
        bonus_multiplier += 0.1

# Distractor loop: iterates but doesn't affect final result
shadow_total = 0
for i in range(3):
    for j in range(2):
        shadow_total += i * j

# Key computation
final_score = int((base_average * correction + 10) * bonus_multiplier)

# Red herring: unused function
def debug_state(data):
    return {k: (v, round(v, 1)) for k, v in data.items()}

# Final irrelevant dictionary operation
metadata_store = {'version': '1.0', 'entries': len(rank_data)}
metadata_store['timestamp'] = 'ignored'

Result: final_score