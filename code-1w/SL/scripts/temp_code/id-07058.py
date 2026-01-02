def normalize(value, min_val=0, max_val=100):
    """Irrelevant normalization function for sensor range (not used in critical path)"""
    return (value - min_val) / (max_val - min_val)


def decode_signal(signal_str):
    """Decodes a hexadecimal signal string into binary and returns bit count"""
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary_str = ''.join(hex_to_bin[char] for char in signal_str.upper())
    return binary_str.count('1')


def transform_sequence(seq):
    """Applies XOR shift on sequence indices — decoy transformation"""
    transformed = []
    for i, val in enumerate(seq):
        transformed.append(val ^ i)  # Irrelevant to final result
    return transformed


def filter_outliers(data, threshold=50):
    """Removes values above threshold — dead code path"""
    return [x for x in data if x <= threshold]


def accumulate_diagnostics(logs):
    """Accumulates diagnostic codes using bitwise OR — actually unused"""
    acc = 0
    for log in logs:
        acc |= decode_signal(log)
    return acc


def process_timestamps(ts_list):
    """Dummy timestamp processor — irrelevant"""
    total_chars = 0
    for ts in ts_list:
        total_chars += len(ts.replace('-', '').replace(':', ''))
    return total_chars


def calculate_entropy(data):
    """Calculates Shannon entropy of value distribution"""
    from math import log2
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return round(entropy, 6)


def recursive_partition(arr, depth=0):
    """Recursively splits array and sums middle elements up to depth 2"""
    if len(arr) <= 1 or depth >= 2:
        return arr[0] if len(arr) == 1 else 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return recursive_partition(left, depth + 1) + recursive_partition(right, depth + 1)


def extract_features(raw):
    """Extracts feature vector — includes red herring operations"""
    feature_vector = []
    for entry in raw:
        s = str(entry)
        digit_sum = sum(int(c) for c in s if c.isdigit())
        vowel_count = len([c for c in s.lower() if c in 'aeiou'])  # Useless for numbers
        feature_vector.append(digit_sum + vowel_count)  # vowel_count always 0
    return feature_vector


def analyze_readings(data):
    """Main analysis: computes entropy then applies recursive partitioning"""
    entropy_value = calculate_entropy(data)
    sorted_data = sorted(data)
    partition_result = recursive_partition(sorted_data)
    magic_offset = len([x for x in data if x % 3 == 0])
    return int((entropy_value * 1000) + partition_result + magic_offset)

# --- Simulated Sensor Readings ---
sensor_logs = ['A1F', 'B2C', 'D3E', 'C4A']  # Unused decoy data
timestamps = ['2023-05-01 10:00:00', '2023-05-01 10:05:00', '2023-05-01 10:10:00']

# --- Core Data Stream ---
raw_readings = [12, 8, 12, 5, 8, 12, 15, 5, 8, 12]

# --- Irrelevant Preprocessing ---
normalized = [normalize(x, 0, 20) for x in raw_readings]  # Dead computation
filtered = filter_outliers(raw_readings, threshold=10)  # Computed but unused
transformed_seq = transform_sequence(raw_readings)  # Distractor
feature_set = extract_features(raw_readings)  # Red herring
acc_diag = accumulate_diagnostics(sensor_logs)  # Unused aggregation
timestamp_weight = process_timestamps(timestamps)  # Meaningless sum

# --- Critical Processing Path ---
processed_data = raw_readings.copy()
final_diagnostic = analyze_readings(processed_data)
print(f"Result: {final_diagnostic}")