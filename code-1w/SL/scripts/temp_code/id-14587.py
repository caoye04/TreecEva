import math

# Simulated sensor array data (irrelevant for final result)
sensor_readings = [0.12, 0.34, 0.56, 0.78, 0.91]
baseline_offset = sum([math.sin(x * 0.5) for x in sensor_readings])
adjusted_readings = [x + baseline_offset for x in sensor_readings]

# Decoy system state variables
device_status = {'active': True, 'mode': 'diagnostic', 'level': 7}
heartbeat_interval = 1.25
sync_threshold = heartbeat_interval * 0.8

# Core logic components (only some are used)
def generate_key(seed):
    return (seed * 17) % 19

def encrypt_step(value, key):
    return (value ^ key) + 1

def decode_chain(sequence):
    result = 0
    for val in sequence:
        result = (result + val) * 2
    return result % 1000

# Unused recursive red herring
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Distractor: complex-looking but unused transformation
transform_pipeline = lambda data: [math.floor(x * 10) / 10 for x in sorted(data, reverse=True)]
filtered_sensors = transform_pipeline(adjusted_readings)

# Real computation begins here — hidden among noise
logic_core = [4, 8, 15, 16, 23, 42]
activation_sequence = [1, 0, 1, 0, 0, 1]  # Bitmask for selection

# Misleading intermediate: appears important but unused
checksum_proxy = sum(logic_core[i] for i in range(len(logic_core)) if activation_sequence[i]) * len(activation_sequence)

# Actual relevant transformation
selected_elements = []
for i in range(len(logic_core)):
    if activation_sequence[i]:
        temp_val = logic_core[i]
        temp_val = encrypt_step(temp_val, generate_key(i+1))
        selected_elements.append(temp_val)

# Another decoy function call with side effect that does nothing critical
def update_registry(entries):
    registry_sum = 0
    for e in entries:
        registry_sum += e % 7
    return registry_sum  # Never used

_ = update_registry(logic_core)

# Critical operation buried in distractions
aggregated = decode_chain(selected_elements)

# Secondary manipulation using dictionary operations (required feature)
metrics_map = {
    'base_score': aggregated,
    'penalty': 12,
    'bonus': 4,
    'multiplier': 3
}

scaling_factor = metrics_map.get('multiplier', 1)
base_adjust = metrics_map['base_score'] - metrics_map['penalty'] + metrics_map['bonus']

# Final computation obscured by irrelevant context
final_diagnostic = base_adjust * scaling_factor

# Red herring: unused conditional affecting no output
if device_status['level'] > 5 and sync_threshold < 1.0:
    final_diagnostic += 100  # This block does not execute due to threshold condition

# Correct result printed at end
print(f"Result: {final_diagnostic}")