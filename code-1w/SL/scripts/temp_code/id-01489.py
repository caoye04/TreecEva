from collections import defaultdict, Counter
import math

# Simulated sensor data processing for a thermal regulation system
def collect_telemetry():
    timestamps = list(range(100, 250, 5))
    temperatures = [20 + 10 * math.sin(i / 20) + 3 * math.cos(i / 35) for i in range(len(timestamps))]
    pressures = [101.3 + 5 * math.sin(i / 15) for i in range(len(timestamps))]
    voltage_levels = [120 - (i % 40) for i in range(len(timestamps))]
    return list(zip(timestamps, temperatures, pressures, voltage_levels))

def filter_outliers(data, threshold=2.5):
    # Irrelevant filtering function (not used in final path)
    avg = sum(x[1] for x in data) / len(data)
    return [x for x in data if abs(x[1] - avg) < threshold]

def compute_thermal_gradient(temp_sequence):
    gradients = []
    for i in range(1, len(temp_sequence)):
        gradients.append(temp_sequence[i] - temp_sequence[i-1])
    smoothed = [sum(gradients[i:i+3]) / 3 for i in range(len(gradients) - 2)]
    return round(sum(smoothed) / len(smoothed), 4) if smoothed else 0.0

def analyze_phase_shift(readings):
    # Dead code path — looks useful but unused
    even_part = readings[::2]
    odd_part = readings[1::2]
    shift = sum(abs(a - b) for a, b in zip(even_part[:10], odd_part[:10]))
    return shift > 50

def generate_checksum(sequence):
    # Distractor function: looks important but not part of critical path
    chk = 0
    for val in sequence:
        chk = (chk + int(val)) ^ (int(val) % 7)
    return chk % 97

def extract_timing_windows(telemetry):
    timing_log = defaultdict(list)
    for ts, temp, press, volt in telemetry:
        bucket = ts // 25
        timing_log[bucket].append((temp, press))
    
    # Add decoy entries
    timing_log[-1] = [(0,0), (0,0)]
    timing_log[99] = [(999, 999)]
    
    return timing_log

def extract_power_profile(telemetry):
    power_readings = []
    for _, _, _, voltage in telemetry:
        wattage = voltage * 0.85  # Assume constant current
        power_readings.append(wattage)
    
    # Misleading transformation
    normalized = [p / max(power_readings) for p in power_readings]
    scaled = [int(p * 1000) for p in normalized]
    
    # The real signal is here
    return power_readings  # Not normalized or scaled

def calculate_stability_index(log):
    # Irrelevant complexity
    entropy = 0.0
    for k in log:
        if k > 0:
            length = len(log[k])
            if length > 1:
                entropy += math.log(length)
    return round(entropy, 3)

def aggregate_metrics(timing_log, power_samples):
    # Core logic buried in noise
    
    # Extract relevant time windows (filter out decoys)
    valid_keys = [k for k in timing_log.keys() if k >= 0]
    active_segments = []
    for k in valid_keys:
        segment_temps = [entry[0] for entry in timing_log[k]]
        if len(segment_temps) > 2:
            avg_temp = sum(segment_temps) / len(segment_temps)
            if avg_temp > 15:
                active_segments.append(avg_temp)
    
    # Real computation starts here
    raw_mean = sum(active_segments) / len(active_segments) if active_segments else 0
    fluctuation = max(active_segments) - min(active_segments)
    
    # Power-based weight adjustment
    high_power_threshold = 95
    sustained_high = len([p for p in power_samples if p >= high_power_threshold])
    duration_ratio = sustained_high / len(power_samples)
    
    # Critical calculation
    adjustment_factor = 1 + (duration_ratio * 0.75)
    weighted_metric = (raw_mean * adjustment_factor) + (fluctuation * 0.5)
    
    # Final diagnostic score
    final_diagnostic = int(round(weighted_metric * 10))
    
    # Red herring: checksum verification (unused)
    fake_validity = generate_checksum([int(raw_mean), int(fluctuation), len(power_samples)])
    
    return final_diagnostic

# Main execution flow
data_stream = collect_telemetry()

# These calls look important but only some contribute
processed_log = extract_timing_windows(data_stream)
power_data = extract_power_profile(data_stream)

baseline_entropy = calculate_stability_index(processed_log)
gradient_rate = compute_thermal_gradient([x[1] for x in data_stream])

# Key statement
final_diagnostic = aggregate_metrics(processed_log, power_data)

# Print result as required
print(f"Result: {final_diagnostic}")