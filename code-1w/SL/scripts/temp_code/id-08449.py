import math

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    raw_readings = [3.2, 4.1, 2.8, 5.6, 3.9, 4.4, 5.1, 3.7]
    offset = 0.3
    adjusted = [x + offset for x in raw_readings]
    return adjusted

# Irrelevant auxiliary function - dead code path (distractor)
def legacy_compatibility(data):
    if len(data) > 10:
        return [x * 0.95 for x in data]
    else:
        return data[::-1]

# Data transformation with slicing and filtering
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    filtered = [x for x in signal if abs(x - mean_val) < 1.0]
    smoothed = [round((filtered[i] + filtered[i+1]) / 2, 3) for i in range(len(filtered)-1)]
    padded = [0.0] + smoothed + [0.0]  # padding for edge cases
    return padded[1:-1]  # remove padding again - net no effect, but distracts

# Character pattern analysis from metadata (irrelevant to final result)
def extract_patterns(config_str):
    chars = list(config_str)
    counts = {}
    for c in chars:
        counts[c] = counts.get(c, 0) + 1
    unique_chars = len([c for c in counts.values() if c == 1])
    return unique_chars * 1.5  # misleading intermediate

# Core processing logic
def compute_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

# Main pipeline
readings = collect_readings()

# Misleading intermediate transformations (some used, some not)
signal_strength = [x ** 2 for x in readings]
avg_power = sum(signal_strength) / len(signal_strength)
threshold = 15.0

# Slice based on dynamic condition (actually used)
active_window = signal_strength[1:6]

# Apply normalization (relevant)
transformed_data = normalize_signal(active_window)

# Baseline configuration string (used in decoy)
baseline_config = 'ENV-2024-XG7'

# Decoy usage of config string - looks important but isn't
config_score = extract_patterns(baseline_config)

# Red herring: conditional that appears significant but leads nowhere
critical_flag = False
if len(transformed_data) >= 4 and config_score > 10:
    temp_result = [math.sin(x) for x in transformed_data]
    magnitude = sum(abs(x) for x in temp_result)
    if magnitude > 5.0:
        critical_flag = True

# Lambda-based aggregation (required Python feature)
aggregator = lambda data, func: func(data)
data_sum = aggregator(transformed_data, sum)
data_count = aggregator(transformed_data, len)
mean_value = data_sum / data_count if data_count else 0

# Secondary irrelevant computation using string methods
version_parts = baseline_config.split('-')
revision_code = version_parts[-1]
checksum = sum(ord(c) for c in revision_code) % 100

# Real processing chain begins here
entropy_metric = compute_entropy(transformed_data)
size_factor = len(''.join(version_parts[:2]))  # uses string slicing and joining

# Weighting factors (only one actually matters)
factors = {
    'entropy': entropy_metric * 1.8,
    'size': size_factor * 0.7,
    'config': config_score * 0.3  # decoy factor
}

# Actual metric combination
combined_index = factors['entropy'] + factors['size']  # ignores 'config'

# Final diagnostic calculation
final_diagnostic = int(round(combined_index * 1000))

print(f"Result: {final_diagnostic}")