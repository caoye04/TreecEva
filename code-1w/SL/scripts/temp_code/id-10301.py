import math

# Sensor calibration constants (some are red herrings)
CALIBRATION_A = 0.87
CALIBRATION_B = 1.03
CALIBRATION_C = 2.11  # Unused in actual logic
dummy_offset = 42  # Distractor

# Simulated environmental sensor readings
raw_readings = [127, 135, 120, 142, 130, 118, 138]

# Irrelevant signal processing function (dead code path)
def smooth_signal(data):
    return [d * 0.9 for d in data if d > 130]

# Data normalization using reference baseline
baseline = 125
normalized = [round((r - baseline) * CALIBRATION_A, 2) for r in raw_readings]

# Flag anomalous spikes (threshold-based)
anomalies = []
for i, val in enumerate(normalized):
    if abs(val) > 8:
        anomalies.append((i, val))

# Decoy statistical analysis (not used in final result)
mean_anomaly = sum([abs(x[1]) for x in anomalies]) / len(anomalies) if anomalies else 0
adjusted_mean = mean_anomaly * 1.5 if len(anomalies) > 2 else mean_anomaly * 0.7  # Unused

# Transform normalized values into diagnostic codes via bit manipulation
encoded_diagnostics = []
for n in normalized:
    # Convert to positive index: shift and scale
    temp_val = int(abs(n) * 10) + 100
    # Apply XOR mask with prime for obfuscation (relevant)
    masked = temp_val ^ 101
    # Bitwise rotation simulation
    rotated = ((masked << 3) & 0xFF) | ((masked >> 5) & 0xFF)
    encoded_diagnostics.append(rotated)

# Hash map to count frequency of encoded patterns
freq_map = {}
for code in encoded_diagnostics:
    freq_map[code] = freq_map.get(code, 0) + 1

# Extract high-frequency codes
frequent_codes = [c for c, f in freq_map.items() if f > 1]

# Process logs through filtering and transformation
processed_logs = []
for code in encoded_diagnostics:
    # Conditional expression used for dynamic thresholding
    threshold = 150 if code > 180 else 120
    if code >= threshold:
        processed_logs.append(code * CALIBRATION_B)
    elif code in frequent_codes:
        processed_logs.append(code + 10)
    else:
        processed_logs.append(int(code * 0.95))

# Secondary decoy structure: geometric progression check (unused)
geo_valid = True
if len(processed_logs) > 2:
    ratio = processed_logs[1] / processed_logs[0] if processed_logs[0] != 0 else 0
    for i in range(2, len(processed_logs)):
        if processed_logs[i] / processed_logs[i-1] != ratio:
            geo_valid = False

# Core diagnostic analyzer (recursive pattern)
def analyze_readings(data):
    if not data:
        return 0
    if len(data) == 1:
        return int(math.sin(math.radians(data[0])) * 100) + 50
    
    mid = len(data) // 2
    left = analyze_readings(data[:mid])
    right = analyze_readings(data[mid:])
    
    # Combine results with modular arithmetic twist
    combined = (left ** 2 + right) % 97
    return int(combined)

# Dummy global used to mislead
system_status = "STABLE"

# Key execution point
final_diagnostic = analyze_readings(processed_logs)

# Output the target result
print(f"Target result: {final_diagnostic}")