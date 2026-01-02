import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_readings = [
        {'temp': 23.5, 'humidity': 65, 'co2': 410},
        {'temp': 24.1, 'humidity': 63, 'co2': 415},
        {'temp': 22.8, 'humidity': 67, 'co2': 405},
        {'temp': 25.3, 'humidity': 60, 'co2': 425},
        {'temp': 21.9, 'humidity': 70, 'co2': 400}
    ]
    return raw_readings

# Irrelevant preprocessing: normalize humidity to z-score (not used in final)
def z_normalize(data_list, key):
    values = [d[key] for d in data_list]
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val)**2 for x in values) / len(values))**0.5
    return [(x - mean_val) / std_dev for x in values] if std_dev != 0 else [0]*len(values)

# Real processing: filter high CO2 and compute temp-humidity index
def process_readings(readings):
    filtered = [r for r in readings if r['co2'] > 408]
    # Compute heat index approximation
    indices = []
    for r in filtered:
        t, h = r['temp'], r['humidity']
        hi = t + 0.5 * (h - 12) + ((t*t - t*68 - 13*h + 2890) * 0.1)
        indices.append(hi)
    return indices

# Misleading function: analyzes outliers but not called
def detect_outliers(data, threshold=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [x for x in data if x < lower or x > upper]

# Core analysis using set operations and lambda
valid_ranges = set(range(35, 85))  # valid humidity percentages

lambda_transform = lambda x: round(x ** 1.1 - 10, 2)

# Secondary processing with unused intermediate
extended_diagnostics = []
for i in range(3):
    temp_set = {10, 20, 30, 40, 50}
    temp_set.add(i * 10)
    extended_diagnostics.append(len(temp_set))  # Dead-end computation

# Unused recursive countdown (red herring)
def countdown(n):
    return 1 if n <= 0 else n - countdown(n-2)

unused_result = countdown(10)

# Actual signal extraction via bit manipulation masking
def extract_signal(intensity):
    mask = 0b1111
    shifted = intensity << 2
    return shifted & mask

# Real pipeline starts here
sensor_data = collect_sensor_data()

# Distractor: z-normalize humidity (not used)
z_humidity = z_normalize(sensor_data, 'humidity')

# Real: process temperature-humidity indices
processed_indices = process_readings(sensor_data)

# Transform using lambda (actually used)
transformed_signals = [lambda_transform(idx) for idx in processed_indices]

# Apply bit extraction on transformed values
bit_extracted = [extract_signal(int(round(ts))) for ts in transformed_signals]

# Aggregate using set logic
signal_set = set(bit_extracted)
baseline_set = {1, 2, 4, 8, 16}
common_features = signal_set & baseline_set  # intersection
unique_only = signal_set ^ baseline_set     # symmetric difference

# Final diagnostic calculation
def analyze_readings(signal_list):
    base_score = sum(signal_list)
    adjustment = len(common_features) * 1.5
    penalty = len(unique_only) * 0.7
    # Final formula
    result = base_score + adjustment - penalty
    return round(result, 6)

# Key execution point
final_diagnostic = analyze_readings(processed_indices)

print(f"Target result: {final_diagnostic}")