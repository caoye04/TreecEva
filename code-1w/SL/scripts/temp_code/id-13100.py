def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(data) % 17

# Misleading intermediate calculation
temp_offset = sum([i * 2 for i in range(15)]) / 4
offset_correction = temp_offset * 0.87

# Real data pipeline
raw_sensor_data = [34, -22, 67, 89, -45, 12, 8, -76, 44, 19]
processed_signal = preprocess_signal(raw_sensor_data)

# Decoy transformation chain
fake_magnitude = 0
for val in processed_signal:
    if val > 0.5:
        fake_magnitude += val ** 2

# Actual signal transformation
decay_factor = 0.9
weighted_sum = 0
for i, val in enumerate(processed_signal):
    weighted_sum += val * (decay_factor ** i)

transformed_data = [weighted_sum * 2.3, len(processed_signal), 42]

# Spurious dictionary with red herring values
status_map = {
    'active': 1,
    'debug_mode': False,
    'last_reset': '2023-08-01',
    'baseline': 7.5,
    'version': 'v2.1'
}

# Dummy logic that seems important but isn't
current_state = 'active'
if status_map[current_state] == 1:
    adjustment = 0.15
    # This branch does not affect final result

# Core analysis logic
key_threshold = 3.14159

def analyze_pattern(data, threshold):
    size_metric = data[1] * data[0]
    magic_constant = generate_sequence(10)[-1]  # Fibonacci-based weight
    score = size_metric + (data[0] / threshold) * magic_constant
    
    # String-based switch (uses string method)
    mode_flag = 'NORMAL_OP'
    if mode_flag.lower().startswith('normal'):
        score *= 1.1
    
    # Additional irrelevant check
    if len(str(int(score))) > 3:
        score -= 100  # Misleading adjustment
    
    # Final computation
    diagnostic_value = int(round(score / 10)) * 10 + data[2]
    return diagnostic_value

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, key_threshold)
print(f"Result: {final_diagnostic}")