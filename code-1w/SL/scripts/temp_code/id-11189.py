import math

# Simulated sensor array diagnostics with embedded logic chain
def analyze_sensor_node(raw_readings, calibration_offset):
    normalized = [x - calibration_offset for x in raw_readings]
    squared_errors = [val ** 2 for val in normalized if val < 10]
    return sum(squared_errors) // len(normalized)

# Irrelevant utility (distractor)
def legacy_checksum(data):
    acc = 0
    for d in data:
        acc = (acc << 1) ^ d & 0xFF
    return acc

# Core transformation pipeline
def transform_signal(amplitude_sequence, gain_profile):
    adjusted = []
    for i, amp in enumerate(amplitude_sequence):
        if i % 2 == 0:
            adjusted.append(amp * gain_profile[0])
        else:
            adjusted.append(max(amp - gain_profile[1], 0))
    return adjusted

# Misleading intermediate analysis (dead path)
def compute_thermal_decay(heat_map):
    temp = [max(h - 273.15, 0) for h in heat_map]
    decay_rate = 0.0
    for t in temp:
        if t > 50:
            decay_rate += math.log(t) * 0.1
    return round(decay_rate, 3)

# Critical diagnostic aggregator
def aggregate_metrics(weights, state):
    # Step 1: Apply bitwise consistency check
    mask = 0b10101010
    weight_flags = sum((w & mask) ^ (i << 1) for i, w in enumerate(weights[:4]))

    # Step 2: Conditional normalization
    if state['mode'] == 'diagnostic':
        scale_factor = 3
    elif state['version'] > 2:
        scale_factor = 7
    else:
        scale_factor = 5

    # Step 3: Filter active components
    active_nodes = [idx for idx, flag in enumerate(state['flags']) if flag and idx % 3 != 2]

    # Step 4: Composite score from weighted contributions
    base_score = 0
    for node in active_nodes:
        if node < len(weights):
            contribution = (weights[node] + weight_flags) * scale_factor
            base_score += contribution % 19

    # Step 5: Adjustment via list comprehension (core calculation)
    adjustments = [int(math.sin(math.pi * i / 6) * 100) for i in range(len(active_nodes))]
    adjusted_score = base_score + sum(abs(adj) for adj in adjustments)

    # Step 6: Final interference filtering
    final_shift = 0
    for i, adj in enumerate(adjustments):
        if adj > 0 and i % 2 == 0:
            final_shift += adj // 10

    return adjusted_score - final_shift

# Irrelevant telemetry structure (distractor)
telemetry_stream = [
    {'ts': 1623456780, 'val': 42, 'type': 'temp'},
    {'ts': 1623456781, 'val': 38, 'type': 'temp'},
    {'ts': 1623456782, 'val': 0,  'type': 'error'}
]

# Real input data
sensor_readings = [12, 15, 8, 20, 5]
calibration_data = [1.0, 0.8, 1.2, 0.9]

# Initialize core variables
tuned_weights = [13, 7, 19, 3, 11]
system_state = {
    'mode': 'diagnostic',
    'version': 3,
    'flags': [True, True, False, True, True],
    'active_channel': 4
}

# Dead code path invocation (misleading call)
legacy_checksum([100, 200, 150])

# Simulate signal transformation (irrelevant to final result)
transformed = transform_signal([10, 20, 30], [1.1, 2.5])

# Compute intermediate diagnostic (red herring)
interim_result = analyze_sensor_node(sensor_readings, 5)

# Thermal model not used downstream (decoy)
thermal_diag = compute_thermal_decay([300, 310, 295])

# --- KEY EXECUTION POINT ---
final_diagnostic = aggregate_metrics(tuned_weights, system_state)

# Output target result
print(f"Result: {final_diagnostic}")