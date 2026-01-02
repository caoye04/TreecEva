import math

# Simulated bio-signal processing pipeline with decoy components

def generate_waveform(baseline, harmonics):
    return lambda phase: sum(math.sin(phase * h) * (1/h) for h in harmonics) + baseline

# Irrelevant signal synthesis (dead path)
def synthesize_noise(frequency, duration):
    return [math.cos(frequency * t) for t in range(int(duration * 100))]

# Unused auxiliary function (distractor)
def normalize_signal(signal):
    max_val = max(signal)
    min_val = min(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

# Decoy data structure (misleading)
noise_profile = {
    'type': 'white',
    'amplitude': 0.87,
    'bandwidth': 20000,
    'sampling_rate': 44100
}

# Real metric computation with hidden logic chain
baseline_shift = 0.37
harmonic_series = [1, 3, 5, 7]
activation_phase = 2.1

# Signal generation (relevant but obscured)
signal_fn = generate_waveform(baseline_shift, harmonic_series)
current_amplitude = signal_fn(activation_phase)

# Multiple distraction variables
buffer_window = [0.12, 0.34, 0.56, 0.78]
scaling_factor = 1.89
offset_correction = -0.05

# Fake diagnostic check (red herring)
def validate_sensor_integrity(raw_data):
    if len(raw_data) > 10:
        return sum(x**2 for x in raw_data) < 100
    return False

# Unused validation call (decoy execution)
_ = validate_sensor_integrity(buffer_window)

# Core transformation logic buried in noise
raw_signature = abs(current_amplitude) * 1000

# String-based mode switch (uses string method)
machine_state = 'CALIBRATION_MODE_ACTIVE'
if 'CALIBRATION' in machine_state and machine_state.endswith('ACTIVE'):
    raw_signature *= 1.15

classification_key = 'diagnose|filter|analyze'
# Slicing operation used meaningfully
mode_slice = classification_key.split('|')[1:3]

# Conditional branching with case conversion
processing_mode = 'FILTER'.lower()
if processing_mode in mode_slice:
    raw_signature = math.sqrt(raw_signature)

# Bit manipulation decoy (irrelevant)
status_flag = 0b10101010
mask = 0b11110000
masked_status = status_flag & mask  # unused later

# Real threshold logic embedded late
threshold_map = {
    'level_a': 25.0,
    'level_b': 35.0,
    'level_c': lambda x: x * 0.7 + 5
}

# Tuple unpacking (distraction)
config_preset = ('gain', 'offset', 'rate')
p1, p2, p3 = config_preset

# Destructuring assignment red herring
diag_labels = ['A', 'B', 'C']
x_label, y_label, z_label = diag_labels

# Lambda function within processing (required feature)
apply_correction = lambda val, func: func(val) if func else val

# Health signature built from processed signal
health_signature = [
    round(raw_signature, 2),
    len(harmonic_series),
    int(baseline_shift * 100)
]

# Main processing function with nested logic
def process_metrics(signature, thresholds):
    base_score = signature[0]
    harmonic_count = signature[1]
    shift_value = signature[2]
    
    # Nested conditional branches
    if harmonic_count >= 4:
        if shift_value > 30:
            base_score *= 1.2
        else:
            base_score *= 0.85
    
    # Additional modification based on dynamic threshold
    dynamic_cap = thresholds['level_c'](base_score)
    if base_score > dynamic_cap:
        base_score = dynamic_cap
    
    # Final adjustment using slicing-like logic (index arithmetic)
    adjustment = (shift_value % 10) * 0.3
    intermediate_result = base_score - adjustment
    
    # Use of string method in logic flow (obscure path)
    flag_string = 'pass|warn|fail'
    flags = flag_string.upper().split('|')
    if intermediate_result > 30 and 'WARN' in flags:
        intermediate_result -= 2.5
    
    # Critical result computed here
    final_score = round(intermediate_result, 4)
    
    # Dead code branch (misleading)
    if final_score < 0:
        return -1 * int(final_score)
        
    return final_score

# Execution point of interest
final_diagnostic = process_metrics(health_signature, threshold_map)

# Print required output
print(f"Target result: {final_diagnostic}")