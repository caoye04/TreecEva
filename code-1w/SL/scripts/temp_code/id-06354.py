def analyze_system_load(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return avg, variance


def compute_hash_chain(seed_value, iterations):
    result = seed_value
    for i in range(iterations):
        result = (result * 7919 + 17) % 65537
    return result

# Irrelevant function - decoy for cryptographic use
def encrypt_data(data, key):
    return ''.join(chr((ord(c) + key) % 128) for c in data)

# Misleading preprocessing - looks important but unused later
raw_logs = "cpu:85|mem:45|disk:60|net:20|gpu:35"
parts = raw_logs.split('|')
log_dict = {item.split(':')[0]: int(item.split(':')[1]) for item in parts}

# Simulated sensor metrics with red herring variables
sensor_ids = ['S1', 'S2', 'S3', 'S4']
sensor_data = {
    'S1': [85, 87, 84, 86],
    'S2': [45, 46, 44, 45],
    'S3': [60, 62, 58, 61],
    'S4': [20, 22, 19, 21]
}

# Dead code path - never invoked
def deprecated_calib(series):
    if len(series) < 3:
        return 0
    return (series[-1] - series[0]) / len(series)

# Distractor: complex bit manipulation that isn't used
bit_flags = 0b101010
shifted = (bit_flags << 3) & 0b11111111
inverted = ~shifted & 0xFF
combined_flag = shifted ^ inverted | 0b00010000

# Real computation begins here
metrics = [85, 45, 60, 20]
baseline = [70, 50, 55, 25]

# Compute differences with list comprehension and enumerate
deviations = [abs(metrics[i] - baseline[i]) for i in range(len(metrics))]
weighted_devs = [dev * (i + 1) for i, dev in enumerate(deviations)]

# Use zip to pair with sensor names for distraction
paired_analysis = list(zip(sensor_ids, deviations, weighted_devs))

# Additional irrelevant transformation
transformed = [round((x + y) / 2) for x, y in zip(weighted_devs, reversed(weighted_devs))]

# Core logic hidden among distractions
normalization_factor = sum(deviations) + 1
adjusted_weights = [w / normalization_factor for w in weighted_devs]

# Hidden dependency: hash chain result affects final outcome
hash_contribution = compute_hash_chain(1234, 5) % 100

# Final evaluation with conditional masking
mask_threshold = 15
masked_devs = [d if d > mask_threshold else 0 for d in deviations]
effective_count = len([d for d in masked_devs if d > 0])

# Actual answer determined here — buried in complexity
performance_index = sum(adjusted_weights) + (hash_contribution * 0.01)

# Key assignment statement
final_score = performance_index * 100

# Another red herring: unused aggregation
aggregated = 0
for idx, val in enumerate(deviations):
    if idx % 2 == 0:
        aggregated += val * 2
    else:
        aggregated -= val

# Print target result
print(f"Result: {final_score}")