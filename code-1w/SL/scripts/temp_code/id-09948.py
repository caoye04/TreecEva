import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_values = [127, 255, 64, 89, 191, 33, 142, 200, 77, 105]
    calibration_offset = 17
    adjusted = [val + calibration_offset for val in raw_values]
    return adjusted

# Irrelevant signal processing function (dead code path)
def process_frequency_signal(signal):
    fft_result = []
    for i in range(len(signal)):
        component = signal[i] * math.sin(i * math.pi / 4)
        fft_result.append(round(component, 2))
    return fft_result

# Data filtering based on dynamic thresholds
def filter_anomalies(data_stream, baseline):
    upper_bound = baseline * 1.8
    lower_bound = baseline * 0.7
    clean_data = []
    for reading in data_stream:
        if lower_bound <= reading <= upper_bound:
            clean_data.append(reading)
        elif reading > upper_bound:
            clean_data.append(int(upper_bound))  # cap high values
    return clean_data

# Core analysis function with set operations and conditional logic
def analyze_readings(readings, critical_levels):
    aggregate_score = 0
    severity_count = {"high": 0, "medium": 0, "low": 0}
    
    temp_snapshot = {x % 50 for x in readings}  # distractor: unused set operation
    
    normalization_factor = len(readings) if readings else 1
    normalized_readings = [r / normalization_factor for r in readings]
    
    avg_reading = sum(readings) / len(readings)
    
    # Evaluate against critical thresholds using set intersection
    high_alert_zone = {x for x in readings if x > 150}
    warning_zone = {x for x in readings if 100 <= x <= 150}
    normal_zone = set(readings) - high_alert_zone - warning_zone
    
    # Misleading diagnostic flag (not used in final result)
    transient_spike_detected = len(high_alert_zone) > 0 and (readings[-1] in high_alert_zone)
    
    # Primary scoring logic
    for val in readings:
        if val in critical_levels:
            aggregate_score += int(math.log(val) * 3)
        elif val > 150:
            aggregate_score += 5
        elif val > 100:
            aggregate_score += 2
        else:
            aggregate_score += 1
    
    # Secondary adjustment based on zone distribution
    if len(high_alert_zone) >= 3:
        aggregate_score = int(aggregate_score * 1.3)
    elif len(warning_zone) > len(high_alert_zone):
        aggregate_score += len(warning_zone)

    # Complex conditional override
    if avg_reading > 140 and len(high_alert_zone) > 0:
        fallback_metric = sum([v**0.5 for v in high_alert_zone])
        aggregate_score = int(fallback_metric * 2.1)

    # Final computation influenced by set size
    zone_ratio = len(normal_zone) / len(critical_levels.union({1}))
    final_adjustment = aggregate_score * (1 + zone_ratio / 4)
    
    return int(final_adjustment)

# Unused auxiliary function (distractor)
def generate_report_snapshot(data):
    timestamp = "2023-12-15T10:30:45Z"
    checksum = sum([d ^ 255 for d in data]) % 1000
    return f"Report-{timestamp}-{checksum}"

# Main execution flow
sensor_data = collect_sensor_data()

# Extraneous transformation (irrelevant)
double_filtered = [x for x in sensor_data if x % 2 == 0]

operational_thresholds = {120, 145, 170, 195, 210}
safety_bounds = {50, 75, 100}  # decoy set

filtered_data = filter_anomalies(sensor_data, baseline=100)

# Early termination check (not triggered)
if len(filtered_data) < 5:
    emergency_code = 999
    exit(emergency_code)

# Key statement
final_diagnostic = analyze_readings(filtered_data, operational_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")