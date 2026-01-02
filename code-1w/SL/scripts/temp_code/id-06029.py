from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for a spacecraft subsystem
def collect_telemetry(raw_bursts):
    aggregated = defaultdict(float)
    temp_log = []
    for burst in raw_bursts:
        for key, value in burst.items():
            if key.startswith('sensor_'):
                aggregated[key] += value * 0.87
                temp_log.append(value)
    noise_floor = sum(temp_log) / len(temp_log) if temp_log else 0
    return dict(aggregated), noise_floor

def validate_checksum(signal):
    # Irrelevant validation for distraction
    total = 0
    for char in signal:
        total ^= ord(char)
    return total % 17 == 0

# Decoy function - never called
def legacy_calibrate(x):
    return (x ** 2 + 3*x + 1) // 5

def analyze_pattern(sequence):
    # Analyze repeating cycles in telemetry (partially relevant)
    count = Counter(sequence)
    modes = [k for k, v in count.items() if v == max(count.values())]
    return sorted(modes)[0] if modes else 0

def generate_baseline(ref_data):
    # Distractor: builds unused baseline model
    base = {}
    for k, v in ref_data.items():
        base[k] = round(math.log(abs(v) + 1) * 1.3, 4)
    return base

def extract_features(data_dict):
    features = []
    keys_used = [k for k in data_dict.keys() if 'sensor_3' in k or 'sensor_7' in k]
    for k in keys_used:
        val = data_dict[k]
        if val > 100:
            features.append(int(val // 10))
        else:
            features.append(int(val ** 0.5))
    return features

def compute_entropy(values):
    # Unused complexity - red herring
    freq = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def process_metrics(signature, readings):
    # Core logic embedded in distractions
    feature_vector = extract_features(readings)
    
    # Irrelevant branching
    if len(feature_vector) > 5:
        adjustment = sum([x for x in feature_vector if x % 2 == 0])
    else:
        adjustment = 0
    
    # Key computation path
    raw_total = sum(feature_vector)
    
    # Misleading intermediate
    dummy_score = (raw_total * 0.93) + 17.5
    
    # Actual logic: find how many times the signature digit appears in flattened features
    digit_count = 0
    for num in feature_vector:
        for digit in str(num):
            if digit == str(signature):
                digit_count += 1
    
    # Final result combines two paths but only one matters
    if dummy_score > 100:
        result = raw_total - digit_count * 3
    else:
        result = raw_total + digit_count * 5
    
    # Dead code branch (never reached due to above structure)
    if False:
        fallback = math.ceil(dummy_score / 2)
        result = fallback
    
    return result

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    telemetry_bursts = [
        {'sensor_1': 45, 'sensor_3': 121, 'sensor_5': 67, 'sensor_7': 144},
        {'sensor_2': 33, 'sensor_3': 98, 'sensor_4': 110, 'sensor_7': 225},
        {'sensor_3': 169, 'sensor_6': 88, 'sensor_7': 196}
    ]

    # Step 1: Collect and normalize telemetry
    normalized_readings, floor_noise = collect_telemetry(telemetry_bursts)

    # Step 2: Generate unused baseline for confusion
    baseline_model = generate_baseline(normalized_readings)

    # Step 3: Extract key pattern from unrelated data (red herring)
    signal_code = 'X9ZP7Q'
    is_valid = validate_checksum(signal_code)

    # Step 4: Build feature set for processing
    trend_sequence = [12, 7, 12, 3, 7, 12]
    dominant_cycle = analyze_pattern(trend_sequence)

    # Step 5: Define critical inputs
    health_signature = 2  # Digit to search for
    
    # Step 6: Process final metrics
    final_diagnostic = process_metrics(health_signature, normalized_readings)

    # Output target result
    print(f"Result: {final_diagnostic}")