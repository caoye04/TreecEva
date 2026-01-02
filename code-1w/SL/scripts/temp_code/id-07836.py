import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw = [i * 1.5 for i in range(30) if i % 3 != 0]
    offset = sum([x for x in raw if x > 10]) / len(raw)
    scaled = [x + offset for x in raw]
    return scaled

def filter_noise(data, level=0.8):
    # Irrelevant smoothing function (not used in final path)
    smoothed = []
    for i in range(len(data)):
        weight = level if i % 2 == 0 else (1 - level)
        smoothed.append(data[i] * weight)
    return smoothed

def transform_frequency(signal):
    # Apply dummy frequency shift (distractor)
    shifted = [(math.sin(x / 3) * 100) for x in signal]
    normalized = [abs(s) % 25 for s in shifted]
    return normalized

def generate_checksum(sequence):
    # Unused cryptographic-style checksum (dead code path)
    chk = 0
    for val in sequence:
        chk ^= int(val) & 255
        chk = (chk << 1) | (chk >> 7)
    return chk & 0xFF

def encode_features(values):
    # Encodes values into buckets (red herring)
    bins = {i: 0 for i in range(5)}
    for v in values:
        bin_key = min(int(v // 5), 4)
        bins[bin_key] += 1
    encoded = ''.join([str(bins[k]) for k in sorted(bins)])
    return encoded

def decode_signature(token):
    # Obfuscated parsing (unused)
    decoded = []
    for c in token:
        if c.isdigit():
            decoded.append(int(c) ** 2)
    return decoded

def validate_integrity(trace, sig):
    # Complex validation not actually affecting result
    if len(trace) < 20:
        return False
    temp = [t * 1.1 for t in trace[:10]]
    check = sum(temp) % 17
    return check == len(sig) % 17

def preprocess_signal(raw_readings):
    # Main preprocessing — only this matters
    clipped = [min(max(r, 0), 40) for r in raw_readings]
    adjusted = [c * 1.2 for c in clipped]
    return adjusted

def build_threshold_map(config_code):
    # Builds actual threshold map used in analysis
    base = {'low': 12.0, 'mid': 24.0, 'high': 36.0}
    factors = {'A': 0.9, 'B': 1.0, 'C': 1.1}
    mode = config_code[0]
    factor = factors.get(mode, 1.0)
    return {k: v * factor for k, v in base.items()}

def analyze_signal(data, thresholds):
    # Core logic: count how many points exceed each tier
    counts = {'low': 0, 'mid': 0, 'high': 0}
    for val in data:
        if val > thresholds['high']:
            counts['high'] += 1
        elif val > thresholds['mid']:
            counts['mid'] += 1
        elif val > thresholds['low']:
            counts['low'] += 1
    # Final diagnostic is weighted sum
    diagnostic_score = (
        counts['low'] * 1 +
        counts['mid'] * 3 +
        counts['high'] * 9
    )
    return diagnostic_score

# --- Execution Workflow ---
raw_sensor_data = collect_samples()

# Distractor: unused noise filtering
smoothed_data = filter_noise(raw_sensor_data, level=0.6)

# Distractor: frequency transformation (not used)
freq_domain = transform_frequency(raw_sensor_data)

# Real processing path begins
processed_data = preprocess_signal(raw_sensor_data)

# Generate unused feature encoding
encoded_pattern = encode_features(freq_domain)

# Build signature (never validated due to dead condition)
config_sig = encode_features([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Create threshold map using configuration
threshold_map = build_threshold_map("B")

# Critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Distractor: integrity check skipped
#if validate_integrity(processed_data, config_sig):
#    final_diagnostic *= 1.1

print(f"Result: {final_diagnostic}")