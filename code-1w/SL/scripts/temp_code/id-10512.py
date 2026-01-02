from itertools import groupby

# Simulate sensor readings with some noise and metadata
timestamped_readings = [
    (100, 23.5, 'OK'), (101, 24.1, 'OK'), (102, 22.8, 'ERR'),
    (103, 23.0, 'OK'), (104, 23.0, 'OK'), (105, 23.9, 'OK'),
    (106, 24.2, 'OK'), (107, 23.1, 'OK'), (108, 22.9, 'OK'),
    (109, 23.4, 'OK'), (110, 23.4, 'OK')
]

# Extract temperature values and filter out erroneous status entries
raw_temps = [temp for _, temp, status in timestamped_readings if status == 'OK']

# Misleading computation: average using lambda (not used later)
avg_temp_func = lambda vals: sum(vals) / len(vals) if vals else 0
baseline_avg = avg_temp_func(raw_temps)

# Introduce distractor: count duplicates (not directly relevant)
duplicate_count = 0
for k, g in groupby(sorted(raw_temps)):
    count = len(list(g))
    if count > 1:
        duplicate_count += count - 1

# Normalize temperatures relative to first valid reading (distractor transformation)
normalized_temps = [round(t - raw_temps[0], 2) for t in raw_temps]

# Apply threshold filter: only temps within ±0.5 of the mode-like value (most frequent rounded value)
rounded_temps = [round(t, 1) for t in raw_temps]
mode_candidate = max(set(rounded_temps), key=rounded_temps.count)
valid_range = (mode_candidate - 0.5, mode_candidate + 0.5)

# Actual filtering logic used in final result
filtered_values = []
for temp in raw_temps:
    if valid_range[0] <= round(temp, 1) <= valid_range[1]:
        filtered_values.append(int(temp * 2))  # Transform for final aggregation

# Key statement
filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")