import itertools

# Simulated system telemetry data
sensor_readings = [127, 255, 193, 64, 95, 128, 200, 32]

# Irrelevant utility function (decoy)
def encrypt_byte(b):
    return (b ^ 0x5A) % 256

def analyze_trend(values):
    trend_vector = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_vector.append(1)
        elif values[i] < values[i-1]:
            trend_vector.append(-1)
        else:
            trend_vector.append(0)
    
    # Distractor: unused transformation
    smoothed = [sum(trend_vector[i:i+3]) / 3 for i in range(len(trend_vector) - 2)]
    
    return trend_vector

# Bit manipulation red herring
def obfuscate_key(key):
    shifted = (key << 3) & 0xFF
    return shifted ^ 0xAA

# Security checksum with misleading complexity
def compute_integrity_hash(data):
    hash_val = 0
    for d in data:
        hash_val ^= d
        hash_val = (hash_val * 31) % 10007
    return hash_val % 256

# Real processing begins here
def extract_peaks(seq, threshold):
    peaks = []
    for i in range(1, len(seq) - 1):
        if seq[i] > threshold and seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            peaks.append(i)
    return peaks

# Unused but plausible diagnostic routine (dead code path)
def legacy_diagnostic(mode=0):
    temp_buf = [i * 2 for i in range(50) if i % 7 == 0]
    return sum(temp_buf) >> mode

# Core metric aggregator (used in final result)
def aggregate_metrics(trend, base):
    score = 0
    # Logical operations and comparisons
    for t in trend:
        if t == 1 and base > 100:
            score += 3
        elif t == -1 or base < 50:
            score -= 2
        else:
            score += 1
    
    # Slicing operation (relevant)
    snippet = trend[:len(trend)//2 + 1]
    bonus = len([x for x in snippet if x == 1])
    
    return score + bonus

# Decoy list transformation using itertools
redundant_pairs = list(itertools.combinations(sensor_readings[:4], 2))
transformed = [a ^ b for a, b in redundant_pairs if (a + b) % 2 == 0]
shadow_metric = sum(transformed) // 2 if transformed else 0

# Lambda function for dynamic filtering (partially relevant)
valid_range_filter = lambda x: 64 <= x <= 192
filtered_sensors = list(filter(valid_range_filter, sensor_readings))

# Baseline derived from filtered sensors
baseline = sum(filtered_sensors) // len(filtered_sensors)

# Trend analysis on original data
raw_trend = analyze_trend(sensor_readings)

# Extract key pattern features
trend_data = [abs(x) for x in raw_trend]

# Security-related checksum (actually used in final step)
security_checksum = compute_integrity_hash(sensor_readings[:6]) // 10

# Dead code with misleading name
auxiliary_audit_trail = [obfuscate_key(b) for b in sensor_readings]

# Critical statement
final_diagnostic = aggregate_metrics(trend_data, baseline) + security_checksum

# Result output
print(f"Result: {final_diagnostic}")