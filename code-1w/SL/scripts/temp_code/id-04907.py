def preprocess_signal(raw_samples):
    # Irrelevant normalization (dead path)
    normalized = [x / max(raw_samples) for x in raw_samples if x > 0]
    adjusted = []
    for i, val in enumerate(raw_samples):
        if i % 3 == 0:
            adjusted.append(val * 1.1)
        elif i % 5 == 0:
            adjusted.append(val * 0.95)
        else:
            adjusted.append(val)
    return adjusted

# Simulated sensor readings (some are decoys)
device_a_readings = [120, 135, 140, 128, 150, 160, 155, 170, 180, 175]
device_b_readings = [95, 100, 98, 105, 110, 108, 115, 120, 118, 125]
device_c_readings = [80, 85, 88, 90, 92, 95, 98, 100, 102, 105]

all_readings = [*device_a_readings, *device_b_readings, *device_c_readings]

# Distractor: unused function
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Misleading transformation chain
shifted = [x - 10 for x in all_readings if x > 100]
scaled = [x * 1.05 for x in shifted]
duplicate_filter = list(set(scaled))  # Order lost, not used later

# Relevant preprocessing
processed_a = preprocess_signal(device_a_readings)
processed_b = preprocess_signal(device_b_readings)
processed_c = preprocess_signal(device_c_readings)

# Decoy aggregation
average_per_device = [
    sum(processed_a) / len(processed_a),
    sum(processed_b) / len(processed_b),
    sum(processed_c) / len(processed_c)
]

# Real processing begins: merge with index tracking
timestamps = list(range(len(processed_a)))
combined_with_time = []
for t in timestamps:
    entry = []
    if t < len(processed_a): entry.append(('A', processed_a[t]))
    if t < len(processed_b): entry.append(('B', processed_b[t]))
    if t < len(processed_c): entry.append(('C', processed_c[t]))
    combined_with_time.append(entry)

# Filter entries where any sensor exceeds dynamic threshold
dynamic_caps = {'A': 155, 'B': 112, 'C': 100}
filtered_data = []
for moment in combined_with_time:
    valid_moment = []
    for source, reading in moment:
        if reading <= dynamic_caps[source]:
            valid_moment.append((source, reading))
    if valid_moment:
        filtered_data.append(valid_moment)

# Distractor dictionary (partially used)
thresh_summary = {
    'A': {'base': 150, 'tolerance': 5, 'active': True},
    'B': {'base': 110, 'tolerance': 2, 'active': False},
    'C': {'base': 95, 'tolerance': 5, 'active': True}
}

# Threshold map construction (only 'base' matters)
threshold_map = {k: v['base'] + (v['tolerance'] if v['active'] else 0) for k, v in thresh_summary.items()}

# Unused recursive helper (red herring)
def count_above_recursive(arr, limit, idx=0):
    if idx >= len(arr):
        return 0
    count = 1 if arr[idx] > limit else 0
    return count + count_above_recursive(arr, limit, idx + 1)

# Core analysis function
def analyze_readings(moment_list, thresholds):
    diagnostics = []
    for idx, moment in enumerate(moment_list):
        status_flags = 0
        for src, val in moment:
            ref = thresholds.get(src, 0)
            if val > ref:
                status_flags |= (1 << ord(src) % 31)  # Bitwise encoding
        # Only last 4 bits matter
        diagnostics.append(status_flags & 0xF)
    
    # Final diagnostic: sum of squares of even-indexed flags
    total = 0
    for i, flag in enumerate(diagnostics):
        if i % 2 == 0:
            total += flag ** 2
    return total + len(moment_list)  # Key contribution

# Critical execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")