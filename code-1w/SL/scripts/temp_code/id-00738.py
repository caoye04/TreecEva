import math

# Simulated system telemetry data
telemetry_stream = [14, 28, 42, 56, 70, 84, 98]

# Irrelevant calibration constants (distractors)
CALIBRATION_OFFSET = 0.987
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256

# Real-time event flags (some are decoys)
event_flags = {
    'overload': False,
    'sync_lock': True,
    'clock_drift': False,
    'data_corrupted': False
}

# Historical log entries with mixed relevance
log_entries = [
    {'id': 1, 'type': 'info', 'value': 14, 'timestamp': 1001},
    {'id': 2, 'type': 'warn', 'value': 28, 'timestamp': 1002},
    {'id': 3, 'type': 'info', 'value': 42, 'timestamp': 1003},
    {'id': 4, 'type': 'error', 'value': 56, 'timestamp': 1004},
    {'id': 5, 'type': 'info', 'value': 70, 'timestamp': 1005}
]

# System state with multiple fields (only some used)
system_state = {
    'uptime': 12345,
    'core_temp': 67.8,
    'load_avg': [0.75, 0.80, 0.92],
    'active_processes': 42,
    'memory_usage': 8576,
    'threshold_limit': 75
}

# Unused helper functions (dead code paths)
def validate_checksum(data):
    return sum(data) % 255

def normalize_readings(readings):
    max_val = max(readings)
    return [x / max_val for x in readings]

def encrypt_log_entry(entry):
    return ''.join(chr(ord(c) ^ 42) for c in str(entry))

# Core processing logic (partially relevant)
filtered_values = []
for entry in log_entries:
    if entry['type'] == 'info' or entry['type'] == 'warn':
        filtered_values.append(entry['value'])

# Bit manipulation red herring
masked_values = [v & 0xFF for v in filtered_values]
shifted_sum = sum(masked_values) >> 2

# Distractor: complex but unused lambda chain
transform_chain = lambda x: math.log(x + 1) if x > 0 else 0
processed_chain = list(map(transform_chain, telemetry_stream))

# Real computation begins here — ignore prior noise
recent_timestamps = [entry['timestamp'] for entry in log_entries if entry['type'] != 'error']
delta_t = recent_timestamps[-1] - recent_timestamps[0]

# Set operation to extract unique types
entry_types = {entry['type'] for entry in log_entries}
type_count_factor = len(entry_types)

# Dictionary aggregation of values by type
aggregated = {}
for entry in log_entries:
    key = entry['type']
    if key not in aggregated:
        aggregated[key] = 0
    aggregated[key] += entry['value']

# Only 'info' type contributes to final result
info_contribution = aggregated.get('info', 0)

# Conditional adjustment based on system load
load_index = int(sum(system_state['load_avg']) * 100)
if system_state['core_temp'] > system_state['threshold_limit']:
    load_index += 10

# Key intermediate (misleading)
baseline_score = info_contribution * delta_t // type_count_factor

# Final diagnostic uses XOR of two critical values and ignores most above
# Despite all distractions, only two values matter
value_a = info_contribution  # from dictionary aggregation
value_b = len(recent_timestamps)  # number of non-error entries

# Critical statement containing actual answer
final_diagnostic = (value_a ^ value_b) + (load_index & 0xF)

print(f"Result: {final_diagnostic}")