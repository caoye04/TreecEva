import math

# Simulated sensor data processing with embedded logic chain
def collect_readings():
    raw = [127, 255, 192, 64, 32, 160, 96, 224]
    scaled = [x * 0.75 for x in raw]
    return scaled

def filter_outliers(data, threshold=75.0):
    # Irrelevant filtering path (dead logic - not used later)
    return [x for x in data if x > threshold]

def generate_checksum(signal):
    # Misleading checksum computation (never actually used in final result)
    chk = 0
    for val in signal:
        chk ^= int(val) & 255
    return chk + 1000

def transform_signal(signal):
    # Actual transformation path
    processed = []
    for s in signal:
        if s > 100:
            processed.append(int(s) >> 2)
        elif s > 50:
            processed.append(int(s) << 1)
        else:
            processed.append(int(s) ^ 15)
    return processed

def compute_entropy(values):
    # Distractor function: looks important but unused
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log(p, 2)
    return round(entropy, 6)

def extract_features(dataset):
    # Red herring feature extraction
    features = {
        'peak': max(dataset),
        'valley': min(dataset),
        'range': max(dataset) - min(dataset),
        'mode': sorted(dataset)[len(dataset)//2],
        'dummy_flag': True
    }
    return features

def analyze_pattern(seq):
    # Core logic: count how many elements are powers of two
    count = 0
    for num in seq:
        if num > 0 and (num & (num - 1)) == 0:  # Bitwise check for power of two
            count += 1
    # Transform count via combinatoric offset
    adjustment = 0
    for i in range(1, count + 1):
        adjustment += i * (i + 1) // 2  # Triangular number summation
    return count * 100 + adjustment

# Begin execution
sensor_feed = collect_readings()

# Apply transformation (key relevant step)
transformed_data = transform_signal(sensor_feed)

# Dead-end branches with misleading computations
outliers_filtered = filter_outliers(sensor_feed)
security_hash = generate_checksum(sensor_feed)
entropy_metric = compute_entropy(sensor_feed)
extracted_attributes = extract_features(transformed_data)

# Critical statement
final_diagnostic = analyze_pattern(transformed_data)

# Print result
print(f"Result: {final_diagnostic}")