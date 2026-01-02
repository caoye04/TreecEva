import math

# Simulated thermal sensor array data from satellite subsystems
temperature_logs = [23.5, 24.1, 25.3, 26.0, 27.8, 28.2, 29.5, 30.1, 31.4, 32.6, 33.0, 34.2, 35.5]

# Irrelevant auxiliary data (distractor)
signal_strength = [89, 92, 87, 95, 90, 85, 93, 88, 91, 86, 94, 84, 96]
packet_latency_ms = [12, 15, 11, 14, 13, 16, 10, 12, 15, 14, 11, 13, 17]

def apply_calibration(data, factor=1.02):
    # Unused calibration function (dead code path)
    return [round(x * factor, 2) for x in data]

def compute_variance(samples):
    # Misleading statistical function (irrelevant to final result)
    mean = sum(samples) / len(samples)
    return sum((x - mean) ** 2 for x in samples) / len(samples)

# Threshold bands for anomaly detection
warning_band = (26.5, 32.0)
critical_band = (32.1, float('inf'))

# Data transformation chain with distractors
adjusted_offsets = [round(t * 0.98 + 1.2, 2) for t in temperature_logs]  # Distractor computation

# Filter valid operational range (preprocessing step)
valid_range = [t for t in temperature_logs if t >= 24.0]

# Bitmask simulation for sensor status (mixed paradigm: bitwise + filtering)
sensor_ids = [0b1010, 0b1100, 0b0110, 0b1111, 0b1001, 0b0101, 0b1110, 0b1011, 0b0011, 0b1000, 0b0111, 0b1101, 0b0001]
active_mask = 0b1111
sensor_health = [(sid & active_mask) == active_mask for sid in sensor_ids]  # Only one fully active

# Simulated fault counter (unused, misleading)
fault_counter = 0
for health in sensor_health:
    if not health:
        fault_counter += 1

# Core logic disguised among distractors
def detect_spikes(data, window=3):
    spikes = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        if data[i+window-1] > window_avg * 1.15:
            spikes.append(1)
        else:
            spikes.append(0)
    return spikes

spike_flags = detect_spikes(valid_range, 3)

# Decoy aggregation (never used)
average_spike_rate = sum(spike_flags) / len(spike_flags) if spike_flags else 0

# Key intermediate transformation
thermal_readings = [t**2 for t in valid_range]  # Amplify signal for diagnostic

# Filtering based on dynamic threshold
baseline = sum(thermal_readings) / len(thermal_readings)
threshold_filter = [t for t in thermal_readings if t > baseline * 1.08]

# Real target function buried in complexity
def aggregate_anomalies(readings, filtered):
    if not filtered:
        return 0
    
    # Composite calculation: combines count, max deviation, and parity check
    count_weight = len(filtered)
    max_deviation = max(filtered) - baseline
    
    # Hidden logic: only odd-indexed original readings contribute beyond baseline
    raw_indices = [i+1 for i, t in enumerate(valid_range) if t**2 in filtered]
    parity_bonus = sum(1 for idx in raw_indices if idx % 2 == 1)
    
    # Final diagnostic score (answer)
    diagnostic_score = int(
        count_weight * 2.5 + 
        (max_deviation / 10) + 
        (parity_bonus * 1.7)
    )
    
    # Additional red herring: unused transformation
    encoded_score = diagnostic_score ^ 0xABCD
    return diagnostic_score

# Execution point of interest
final_diagnostic = aggregate_anomalies(thermal_readings, threshold_filter)

# Output result as required
print(f"Target result: {final_diagnostic}")