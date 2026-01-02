def analyze_component_health(sensor_data, config):
    # Irrelevant health check stub
    if len(sensor_data) == 0:
        return 0

    base_score = 0
    for entry in sensor_data:
        base_score += entry.get('reading', 0) * config.get('weight', 1)

    adjustment = config.get('adjustment', 0)
    return max(base_score - adjustment, 0)


def decode_signal_sequence(signal_str):
    # Distractor: signal decoding not actually used in final path
    if not signal_str.strip():
        return []
    parts = signal_str.split('|')
    decoded = []
    for p in parts:
        cleaned = p.strip().lower().replace("_", "")
        if cleaned.startswith('sig'):
            try:
                num = int(cleaned[3:])
                decoded.append(num % 256)
            except ValueError:
                continue
    return decoded

# Unused legacy mapping (red herring)
signal_compat_table = {
    'A': [1, 2], 'B': [3, 4], 'C': [5, 6]
}

# Dead function - looks important but unused
def validate_calibration(sequence, mode="strict"):
    count = 0
    for x in sequence:
        if x > 0 and x % 2 == 0:
            count += 1
    return count >= 2

# Main data structures
threshold_map = {
    'critical': 75,
    'warning': 30,
    'info': 5
}

diagnostics = [
    {'sensor': 'temp_core', 'reading': 85, 'unit': 'C'},
    {'sensor': 'voltage_io', 'reading': 22, 'unit': 'V'},
    {'sensor': 'fan_speed', 'reading': 4, 'unit': 'kRPM'},
    {'sensor': 'load_avg', 'reading': 88, 'unit': '%'}
]

# Intermediate processing with distractors
raw_weights = [1.2, 0.8, 1.5, 2.0]
weight_sum = sum(raw_weights)
normalized_weights = [w / weight_sum for w in raw_weights]  # Unused

config_params = {
    'weight': 1,
    'adjustment': 10,
    'mode': 'aggressive'
}

# Simulate auxiliary system check (dead path)
aux_status = "OK"
if diagnostics[0]['reading'] > 80:
    aux_status = "COOLING_ACTIVE"
else:
    aux_status = "STANDBY"

# Real computation begins here
aggregate = 0
for item in diagnostics:
    val = item['reading']
    if val > threshold_map['critical']:
        aggregate += val // 2  # Integer division
    elif val > threshold_map['warning']:
        aggregate += val // 3
    else:
        aggregate += val

# Secondary transformation chain
shifted_value = aggregate * 3 - 17

# Bit manipulation layer (relevant)
bit_field = shifted_value ^ 0xFF  # XOR with 255
bit_field = bit_field & 0xFFFF  # Mask to 16 bits

# String-based flag processing (uses string method)
flags = ["ERROR_RED", "WARN_YELLOW", "INFO_BLUE"]
active_flag = None
for f in flags:
    if f.lower().startswith("error") and diagnostics[0]['reading'] > 80:
        active_flag = f
        break

flag_penalty = 25 if active_flag and 'RED' in active_flag else 0

# Final processing step
interim = (bit_field + flag_penalty) // 4

# Key control flow with nesting depth 4
if interim > 100:
    if diagnostics[3]['reading'] > 50:
        scaling_factor = 0.75
        if 'temp_core' in diagnostics[0]['sensor']:
            if bit_field % 2 == 0:
                interim = int(interim * scaling_factor)
            else:
                interim = int(interim * 0.9)
    else:
        interim = interim - 20
else:
    interim = max(interim, 10)

# Final output computation
final_output = analyze_component_health(
    [{'reading': interim}], {'weight': 2, 'adjustment': 5}
)

# Red herring: this modifies a non-used variable
shadow_copy = diagnostics.copy()
for d in shadow_copy:
    d['processed'] = True

# Output result
print(f"Result: {final_output}")