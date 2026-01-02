from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
raw_readings = [23.1, 24.5, 24.5, 25.3, 23.1, 26.7, 25.3, 24.5]

# Misleading auxiliary data (distractor)
phantom_timestamps = [201, 202, 203]
phantom_values = [99.9, 99.9, 99.9]

# Map readings to timestamps using zip
temp_data = list(zip(timestamps, raw_readings))

# Extract unique readings and count frequency
reading_counts = Counter(raw_readings)
unique_readings = [val for val, cnt in reading_counts.items() if cnt == 1]
duplicated_readings = [val for val, cnt in reading_counts.items() if cnt > 1]

# Process data: filter out duplicated readings and shift timestamp via bitwise XOR (semi-relevant)
filtered_data = []
for ts, val in temp_data:
    if val not in duplicated_readings:
        # Apply non-trivial transformation: mix timestamp with sensor ID (10) via XOR
        obfuscated_ts = ts ^ 10  # distractor transformation
        normalized_val = round(val - 20.0, 2)
        filtered_data.append((obfuscated_ts, normalized_val))

# Secondary filtering based on normalized value threshold (relevant)
valid_entries = [(ts, v) for ts, v in filtered_data if v > 2.0]

# Build time-series profile using defaultdict (core structure)
profile = defaultdict(float)
for ts, norm_val in valid_entries:
    profile[ts] += norm_val * 1.5  # cumulative weighting

# Calculate statistical baseline (distractor computation)
mean_norm = sum(norm_val for _, norm_val in filtered_data) / len(filtered_data) if filtered_data else 0
variance_proxy = sum((v - mean_norm) ** 2 for _, v in filtered_data) / len(filtered_data) if filtered_data else 0
adjusted_var = variance_proxy * 0.85  # never used later

# Prepare processed data using enumerate for index-aware processing
indexed_deltas = []
for i, (ts, nv) in enumerate(valid_entries):
    delta = nv - mean_norm
    index_weight = (i + 1) * 0.1
    compensated_delta = delta + index_weight
    indexed_deltas.append(compensated_delta)

# Final aggregation function
def calculate_final_score(data_part):
    if not data_part:
        return 0.0
    base_sum = sum(data_part)
    # Introduce dummy control flow (short-circuit logic)
    bonus = 10 if len(data_part) > 2 and (sum(data_part) > 5 or True and False) else 5
    penalty_factor = 0.9 if base_sum > 10 else 1.0
    return int((base_sum * penalty_factor) + bonus)

# Execute key statement
final_score = calculate_final_score(indexed_deltas)

# Print result as required
print(f"Result: {final_score}")