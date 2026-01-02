def parse_sensor_stream(raw_stream):
    segments = raw_stream.split('|')
    parsed = []
    for seg in segments:
        if 'ERR' in seg:
            continue
        clean_seg = seg.strip().replace('X', '').zfill(4)
        if clean_seg.isdigit():
            parsed.append(int(clean_seg))
    return parsed


def validate_checksum(data_chunk):
    if len(data_chunk) < 2:
        return False
    checksum = sum(data_chunk[:-1]) % 100
    return checksum == data_chunk[-1]


def transform_coordinates(x, y, mode='cartesian'):
    import math
    if mode == 'polar':
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return round(r, 3), round(theta, 3)
    elif mode == 'spherical':
        # unused path — red herring
        rho = math.sqrt(x**2 + y**2 + 1)
        return rho
    return x * 2, y * 2  # default scaling


def decode_payload(payload_str):
    # Irrelevant transformation — distractor
    decoded = ''
    for c in payload_str:
        if c.isalpha():
            decoded += chr((ord(c) - ord('A') + 3) % 26 + ord('A'))
        else:
            decoded += c
    return decoded.lower()


def filter_anomalies(readings, sensitivity=0.85):
    baseline = sum(readings) / len(readings)
    filtered = []
    anomalies = []
    for val in readings:
        if abs(val - baseline) > baseline * (1 - sensitivity):
            anomalies.append(val)
        else:
            filtered.append(val)
    # Misleading intermediate: not used later
    anomaly_ratio = len(anomalies) / len(readings) if readings else 0
    return filtered


def recursive_sum(seq, index=0):
    if index >= len(seq):
        return 0
    return seq[index] + recursive_sum(seq, index + 1)


def generate_signature(elements):
    # Dead code path — never called
    sig = 1
    for e in elements:
        sig *= (e % 7 + 1)
    return sig % 97


def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def analyze_readings(data_list, config_map):
    temp_scale = config_map['temp_scale']
    pressure_adj = config_map['pressure_factor']
    offset = config_map.get('offset', 0)

    temps = [x for x in data_list if 30 <= x <= 220]
    pressures = [x for x in data_list if 500 <= x <= 999]

    # Distractor variables
    avg_temp = sum(temps) / len(temps) if temps else 0
    max_pressure = max(pressures) if pressures else 0
    pressure_sum = recursive_sum(pressures)

    adjusted_temps = [int(t * temp_scale + offset) for t in temps]
    corrected_pressures = [int(p * pressure_adj) for p in pressures]

    # Key logic chain
    temp_flag = any(t > 180 for t in adjusted_temps)
    press_stable = all(p < 850 for p in corrected_pressures)

    # Secondary filtering — only some affect result
    valid_pairs = 0
    for t in adjusted_temps:
        for p in corrected_pressures:
            if (t + p) % 13 == 0:
                valid_pairs += 1

    # Critical decision tree with nesting depth 4
    if len(adjusted_temps) > 3:
        if temp_flag:
            if press_stable:
                if valid_pairs >= 2:
                    score = 85
                else:
                    score = 60
            else:
                score = 45
        else:
            if len(corrected_pressures) == 0:
                score = 20
            else:
                score = 70
    else:
        score = 30

    # Final computation using string method as per requirement
    status_code = f"SYS-{score}".zfill(8)
    digit_sum = sum(int(d) for d in status_code if d.isdigit())

    final_diagnostic = score * 2 - digit_sum

    return final_diagnostic

# Main execution flow
raw_data = "X120|X095|X130|X110|X105|X140|X135|X800|X720|X510|X990|XERR|X160"
processed_raw = parse_sensor_stream(raw_data)

# Validate and filter
if validate_checksum([120, 95, 130, 110, 105, 140, 135, 800, 720, 510, 990]):
    stage_one = processed_raw
else:
    stage_one = processed_raw[:10]

filtered_stage = filter_anomalies(stage_one, sensitivity=0.88)

# Coordinate distraction — irrelevant to final result
coord_x, coord_y = transform_coordinates(12, 5, mode='cartesian')
decoded_msg = decode_payload("KHOORZRUOG")  # "HELLOWORLD" + 3 shift

# Build configuration map
threshold_map = {
    'temp_scale': 1.1,
    'pressure_factor': 0.93,
    'offset': -5
}

# Execute critical statement
final_diagnostic = analyze_readings(filtered_stage, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")