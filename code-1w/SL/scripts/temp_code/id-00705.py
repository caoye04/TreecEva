from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and redundant readings
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]

# Irrelevant preprocessing: frequency analysis of digits (distractor)
digit_freq = Counter(data_stream)
most_common_digit = digit_freq.most_common(1)[0][0]

# Redundant transformation: reverse cumulative sum (not used in final logic)
reverse_cumsum = []
cumulative = 0
for i in range(len(data_stream) - 1, -1, -1):
    cumulative += data_stream[i]
    reverse_cumsum.append(cumulative)
reverse_cumsum.reverse()

# Distractor function: computes statistical dispersion but unused
def calculate_spread(arr):
    mean_val = sum(arr) / len(arr)
    variance = sum((x - mean_val) ** 2 for x in arr) / len(arr)
    return math.sqrt(variance)

# Another decoy: attempts to fit polynomial trend (dead code path)
def fit_trend(series):
    n = len(series)
    slope = (n * sum(i * series[i] for i in range(n)) - sum(range(n)) * sum(series)) \
             / (n * sum(i**2 for i in range(n)) - sum(range(n))**2 + 1e-9)
    return [int(slope * i) for i in range(n)]

# Real signal extraction: isolate strictly increasing runs
filtered_runs = []
current_run = [data_stream[0]]

for i in range(1, len(data_stream)):
    if data_stream[i] > data_stream[i - 1]:
        current_run.append(data_stream[i])
    else:
        if len(current_run) > 1:
            filtered_runs.append(current_run)
        current_run = [data_stream[i]]

if len(current_run) > 1:
    filtered_runs.append(current_run)

# Transform each run by squaring elements and taking modulo 7
transformed_runs = []
for run in filtered_runs:
    transformed = [(x ** 2) % 7 for x in run]
    transformed_runs.append(transformed)

# Flatten transformed runs into single list
transformed_data = []
for tr in transformed_runs:
    for val in tr:
        transformed_data.append(val)

# Decoy aggregation: count transitions (misleading intermediate)
transition_count = defaultdict(int)
for i in range(len(transformed_data) - 1):
    key = (transformed_data[i], transformed_data[i + 1])
    transition_count[key] += 1

# Threshold determined from median of original data (critical real path)
sorted_data = sorted(data_stream)
median_val = sorted_data[len(sorted_data) // 2]
threshold = (median_val ** 2) % 11  # Non-obvious derivation

# Core analysis function: counts occurrences above threshold in transformed set
def analyze_pattern(signal, limit):
    count_above = 0
    total_sum = 0.0
    for x in signal:
        total_sum += x
        if x > limit:
            count_above += 1
    # Final diagnostic is weighted combination
    weight = 1.5 if count_above > 3 else 1.0
    return int((count_above * 100) + (total_sum / (len(signal) or 1)) * weight)

# Dead code: recursive checksum (never called)
def recursive_checksum(arr, depth=0):
    if depth >= 3 or len(arr) == 0:
        return 0
    return arr[0] ^ recursive_checksum(arr[1:], depth + 1)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")