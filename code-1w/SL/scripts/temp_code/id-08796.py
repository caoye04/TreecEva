def calculate_base_load(units):
    base_load = 0
    for unit in units:
        if unit['status'] == 'active':
            base_load += unit['power'] * 0.8
    return base_load

units = [
    {'id': 1, 'power': 120, 'status': 'active', 'type': 'A'},
    {'id': 2, 'power': 85, 'status': 'inactive', 'type': 'B'},
    {'id': 3, 'power': 200, 'status': 'active', 'type': 'A'},
    {'id': 4, 'power': 90, 'status': 'active', 'type': 'C'}
]

# Redundant mapping - only some values are actually used later
efficiency_map = {u['id']: (0.95 if u['type'] == 'A' else 0.88) for u in units}

# Distractor: Irrelevant computation on status counts
status_count = {'active': 0, 'inactive': 0}
for u in units:
    status_count[u['status']] += 1

auxiliary_sum = 0
for i, u in enumerate(units):
    auxiliary_sum += i * u['power'] // (i + 1)  # Semi-relevant but not critical

# Sorting for no real effect - red herring
sorted_units = sorted(units, key=lambda x: x['power'], reverse=True)
processed_indices = []
for idx, unit in enumerate(sorted_units):
    if unit['status'] == 'active':
        processed_indices.append(idx)

# Actual core logic masked by noise
def calculate_remaining_capacity(unit_list, eff_map):
    total_capacity = 0
    adjusted_power = []
    
    for unit in unit_list:
        if unit['status'] != 'active':
            continue
        raw_power = unit['power']
        efficiency = eff_map[unit['id']]
        net_power = raw_power * efficiency
        adjusted_power.append(net_power)
    
    # Real computation interleaved with distraction
    temp_offset = 0
    for j, p in enumerate(adjusted_power):
        temp_offset += p % 17  # minor side-effect
    
    total_capacity = int(sum(adjusted_power) - temp_offset)
    
    # More misdirection
    fake_reduction = 0
    for a, b in zip(adjusted_power, adjusted_power[1:]):
        fake_reduction += abs(a - b) * 0.1
    
    return total_capacity + 5  # Final adjustment

interim_load = calculate_base_load(units)

# Key statement
final_capacity = calculate_remaining_capacity(units, efficiency_map)

Result: final_capacity