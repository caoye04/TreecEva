import math

# Simulated sensor network diagnostics with data filtering and analysis
def collect_sensor_data():
    raw_readings = [107, 214, 198, 255, 132, 189, 203, 176, 168, 221, 154, 143]
    timestamps = list(range(1000, 1012))
    statuses = ['OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK', 'OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK']
    return list(zip(raw_readings, timestamps, statuses))


def filter_noisy_data(data):
    # Irrelevant transformation: amplifies values but not used in final path
    amplified = [x[0] * 1.1 for x in data if x[2] != 'ERROR']
    filtered = [x[0] for x in data if x[2] == 'OK' or x[2] == 'WARNING']
    decoy_sum = sum([x ^ 255 for x in filtered])  # Bitwise red herring
    normalized = [x for x in filtered if x > 150]  # Only keep significant readings
    return normalized


def compute_checksum(values):
    # Unused function - dead code path (decoy)
    checksum = 0
    for v in values:
        checksum = (checksum + v) * 3 % 97
    return checksum


def rolling_average(values, window=3):
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    padding = [None] * (window // 2)
    return padding + averages + padding


def classify_trend(avg_list):
    valid_avgs = [x for x in avg_list if x is not None]
    if len(valid_avgs) < 2:
        return 'STABLE'
    diff = valid_avgs[-1] - valid_avgs[0]
    if diff > 15:
        return 'INCREASING'
    elif diff < -15:
        return 'DECREASING'
    else:
        return 'STABLE'


def transform_values(vals):
    # Complex but ultimately unused transformation chain
    temp_a = [v + 10 for v in vals]
    temp_b = [t ** 0.5 for t in temp_a]
    temp_c = [round(t, 1) for t in temp_b]
    mapping = {i: temp_c[i] for i in range(len(temp_c))}
    inverse_map = {v: k for k, v in mapping.items()}
    return [mapping[k] for k in sorted(mapping.keys())]  # Not used


def analyze_readings(logs):
    base_weight = 1.75
    adjustment_factor = 0.9
    
    # Real processing begins here
    magnitude = sum(logs)
    entropy_proxy = 0
    for val in logs:
        if val > 0:
            entropy_proxy += val * math.log(val, 2)
    
    # Critical distractor: complex bitwise manipulation with no effect
    decoy_value = 0
    for i in range(len(logs)):
        decoy_value ^= (logs[i] << 2) | (logs[i] >> 3)
    decoy_value = (decoy_value ^ 0xFFFF) & 0xFFF
    
    # Another red herring: string-based encoding of numbers
    encoded = ''.join([hex(x)[-1] for x in logs])
    fake_digest = sum([int(c, 16) * (i + 1) for i, c in enumerate(encoded)])
    
    # Actual logic contributing to answer
    trend_data = rolling_average(logs)
    trend_class = classify_trend(trend_data)
    
    # Final computation
    if trend_class == 'INCREASING':
        multiplier = 2.1
    elif trend_class == 'DECREASING':
        multiplier = 0.85
    else:
        multiplier = 1.35  # STABLE case
    
    # This is the actual answer computation
    final_diagnostic = int((magnitude * base_weight * multiplier) - 127)
    
    # Dead code after this point
    post_hoc_correction = math.floor(final_diagnostic * adjustment_factor)
    if post_hoc_correction < 0:
        post_hoc_correction = 0
        
    return final_diagnostic

# Main execution flow
sensor_data = collect_sensor_data()
processed_logs = filter_noisy_data(sensor_data)

# Transformations that look important but don't affect outcome
dummy_transform = transform_values(processed_logs)

# Key statement where answer is determined
final_diagnostic = analyze_readings(processed_logs)

print(f"Result: {final_diagnostic}")