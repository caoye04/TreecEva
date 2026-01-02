import math

# Simulated sensor array data (irrelevant preprocessing)
sensor_raw = [0.88, 0.72, 0.54, 0.91, 0.33, 0.67, 0.45, 0.76]
normalized = [round((x - min(sensor_raw)) / (max(sensor_raw) - min(sensor_raw)), 3) for x in sensor_raw]

# Irrelevant signal smoothing (dead path)
def smooth_signal(data, passes=2):
    temp = data[:]
    for _ in range(passes):
        temp = [(temp[i-1] + temp[i] + temp[(i+1) % len(temp)]) / 3 for i in range(len(temp))]
    return temp

# Unused noise filter
class NoiseFilter:
    def __init__(self, cutoff=0.1):
        self.cutoff = cutoff
    def apply(self, x):
        return x if abs(x) > self.cutoff else 0.0

# Core diagnostic logic (obfuscated with distractors)
raw_diagnostics = {
    'voltage_peaks': [18, 22, 15, 30, 12],
    'phase_shifts': [0.4, 0.7, 0.2, 0.9, 0.5],
    'checksum_log': [0xAA1F, 0xB3E4, 0xCC22, 0xD10F, 0xE55A]
}

# Misleading transformation chain
encoded = []
for i, val in enumerate(raw_diagnostics['voltage_peaks']):
    phase = raw_diagnostics['phase_shifts'][i]
    chk = raw_diagnostics['checksum_log'][i]
    # Complex but irrelevant encoding
    enc_val = (val * 100) + int(phase * 100)
    enc_val ^= chk & 0xFF
    enc_val = ((enc_val >> 4) | (enc_val << 4)) & 0xFFFF
    encoded.append(enc_val)

# Decoy analysis function that's never called
def legacy_diagnose(seq):
    total = 0
    for x in seq:
        if x % 3 == 0:
            total += x // 3
        elif x % 5 == 0:
            total += x // 5
    return total * 0.77

# Real processing begins here (buried among distractions)
processed_data = []
for i in range(5):
    v = raw_diagnostics['voltage_peaks'][i]
    p = raw_diagnostics['phase_shifts'][i]
    score = v * (1 + p) ** 2
    processed_data.append(round(score, 3))

# Threshold map with red herring entries
threshold_map = {
    'critical': 45.0,
    'warning': 30.0,
    'info': 15.0,
    'debug': 5.0,
    'unused_mode_x': 100.0,  # decoy
    'legacy_tune': 0.88        # decoy
}

# Conditional expression and actual core logic
status_flags = [
    'OK' if x >= threshold_map['warning'] else 'LOW' 
    for x in processed_data
]

# Distractor: fake aggregation
fake_agg = sum(encoded) % 1000

# Real analysis function
def analyze_signal(data, thresholds):
    base = 0
    for val in data:
        if val >= thresholds['critical']:
            base += 12
        elif val >= thresholds['warning']:
            base += 7
        elif val >= thresholds['info']:
            base += 3
        else:
            base += 1
    
    # Secondary adjustment based on pattern
    consecutive_warnings = 0
    max_consecutive = 0
    for flag in status_flags:
        if flag == 'LOW':
            consecutive_warnings += 1
        else:
            max_consecutive = max(max_consecutive, consecutive_warnings)
            consecutive_warnings = 0
    max_consecutive = max(max_consecutive, consecutive_warnings)
    
    # Final computation
    adjustment = 5 if max_consecutive >= 2 else 2
    result = base * adjustment
    
    # Apply bit manipulation as final touch (relevant)
    result = (result ^ 0xF) + (result & 0x7)
    return result

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")