def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def encode_sequence(seq):
    encoded = 0
    for val in seq:
        encoded = (encoded << 1) ^ int(abs(val) * 1000)
    return encoded


def validate_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum += val * (i + 1)
    return checksum % 1024


def generate_lookup(keys):
    lookup = {}
    for k in keys:
        lookup[k] = k ^ (k >> 2)  # Bitwise transformation
    return lookup


def aggregate_metrics(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return round(mean * variance, 4)


def extract_features(dataset):
    features = []
    for item in dataset:
        if isinstance(item, str):
            length_score = len(item.strip())
            upper_ratio = sum(1 for c in item if c.isupper()) / len(item)
            score = length_score * (1 + upper_ratio)
            features.append(int(score))
    return features


def analyze_pattern(data):
    temp_result = 0
    for i in range(len(data)):
        if i % 2 == 0:
            temp_result += data[i] * (i + 1)
        else:
            temp_result -= data[i] // (i + 1) if data[i] != 0 else 0
    
    intermediate = abs(temp_result) ^ 54321
    final_diagnostic = (intermediate + (intermediate >> 4)) & 0xFFFF
    return final_diagnostic

# Irrelevant auxiliary functions (distractors)
def unused_signal_filter(buf):
    return [x for x in buf if x > 0]

def dummy_compress(stream):
    return sum(len(str(x)) for x in stream) % 100

# Simulated sensor input (red herring variables)
sensor_log = ['ERROR:OFF', 'STATUS_OK', 'WARNING:LOW', 'INFO:HIGH']
log_analysis = extract_features(sensor_log)

# Main data pipeline
raw_sensor_data = [0.23, -0.45, 0.12, 0.67, -0.89, 0.03, 0.55, -0.22]
cleaned_data = preprocess_signal(raw_sensor_data)
encoded_stream = encode_sequence(cleaned_data)
checksum_valid = validate_checksum(cleaned_data)

# Unused transformations (dead code paths)
key_list = [128, 256, 512, 1024]
lookup_table = generate_lookup(key_list)
fake_aggregation = aggregate_metrics([0.1, 0.2, 0.3])

# Core computation chain
transformed_data = [
    int(abs(x) * 100) for x in cleaned_data
]

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")