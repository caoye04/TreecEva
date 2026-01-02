from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def process_sensor_data(log_entries):
    event_counts = defaultdict(int)
    severity_sum = 0
    temp_buffer = []
    debug_flag = False

    for entry in log_entries:
        parts = entry.split('|')
        timestamp = parts[0]
        event_type = parts[1]
        value_str = parts[2]

        # Legitimate parsing
        if 'ERROR' in event_type:
            try:
                val = float(value_str.strip())
                severity_sum += abs(val) ** 0.5
                event_counts[event_type] += 1
            except:
                continue

        # Distractor: irrelevant temperature grouping
        if 'TEMP' in event_type:
            try:
                temp_val = float(value_str)
                temp_buffer.append(temp_val)
                if temp_val > 75:
                    debug_flag = True  # Dead end
            except:
                pass

    # Irrelevant aggregation
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    peak_temp = max(temp_buffer) if temp_buffer else 0

    # Real computation buried here
    error_count = sum(event_counts[e] for e in event_counts if 'ERROR' in e)
    base_score = severity_sum * 1.75

    # Decoy calculation
    if debug_flag:
        base_score -= avg_temp / 10

    return base_score, error_count, peak_temp  # Only first two are used later


# Misleading auxiliary function (never called)
def legacy_calibrate(x):
    if x < 0:
        return (x ** 2) % 7
    return (x + 3) * 2

# Another decoy: unused data transformation
token_map = {chr(i): i-97 for i in range(97, 123)}
token_counter = Counter('diagnostics')
rolling_hash = 0
for ch in 'diagnostics':
    rolling_hash = (rolling_hash * 31 + token_map[ch]) % 10007

# Simulated network packet checksum (irrelevant)
defective_packets = [0, 1, 0, 0, 1]
packet_loss_rate = sum(defective_packets) / len(defective_packets)
penalty_adjustment = packet_loss_rate * 100

# Main execution
log_data = [
    '12:01|SYS_ERROR_3|-49.0',
    '12:02|TEMP_SENSOR|83.1',
    '12:03|NET_ERROR|-64.0',
    '12:04|TEMP_SENSOR|76.5',
    '12:05|SYS_ERROR_3|-25.0',
    '12:06|DATA_CORRUPT|ignored',  # malformed on purpose
    '12:07|NET_ERROR|-36.0',
    '12:08|TEMP_SENSOR|90.2',
    '12:09|SYS_ERROR_3|-16.0'
]

# Real data flow starts here
aggregate_score, errors_detected, _ = process_sensor_data(log_data)

# Secondary distraction: historical thresholds (unused)
historical_max = 42.5
compliance_window = [historical_max * (0.8 + i*0.05) for i in range(5)]

# Another distraction: string-based state tracking
current_state = "diagnostic_active"
state_flags = {
    'initialized': current_state.startswith('diag'),
    'locked': 'active' in current_state and len(current_state) % 2 == 0,
    'legacy_mode': False
}

# Core logic hidden among noise
if errors_detected >= 3:
    multiplier = 2
else:
    multiplier = 1

adjusted_severity = aggregate_score * multiplier

# Correction based on modular pattern in error count
mod_key = (errors_detected * 7) % 5
if mod_key == 1:
    correction_factor = 10
elif mod_key == 2:
    correction_factor = -5
elif mod_key == 3:
    correction_factor = 15
else:  # mod_key == 0 or 4
    correction_factor = 8

# Critical assignment
final_diagnostic = aggregate_score + correction_factor

# Print required result
print(f"Result: {final_diagnostic}")