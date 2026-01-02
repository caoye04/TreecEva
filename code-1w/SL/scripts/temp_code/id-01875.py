def analyze_distribution(items):
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


def validate_sequence(seq):
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True

# Simulate warehouse storage units with initial capacity
storage_units = [120, 200, 150, 300, 250]
utilization_rate = [0.4, 0.65, 0.5, 0.7, 0.8]

# Irrelevant list comprehension - distractor (computes unused ratios)
transfer_ratios = [round((u * 100) / cap, 2) for cap, u in zip(storage_units, utilization_rate)]

# Allocation history as list of tuples (unit_index, allocated_amount)
allocation_list = [(0, 25), (1, 30), (0, 15), (2, 40), (3, 50), (1, 20), (4, 60)]

# Build current storage map from base capacity and utilization
storage_map = {}
for idx, base in enumerate(storage_units):
    used = int(base * utilization_rate[idx])
    storage_map[f'unit_{idx}'] = {'base': base, 'used': used}

# Track total reallocated amount - semi-relevant but not final
reallocated_total = sum(alloc[1] for alloc in allocation_list)

# Dummy set operation - distractor
active_indices = {idx for idx, _ in allocation_list}
handled_indices = {0, 1, 2, 3}
inactive_set = active_indices - handled_indices  # unused later

# Helper function to compute available headroom before reallocations
def calculate_headroom(unit_data):
    return unit_data['base'] - unit_data['used']

# Another distractor: recursive character counter (not related)
def count_chars_recursive(s):
    if not s:
        return 0
    return 1 + count_chars_recursive(s[1:])

total_chars = count_chars_recursive("warehouse")

# Core logic: calculate remaining capacity after applying allocations
def calculate_remaining_capacity(storage, allocations):
    temp_storage = {}
    for k, v in storage.items():
        temp_storage[k] = v.copy()
    
    # Apply each allocation
    for unit_idx, amount in allocations:
        key = f'unit_{unit_idx}'
        if key in temp_storage:
            temp_storage[key]['used'] += amount
    
    # Compute final available capacity across all units
    total_base = sum(v['base'] for v in temp_storage.values())
    total_used = sum(v['used'] for v in temp_storage.values())
    return total_base - total_used

# Execute main computation
final_capacity = calculate_remaining_capacity(storage_map, allocation_list)

# Print result as required
print(f"Result: {final_capacity}")