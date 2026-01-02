from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.5, 24.1, 24.1, 25.0, 23.5, 22.8, 26.3, 24.1, 25.0, 25.7]
humidity_readings = [45, 46, 48, 45, 50, 52, 46, 48, 49, 45]
pressure_readings = [1013, 1012, 1015, 1013, 1010, 1014, 1013, 1016, 1012, 1013]

# Irrelevant transformation - red herring
decoy_transform = [round((x - 32) * 5/9, 2) for x in temperature_readings]

# Misleading statistical summary
temp_mean = sum(temperature_readings) / len(temperature_readings)
humid_mode = Counter(humidity_readings).most_common(1)[0][0]
pressure_peak = max(pressure_readings) - min(pressure_readings)

# Unused function - dead code path
def analyze_anomaly(data):
    z_scores = [(x - sum(data)/len(data)) / (sum((d - sum(data)/len(data))**2 for d in data)/len(data))**0.5 for x in data]
    return [abs(z) > 2 for z in z_scores]

# Decoy variables with plausible but unused calculations
baseline_offset = 0.78
scaling_factor = 1.0 + (sum(humidity_readings) % 10) / 100
adjusted_temps = [t * scaling_factor for t in temperature_readings]

# Bit manipulation for checksum - looks important but only partially used
temp_checksum = 0
for t in temperature_readings:
    temp_checksum ^= int(t * 10)  # Scale to avoid decimals

temp_checksum &= 0xFF  # Keep within byte range

# Real computation begins: detect stable periods using sliding window
stable_windows = []
for i in range(len(temperature_readings) - 2):
    window = temperature_readings[i:i+3]
    if max(window) - min(window) <= 0.6:
        stability_score = 100 - (max(window) - min(window)) * 10
        humidity_influence = 1 - abs(humidity_readings[i+1] - 47) / 50
        pressure_trend = (pressure_readings[i+2] - pressure_readings[i]) / 3
        trend_penalty = abs(pressure_trend) * 5
        adjusted_score = stability_score * humidity_influence - trend_penalty
        stable_windows.append(max(adjusted_score, 0))

# Secondary analysis on mode consistency
mode_humidity_window = [Counter(humidity_readings[i:i+3]).most_common(1)[0][1] for i in range(len(humidity_readings)-2)]
humidity_consistency_bonus = sum(1 for count in mode_humidity_window if count >= 2)

# Distractor: complex but unused formula involving bitwise and modular arithmetic
phantom_metric = (temp_checksum << 3) & 0x1FF
phantom_metric = (phantom_metric + len(pressure_readings)) % 97

# Main aggregation logic - depends on stable_windows and consistency bonus
def compute_aggregate(stable_scores, bonus, checksum):
    if not stable_scores:
        return 0
    
    base_value = sum(stable_scores) / len(stable_scores)
    bonus_weight = 1.5 if bonus > 3 else 0.8
    
    # Conditional expression usage
    adjustment = 1.1 if (checksum ^ 0xAA) > 100 else 0.9
    
    # Composite calculation combining multiple concepts
    raw_score = base_value * bonus_weight * adjustment
    
    # Final smoothing using modular influence from pressure cycle
    pressure_cycle = sum(pressure_readings) % 12
    final = raw_score - (pressure_cycle * 0.7 if pressure_cycle % 2 == 1 else 0)
    
    return round(final, 4)

# Additional red herring: recursive function that is never called
def recursive_denoise(data, threshold=1.0, depth=0):
    if depth >= 3 or len(data) < 3:
        return data
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        neighbor_avg = (data[i-1] + data[i+1]) / 2
        if abs(data[i] - neighbor_avg) < threshold:
            smoothed.append(neighbor_avg)
        else:
            smoothed.append(data[i])
    smoothed.append(data[-1])
    return recursive_denoise(smoothed, threshold*0.9, depth+1)

# Another decoy structure - unused dictionary aggregation
data_summary = defaultdict(dict)
data_summary['temp']['mean'] = temp_mean
data_summary['temp']['range'] = max(temperature_readings) - min(temperature_readings)
data_summary['humid']['mode'] = humid_mode
data_summary['pressure']['trend'] = pressure_peak

# Critical execution point
final_score = compute_aggregate(stable_windows, humidity_consistency_bonus, temp_checksum)

# Print result for evaluation
print(f"Result: {final_score}")