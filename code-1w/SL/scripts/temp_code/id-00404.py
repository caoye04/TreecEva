def analyze_sequence(data_stream):
    checksum = 0
    for val in data_stream:
        checksum ^= val
        checksum = (checksum + val * 2) % 101
    return checksum

# Irrelevant helper: simulates signal but unused in final logic
def generate_pulse(frequency, duration=0.5):
    import math
    samples = []
    for t in range(10):
        samples.append(int(math.sin(frequency * t) * 10))
    return samples  # Dead code path

# Key transformation function
def transform_state(state_vector, mode='strict'):
    shifted = [((x << 1) & 255) for x in state_vector]
    if mode == 'strict':
        shifted = [x ^ 170 for x in shifted]  # Invert high bits
    return shifted

# Core logic with distractions
status_codes = [10, 15, 20, 30, 40]
buffer_log = {'entries': [], 'size': 0}
diagnostic_trace = [{'step': i, 'flag': False} for i in range(6)]

# Distractor: complex-looking but unused structure
analysis_pipeline = {
    'preprocess': lambda x: sum(v ** 0.5 for v in x if v > 5),
    'validate': lambda x: all(v % 2 == 0 for v in x),
    'encode': lambda x: ''.join(chr(v % 97 + 33) for v in x)
}

# Real computation begins
raw_input = [85, 45, 72, 66, 91]
processed_frame = transform_state(raw_input)

# Multiple red herrings
entropy_probe = 0
for idx, byte in enumerate(processed_frame):
    entropy_probe += (byte * idx) % 19
    if byte > 100:
        entropy_probe -= 5  # Misleading adjustment

# Simulated sensor array (unused)
sensor_array = [[i + j for j in range(4)] for i in range(5)]
active_sensors = [any(x > 2 for x in row) for row in sensor_array]

# Actual critical logic hidden among noise
logic_flow = [processed_frame[i] & status_codes[i % len(status_codes)] for i in range(len(processed_frame))]
activation_threshold = analyze_sequence(raw_input) % 50

# Secondary distraction: character frequency analysis
log_text = "sys_init_" + "debug_x9" * 3
char_freq = {}
for c in log_text:
    char_freq[c] = char_freq.get(c, 0) + 1
top_char_score = sum(v for k, v in char_freq.items() if k in 'abcdef')

# Critical assignment buried in context
baseline_correction = 0
for v in logic_flow:
    if v > activation_threshold:
        baseline_correction += v // 3
    else:
        baseline_correction += v % 7

# Final computation
final_diagnostic = process_metrics(logic_flow, activation_threshold)

# Implementation of required function
def process_metrics(metrics, threshold):
    aggregate = 0
    for m in metrics:
        if m > threshold:
            aggregate += m * 2
        else:
            aggregate += m + 5
    # Apply bit-based weighting
    flag_weight = bin(threshold).count('1')
    return (aggregate + flag_weight) % 10000

# Print result as required
Result: {final_diagnostic}