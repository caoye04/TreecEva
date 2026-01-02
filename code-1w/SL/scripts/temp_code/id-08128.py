import math

# Simulated sensor data preprocessing with red herrings
def collect_readings():
    raw_values = [i * 0.7 + (i % 3) for i in range(15)]
    offset = 12.8  # unused distraction
    scale_factor = 2.1  # decoy parameter, never used
    filtered = [x for x in raw_values if x > 4.0]
    return filtered

# Irrelevant auxiliary function (dead code path)
def calibrate_system(data):
    adjustment = sum([math.sin(x) for x in data]) / len(data)
    normalized = [x - adjustment for x in data]
    return normalized  # never called

# Real processing chain
def encode_sequence(values):
    encoded = []
    for v in values:
        temp = int(abs(v * 10)) % 7
        encoded.append(temp)
    return encoded

def transform_block(block):
    # Bit manipulation red herring
    xor_key = 255
    shifted = [(b << 1) ^ xor_key for b in block]  # misleading transformation
    return [b % 100 for b in shifted]  # normalization discards most bits

# Core logic disguised among distractions
def compute_entropy(signal):
    total = 0
    for x in signal:
        if x != 0:
            total += x * math.log(x, 2)
    return round(-total, 4)

# Unused statistical decoy
def calculate_kurtosis(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0
    kurtosis = sum((x - mean) ** 4 for x in data) / (variance ** 2) / n
    return kurtosis  # computed but irrelevant

# Higher-order function distraction
def make_amplifier(factor):
    return lambda x: x * factor

amplify = make_amplifier(3.5)  # looks important, never used

# Actual critical computation path
def aggregate_metrics(encoded):
    count = 0
    for val in encoded:
        count += (val + 1) ** 2
    return count

def generate_checksum(value_list):
    checksum = 0
    for i, v in enumerate(value_list):
        checksum ^= (v * (i + 1))  # simple XOR-based checksum
    return checksum

def analyze_signal(data):
    entropy_score = compute_entropy(data)  # distraction calculation
    metric_total = aggregate_metrics(data)
    check = generate_checksum(data)
    # Final diagnostic combines two key results with bit trick
    final_value = (metric_total + check) & 0xFFFF  # clamp to 16-bit
    return final_value

# Orchestration with misleading steps
if __name__ == '__main__':
    readings = collect_readings()                    
    processed_data = encode_sequence(readings)       # real input generation
    scaled_data = [x * 1.5 for x in readings]         # dead branch, unused
    calibrated = calibrate_system(scaled_data)        # never used
    blocked = transform_block(processed_data)         # computed but irrelevant
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")