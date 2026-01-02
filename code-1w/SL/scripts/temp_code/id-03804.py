def preprocess_signal(raw_input, filter_bias):
    filtered = [x - filter_bias for x in raw_input if x > 0]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    normalized = [round(x / baseline, 3) for x in filtered] if baseline else []
    return normalized


def generate_sequence(seed_value, length):
    seq = []
    val = seed_value
    for i in range(length):
        val = (val * 17 + 257) % 65537
        seq.append(val)
    return seq  # Dead function - not used in main logic


def decode_payload(encoded):
    decoded = []
    for x in encoded:
        decoded.append((x ^ 255) + 10)  # Bitwise XOR manipulation
    return decoded

# Simulated sensor array data (irrelevant to final result)
sensor_array = [[18, 24, 36], [45, 50, 55], [60, 70, 80]]
aggregated_diagnostics = []
for row in sensor_array:
    avg_temp = sum(row) / len(row)
    status_flag = 'OK' if avg_temp < 60 else 'HIGH'
    aggregated_diagnostics.append({'average': avg_temp, 'status': status_flag})

# Core signal processing chain
raw_data_stream = [128, 256, 192, 320, 288, 352, 416, 384]
offset_correction = 128
processed_signal = preprocess_signal(raw_data_stream, offset_correction)

# Irrelevant transformation branch
temp_analysis = [x * 1.8 + 32 for x in raw_data_stream]  # Misleading: Fahrenheit conversion
extended_metrics = {'count': len(temp_analysis), 'peak': max(temp_analysis)}

# Key data transformation
transformed_data = []
for i, val in enumerate(processed_signal):
    if i % 2 == 0:
        transformed_data.append(int(val * 100))
    else:
        transformed_data.append(int(val * 50))

# Decoy control flow with unused conditionals
mode_selector = 'diagnostic'
if mode_selector == 'calibration':
    transformed_data = [x + 10 for x in transformed_data]
elif mode_selector == 'test':
    transformed_data = [x - 5 for x in transformed_data]
else:
    pass  # Intentional no-op: distractor path

# Threshold logic with slicing and set operations
activation_peaks = transformed_data[::2]  # Every second element
background_noise = set(transformed_data[1::2])
key_threshold = sum(activation_peaks) // len(activation_peaks)

# Conditional expression with case conversion (distractor)
diagnostic_mode = 'ACTIVE'.lower() if len(activation_peaks) > 3 else 'STANDBY'.upper()

# Real computation obscured by noise
adjusted_set = set(activation_peaks) - background_noise
refined_list = sorted(list(adjusted_set))

# Final analysis using bitwise and arithmetic logic
def analyze_pattern(data, threshold):
    cumulative_score = 0
    for item in data:
        if item > threshold:
            cumulative_score += (item & 255)  # Bitwise AND to mask byte
        elif item == threshold:
            cumulative_score += 50
        else:
            cumulative_score -= (item % 15)  # Small deduction based on modulo
    return cumulative_score + len(data)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Additional red herring: string processing unrelated to numeric result
log_entry = "Error_Code_XZ".replace('_', '').lower()
error_flags = {c for c in log_entry if c in 'aeiou'}  # Set comprehension distraction

# Output the required result
print(f"Result: {final_diagnostic}")