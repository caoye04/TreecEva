from collections import defaultdict

# Simulated sensor data stream with noise and redundancy
data_stream = [107, 214, 107, 321, 214, 428, 321, 535, 642, 535]

# Irrelevant statistical tracking (distractor)
mean_value = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_value) ** 2 for x in data_stream)
entropy_approx = len(set(data_stream)) / len(data_stream)

# Frequency analysis with defaultdict (relevant but indirect)
frequency_map = defaultdict(int)
for val in data_stream:
    frequency_map[val] += 1

# Extract unique values while preserving order (red herring)
seen = set()
unique_ordered = [x for x in data_stream if not (x in seen or seen.add(x))]

# Misleading trend detection (dead path)
trend_direction = 0
if unique_ordered[-1] > unique_ordered[0]:
    trend_direction = 1
elif unique_ordered[-1] < unique_ordered[0]:
    trend_direction = -1

# Weight assignment based on position and frequency (partially relevant)
base_weights = [i * 0.1 for i in range(1, len(data_stream) + 1)]
adjusted_weights = []
for idx, val in enumerate(data_stream):
    adjustment = frequency_map[val] * 0.05
    adjusted_weights.append(base_weights[idx] + adjustment)

# Decoy transformation using list comprehension and zip (irrelevant)
squared_pairs = [(a**2, b**2) for a, b in zip(data_stream, data_stream[::-1]) if a % 2 == 0]
filtered_sums = [x + y for x, y in squared_pairs if x < 50000]
aggregate_noise = sum(filtered_sums) / (len(filtered_sums) + 1) if filtered_sums else 0

# Hidden pattern: longest run of consecutive duplicates in frequency
max_run = current_run = 1
for i in range(1, len(data_stream)):
    if data_stream[i] == data_stream[i-1]:
        current_run += 1
        max_run = max(max_run, current_run)
    else:
        current_run = 1

# Consistency flag based on duplicate clustering (key input)
consistency_flag = 1 if max_run >= 2 else 0

# Auxiliary checksum (decoy)
checksum = 0
for i, w in enumerate(adjusted_weights):
    checksum += int(w * 10) * (i + 1)
checksum %= 97

# Core logic disguised within distractions
def evaluate_stability(flag, weights):
    total = 0.0
    for i, w in enumerate(weights):
        if i % 3 == 0:
            total += w * flag
        elif i % 5 == 0:
            total -= w * 0.5
    return total

# Secondary processing chain
intermediate_score = evaluate_stability(consistency_flag, adjusted_weights)

# Final computation buried in abstraction
def process_outcome(flag, weights):
    weighted_sum = sum(w * (i+1) for i, w in enumerate(weights))
    penalty = 0
    for i in range(1, len(weights)):
        if weights[i] < weights[i-1]:
            penalty += 0.01
    # Critical dependency on consistency_flag
    if flag:
        result = weighted_sum * 0.85 - penalty * 100
    else:
        result = weighted_sum * 0.65 + penalty * 50
    return int(result)

# Execution point of interest
final_score = process_outcome(consistency_flag, adjusted_weights)

# Output as required
print(f"Target result: {final_score}")