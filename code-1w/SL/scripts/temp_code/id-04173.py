import itertools

# Simulated sensor array data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 20.4, 21.7, 26.8, 18.9, 27.1]
humidity_readings = [45, 50, 52, 61, 42, 58, 54, 39, 63, 41]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1016, 1007, 1020, 1011]

# Irrelevant auxiliary arrays (distractors)
elevation_zones = [120, 205, 180, 250, 110, 195, 210, 90, 260, 130]
wind_speeds = [8.2, 6.5, 7.1, 9.3, 5.8, 7.6, 6.9, 10.1, 8.7, 6.3]

# Misleading preprocessing: appears important but unused in final calculation
calibration_offsets = list(map(lambda x: round(x * 0.02, 2), temperature_readings))
adjusted_temps = [round(t + o, 2) for t, o in zip(temperature_readings, calibration_offsets)]

# Distractor function: looks like it's used, but isn't called
def compute_wind_chill(temp, wind):
    return 13.12 + 0.6215*temp - 11.37*(wind**0.16) + 0.3965*temp*(wind**0.16)

# Real processing begins here
combined_readings = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Filter based on anomalous pressure thresholds (real logic path)
def filter_anomalies(data):
    valid_entries = []
    for entry in data:
        temp, hum, pres = entry
        if 1008 <= pres <= 1018:  # Normal pressure range
            valid_entries.append(entry)
    return valid_entries

filtered_data = filter_anomalies(combined_readings)

# Secondary filter: remove high humidity extremes (part of real logic)
moderate_humidity = [entry for entry in filtered_data if 40 <= entry[1] <= 55]

# Dead code path - never executed, but looks plausible
if len(moderate_humidity) > 100:
    moderate_humidity = moderate_humidity[:5]

# Real transformation: extract temperature and apply weighted drift correction
baseline_temp = sum(t for t, h, p in moderate_humidity) / len(moderate_humidity)
temp_drift = list(itertools.accumulate([abs(t - baseline_temp) for t in [t for t, h, p in moderate_humidity]]))

def adjust_for_drift(drift_values, base):
    if not drift_values:
        return base
    cumulative_drift = drift_values[-1]
    return round(base - cumulative_drift, 2)

adjusted_baseline = adjust_for_drift(temp_drift, baseline_temp)

# Complex diagnostic engine with red herrings
system_flags = {"stable": True, "warning": False, "critical": False}
flag_weights = {"stable": 1, "warning": 2, "critical": 5}

# Unused flag computation (distractor)
total_weight = sum(flag_weights[flag] for flag in system_flags if system_flags[flag])

# Core diagnostic logic
health_metrics = []
for temp, hum, pres in moderate_humidity:
    # Scoring system: temp deviation, humidity efficiency, pressure stability
    t_score = abs(temp - adjusted_baseline) * 1.5
    h_score = max(0, abs(hum - 48) - 2) * 0.8  # Ideal humidity = 48%
    p_score = abs(pres - 1013) * 0.3
    
    # Early termination red herring (never triggers due to data)
    if t_score > 100:
        health_metrics.append(50)
        break
        
    composite = t_score + h_score + p_score
    health_metrics.append(composite)

# Another distractor: uses itertools but doesn't affect result
rolling_averages = list(itertools.starmap(lambda a, b: (a + b) / 2, itertools.pairwise(health_metrics)))

# Final aggregation
raw_diagnostic = sum(health_metrics) / len(health_metrics)

# Final processing function
def process_readings(data):
    # Dummy operations on unused parameters
    readings_count = len(data)
    entropy_proxy = 0
    for val in health_metrics:
        if val > 0:
            entropy_proxy += val * (-val / raw_diagnostic)  # Misleading formula
    
    # Actual answer computation
    normalized = int(round(raw_diagnostic * 17.3, 0))  # Key transformation
    checksum = sum(int(b) for b in format(normalized, 'b')[::2])  # Bit manipulation distraction
    return normalized - checksum

final_diagnostic = process_readings(filtered_data)
print(f"Target result: {final_diagnostic}")