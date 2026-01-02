import math

# System telemetry and diagnostic constants
telemetry_data = [14, 28, 42, 56, 70]
baseline_offset = 14
scaling_factor = 2.5
diagnostic_flag = True

# Irrelevant sensor buffers (distraction)
sensor_buffer_a = [0] * 10
sensor_buffer_b = [0] * 10
for i in range(10):
    sensor_buffer_a[i] = i * 2 + 1
    sensor_buffer_b[i] = i * 3 - 1

# Decoy function - appears important but unused
def compute_shadow_state(x):
    return (x ** 2 + 3 * x + 1) % 17

# Real processing begins
active_nodes = [x for x in telemetry_data if x % baseline_offset == 0]
node_count = len(active_nodes)

# Simulated logic signature generation
logic_signature = 0
for val in active_nodes:
    logic_signature ^= (val // baseline_offset) * 3

# System state vector with red herring values
system_state = {
    'power_level': 84,
    'thermal_load': 47,
    'core_stability': 91,
    'aux_flag': False,
    'timestamp': 1678886400
}

# Misleading intermediate calculation (dead path)
candidate_states = []
for i in range(5):
    candidate = (system_state['power_level'] + i * 7) % 100
    candidate_states.append(candidate)

# Conditional mutation based on irrelevant flag
if diagnostic_flag:
    system_state['power_level'] = system_state['power_level'] - 10

# Bit manipulation decoy chain
bit_probe = node_count
for shift in [1, 2, 1]:
    bit_probe = (bit_probe << shift) ^ (bit_probe >> shift)

# Core transformation using lambda (required feature)
transform_metric = lambda x, y: int((x * scaling_factor) + (y / 2.0))

# Spurious data structure with cross-reference distraction
data_cube = {
    'layer1': {'ref': node_count, 'val': transform_metric(node_count, logic_signature)},
    'layer2': {'ref': logic_signature, 'val': transform_metric(logic_signature, node_count)}
}

# Actual critical computation path
consistency_check = 0
for key in ['power_level', 'thermal_load', 'core_stability']:
    consistency_check += system_state[key] % 13

# Secondary validation via tuple unpacking (required concept)
validation_set = (logic_signature, node_count, consistency_check)
a, b, c = validation_set
interim_result = (a * b) + (c ^ a)

# Final processing with conditional expression (suggested paradigm)
final_diagnostic = None
if interim_result > 50:
    adjustment = 7 if system_state['aux_flag'] else 11
    final_diagnostic = process_metrics(logic_signature, system_state)  # Key statement
else:
    final_diagnostic = -999

# Simulate missing function definition to avoid error
# In real benchmark, this would be defined; here we inline its logic
# Replacing call to process_metrics(sig, state):
def process_metrics(sig, state):
    base = sig * 13
    thermal_component = int(math.log(state['thermal_load'] + 1) * 10)
    stability_factor = state['core_stability'] // 10
    power_adj = state['power_level'] % 19
    return base + thermal_component + stability_factor - power_adj

# Recompute final_diagnostic with actual logic
base = logic_signature * 13
thermal_component = int(math.log(system_state['thermal_load'] + 1) * 10)
stability_factor = system_state['core_stability'] // 10
power_adj = system_state['power_level'] % 19
final_diagnostic = base + thermal_component + stability_factor - power_adj

print(f"Result: {final_diagnostic}")