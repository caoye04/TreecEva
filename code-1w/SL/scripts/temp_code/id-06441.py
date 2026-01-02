def transform_sequence(seq, factor):
    return [x * factor for x in seq if x % 2 == 1]

# Irrelevant transformation chain (dead path)
def legacy_encode(data):
    encoded = []
    for item in data:
        temp = bin(item)[2:]
        if len(temp) < 8:
            temp = '0' * (8 - len(temp)) + temp
        encoded.append(temp[::-1])
    return encoded

# Unused helper function (decoy)
def calculate_entropy(values):
    from math import log2
    freq_map = {}
    total = len(values)
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

# Sensor simulation with red herring variables
def generate_signals(base_freq, duration, noise_level=0.1):
    import math
    signal = []
    for t in range(duration):
        raw = math.sin(2 * math.pi * base_freq * t / 10) + noise_level * t
        quantized = int(abs(raw * 100))
        signal.append(quantized)
    return signal

# Core processing with meaningful but obscured logic
def normalize_readings(raw_seq, offset=50):
    adjusted = [max(0, x - offset) for x in raw_seq]
    filtered = [x for x in adjusted if x > 0]
    return sorted(filtered, reverse=True)

def aggregate_metrics(items):
    stats = {
        'sum': sum(items),
        'count': len(items),
        'peak': max(items) if items else 0,
        'floor': min(items) if items else 0
    }
    # Distractor computation
    dummy_sum = 0
    for i in range(len(items)):
        if i % 3 == 0:
            dummy_sum += items[i] * 1.5
    stats['dummy'] = int(dummy_sum)  # unused field
    return stats

# Real processing path buried among decoys
def preprocess_record(record_str):
    # Use string method meaningfully
    cleaned = record_str.strip().replace("_", ",").replace(" ", "")
    parts = cleaned.split(',')
    nums = [int(p) for p in parts if p.isdigit()]
    return transform_sequence(nums, 3)

# Critical function - answer depends on this
threshold_map = {
    'level_a': 65,
    'level_b': 85,
    'critical': 100
}

def analyze_readings(data_list, limits):
    high_vals = [x for x in data_list if x > limits['level_b']]
    medium_vals = [x for x in data_list if limits['level_a'] <= x <= limits['level_b']]
    score = len(high_vals) * 7 + sum(medium_vals) // 10
    if len(high_vals) >= 3:
        score += 25
    return score

# Simulate input data using multiple steps
raw_signal = generate_signals(base_freq=1.3, duration=25, noise_level=0.15)
processed_data = normalize_readings(raw_signal, offset=42)

# Decoy data structure manipulation
shadow_copy = processed_data.copy()
for i in range(len(shadow_copy)):
    if shadow_copy[i] % 4 == 0:
        shadow_copy[i] = shadow_copy[i] // 4
    elif shadow_copy[i] > 70:
        shadow_copy[i] = 11

# Tuple unpacking distraction
summary_stats = aggregate_metrics(processed_data)
(total_sum, item_count, peak_val, floor_val) = (
    summary_stats['sum'],
    summary_stats['count'],
    summary_stats['peak'],
    summary_stats['floor']
)

# Set operation red herring
distinct_highs = set([x for x in processed_data if x > 90])
expected_set_size = len(distinct_highs) + 2  # never used

data_string = "sensor_78_91_64_73_88_95"
extracted_nums = preprocess_record(data_string)

# Another distractor: sorting irrelevant list
temp_analysis = extracted_nums + [total_sum % 100]
sorted_temp = sorted(temp_analysis, key=lambda x: str(x)[::-1])

# Main execution flow
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")