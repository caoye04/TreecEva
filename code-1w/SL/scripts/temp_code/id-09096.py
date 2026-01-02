import math

# Simulated telemetry data from a distributed sensor array
telemetry_stream = [
    {'id': 'S1', 'val': 127, 'flags': 0b101, 'seq': 1},
    {'id': 'S2', 'val': 255, 'flags': 0b110, 'seq': 4},
    {'id': 'S3', 'val': 64,  'flags': 0b001, 'seq': 2},
    {'id': 'S4', 'val': 192, 'flags': 0b111, 'seq': 3}
]

# System configuration state
system_state = {
    'active_nodes': 3,
    'threshold': 100,
    'encryption_key': 0xDEADBEEF,
    'debug_mode': False,
    'version': '2.1.9'
}

# Auxiliary lookup table for error correction (irrelevant to final result)
correction_map = {
    i: (i * 257) % 101 for i in range(10)
}

# Misleading diagnostic function that appears important but is never called
def analyze_failure_modes(data):
    total_risk = 0
    for entry in data:
        risk = (entry['val'] >> 2) & entry['flags']
        total_risk += risk ** 2
    return total_risk

# Decoy transformation using string methods (dead code path)
def encode_sequence(stream):
    raw_ids = ''.join([s['id'] for s in stream])
    encoded = raw_ids.replace('S', 'X').lower().swapcase()
    return encoded[::-1]

# Core processing pipeline

# Pre-filter valid sensors based on flag pattern
valid_sensors = [s for s in telemetry_stream if (s['flags'] & 0b100)]

# Extract values and apply nonlinear calibration (relevant)
calibrated_vals = []
for sensor in valid_sensors:
    raw_val = sensor['val']
    # Apply logarithmic compression
    if raw_val > 0:
        calibrated = math.log(raw_val, 2)
    else:
        calibrated = 0
    calibrated_vals.append(round(calibrated, 3))

# Compute rolling checksum (distraction with modular arithmetic)
rolling_hash = 0
for i, v in enumerate(calibrated_vals):
    rolling_hash = (rolling_hash + int(v) * (i + 1)) % 97

# Simulate packet loss compensation (unused)
interpolated = []
for i in range(len(calibrated_vals) - 1):
    interp_val = (calibrated_vals[i] + calibrated_vals[i+1]) / 2
    interpolated.append(interp_val)

# Bitmask analysis of system flags (partially relevant)
system_signature = 0
for sensor in telemetry_stream:
    system_signature ^= sensor['flags'] << 2

# Conditional expression to determine processing mode
processing_mode = 'enhanced' if system_state['active_nodes'] >= 3 else 'basic'

# Real-time anomaly scoring (distractor)
anomaly_scores = list(map(
    lambda x: (x['val'] / (x['seq'] + 1)) if x['seq'] > 0 else 0,
    telemetry_stream
))
dynamic_weight = sum(anomaly_scores) / len(anomaly_scores) if anomaly_scores else 0

# Main metric processor (key function)
def process_metrics(logs, config):
    # Filter by threshold
    filtered = [e for e in logs if e['val'] > config['threshold']]
    
    # Aggregate using bit manipulation and arithmetic
    accumulator = 0
    for entry in filtered:
        # Use XOR shift pattern
        temp = (entry['val'] ^ 0xFF) + 1
        # Apply modular scaling
        scaled = (temp * 3) % 251
        accumulator += scaled
    
    # Secondary adjustment based on system signature parity
    if system_signature & 0x8:
        accumulator = int(accumulator * 1.5)
    else:
        accumulator = int(accumulator * 0.9)
    
    # Final clamp and offset
    clamped = max(accumulator, 500)
    
    # Incorporate processing mode via conditional expression
    final_adjust = clamped + (50 if processing_mode == 'enhanced' else -25)
    
    # Spurious string operation (red herring)
    mode_flag = f"MODE_{processing_mode.upper()}"
    mode_hash = sum([ord(c) for c in mode_flag]) % 100
    
    # Return adjusted accumulator (this is the real answer)
    return final_adjust - mode_hash

# Execute critical statement
final_diagnostic = process_metrics(telemetry_stream, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")