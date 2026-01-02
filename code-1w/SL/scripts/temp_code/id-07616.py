import math

# Simulated sensor data from industrial monitoring system
def fetch_sensor_data():
    raw_values = [127, 255, 192, 64, 31, 156, 88, 201]
    timestamps = [1623456000 + i*60 for i in range(len(raw_values))]
    return list(zip(timestamps, raw_values))

def decode_signal(value):
    # Bit manipulation to extract embedded status flags
    mode_flag = (value >> 6) & 0b11
    intensity = value & 0x3F
    checksum = (value >> 7) ^ (value & 0xF)
    parity = bin(value).count('1') % 2
    if parity != 0:
        intensity = intensity * 0.9
    return {'intensity': intensity, 'mode': mode_flag, 'valid': parity == 0}

def encrypt_log(data):
    # Irrelevant encryption function - dead end
    encrypted = ''
    for c in str(data):
        encrypted += chr((ord(c) + 3) % 127)
    return encrypted

def parse_metadata(log_entry):
    # Extract metadata (unused in final calculation)
    ts, val = log_entry
    day_of_year = (ts // 86400) % 365
    hour = (ts % 86400) // 3600
    season = ['spring', 'summer', 'fall', 'winter'][day_of_year // 91]
    shift = 'night' if hour < 6 or hour > 18 else 'day'
    return {'season': season, 'shift': shift, 'raw_ts': ts}

def filter_anomalies(decoded_list):
    # Remove invalid readings based on decode rules
    clean = []
    anomalies = []
    for item in decoded_list:
        if item['valid'] and item['intensity'] > 0:
            clean.append(item)
        else:
            anomalies.append(item)
    # Dead path: anomaly statistics not used later
    anomaly_rate = len(anomalies) / len(decoded_list) if decoded_list else 0
    avg_anomaly_intensity = sum(a['intensity'] for a in anomalies) / len(anomalies) if anomalies else 0
    return clean

def compute_envelope(signal_list):
    # Calculate RMS envelope of signal
    squares = [entry['intensity']**2 for entry in signal_list]
    mean_square = sum(squares) / len(squares) if squares else 0
    rms = math.sqrt(mean_square)
    peak = max(entry['intensity'] for entry in signal_list) if signal_list else 0
    crest_factor = peak / rms if rms else 0
    return {'rms': rms, 'crest_factor': crest_factor, 'peak': peak}

def apply_calibration(envelope):
    # Apply non-linear calibration curve
    raw_rms = envelope['rms']
    calibrated = 10 * math.log10(1 + raw_rms)  # dB-like scale
    threshold = 3.5 + 0.02 * raw_rms
    state = 'stable' if calibrated < threshold else 'critical'
    return {'calibrated_value': calibrated, 'state': state, 'margin': threshold - calibrated}

def generate_report(calibrated_data, envelope):
    # Complex reporting logic with unused fields
    report_id = hash('report_' + str(calibrated_data['calibrated_value'])) % 10000
    severity = 0
    if calibrated_data['state'] == 'critical':
        severity = 3
    elif envelope['crest_factor'] > 2.5:
        severity = 2
    else:
        severity = 1
    # Many irrelevant string operations
    status_str = f"System operating in {calibrated_data['state']} state."
    status_str = status_str.upper().replace(' ', '_').strip('.')
    status_str = status_str[::-1]  # Reverse string - unused
    return {
        'id': report_id,
        'status': status_str,
        'level': severity,
        'timestamp': '2023-07-15T10:30:00Z'
    }

def analyze_readings(processed):
    # Final diagnostic computation
    if not processed:
        return -1
    total_weight = 0
    weighted_sum = 0
    for entry in processed:
        weight = entry['intensity'] ** 0.5
        total_weight += weight
        weighted_sum += weight * entry['mode']
    average_mode = weighted_sum / total_weight if total_weight else 0
    
    # Secondary metric: count of high-intensity pulses
    high_pulses = sum(1 for e in processed if e['intensity'] > 40)
    pulse_ratio = high_pulses / len(processed)
    
    # Final formula combining multiple factors
    diagnostic_score = (average_mode * 100) + (pulse_ratio * 50)
    
    # Red herring: complex bit manipulation with fixed outcome
    temp = int(diagnostic_score)
    temp = (temp << 3) & 0xFF
    temp = (temp ^ 0b10101010) | (temp >> 4)
    temp = temp & 0x7F  # Mask to 7 bits
    
    # Actual answer derived here
    final_diagnostic = int(temp * 1.25)  # Deterministic transformation
    return final_diagnostic

# Main execution flow
data_packets = fetch_sensor_data()

decoded_signals = [decode_signal(val) for _, val in data_packets]

# Parse metadata (stored but not used later - distraction)
all_metadata = [parse_metadata(packet) for packet in data_packets]
metadata_summary = {m['season']: 0 for m in all_metadata}
for m in all_metadata:
    metadata_summary[m['season']] += 1

# Filter out invalid readings
filtered_signals = filter_anomalies(decoded_signals)

# Signal processing chain
signal_envelope = compute_envelope(filtered_signals)
calibrated_output = apply_calibration(signal_envelope)

# Generate report (called but not used - dead path)
unused_report = generate_report(calibrated_output, signal_envelope)

# Encrypt logs (never used - decoy operation)
encrypted_diagnostics = encrypt_log(filtered_signals)

# Critical processing step
processed_logs = filtered_signals  # Rename for semantic clarity

# Key statement: final analysis
final_diagnostic = analyze_readings(processed_logs)

print(f"Target result: {final_diagnostic}")