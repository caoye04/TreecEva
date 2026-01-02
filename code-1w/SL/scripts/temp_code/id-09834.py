from collections import defaultdict, Counter
import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 25.1, 22.8, 24.6, 26.3, 21.9, 25.7, 24.2]
humidity_readings = [45, 52, 58, 49, 61, 55, 50, 53]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1016, 1014, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 41, 38, 45, 50, 37, 40, 43]  # Decibel readings - not used
light_intensity = [800, 950, 1100, 1000, 1200, 870, 930, 1050]  # Lux - not used

# Data preprocessing with multiple layers
valid_sensors = []
calibration_offsets = {i: round(math.sin(i) * 0.2, 2) for i in range(len(temperature_readings))}
adjusted_temps = [round(t + calibration_offsets[idx], 2) for idx, t in enumerate(temperature_readings)]

# Misleading intermediate aggregation (red herring)
avg_sound = sum(sound_levels) / len(sound_levels)
predicted_light_trend = max(light_intensity) - min(light_intensity)

# Core signal extraction
thermal_variance = round(max(adjusted_temps) - min(adjusted_temps), 2)
humidity_mode = Counter(humidity_readings).most_common(1)[0][0]
pressure_stability = len([i for i in range(1, len(pressure_readings)) if abs(pressure_readings[i] - pressure_readings[i-1]) < 3])

# Complex derived metrics
entropy_score = 0.0
for p in pressure_readings:
    prob = p / sum(pressure_readings)
    entropy_score -= prob * math.log(prob)
entropy_score = round(entropy_score, 3)

# Distractor function (dead code path)
def compute_wind_chill(temp, humidity):
    return 13.12 + 0.6215*temp - 11.37*(12**0.16) + 0.3965*temp*(12**0.16)  # Uses fake wind speed

# Another decoy transformation
def analyze_light_cycles(data):
    peaks = [i for i in range(1, len(data)-1) if data[i] > data[i-1] and data[i] > data[i+1]]
    return len(peaks), sum(data) // len(data)

# Unused complex structure
diagnostic_map = defaultdict(lambda: 'unknown')
for i, temp in enumerate(adjusted_temps):
    if temp > 25:
        diagnostic_map[f'sensor_{i}'] = 'overheat_risk'
    elif temp < 22:
        diagnostic_map[f'sensor_{i}'] = 'cold_drift'
    else:
        diagnostic_map[f'sensor_{i}'] = 'stable'

# Real processing chain
status_flags = []
for t, h in zip(adjusted_temps, humidity_readings):
    if t > 25 and h > 50:
        status_flags.append(3)
    elif t < 22 or h < 48:
        status_flags.append(1)
    else:
        status_flags.append(2)

flag_distribution = Counter(status_flags)

# Simulated fault detection heuristics
anomaly_count = 0
for i in range(1, len(adjusted_temps)):
    temp_change = abs(adjusted_temps[i] - adjusted_temps[i-1])
    if temp_change > 1.0:
        anomaly_count += 1

# Distractor list comprehension with no effect
echo_values = [x * 0.9 + 5 for x in sound_levels if x > 40]

# Nested conditional data routing (relevant)
processing_chain = []
if thermal_variance > 3.0:
    processing_chain.append('high_variance_protocol')
    if humidity_mode > 50:
        processing_chain.append('dehumidify_sequence')
        if anomaly_count > 2:
            processing_chain.append('deep_diagnostic_scan')
            sub_diagnostics = []
            for i, p in enumerate(pressure_readings):
                if i % 3 == 0:
                    shifted = p >> 2  # Bitwise shift as complexity marker
                    inverted = ~shifted & 0xFFFF  # More bit manipulation
                    sub_diagnostics.append((inverted ^ i) % 100)
            diagnostics = {
                'sub_results': sub_diagnostics,
                'entropy': entropy_score,
                'stability_index': pressure_stability
            }
        else:
            processing_chain.append('quick_recalibrate')
            diagnostics = {'base': 'fast_path'}
    else:
        processing_chain.append('monitor_passively')
        diagnostics = {'base': 'low_risk'}
elif len(adjusted_temps) > 5:
    processing_chain.append('standard_survey')
    diagnostics = {'base': 'routine'}
else:
    processing_chain.append('minimal_check')
    diagnostics = {'base': 'limited'}

# Key statement
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Actual implementation of required function (must be at end to avoid early discovery)
def aggregate_metrics(chain, diag):
    base_score = 0
    if 'high_variance_protocol' in chain:
        base_score += 50
    if 'dehumidify_sequence' in chain:
        base_score += 30
    if 'deep_diagnostic_scan' in chain:
        base_score += 45
        sub_vals = diag['sub_results']
        # Use slicing and statistical reduction
        relevant_parts = sub_vals[::2]  # Every other element
        base_score += sum(relevant_parts) // len(relevant_parts) if relevant_parts else 0
        base_score += int(diag['entropy'] * 10)
        base_score += diag['stability_index'] * 2
    elif 'quick_recalibrate' in chain:
        base_score += 20
    elif 'standard_survey' in chain:
        base_score += 15
    else:
        base_score += 5
    return base_score

print(f"Result: {final_diagnostic}")