from collections import defaultdict, Counter

# Simulated system performance metrics over time
timestamps = [100, 101, 102, 103, 104]
raw_data = [
    {'cpu': 75, 'mem': 80, 'disk': 40, 'net': 60},
    {'cpu': 80, 'mem': 85, 'disk': 45, 'net': 65},
    {'cpu': 90, 'mem': 90, 'disk': 50, 'net': 70},
    {'cpu': 85, 'mem': 88, 'disk': 55, 'net': 68},
    {'cpu': 70, 'mem': 82, 'disk': 60, 'net': 72}
]

# Irrelevant historical thresholds (distractor)
historical_thresholds = defaultdict(lambda: 50)
historical_thresholds.update({'cpu': 95, 'mem': 90, 'disk': 75})

# Weight configuration for current evaluation
weights = {'cpu': 0.4, 'mem': 0.3, 'disk': 0.2, 'net': 0.1}

# Misleading normalization function (not actually used in final computation)
def normalize_legacy(data_list):
    result = []
    for entry in data_list:
        norm_entry = {k: v / 100.0 for k, v in entry.items()}
        result.append(norm_entry)
    return result

# Decoy aggregation using string operations (red herring)
def string_based_aggregation(data_list):
    as_strings = [str(d['cpu']) + str(d['mem']) for d in data_list]
    concatenated = ''.join(as_strings)
    fake_sum = sum(int(c) for c in concatenated if int(c) % 2 == 0)
    return fake_sum  # Dead end

# Actual processing pipeline
processed_metrics = defaultdict(list)
for record in raw_data:
    for key, value in record.items():
        processed_metrics[key].append(value)

# Compute averages per metric
averages = {key: sum(values) / len(values) for key, values in processed_metrics.items()}

# Bit manipulation distraction (irrelevant)
bit_flags = 0b101010
shifted_flags = (bit_flags << 3) & 0b11111111
inverted = ~shifted_flags & 0b11111111
checksum_fake = (inverted ^ 0b10101010) >> 4

# Another decoy: frequency analysis on irrelevant patterns
all_cpu_values = [d['cpu'] for d in raw_data]
frequency_count = Counter(all_cpu_values)
dominant_cpu = frequency_count.most_common(1)[0][1]  # Used nowhere important

# Conditional expression red herring
penalty = 10 if averages['cpu'] > 85 else 5 if averages['mem'] > 85 else 0
bonus = 5 if all(v > 70 for v in averages.values()) else 0

# Core logic disguised among noise
scaling_factor = 1.0
if averages['disk'] < 50:
    scaling_factor *= 0.9
if averages['net'] > 65:
    scaling_factor *= 1.05  # This branch taken

adjusted_averages = {k: v * scaling_factor for k, v in averages.items()}

# Final aggregation function
def aggregate_performance(avg_dict, weight_dict):
    total = 0.0
    for metric in weight_dict:
        # Apply conditional adjustment based on threshold
        val = avg_dict[metric]
        if val > 80:
            val += 2  # Performance bonus for high utilization
        elif val < 60:
            val -= 3
        total += val * weight_dict[metric]
    return int(round(total))

# Unused recursive distraction
def recursive_variance(data, depth=0):
    if depth >= 2 or len(data) == 1:
        return abs(data[-1] - data[0])
    mid = len(data) // 2
    left = recursive_variance(data[:mid], depth + 1)
    right = recursive_variance(data[mid:], depth + 1)
    return (left + right) / 2

# Trigger the actual computation
final_score = aggregate_performance(averages, weights)

# Print result
print(f"Target result: {final_score}")