import itertools

# Sensor simulation and diagnostic analysis system
def collect_sensor_readings():
    # Simulated multi-sensor data (real values)
    raw_stream = [127, 255, 192, 144, 224, 168, 132, 240]
    return raw_stream

def apply_noise_filter(data):
    # Irrelevant transformation: converts to frequency domain (not used in final result)
    filtered = []
    for i in range(len(data)):
        filtered.append((data[i] ^ 0xAA) & 0xFF)  # Bit manipulation red herring
    return filtered

def extract_critical_signals(data):
    # Extract every 2nd element starting at index 1 (relevant)
    return [x for i, x in enumerate(data) if i % 2 == 1]

def compute_baseline_average(signals):
    # Used to calculate adjustment factor (relevant step)
    total = 0
    count = 0
    for val in signals:
        if val > 150:
            total += val
            count += 1
    return total // count if count else 0

def adjust_for_drift(signals, baseline):
    # Adjust signal values based on baseline (relevant)
    adjusted = []
    for val in signals:
        if val < baseline:
            adjusted.append(val + (baseline - val) // 2)
        else:
            adjusted.append(val - (val - baseline) // 4)
    return adjusted

def generate_checksum(data):
    # Distractor function: looks important but unused
    checksum = 0
    for val in data:
        checksum = (checksum * 13 + val) % 10007
    return checksum

def build_threshold_map(adjusted):
    # Create mapping of index -> dynamic threshold (relevant)
    tmap = {}
    for idx, val in enumerate(adjusted):
        tmap[idx] = val * 0.75 if idx % 3 == 0 else val * 0.85
    return tmap

def validate_signal_integrity(data):
    # Dead path: never called, misleading
    for d in data:
        if d < 0 or d > 255:
            return False
    return True

def dummy_transformation(seq):
    # Unused transformation function (red herring)
    return [((x << 2) & 0xFF) | (x >> 6) for x in seq]

def analyze_readings(data, thresholds):
    # Final diagnostic logic (key computation)
    score = 0
    for i, val in enumerate(data):
        if i in thresholds:
            if val >= thresholds[i]:
                score += (val - int(thresholds[i])) * 2
            else:
                score -= int(thresholds[i]) - val
    return score + len(thresholds)

# Main execution flow
sensor_data = collect_sensor_readings()

# Irrelevant processing branch (distractor)
fault_flags = []
temp_analysis = sensor_data[::2]
for reading in temp_analysis:
    if reading & 0x0F > 8:
        fault_flags.append(True)
    else:
        fault_flags.append(False)

# Real processing path begins
core_signals = extract_critical_signals(sensor_data)  # [255, 144, 168, 240]
baseline_avg = compute_baseline_average(core_signals)  # Only values > 150: 255, 168, 240 → avg = 217
adjusted_signals = adjust_for_drift(core_signals, baseline_avg)

# Another irrelevant transformation (misleading intermediate)
expanded = list(itertools.chain.from_iterable([[x, x//2] for x in adjusted_signals]))
trimmed = expanded[:len(expanded)//2]  # Looks meaningful but unused

threshold_map = build_threshold_map(adjusted_signals)

# Dummy call that computes something irrelevant
_ = generate_checksum(sensor_data)  # Computed but not used

# Key statement
final_diagnostic = analyze_readings(adjusted_signals, threshold_map)

print(f"Result: {final_diagnostic}")