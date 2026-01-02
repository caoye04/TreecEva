import math

# Simulated sensor array data with noise and redundant fields
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 47, 50, 44, 52, 48, 46, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant signal processing (distractor)
def apply_fourier_smoothing(data):
    smoothed = []
    for i in range(len(data)):
        val = sum(data[max(0, i-1):min(len(data), i+2)]) / 3
        smoothed.append(val * 0.98)
    return smoothed

# Unused transformation chain (dead code path)
def legacy_normalization(arr):
    min_val, max_val = min(arr), max(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Misleading intermediate metric (red herring)
avg_temp = sum(temperature_readings) / len(temperature_readings)
adjusted_avg = avg_temp * 1.02  # fake calibration

# Real preprocessing pipeline
def clean_sensor_data(raw_temps):
    filtered = [t for t in raw_temps if 20 <= t <= 30]  # remove outliers
    return list(map(lambda x: round(x, 1), filtered))

# Bit manipulation decoy (irrelevant to final result)
def encode_timestamp(ts):
    encoded = 0
    for i, digit in enumerate(str(ts)):
        encoded |= int(digit) << (i * 3)
    return encoded ^ 0xAA

# Complex but ultimately unused diagnostic (distractor)
class RedundantAnalyzer:
    def __init__(self, data):
        self.data = data
        self.checksum = sum([x**2 % 17 for x in data])
    
    def get_stability_index(self):
        diffs = [abs(self.data[i] - self.data[i-1]) for i in range(1, len(self.data))]
        return round(sum(diffs) / len(diffs), 3)

analyzer = RedundantAnalyzer(temperature_readings)
stability_metric = analyzer.get_stability_index()  # never used

# Actual relevant logic starts here
cleaned_temps = clean_sensor_data(temperature_readings)

# Simulate data windowing
def create_sliding_windows(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    return windows

# Apply windowing
temp_windows = create_sliding_windows(cleaned_temps)

# Compute rolling metrics
rolling_means = [sum(window)/len(window) for window in temp_windows]
extremes = {'min': min(rolling_means), 'max': max(rolling_means)}

# Hidden key computation: harmonic mean of extremes
harmonic_extreme = 2 * extremes['min'] * extremes['max'] / (extremes['min'] + extremes['max'])

# Diagnostic flags with string-based encoding (relevant)
diagnostic_flags = {
    'A': 'CALIBRATION_OK',
    'B': 'SENSOR_STABLE',
    'C': 'ENV_NORMAL'
}

flag_values = list(diagnostic_flags.values())
status_summary = ''.join([f[0] for f in flag_values])  # 'CSE'

# Processing chain involving dictionary and recursion (key concept)
def recursive_variance(data_list, depth=0):
    if depth >= 2 or len(data_list) < 2:
        return round(abs(max(data_list) - min(data_list)), 2)
    mean_val = sum(data_list) / len(data_list)
    squared_diffs = [(x - mean_val)**2 for x in data_list]
    variance = sum(squared_diffs) / len(squared_diffs)
    return recursive_variance([math.sqrt(v) for v in squared_diffs], depth + 1)

# Trigger recursive processing
variance_diagnostic = recursive_variance(rolling_means)

# Final aggregation function combining multiple concepts
def aggregate_metrics(chain, flags_dict):
    base = harmonic_extreme
    adjustment = len(flags_dict) * 0.25
    
    # String-based switch using flag initials
    code_map = {ch: idx + 1 for idx, ch in enumerate(status_summary)}
    multiplier = sum(code_map.values())  # 1+2+3 = 6
    
    # Bitwise twist (actually used)
    bit_factor = (len(temp_windows) << 1) & 7  # (6 << 1) & 7 = 12 & 7 = 4
    
    result = base + adjustment
    result *= multiplier
    result += bit_factor
    
    # One final check
    if int(result) & 1:  # if odd
        result = math.ceil(result)
    else:
        result = math.floor(result)
    
    return result

# Execution point of interest
final_diagnostic = aggregate_metrics(temp_windows, diagnostic_flags)
print(f"Target result: {final_diagnostic}")