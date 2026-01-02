import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    timestamps = list(range(100, 200, 2))
    signals = []
    for t in timestamps:
        raw = (math.sin(t * 0.1) * 100) + (t % 7) + ((t ** 0.5) % 10)
        signals.append(round(raw, 2))
    return dict(zip(timestamps, signals))

# Irrelevant helper: computes unused checksum
def compute_checksum(data):
    return sum(len(str(k)) + len(str(v)) for k, v in data.items()) % 1000

# Dead function: never called but looks important
def legacy_transform(x):
    if x < 0:
        return int(abs(x) ** 0.3) * -1
    return int(x ** 0.6)

# Unused aggregation method
def aggregate_peaks(signal_dict):
    peaks = [v for v in signal_dict.values() if v > 75]
    return sum(peaks) / len(peaks) if peaks else 0

# Auxiliary analysis: character frequency in string-encoded values (distractor)
def char_frequency_analysis(log_data):
    combined = ''.join(f'{k}{v}' for k, v in log_data.items())
    freq = {}
    for c in combined:
        freq[c] = freq.get(c, 0) + 1
    # Returns most frequent digit, irrelevant to main logic
    digits = {d: freq[d] for d in '0123456789' if d in freq}
    return max(digits, key=digits.get) if digits else '0'

# Real processing chain
system_logs = generate_telemetry()

# Distractor variables
checksum = compute_checksum(system_logs)
dummy_list = [legacy_transform(v * 2) for v in system_logs.values() if v > 50]
peak_summary = aggregate_peaks(system_logs)
most_common_digit = char_frequency_analysis(system_logs)

# Hidden relevant logic: filter and transform
filtered_readings = [
    v for k, v in system_logs.items()
    if (k % 13 == 0) and (v > 0)
]

# Multiple steps of calculation
normalized = [abs(x) ** 0.5 for x in filtered_readings]
squared_offsets = [(x - math.floor(x)) ** 2 for x in normalized]
shifted = [y + 0.1 for y in squared_offsets if y > 0.1]

# Statistical computation
mean_shifted = sum(shifted) / len(shifted) if shifted else 0.0
variance_proxy = sum((z - mean_shifted) ** 2 for z in shifted) / len(shifted) if shifted else 0.0

count_distribution = {}
for val in shifted:
    bucket = int(val * 10)
    count_distribution[bucket] = count_distribution.get(bucket, 0) + 1

# Main metric derived from distribution
max_bucket = max(count_distribution.keys()) if count_distribution else 0
bucket_weights = {
    k: v * (k / (max_bucket + 1e-6)) 
    for k, v in count_distribution.items()
}
weighted_total = sum(bucket_weights.values())

decay_factor = 0.95 ** len(shifted)
adjusted_metric = weighted_total * decay_factor

# Final transformation using dictionary operations
config_map = {
    'threshold': 1.45,
    'scale': 2.1,
    'offset': -0.33,
    'damping': 0.88
}

interim = adjusted_metric * config_map['scale']
if interim > config_map['threshold']:
    interim -= config_map['offset']
else:
    interim += config_map['offset']

# Apply damping only if length conditions are met
if len(filtered_readings) % 4 == 2:
    interim *= config_map['damping']

# Final diagnostic score
final_diagnostic = round(interim, 6)

# Output result as required
print(f"Result: {final_diagnostic}")