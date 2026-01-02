import math

# Irrelevant helper function (dead code path)
def unused_util(x):
    return sum(i * 2 for i in x if i % 3 == 0)

# Distractor data structure
telemetry_cache = {
    'sensor_7': [1, 5, 9, 14],
    'sensor_4': [2, 8, 11, 16],
    'baseline': [0, 0, 0, 0]
}

# Real processing starts here
raw_readings = [3, 7, 12, 15, 19, 23]
offset_correction = 2
adjusted = [x - offset_correction for x in raw_readings]  # [1, 5, 10, 13, 17, 21]

# Bit manipulation red herring
bit_flags = 0b101010
masked = bit_flags & 0b111100  # 40, irrelevant

# Decoy transformation chain
def bad_transform(data):
    return [d ** 2 % 7 for d in data]

# Real transformation using lambda (required feature)
scale_func = lambda val: val * 3 + 1
transformed_data = list(map(scale_func, adjusted))  # [4, 16, 31, 40, 52, 64]

# Misleading intermediate accumulation
dummy_sum = 0
for i in range(len(transformed_data)):
    if i % 2 == 0:
        dummy_sum += transformed_data[i] * 0.5  # Partial fake use

# Simulated historical data (unused)
historical_max = {
    'Q1': 30,
    'Q2': 45,
    'Q3': 50,
    'Q4': 60
}

# Real recursive function (required concept)
def count_peaks(lst, idx=0):
    if idx >= len(lst) - 1:
        return 0
    current_peak = 1 if lst[idx] < lst[idx + 1] else 0
    return current_peak + count_peaks(lst, idx + 1)

peak_count = count_peaks(transformed_data)  # 5 peaks (only one direction matters)

# Conditional decoy with early return distraction
def check_anomaly(seq):
    if sum(seq) > 200:
        return False  # Misleading logic
    if len(seq) < 5:
        return True
    return seq[0] > seq[-1]

anomaly_flag = check_anomaly(adjusted)  # False, unused

# Core analysis logic
threshold = 35
count_above = sum(1 for x in transformed_data if x > threshold)  # 4 values > 35

# Secondary metric (distractor)
weighted_avg = sum(i * v for i, v in enumerate(transformed_data)) / len(transformed_data)

# Real pattern analyzer (uses lambda indirectly via composition)
analyze_pattern = lambda data: len(data) * count_peaks(data) - count_above * 2

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output result as required
print(f"Result: {final_diagnostic}")