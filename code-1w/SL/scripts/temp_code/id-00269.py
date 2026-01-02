from itertools import zip_longest

# System health monitoring simulation with diagnostic interference

def analyze_component_stability(readings):
    if not readings:
        return 0
    squared_devs = [(x - sum(readings)/len(readings))**2 for x in readings]
    variance = sum(squared_devs) / len(squared_devs)
    return int(variance * 100) // 10

# Irrelevant helper: simulates network jitter (not used in final calculation)
def simulate_jitter(samples):
    base = [abs(hash(str(i)) % 100) for i in range(samples)]
    return [b ^ 7 for b in base if b % 3 != 0]

# Real data stream
sensor_inputs = [85, 90, 88, 92, 87]

# Distractor variables
network_latency_log = [hash('latency') % 50 for _ in range(10)]
temporal_offset = sum(network_latency_log) / len(network_latency_log)
jitter_buffer = simulate_jitter(20)

# Core signal processing chain
baseline_adjustment = sum(sensor_inputs) // len(sensor_inputs)
device_skew = analyze_component_stability(sensor_inputs)

# Multiple assignment distraction
calibration_x, calibration_y = 17, 23
offset_map = {calibration_x: 'A', calibration_y: 'B'}

# Conditional expression with meaningful logic
aggregate_health_score = baseline_adjustment - (device_skew if device_skew > 5 else 0)

# Bitwise red herring
mask_sequence = 0
for val in sensor_inputs:
    mask_sequence ^= (val & 15) << 1

# Unused but plausible intermediate
consistency_check = all(x >= 80 for x in sensor_inputs)
diagnostic_trace = ''.join(chr(65 + (sum(sensor_inputs) % 26)))

# State tracking distraction
state_history = []
for i in range(3):
    state_history.append({
        'cycle': i,
        'flag': bool((sum(sensor_inputs) + i) & 1),
        'value': hash('state') % 1000
    })

# Key control flow with short-circuit logic
integrity_flag = len(sensor_inputs) > 4 and consistency_check
adjustment_magnitude = 5 if integrity_flag else -5
correction_factor = adjustment_magnitude * 2

# Dead code path — looks important but unused
if __debug__:
    debug_snapshot = [
        {'raw': s, 'norm': s - baseline_adjustment} for s in sensor_inputs
    ]

# Composite calculation with distractors
auxiliary_metric = sum([mask_sequence & 0xFF, len(jitter_buffer[:3])]) // 2
placeholder_result = next(
    (item['value'] for item in state_history if item['flag']), 0
)

# Critical execution point
final_diagnostic = aggregate_health_score + (integrity_flag and correction_factor)

# Output
print(f"Result: {final_diagnostic}")