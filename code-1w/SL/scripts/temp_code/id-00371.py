from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
data_stream = [
    {'id': 1, 'value': 85, 'type': 'temp', 'status': 'active'},
    {'id': 2, 'value': 45, 'type': 'pressure', 'status': 'active'},
    {'id': 3, 'value': 90, 'type': 'temp', 'status': 'active'},
    {'id': 4, 'value': 30, 'type': 'pressure', 'status': 'inactive'},
    {'id': 5, 'value': 95, 'type': 'temp', 'status': 'active'},
    {'id': 6, 'value': 40, 'type': 'pressure', 'status': 'active'},
    {'id': 7, 'value': 87, 'type': 'temp', 'status': 'active'},
    {'id': 8, 'value': 50, 'type': 'pressure', 'status': 'active'}
]

# Irrelevant statistical counters (distractor)
stats_counter = defaultdict(int)
total_reads = 0
valid_count = 0

# Accumulate meaningless stats across all entries
for entry in data_stream:
    stats_counter[entry['type']] += 1
    total_reads += 1
    if entry['value'] > 40:
        valid_count += 1

# Misleading intermediate transformation (dead path)
decayed_values = []
for entry in data_stream:
    decayed_value = entry['value'] * 0.95 ** (entry['id'] % 3)
    decayed_values.append(decayed_value)

# Extract only active temperature readings above baseline
baseline = 80
relevant_entries = [e for e in data_stream if e['status'] == 'active' and e['value'] > baseline and e['type'] == 'temp']

# Use slicing to skip first reading (simulates calibration skip)
filtered_data = relevant_entries[1:]  # Skip first temp reading for stabilization

# Secondary filter based on id parity (irrelevant but plausible)
filtered_data = [e for e in filtered_data if e['id'] % 2 == 1]

# Compute aggregate metrics (some used, some not)
values_only = [e['value'] for e in filtered_data]
mean_val = sum(values_only) / len(values_only) if values_only else 0
max_val = max(values_only) if values_only else 0
min_val = min(values_only) if values_only else 0

# Bitwise interference: encode status into flag (distractor logic)
flag_register = 0
for v in values_only:
    flag_register ^= (v << 2) & 0xFF  # Truncate to byte

# Threshold determined by non-obvious logic (key dependency)
threshold = int(mean_val - min_val) if len(values_only) > 1 else 5

# Helper function with red herring parameters
def analyze_spike(value, sensitivity=0.1, normalize=False):
    norm_factor = 100 if normalize else 1
    return (value / norm_factor) > sensitivity

# Unused recursive accumulator (dead code)
def accumulate_recursively(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + accumulate_recursively(arr, idx + 1)

# Core processing function with conditional logic
def process_signals(data_list, limit):
    if not data_list:
        return -1
    
    result = 0
    spike_count = 0
    
    for item in data_list:
        raw = item['value']
        # Apply hidden correction factor based on ID
        corrected = raw - (item['id'] % 4)  # Subtle adjustment
        if corrected > limit:
            spike_count += 1
        result += corrected
    
    # Final output combines accumulation and spike logic
    return result * spike_count + (limit % 7)

# Execute main computation
final_output = process_signals(filtered_data, threshold)

# Print result in required format
print(f"Target result: {final_output}")