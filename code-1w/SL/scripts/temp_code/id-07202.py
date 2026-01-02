import math

# Simulated sensor array diagnostics with signal processing and noise filtering
def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 31, 88, 144, 201]
    gain_factor = 1.75
    adjusted = [r * gain_factor for r in raw_readings]
    return adjusted

def apply_noise_floor(signal_list, threshold=45.0):
    # Irrelevant smoothing operation (dead code path)
    smoothed = [s if s > threshold else threshold for s in signal_list]
    return smoothed

def generate_checksum(data):
    # Distractor function: used nowhere, decoy for bit manipulation focus
    checksum = 0
    for val in data:
        truncated = int(val) & 0xFF
        checksum ^= truncated
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF
    return checksum

def filter_anomalies(readings):
    filtered = []
    for r in readings:
        if r < 100 or r > 300:
            continue
        if int(r) & 1:  # Only keep even-magnitude signals
            r += 1.0
        filtered.append(r)
    return filtered

def calculate_entropy(values):
    # Misleading scientific computation - not used in final result
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 6)

def reconstruct_phase_signal(filtered):
    # Unused complex transformation (red herring)
    phase_shifted = []
    for i, val in enumerate(filtered):
        shifted = val * math.cos(math.pi * i / 4)
        phase_shifted.append(round(shifted, 3))
    return phase_shifted

def count_critical_peaks(signal):
    count = 0
    for s in signal:
        if s > 200:
            count += 1
    return count

def compute_baseline_stability(signal):
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    return round(mean_val - variance * 0.5, 3)

def extract_diagnostic_flags(stable_baseline):
    # Conditional expression usage (required feature)
    flag_str = "ERR" if stable_baseline < 120 else "OK"
    flag_code = 1 if "OK" in flag_str else 0
    return flag_code

def compress_signal_data(signal):
    # Dead-end data transformation
    hex_stream = ''.join([hex(int(x))[2:] for x in signal])
    return hex_stream.upper()

def analyze_readings(validated):
    peak_count = count_critical_peaks(validated)
    baseline = compute_baseline_stability(validated)
    flag = extract_diagnostic_flags(baseline)
    
    # Key calculation step
    score_component = peak_count * 1000
    stability_offset = int(baseline)
    
    # Final diagnostic derived from multiple logic paths
    result = score_component + stability_offset + flag
    return result

# Main execution sequence
sensor_output = collect_sensor_data()
noise_filtered = apply_noise_floor(sensor_output)
processed_signals = filter_anomalies(noise_filtered)

# Irrelevant intermediate usages (distractors)
current_entropy = calculate_entropy(processed_signals)
phase_data = reconstruct_phase_signal(processed_signals)
signal_checksum = generate_checksum([int(x) for x in processed_signals])
compressed_trace = compress_signal_data(processed_signals)

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Output requirement
print(f"Result: {final_diagnostic}")