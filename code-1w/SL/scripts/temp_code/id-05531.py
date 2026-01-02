from itertools import compress, cycle
import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.9, 23.7, 22.4]
humidity_readings = [45, 48, 52, 44, 60, 58, 50, 46]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B3', 'C9', 'D1', 'E8']
error_flags = [False, False, True, False, False, False, True, False]

# Misleading intermediate transformation (dead path)
def legacy_compatibility_mode(data):
    return [hex(int(x)) for x in data if isinstance(x, (int, float)) and x > 0]

legacy_output = legacy_compatibility_mode(pressure_readings)  # Unused

# Data normalization function with red herring parameters
def normalize_sequence(seq, base=100.0, mode='linear'):
    if mode == 'log':
        return [math.log(x + 1) for x in seq]
    else:
        return [(x / base) * 10 for x in seq]  # Linear normalization

# Apply normalization (only temperature is meaningfully used later)
norm_temp = normalize_sequence(temperature_readings, base=25.0)
norm_humidity = normalize_sequence(humidity_readings, base=50.0, mode='log')
norm_pressure = normalize_sequence(pressure_readings, base=1000.0)

# Complex conditional processing using lambda and itertools
temp_alerts = list(map(lambda x: x > 24.0, temperature_readings))
valid_readings_mask = [not err for err in error_flags]

# Use of itertools.compress to filter valid data points (critical step)
filtered_temps = list(compress(temperature_readings, valid_readings_mask))
filtered_humidity = list(compress(humidity_readings, valid_readings_mask))

# Decoy aggregation functions
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

entropy_value = compute_entropy(filtered_humidity)  # Computed but unused

# Real processing begins: construct processed_data
def process_sensor_array(temp, hum, pres):
    trend = sum(1 for i in range(1, len(temp)) if temp[i] > temp[i-1])
    avg_temp = sum(temp) / len(temp)
    peak_hum = max(hum)
    stable_pressure = all(abs(pres[i] - pres[i-1]) < 10 for i in range(1, len(pres)))
    
    # Red herring calculation
    dummy_cycle = list(zip(temp, cycle(['X', 'Y', 'Z']), hum))
    
    return {
        'trend_index': trend,
        'average_temperature': avg_temp,
        'peak_humidity': peak_hum,
        'pressure_stable': stable_pressure,
        'size_hint': len(temp) * 2
    }

processed_data = process_sensor_array(filtered_temps, filtered_humidity, pressure_readings)

# Create misleading threshold variants
threshold_map = {
    'high_temp': 24.5,
    'low_humid': 47,
    'noise_floor': 0.5,  # Unused
    'complex_flag': True
}

# Another decoy: recursive function that isn't used
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

fib_sequence = [fibonacci(i) for i in range(8)]  # Computed but irrelevant

# Core analysis logic with conditional expressions and lambdas
def analyze_readings(data, thresholds):
    # Multi-step reasoning with branching logic
    base_score = data['trend_index'] * 10
    
    temp_factor = 5 if data['average_temperature'] > thresholds['high_temp'] else -3
    humid_risk = 8 if data['peak_humidity'] < thresholds['low_humid'] else 0
    stability_bonus = 12 if data['pressure_stable'] else -5
    
    # Complex conditional expression
    size_modifier = 2 if data['size_hint'] > 10 else (1 if data['size_hint'] == 10 else 0)
    
    # Critical calculation chain
    intermediate = base_score + temp_factor
    intermediate = intermediate + humid_risk if thresholds['complex_flag'] else intermediate
    intermediate += stability_bonus
    final_score = intermediate * size_modifier
    
    # Dead code branch (misleading)
    if final_score < 0:
        fallback = sum([len(str(x)) for x in legacy_codes])
        final_score += fallback  # Never reached in this case
    
    # Final transformation
    diagnostic_code = int(math.ceil(final_score / 2.0)) * 3
    
    return diagnostic_code

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")