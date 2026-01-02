import math

# Simulated sensor array data with noise and calibration offsets
data_stream = [145, 128, 192, 255, 0, 64, 200, 172]
calibration_factor = 0.87
noise_floor = 12
offset_map = {i: (i * 0.1) for i in range(8)}

# Irrelevant temperature simulation (distractor)
temperature_readings = [22.1, 23.5, 21.8, 24.0, 22.9]
avg_temp = sum(temperature_readings) / len(temperature_readings)
temp_status = 'nominal' if avg_temp < 25 else 'overheat'

# Signal preprocessing with red herring transformations
filtered_signal = []
for val in data_stream:
    adjusted = (val - noise_floor) * calibration_factor
    if adjusted > 200:
        adjusted = 200
    elif adjusted < 0:
        adjusted = 0
    filtered_signal.append(round(adjusted))

# Decoy frequency analysis (dead code path)
def analyze_frequency(signal):
    return sum(s ** 2 for s in signal[:4]) // len(signal[:4])

# Unused but plausible function call (misleading)
frequency_score = analyze_frequency(filtered_signal)

# Normalization using min-max scaling
min_val = min(filtered_signal)
max_val = max(filtered_signal)
range_val = max_val - min_val

if range_val == 0:
    normalized_data = [0 for _ in filtered_signal]
else:
    normalized_data = [(x - min_val) / range_val for x in filtered_signal]

# Bitmask simulation for hardware flags (complex distractor)
hw_status_word = 0b11010110
diagnostic_bits = {
    'overload': bool(hw_status_word & (1 << 7)),
    'cal_error': bool(hw_status_word & (1 << 6)),
    'io_ready': bool(hw_status_word & (1 << 5)),
    'buf_half': bool(hw_status_word & (1 << 4)),
    'irq_pending': bool(hw_status_word & (1 << 3)),
    'parity_ok': bool(hw_status_word & (1 << 2)),
    'clock_sync': bool(hw_status_word & (1 << 1)),
    'power_good': bool(hw_status_word & (1 << 0))
}

# Redundant flag processing with unused lambdas (decoy)
flag_priority = lambda f: sum(1 for v in f.values() if v)
status_rank = flag_priority(diagnostic_bits)

# Actual control flags used in computation (critical path)
flags = {
    'debug_mode': False,
    'strict_bounds': True,
    'use_scaling': True
}

# Complex data transformation pipeline with conditional logic
def apply_envelope(signal, scale=1.0, clip=True):
    env = []
    for i, s in enumerate(signal):
        # Apply raised cosine envelope
        phase = (i / (len(signal) - 1)) * math.pi if len(signal) > 1 else 0
        window = (1 - math.cos(phase)) / 2
        processed = s * window * scale
        if clip and processed > 1:
            processed = 1
        env.append(round(processed, 6))
    return env

# Apply envelope modulation (relevant)
enveloped_data = apply_envelope(normalized_data, scale=1.5, clip=True)

# Set operations to simulate feature selection (mixed relevance)
active_indices = set(range(len(enveloped_data)))
weak_signal_mask = {i for i, v in enumerate(enveloped_data) if v < 0.3}
strong_components = active_indices - weak_signal_mask
retained_signals = sorted(strong_components)

# Final metric processor (key function)
def process_metrics(data_list, config):
    # Local dictionary mapping for weight adjustment
    weights = {i: 0.8 + (i * 0.05) for i in range(len(data_list))}
    
    # Conditional scaling based on config
    if config.get('use_scaling') and config.get('strict_bounds'):
        scaled_vals = [min(v * weights[i], 1.0) for i, v in enumerate(data_list)]
    else:
        scaled_vals = data_list
    
    # Compute weighted diagnostic index
    total_weight = sum(weights[i] for i in range(len(scaled_vals)))
    if total_weight == 0:
        return 0.0
    
    diagnostic_index = sum(scaled_vals[i] * weights[i] for i in range(len(scaled_vals)))
    
    # Apply final nonlinearity if debug mode is off
    if not config.get('debug_mode'):
        diagnostic_index = math.sqrt(diagnostic_index) * 100
    
    return round(diagnostic_index, 6)

# Critical execution point
final_diagnostic = process_metrics(normalized_data, flags)

# Print result as required
print(f"Target result: {final_diagnostic}")