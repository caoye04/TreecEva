def analyze_readings(raw_data, threshold=0.75):
    """Process sensor readings and filter anomalies (distractor function)."""
    filtered = [x for x in raw_data if x > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

# Irrelevant sensor simulation data
temperature_readings = [0.62, 0.81, 0.93, 0.45, 0.77, 0.88, 0.91]
humidity_readings = [0.33, 0.41, 0.52, 0.68, 0.71, 0.67]
pressure_readings = [1.02, 0.99, 1.05, 0.97, 1.01]

# Decoy processing
avg_temp = analyze_readings(temperature_readings)
avg_humidity = analyze_readings(humidity_readings, 0.5)

# Unused transformation functions (dead code path)
def encrypt_sequence(seq):
    return [((x * 257) % 1009) for x in seq]

def decode_payload(token):
    return sum([ord(c) for c in str(token)]) % 100

# Core system: Signal calibration engine
def generate_calibration(baseline, length):
    sequence = []
    value = baseline
    for i in range(length):
        if i % 3 == 0:
            value = (value * 1.1 + 0.5) % 100
        elif i % 5 == 0:
            value = (value * 0.9 - 0.3) % 100
        else:
            value = (value + 1.7) % 100
        sequence.append(round(value, 3))
    return sequence

def validate_checksum(data):
    """Checksum validation (used in main logic)."""
    total = sum(data)
    return int(total * 100) % 7

def shift_pattern(sequence, offset):
    """Apply circular shift based on offset."""
    n = len(sequence)
    if n == 0:
        return sequence
    offset = offset % n
    return sequence[offset:] + sequence[:offset]

def compute_entropy(values):
    """Calculate approximate entropy (distractor metric)."""
    import math
    counts = {}
    for v in values:
        key = int(v)
        counts[key] = counts.get(key, 0) + 1
    entropy = 0.0
    for count in counts.values():
        prob = count / len(values)
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return round(entropy, 4)

# Real data initialization
baseline_offset = 13

# Generate signal calibration sequence
raw_calibration = generate_calibration(baseline_offset, 12)

# Apply bit manipulation mask based on checksum
checksum = validate_checksum(raw_calibration)
bit_mask = (checksum << 2) ^ 5
masked_values = [int(x) ^ bit_mask for x in raw_calibration]

# String-based flag encoding (uses string method)
status_flag = "CALIBRATED_0x{:02X}".format(checksum)
flag_length = len(status_flag)
flag_sum = sum([ord(ch) for ch in status_flag if ch.isdigit()])

# Shift based on flag characteristics
shift_amount = flag_length % 5 + (flag_sum % 3)
adjusted_sequence = shift_pattern(masked_values, shift_amount)

# Secondary filtering based on entropy threshold (distractor logic)
entropy_value = compute_entropy(adjusted_sequence)
if entropy_value > 3.0:
    adjusted_sequence = [x for x in adjusted_sequence if x % 2 == 1]  # Keep odds only

# Final transformation chain
calibration_sequence = []
for val in adjusted_sequence:
    temp = val
    if temp > 50:
        temp = temp // 2
    elif temp < 10:
        temp = temp * 3 + 1
    calibration_sequence.append(temp)

# Key computation step
final_diagnostic = process_metrics(calibration_sequence, baseline_offset)

# Helper used in final step
def process_metrics(seq, base):
    total = 0
    multiplier = base % 8 + 1
    for i, num in enumerate(seq):
        if i % 2 == 0:
            total += num * multiplier
        else:
            total -= num // 2
    # Inject string-derived offset
    tag = "DIAG_{}".format(base)
    adjustment = len(tag.replace("_", ""))  # Uses string method
    return total + adjustment

# Print result as required
Result: {final_diagnostic}