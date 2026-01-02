from collections import defaultdict
import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.4, 25.1, 22.8, 26.5, 24.3, 27.0, 23.9, 25.6]
humidity_readings = [45, 52, 48, 60, 55, 62, 50, 58]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1009, 1016, 1011]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B3', 'C9', 'D1', 'E8', 'F2', 'G5', 'H6']
error_flags = [False, False, True, False, False, False, True, False]

def apply_calibration(data, factor=1.02):
    return [round(x * factor, 2) for x in data]

def filter_outliers(data, margin=2.0):
    mean = sum(data) / len(data)
    return [x for x in data if abs(x - mean) <= margin]

def compute_entropy(data):
    # Unused complex distractor function
    from math import log
    freq = defaultdict(int)
    for x in data:
        freq[round(x)] += 1
    total = len(data)
    return -sum((count/total) * log(count/total) for count in freq.values())

# Apply calibration to temperature (relevant)
calibrated_temps = apply_calibration(temperature_readings)

# Misleading transformation chain (partly dead code)
stabilized_humidity = [h - 5 if h > 55 else h for h in humidity_readings]
adjusted_pressure = [p + 3 for p in pressure_readings]  # Not used later

# Data fusion step
raw_combined = [(t, h) for t, h in zip(calibrated_temps, stabilized_humidity)]

# Decoy processing branch (never called)
def legacy_process(seq):
    return [s[::-1] for s in seq if s[0] in 'BCDFG']

# Real transformation path
def transform_sequence(pairs, offset=1.5):
    result = []
    for i, (t, h) in enumerate(pairs):
        # Complex but deterministic transformation
        val = (t * 1.1) + (h * 0.3) - (i * 0.2)
        if i % 3 == 0:
            val = math.sin(val / 10) * 100
        elif i % 4 == 0:
            val = abs(val - 50)
        result.append(round(val, 2))
    return result

def build_threshold_map(values):
    base = sum(values) / len(values)
    return {
        'low': base - 5,
        'optimal': base,
        'high': base + 7.5
    }

def evaluate_stability(index, value, thresholds):
    if value < thresholds['low']:
        return 1
    elif value > thresholds['high']:
        return -1
    else:
        return 0

# Lambda-based filtering (required feature)
adaptive_filter = lambda x: x > 24.0
filtered_indices = [i for i, t in enumerate(calibrated_temps) if adaptive_filter(t)]

# Slicing operation (required feature)
sliced_data = calibrated_temps[1:6:2]  # [25.5, 26.9, 27.5] approx

# Main data transformation
transformed_data = transform_sequence(raw_combined)

# Build dynamic threshold map
threshold_map = build_threshold_map(transformed_data)

# Secondary decoy structure (irrelevant)
stats_summary = {
    'avg_temp': round(sum(calibrated_temps)/len(calibrated_temps), 2),
    'max_humidity': max(stabilized_humidity),
    'pressure_trend': 'decreasing' if adjusted_pressure[-1] < adjusted_pressure[0] else 'increasing',
    'outlier_count': len(humidity_readings) - len(filter_outliers(stabilized_humidity))
}

# Core diagnostic processor
def process_readings(data_list, limits):
    accumulator = defaultdict(int)
    history = []
    
    for j, reading in enumerate(data_list):
        # Nested logic with multiple steps
        if j == 0:
            adjusted = reading + 1.5
        elif j % 2 == 0:
            adjusted = reading * 0.9
        else:
            adjusted = reading - 1.1
        
        # Multi-step classification
        category_score = 0
        if adjusted < limits['low']:
            category_score = -2
        elif adjusted > limits['high']:
            category_score = 3
        elif limits['optimal'] - 2 <= adjusted <= limits['optimal'] + 2:
            category_score = 5
        else:
            category_score = 1
        
        # Stateful accumulation
        accumulator['total'] += adjusted
        accumulator['score_sum'] += category_score
        history.append(evaluate_stability(j, adjusted, limits))
    
    # Final computation with interference from unused fields
    base_result = accumulator['total'] * 0.33
    penalty = sum(1 for h in history if h == -1) * 2.5
    bonus = len([h for h in history if h == 1]) * 1.7
    final_value = base_result + bonus - penalty + accumulator['score_sum'] * 0.4
    
    # Red herring operations
    temp_debug = [math.ceil(x) for x in data_list if x > 30]  # likely empty
    if len(temp_debug) > 3:
        final_value *= 0.9
    
    return round(final_value, 4)

# Execute main computation
final_diagnostic = process_readings(transformed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")