import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [127, 255, 192, 64, 32, 160]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

def transform_signal(data):
    # Irrelevant transformation path (dead code)
    if len(data) > 10:
        return [x ** 0.5 for x in data]
    
    # Actual relevant transformation
    transformed = []
    for val in data:
        if val > 100:
            transformed.append(int(val) | 15)  # Bitwise interference
        else:
            transformed.append(int(val) & 240)
    return transformed

def validate_checksum(signal):
    # Distractor function - never actually used
    checksum = 0
    for x in signal:
        checksum ^= x
    return checksum == 255

def filter_anomalies(packets):
    # Unused filtering logic (red herring)
    clean_packets = []
    for p in packets:
        if p % 16 != 0:
            clean_packets.append(p)
    return clean_packets

def decode_header(signal):
    # Meaningless header extraction
    header_value = 0
    if len(signal) >= 4:
        header_value = (signal[0] << 2) ^ (signal[3] >> 1)
    return header_value

def compute_entropy(data):
    # Decoy statistical analysis
    total = sum(data)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in data:
        prob = x / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 6)

def analyze_signal(data):
    # Core logic hidden among distractions
    threshold = 100
    count_above = 0
    running_sum = 0
    
    for val in data:
        if val > threshold:
            count_above += 1
            running_sum += val
        else:
            running_sum -= val
    
    # Critical calculation
    if count_above == 0:
        return 0
    
    base_metric = running_sum / count_above
    
    # Secondary adjustment using string-based key (obscure but valid)
    key_str = 'diagnostic_7'
    suffix_digit = int(key_str[-1])  # Extract '7' from string
    adjusted_metric = base_metric + suffix_digit
    
    # Tertiary logic with tuple unpacking (relevant)
    flags = (True, False, True)
    flag_a, flag_b, flag_c = flags
    if flag_a and not flag_b or flag_c:
        adjusted_metric *= 2
    
    return int(adjusted_metric)

# Main execution flow
raw_data = collect_readings()
processed_data = transform_signal(raw_data)

# Dead code paths (distractors)
data_valid = validate_checksum(processed_data)
header = decode_header(processed_data)
entropy_score = compute_entropy(processed_data)

# Unused variable assignments (misleading)
buffer_snapshot = processed_data[:3]
anomaly_free = filter_anomalies(processed_data)
system_flag = buffer_snapshot[0] > 150

# Key statement where answer is determined
def final_execution():
    global final_diagnostic
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")

final_execution()