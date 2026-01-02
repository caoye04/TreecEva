import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9]
humidity_readings = [45, 52, 61, 43, 55, 67, 59, 50]
co2_levels = [410, 415, 420, 405, 430, 445, 435, 425]

# Irrelevant baseline constants for other sensor types (distractor)
base_pressure = 1013.25
pressure_trend_threshold = 0.5

# Distractor: unused function simulating pressure drift (dead code path)
def calculate_pressure_drift(values):
    return sum(abs(values[i] - values[i-1]) for i in range(1, len(values)))

# Preprocessing: normalize readings to z-scores (relevant)
def normalize_data(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean) / std_dev for x in data]

# Distractor: auxiliary function not used in final computation
def smooth_signal(data, factor=0.3):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(factor * data[i] + (1 - factor) * smoothed[-1])
    return smoothed

# Signal categorization based on thresholds (relevant)
def categorize_signal(value):
    if value > 1.0:
        return 'HIGH'
    elif value < -1.0:
        return 'LOW'
    else:
        return 'NORMAL'

# Irrelevant string-based status mapping (partial red herring)
status_map = {
    'HIGH': 'Alert',
    'LOW': 'Warning',
    'NORMAL': 'Stable'
}

# Another distractor: complex string transformation not used later
def generate_status_report(categories):
    counts = {cat: categories.count(cat) for cat in set(categories)}
    report_lines = []
    for cat, cnt in counts.items():
        status_label = status_map[cat]
        line = f"{status_label}: {cnt} occurrence(s)"
        report_lines.append(line.upper().replace(' ', '_'))
    return '\n'.join(report_lines)

# Process all sensor streams into unified signal strength (relevant)
processed_signals = []
for temp, hum, co2 in zip(temperature_readings, humidity_readings, co2_levels):
    # Composite index combining normalized contributions
    norm_temp = (temp - 22.0) / 5.0  # Simplified normalization
    norm_hum = (hum - 50) / 20.0
    norm_co2 = (co2 - 400) / 50.0
    
    # Signal strength uses only temperature and CO2 (humidity is decoy)
    signal_strength = norm_temp * 0.6 + norm_co2 * 0.4
    processed_signals.append(round(signal_strength, 3))

# Distractor: list comprehension creating unused diagnostic trace
event_triggers = [s for s in processed_signals if abs(s) > 1.2]
signal_labels = [categorize_signal(s) for s in processed_signals]

# Unused transformation chain with string methods (heavily distracting)
raw_trace = ','.join(f'{s:.3f}' for s in processed_signals)
encoded_trace = raw_trace.replace('.', 'p').split(',')
filtered_segments = [seg for seg in encoded_trace if 'p' in seg and not seg.startswith('p')]
decoded_count = len([seg.replace('p', '.') for seg in filtered_segments])

# Core analysis function: count significant deviations above threshold (relevant)
def analyze_readings(signals):
    threshold = 0.85
    count_above = 0
    cumulative_shift = 0.0
    
    for sig in signals:
        if sig > threshold:
            count_above += 1
            cumulative_shift += sig
        # Early return red herring: commented out logic
        # if count_above > 3:
        #     return -999  # fake emergency override
    
    # Final result depends on both count and average shift
    if count_above == 0:
        return 0.0
    avg_shift = cumulative_shift / count_above
    return count_above * 100 + round(avg_shift, 3)

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output the target result
print(f"Target result: {final_diagnostic}")