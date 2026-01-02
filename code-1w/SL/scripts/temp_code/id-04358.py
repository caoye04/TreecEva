import math

def analyze_phase_shift(signal, threshold=0.7):
    count = 0
    temp_result = 0
    for x in signal:
        if abs(x) > threshold:
            count += 1
            temp_result += math.sin(x) ** 2
    return count > 5, temp_result

def validate_checksum(data):
    # Irrelevant validation function (dead path)
    checksum = 0
    for d in data:
        checksum ^= d % 256
    return checksum == 128

def encode_timestamp(timestamps):
    # Distractor encoding with list comprehension
    encoded = [((t // 10) ^ 7) + 2 for t in timestamps if t > 100]
    scaled = [math.log(e) if e > 0 else 0 for e in encoded]
    return sum(scaled)

def process_flags(flag_bytes):
    # Bit manipulation decoy
    active_bits = 0
    for b in flag_bytes:
        active_bits += bin(b).count('1')
    return active_bits > 10

def filter_outliers(values, limit=50):
    # Misleading statistical filter
    mean_val = sum(values) / len(values)
    deviations = [abs(v - mean_val) for v in values]
    return [v for v in values if abs(v - mean_val) < limit], sum(deviations)

def aggregate_metrics(logs, indicators):
    base_score = 0
    adjustment = 0.0
    
    # Core logic interwoven with distractions
    for entry in logs:
        if entry % 4 == 0:
            base_score += entry ^ 3
        elif entry % 3 == 0:
            base_score -= entry >> 1
    
    # Real impact: counting specific flag patterns
    flag_count = sum(1 for f in indicators if f & 0b1010)  # Only certain bit pattern matters
    
    # Decoy transformation chain
    transformed = [x * 1.5 for x in logs if x < 90]
    dummy_agg = sum(transformed) / len(transformed) if transformed else 0
    
    # Conditional expression with red herring variables
    offset = len(indicators) if flag_count > 3 else 0
    adjustment = math.sqrt(offset * 5) if offset else -1.5
    
    # Final computation that actually matters
    intermediate = base_score * 2
    correction = flag_count * 7
    final_diagnostic = intermediate + correction - 5
    
    # Dead code branch (never executed due to logic)
    if dummy_agg > 1000:
        fallback = encode_timestamp(logs)
        final_diagnostic += fallback
    
    return final_diagnostic

# Simulated sensor data (main input)
timing_data = [12, 15, 24, 33, 42, 51, 60, 72, 81, 90]
flags = [0b1010, 0b0101, 0b1010, 0b1111, 0b1010, 0b0000, 0b1010]

# Dead variables and irrelevant processing
checksum_valid = validate_checksum(timing_data)
outlier_free, dev_sum = filter_outliers(timing_data, limit=40)
phase_status, phase_energy = analyze_phase_shift([0.1, 0.8, 1.2, 0.9, 0.75, 1.3, 0.6])

# Key execution point
final_diagnostic = aggregate_metrics(timing_data, flags)

# Output result as required
print(f"Target result: {final_diagnostic}")