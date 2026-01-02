import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8]
humidity_readings = [55.2, 57.8, 53.1, 60.4, 62.0, 59.7, 56.3]
pressure_readings = [1013, 1011, 1009, 1007, 1008, 1010, 1012]

# Irrelevant auxiliary mappings (distractor)
legacy_code_mapping = {'A': 65, 'B': 66, 'Z': 90}
ascii_shift = lambda x: x + 10 if x < 70 else x - 5

# Signal processing pipeline
scaling_factor = 1.05
gain_adjustment = lambda val: val * scaling_factor

# Apply gain to temperature (relevant)
adjusted_temps = list(map(gain_adjustment, temperature_readings))

# Noise filtering using moving average (relevant)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

filtered_temps = smooth_signal(adjusted_temps)

# Compute dew point (irrelevant calculation - distractor)
def compute_dew_point(temp, hum):
    a, b = 17.27, 237.7
    alpha = ((a * temp) / (b + temp)) + math.log(hum / 100.0)
    return (b * alpha) / (a - alpha)

dew_points = [round(compute_dew_point(t, h), 2) for t, h in zip(temperature_readings, humidity_readings)]

# Dummy state machine for legacy system emulation (dead path)
class LegacyProcessor:
    def __init__(self):
        self.mode = 'IDLE'
    def activate(self):
        self.mode = 'ACTIVE'
    def process(self, data):
        return [x * 0.9 for x in data]  # Unused

# Unused instance (distractor)
legacy_proc = LegacyProcessor()
legacy_output = legacy_proc.process(pressure_readings)

# Frequency domain transformation attempt (misleading intermediate)
def spectral_weight(signal):
    weighted = 0
    for i, x in enumerate(signal):
        weighted += x * math.sin(i * math.pi / 4)
    return round(weighted, 3)

spectral_score = spectral_weight(filtered_temps)  # Computed but not used

# Core diagnostic logic (critical path)
baseline_ref = sum(filtered_temps[:3]) / 3
variance = sum((x - baseline_ref) ** 2 for x in filtered_temps) / len(filtered_temps)
amplitude_mod = max(filtered_temps) - min(filtered_temps)

event_threshold = 1.8
fluctuation_index = amplitude_mod / (variance + 1e-8)

alert_mode = False
if fluctuation_index > event_threshold:
    alert_mode = True
elif spectral_score > 50:  # Misleading condition (never triggers)
    alert_mode = 'DEGRADED'  # Invalid type assignment - won't affect logic

# Data fusion and encoding (red herring)
encoded_diagnostics = ''
for i, temp in enumerate(filtered_temps):
    code_point = int(temp) ^ (i % 16)
    encoded_diagnostics += chr(ascii_shift(code_point))  # Complex but irrelevant

# Final analysis function (key computation)
def analyze_readings(readings):
    sorted_vals = sorted(readings)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    outlier_boundary = q3 + 1.5 * iqr
    
    # Count significant deviations
    deviant_count = sum(1 for x in readings if x > outlier_boundary)
    
    # Apply correction factor based on IQR and length
    correction = math.log(len(readings) + 1, 2)
    return int((iqr * 100) + deviant_count - correction)

# Process signals (wrapper abstraction - adds complexity)
processed_signals = [
    round(x, 2) for x in filtered_temps
    if x > baseline_ref * 0.95  # Filter near baseline (redundant but valid)
]

# Key statement
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")