from itertools import cycle

# Simulate time-series sensor readings over a monitoring period
time_points = list(range(10))
sensor_data = [22.1, 23.5, 24.0, 23.8, 26.3, 27.1, 25.9, 24.2, 23.0, 22.5]

# Track state variables for system health assessment
spike_count = 0
baseline = 0.0
rolling_average_window = []
anomaly_detected = False
recovery_phases = 0

# Secondary unrelated tracking (distractor)
event_counter = {"normal": 0, "warning": 0, "critical": 0}
phase_log = []
checksum_accum = 0

# Compute baseline as average of first half
for i in range(len(time_points[:5])):
    baseline += sensor_data[i]
baseline /= 5

# Analyze trend with sliding window and detect anomalies
for t in time_points:
    current_reading = sensor_data[t]
    rolling_average_window.append(current_reading)
    
    # Unrelated checksum update (distractor)
    checksum_accum += int(current_reading) % 7
    
    # Classify event type (partially relevant but not used in final answer)
    if current_reading < baseline - 1.0:
        event_type = "warning"
        spike_count += 1
    elif current_reading > baseline + 2.0:
        event_type = "critical"
        anomaly_detected = True
    else:
        event_type = "normal"
        
    event_counter[event_type] += 1
    
    # Simulate recovery phase detection (semi-relevant)
    if anomaly_detected and current_reading < baseline:
        recovery_phases += 1
        anomaly_detected = False  # Reset for next cycle

# Additional distractor: cycling through dummy states
state_cycle = cycle(['IDLE', 'ACTIVE', 'STANDBY'])
dummy_states = [next(state_cycle) for _ in range(len(time_points))]

# Core diagnostic logic
base_score = int(baseline * 10)  # Convert to integer score
anomaly_penalty = spike_count * 15
recovery_credit = recovery_phases * 8

# Key statement
final_diagnostic = base_score + anomaly_penalty - recovery_credit

# Irrelevant transformation chain (distractor)
final_diagnostic_hex = hex(final_diagnostic)
diagnostic_str = f"DIAG_{final_diagnostic_hex.upper()}"
diagnostic_str = diagnostic_str.replace('_', '')

# Output result
print(f"Result: {final_diagnostic}")