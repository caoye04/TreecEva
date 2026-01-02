import math

def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

# Simulated sensor readings (irrelevant to final result)
sensor_a = [0.1, 0.4, 0.8, -0.9, 0.3]
sensor_b = [0.6, 0.7, -1.2, 0.0, 0.5]

avg_a = analyze_signal(sensor_a)
avg_b = analyze_signal(sensor_b)

# System state flags (some are red herrings)
current_mode = 'diagnostic'
error_count = 3
last_reset_cycle = 12
is_active = True
power_level = 87

# Diagnostic log entries with metadata
timestamps = [1678886400, 1678886460, 1678886520, 1678886580]
event_types = ['INFO', 'WARN', 'ERROR', 'DEBUG']
payloads = [
    {'code': 200, 'duration': 45},
    {'code': 404, 'duration': 12},
    {'code': 500, 'duration': 6},
    {'code': 200, 'duration': 78}
]

log_entries = list(zip(timestamps, event_types, payloads))

# Auxiliary function that appears important but is unused
def compute_stability_index(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return math.exp(-variance)

# Another decoy: historical metrics not used in final calculation
historical_load = {
    'peak': 98.2,
    'avg': 43.7,
    'last_updated': 1678886000
}

# Critical diagnostic processor
system_state = {
    'mode': current_mode,
    'errors': error_count,
    'active': is_active,
    'cycle': last_reset_cycle
}

# Misleading intermediate computation
temp_score = (power_level * 0.3) + (error_count * 5)
adjustment_factor = temp_score / 100  # looks important, never used

# Core processing logic
status_weights = {'INFO': 1, 'WARN': 3, 'ERROR': 6, 'DEBUG': 0}

weighted_sum = 0
total_weight = 0
for entry in log_entries:
    event_type = entry[1]
    payload = entry[2]
    weight = status_weights.get(event_type, 1)
    # Only include entries where duration > 10 or code != 500
    if payload['duration'] > 10 or payload['code'] != 500:
        weighted_sum += weight * (payload['code'] % 100)
        total_weight += weight

# Conditional expression determining baseline
baseline = 100 if system_state['errors'] < 5 else 200

# Secondary filter based on mode
if system_state['mode'] == 'diagnostic':
    # Apply modular correction based on cycle number
    cycle_mod = system_state['cycle'] % 7
    adjusted_baseline = baseline - (cycle_mod * 8)
else:
    adjusted_baseline = baseline + 50

# Final aggregation using tuple unpacking
aggregation_key = (adjusted_baseline, weighted_sum)
base_val, signal_val = aggregation_key

# Actual answer computation hidden among distractions
diagnostic_core = base_val + (signal_val // (total_weight if total_weight > 0 else 1))

# Destructuring fake-out (has no effect)
*_, last_payload = payloads

# Final diagnostic depends only on core logic and active flag
final_diagnostic = diagnostic_core if system_state['active'] else -1

# Irrelevant formatting block (dead path)
if power_level > 90:
    final_diagnostic *= 1.1
elif avg_a > 0.5:
    final_diagnostic = int(final_diagnostic)

# Key output
Target result: {final_diagnostic}