from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8, 24.2, 26.1, 23.5, 24.8, 25.5]
humidity_readings = [45, 47, 50, 52, 46, 55, 58, 51, 49, 44]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1011, 1017, 1019, 1020]

# Irrelevant auxiliary data (distractor)
legacy_sensor_ids = ['LGS001', 'LGS002', 'LGS003']
calibration_offsets = {'temp': 0.3, 'hum': -2, 'pres': 1}
metadata_log = defaultdict(lambda: 'N/A')
for sid in legacy_sensor_ids:
    metadata_log[sid] = 'deprecated'

# Misleading intermediate transformations (red herring)
adjusted_temps = [t + calibration_offsets['temp'] for t in temperature_readings]
scaled_humidity = [h * 1.05 for h in humidity_readings]
filtered_pressure = [p for p in pressure_readings if p > 1014]

# Decoy function - looks important but unused in final path
def analyze_trend(data, window=3):
    trends = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        trend = 'up' if data[i+window-1] > data[i] else 'down'
        trends.append((window_avg, trend))
    return trends

# Unused recursive distraction
def binary_entropy(n):
    if n <= 1:
        return 0
    return n * math.log(n, 2) + binary_entropy(n - 1)

# Real processing begins here — core logic buried in noise
effective_temps = [t for t in temperature_readings if 23.0 <= t <= 25.5]
valid_pairs = [(t, h) for t, h in zip(effective_temps, humidity_readings[:len(effective_temps)])]

# Compute composite index using logical conditions and arithmetic
composite_index = 0
for temp, hum in valid_pairs:
    if temp > 24.0 and hum < 50:
        composite_index += temp * (50 - hum) / 10.0
    elif temp <= 24.0 and hum >= 50:
        composite_index -= hum / (temp + 1)
    else:
        composite_index += (temp + hum) / 20.0

# Destructuring assignment (real use)
primary_temp, secondary_temp = effective_temps[0], effective_temps[-1]

# Bit manipulation decoy (irrelevant)
status_flag = 0b10101010
mask = 0b11110000
masked_status = status_flag & mask
inverted = ~masked_status & 0xFF

# Another red herring: frequency counting of unimportant values
humidity_counter = Counter(humidity_readings)
dominant_humidity = humidity_counter.most_common(1)[0][0]

# Core calculation hidden among distractions
def compute_aggregate(readings, threshold, boost_factor=1.5):
    count = len(readings)
    base = sum(readings) / count
    outliers = [r for r in readings if r > base + 1.5]
    adjustment = len(outliers) * boost_factor
    
    # Critical nested logic with multiple reasoning steps
    if base > threshold:
        if adjustment > 2:
            result = base * 1.2 - adjustment
        else:
            result = base * 1.1
    else:
        if count % 2 == 0:
            result = base + adjustment * 0.8
        else:
            result = max(readings) - min(readings) + base * 0.9
    
    # Final twist: apply correction only if certain bitwise condition met (never true here)
    flag = 0b1000
    if (count & flag) and False:  # Dead condition
        result = round(result, 1)
    return result

# Fake usage to mislead
_ = compute_aggregate(pressure_readings, 1015)
_ = compute_aggregate(scaled_humidity, 50)

# ACTUAL critical call
final_score = compute_aggregate(effective_temps, 24.0, boost_factor=1.5)

# Output requirement
print(f"Target result: {final_score}")