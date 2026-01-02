def analyze_signal(pattern):
    # Irrelevant signal processing (dead end)
    if len(pattern) % 2 == 0:
        return sum([ord(c) for c in pattern]) // len(pattern)
    return None

def decode_sequence(seq):
    # Unused decoding function (distractor)
    base = 0
    for i, char in enumerate(seq):
        base += (i + 1) * ord(char)
    return base % 1000

def validate_checksum(data):
    # Misleading validation logic (not used in final path)
    total = 0
    for item in data:
        if isinstance(item, int):
            total += item * 2
        elif isinstance(item, str):
            total += len(item)
    return total % 7 == 0

def extract_features(raw):
    # Red herring feature extraction
    features = []
    for entry in raw:
        if 'x' in entry:
            features.append(entry.count('x'))
    return features

def compute_entropy(values):
    # Complex but irrelevant entropy calculation
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = 0.0
    n = len(values)
    for count in freq.values():
        p = count / n
        entropy -= p * log2(p)
    return round(entropy, 4)

def filter_anomalies(stream):
    # Distractor: modifies a copy, not original
    cleaned = []
    for val in stream:
        if val > 5 and val < 95:
            cleaned.append(val)
    return cleaned

def process_readings(data):
    # Core logic buried among distractions
    readings = []
    for line in data:
        # Parse using string methods
        parts = line.strip().split(',')
        for part in parts:
            part = part.strip()
            if part.isdigit():
                readings.append(int(part))
    
    # Real computation begins
    temp_sum = 0
    count = 0
    for num in readings:
        if num % 3 == 0 and num % 5 != 0:  # divisible by 3 but not 5
            temp_sum += num ** 2
            count += 1
    
    if count == 0:
        average_power = 0
    else:
        average_power = temp_sum / count
    
    # Secondary transformation
    adjusted = int(average_power // 1.5)
    
    # Bit manipulation stage (key step)
    bit_shifted = (adjusted << 2) ^ 0b1101  # Multiply by 4 then XOR with 13
    
    # Final adjustment using string length side effect
    tag = "DGN-{}".format(bit_shifted)
    checksum_offset = len(tag.replace('-', ''))  # Length without hyphen
    final_value = bit_shifted + checksum_offset
    
    return final_value

# Simulated sensor input (looks like logs)
sensor_data = [
    "78, x33, 45, abc",           # mixed noise
    "92, 60, 21, zzz",            # contains valid numbers
    "no_data, 87, 12",            # partial valid
    "",                            # empty line
    "33, 99, 15, 7",              # more inputs
]

# Dead code paths invoked to increase interference
_ = analyze_signal("testpattern")
_ = decode_sequence("ABCDEFG")
_ = validate_checksum([10, 20, 'hello'])
_ = extract_features(['xxx', 'xyx', 'xx'])
_ = compute_entropy([1,1,2,2,3,3,3])
_ = filter_anomalies([1, 50, 100, 40, 90])

# Critical execution point
final_diagnostic = process_readings(sensor_data)
print(f"Result: {final_diagnostic}")