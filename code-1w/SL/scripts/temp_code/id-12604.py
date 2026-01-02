import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 52, 43]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1010]

# Irrelevant transformation - red herring
shifted_temps = [t + 273.15 for t in temperature_readings]  # Kelvin conversion (unused)
log_humidity = [math.log(h) for h in humidity_readings if h > 0]  # Unused logarithmic scale

# Signal processing pipeline
def filter_outliers(data, threshold=1.5):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

# Decoy function with misleading name
def compute_thermal_index(temp_data):
    index = 0
    for t in temp_data:
        if t > 24:
            index += t * 1.2
        else:
            index += t * 0.8
    return index * 0.1  # Unused result

# Real signal processor with distractors embedded
def preprocess_signal(raw_data):
    cleaned = filter_outliers(raw_data)
    normalized = [(x - min(cleaned)) / (max(cleaned) - min(cleaned)) for x in cleaned]
    
    # Bit manipulation red herring
    bit_encoded = 0
    for i, val in enumerate(normalized):
        bit_encoded ^= int(val * 100) << (i % 6)  # Complex but unused encoding
    
    # Actual relevant transformation
    avg_normalized = sum(normalized) / len(normalized)
    return normalized, avg_normalized

# Multiple assignments and set operations (required feature)
valid_ranges = {
    'temp': (22.0, 26.0),
    'humidity': (40, 55),
    'pressure': (1010, 1020)
}

exceeded_thresholds = set()
stable_metrics = set(['baseline'])
stable_metrics.remove('baseline')  # Initialize empty

for reading in temperature_readings:
    if reading < valid_ranges['temp'][0] or reading > valid_ranges['temp'][1]:
        exceeded_thresholds.add('temperature')
    else:
        stable_metrics.add('temperature')

for h in humidity_readings:
    if h < valid_ranges['humidity'][0] or h > valid_ranges['humidity'][1]:
        exceeded_thresholds.add('humidity')
    else:
        stable_metrics.add('humidity')

# Unused complex data structure
history_buffer = [
    {'seq': i, 'data': [temperature_readings[i], humidity_readings[i]], 'flag': False}
    for i in range(len(temperature_readings))
]

# Signal correlation attempt (distractor)
correlation_score = 0
for i in range(min(len(temperature_readings), len(humidity_readings))):
    temp_anomaly = abs(temperature_readings[i] - 24.0)
    hum_anomaly = abs(humidity_readings[i] - 47)
    correlation_score += temp_anomaly * hum_anomaly

# Main processing chain
filtered_temps, norm_temp_avg = preprocess_signal(temperature_readings)
_, norm_hum_avg = preprocess_signal(humidity_readings)

# Tuple unpacking distraction
summary_stats = (len(filtered_temps), norm_temp_avg, max(filtered_temps))
filtered_count, avg_norm_temp, peak_norm = summary_stats

# Complex conditional with short-circuit logic
is_system_stable = (
    len(exceeded_thresholds) == 0 
    and 'pressure' in stable_metrics 
    and (norm_temp_avg > 0.3 or norm_hum_avg > 0.4)  # Always true
)

# Set operations: intersection as key step (required python feature)
expected_stable = {'temperature', 'humidity', 'pressure'}
actual_consistent = expected_stable - exceeded_thresholds
consistency_score = len(expected_stable & actual_consistent) * 100

# Secondary processing path - looks important but isn't
aggregated_diagnostics = []
for idx, pt in enumerate(filtered_temps):
    diagnostic_code = int(pt * 10) ^ idx  # XOR operation red herring
    aggregated_diagnostics.append(diagnostic_code)

# Key computation hidden among distractions
def analyze_readings(signal_avgs):
    raw_magnitude = signal_avgs * 1000
    phase_shift = math.sin(math.pi * 0.25)
    adjusted = raw_magnitude * phase_shift
    
    # Final deterministic calculation
    checksum = 0
    for i in range(1, 6):
        checksum += (adjusted // i) % 10
    
    return int(adjusted) + checksum

# Unused recursive red herring
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def process_signals():
    temp_signal = preprocess_signal(temperature_readings)[1]
    hum_signal = preprocess_signal(humidity_readings)[1]
    
    composite = (temp_signal * 0.6) + (hum_signal * 0.4)
    
    # Looks critical but not used in final answer
    decoy_final = fibonacci(8) + len(aggregated_diagnostics)
    
    return composite

# Critical execution point
processed_signals = process_signals()
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")