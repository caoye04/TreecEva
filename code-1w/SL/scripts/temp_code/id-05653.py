def analyze_utilization(records):
    utilization = {}
    for idx, (res, usage) in enumerate(records):
        if res not in utilization:
            utilization[res] = 0
        utilization[res] += usage * (idx + 1)
    return utilization


def filter_redundant(data, threshold=10):
    # Irrelevant filtering function – distractor
    result = []
    total = 0
    for k, v in data.items():
        if v > threshold:
            result.append((k, v))
        total += v // 2  # Unused computation
    return result

resource_map = [('cpu', 8), ('memory', 32), ('storage', 500), ('network', 10)]
allocation_log = [1, 0, 3, 2, 1, 3, 0, 2]

# Misleading intermediate calculations
baseline_score = 0
for i, item in enumerate(resource_map):
    baseline_score += len(item[0]) * item[1]

# Dummy structure – red herring
snapshot = {}
for i, log in enumerate(allocation_log):
    snapshot[i] = {'index': log, 'weight': (i * log) % 7}

# Actual core logic embedded with noise
usage_counts = {i: 0 for i in range(len(resource_map))}
for entry in allocation_log:
    usage_counts[entry] += 1

weighted_util = []
total_shift = 0
for key, count in usage_counts.items():
    shift_val = (key + 1) ** 2 % 4
    adjusted = resource_map[key][1] * count + shift_val
    weighted_util.append(adjusted)
    total_shift += shift_val  # Semi-relevant but not critical

# Use of zip and enumerate as required
combined_data = list(zip(resource_map, weighted_util))
indexed_contributions = []
for i, ((res_type, base_val), weight) in enumerate(combined_data):
    contribution = weight * (i + 1)
    if res_type == 'storage':
        contribution += 5  # Special adjustment
    indexed_contributions.append(contribution)

# Secondary analysis – mostly irrelevant
audit_trace = []
cumulative = 0
for i, val in enumerate(indexed_contributions):
    cumulative += val
    audit_trace.append(cumulative * 0.1)  # Distractor values

# Core final calculation
def calculate_system_capacity(resources, logs):
    cap = 0
    freq = {}
    for x in logs:
        freq[x] = freq.get(x, 0) + 1
    
    for i, (rtype, base) in enumerate(resources):
        multiplier = freq.get(i, 0)
        if rtype == 'network':
            cap += base * multiplier // 2
        else:
            cap += base * multiplier
    
    # Final modulation using modular arithmetic
    mod_factor = len(logs) % 9
    if mod_factor > 0:
        cap = (cap + mod_factor * 2) // mod_factor
    
    return int(cap)

# Execution point of interest
final_capacity = calculate_system_capacity(resource_map, allocation_log)

# Print result as required
print(f"Target result: {final_capacity}")