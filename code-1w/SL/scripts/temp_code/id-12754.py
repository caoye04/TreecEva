import math

# Irrelevant sensor calibration constants (distractors)
CALIBRATION_OFFSET_X = 0.872
CALIBRATION_OFFSET_Y = -1.034
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 1024

# Real-time telemetry monitoring (mostly unused)
telemetry_log = []
active_sensors = ['flow', 'pressure', 'temp']
sensor_status = {sensor: True for sensor in active_sensors}

# Simulated industrial data stream with mixed signal types
data_stream = [
    {'time': 0.1, 'signal_a': 127, 'signal_b': 64, 'noise': 15},
    {'time': 0.2, 'signal_a': 135, 'signal_b': 60, 'noise': 18},
    {'time': 0.3, 'signal_a': 118, 'signal_b': 70, 'noise': 12},
    {'time': 0.4, 'signal_a': 142, 'signal_b': 58, 'noise': 22},
    {'time': 0.5, 'signal_a': 129, 'signal_b': 66, 'noise': 14}
]

# Decoy function: appears important but unused in critical path
def calibrate_sensor(data, offset):
    return [x + offset for x in data] if isinstance(data, list) else data + offset

# Misleading transformation chain (dead code path)
preprocessed_cache = []
for entry in data_stream:
    temp_val = (entry['signal_a'] * 0.7) + (entry['signal_b'] * 0.3)
    normalized = temp_val / 255.0
    preprocessed_cache.append(normalized)

# Bit manipulation red herring
bit_flags = 0b1010
bit_flags |= 0b0101
bit_flags ^= 0b1111
flag_check = (bit_flags & 0b0010) >> 1

# Unused statistical summary (distractor)
mean_signal_a = sum(entry['signal_a'] for entry in data_stream) / len(data_stream)
variance_proxy = sum((entry['signal_a'] - mean_signal_a) ** 2 for entry in data_stream)

# Core processing pipeline (actual logic)
filter_kernel = lambda x, y: int((x * 0.6) + (y * 0.4))

threshold_map = {
    'low': 100,
    'medium': 120,
    'high': 140
}

event_counter = 0
alert_buffer = []

# Main processing function with nested logic and distractors
def analyze_event(signal_value, baseline):
    nonlocal event_counter
    if signal_value > threshold_map['high']:
        event_counter += 1
        return 'CRITICAL'
    elif signal_value > threshold_map['medium']:
        adjustment = math.log(signal_value, 2) if signal_value > 0 else 0
        adjusted_baseline = baseline + adjustment
        return f"WARNING:{adjusted_baseline:.2f}"
    else:
        return "NORMAL"

# Complex pipeline with irrelevant stages
def process_pipeline(stream):
    global optimized_flow_rate
    flow_accumulator = 0
    pressure_factor = 1.0
    temp_correction = []

    # Stage 1: Signal fusion (relevant)
    for record in stream:
        fused_level = filter_kernel(record['signal_a'], record['signal_b'])
        
        # Conditional branching with side effects
        if fused_level > 120:
            pressure_factor *= 1.05
            
            # Nested condition with bit-level distraction
            binary_rep = bin(fused_level)[2:]
            ones_count = binary_rep.count('1')
            if ones_count % 2 == 0:
                pressure_factor *= 0.98  # Minor correction
        
        # Stage 2: Flow accumulation with conditional override (relevant)
        if record['time'] >= 0.3:
            flow_accumulator += fused_level * pressure_factor
        
        # Red herring: temperature simulation (never used)
        raw_temp = record['noise'] * 0.5
        corrected_temp = raw_temp + 27.3
        temp_correction.append(corrected_temp)
    
    # Stage 3: Final transformation (critical)
    raw_flow_rate = flow_accumulator / 3.0  # Only last 3 records count
    
    # Multiple competing corrections (only one matters)
    legacy_damping = 0.92
    quantum_gain = 1.08  # Marketing term, not real
    stability_trim = 0.99

    # Actual final computation
    optimized_flow_rate = raw_flow_rate * stability_trim  # Correct path
    
    # DEAD CODE: alternative formula (misleading)
    # optimized_flow_rate = raw_flow_rate * quantum_gain * (1 - legacy_damping)
    # alert_buffer.append("Quantum stabilization applied")
    
    # Unused sorting distraction
    sorted_signals = sorted(
        [entry['signal_a'] for entry in stream],
        key=lambda x: x % 10
    )
    
    return {
        'final_flow': optimized_flow_rate,
        'events': event_counter,
        'diagnostics': sorted_signals[:2]
    }

# Execute main logic
telemetry_log.append('System online')
final_output = process_pipeline(data_stream)
Result: {final_output['final_flow']}