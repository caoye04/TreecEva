def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def generate_sequence(length):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[i-1] + seq[i-2])
    return seq  # Unused in final result

def corrupt_data(data):
    return [x * 0.5 + 10 for x in data]  # Dead function - never called

raw_sensor_data = [0.5, -0.3, 0.8, 0.0, -1.2, 0.7, 0.15, -0.25, 0.6]
baseline_offset = sum([x**2 for x in raw_sensor_data]) / len(raw_sensor_data)
adjusted_data = [x - baseline_offset * 0.1 for x in raw_sensor_data]

# Irrelevant transformation chain
fft_approximation = []
for i in range(len(adjusted_data)):
    val = 0
    for j in range(len(adjusted_data)):
        val += adjusted_data[j] * (i * j % 3)
    fft_approximation.append(val)

# Real processing begins here — slicing and filtering
windowed_data = adjusted_data[1:-1]  # Remove first and last
smoothed = []
for i in range(1, len(windowed_data)-1):
    smoothed.append(sum(windowed_data[i-1:i+2]) / 3)
if len(smoothed) % 2 == 0:
    smoothed = smoothed[:-1]  # Make odd-length

# Bit manipulation layer
bit_encoded = 0
for x in smoothed:
    shifted = int(abs(x) * 100) & 0xFF
    bit_encoded ^= shifted << 1
    bit_encoded = bit_encoded & 0xFFFF  # Keep within 16 bits

# Data transformation
transformed_data = [int(abs(x) * 1000) % 100 for x in smoothed]
if len(transformed_data) > 4:
    transformed_data = transformed_data[:len(transformed_data)//2 + 1]

# Dummy control flow with red herring variables
mode_flag = True
tracking_log = []
buffer_state = None
for idx, val in enumerate(transformed_data):
    if val > 50:
        tracking_log.append((idx, val))
    elif val < 10:
        buffer_state = 'ALERT'
    else:
        mode_flag = not mode_flag

# Key threshold derived from bit_encoded lower byte
key_threshold = (bit_encoded & 0xFF) % 15

# Decoy statistical computation
mean_decoy = sum(transformed_data) / len(transformed_data)
variance_red_herring = sum((x - mean_decoy)**2 for x in transformed_data)

# Actual analysis function used in final step
def analyze_pattern(data, threshold):
    count = 0
    for i in range(1, len(data)):
        if (data[i] ^ data[i-1]) > threshold:  # XOR comparison
            count += 1
    return count * threshold

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

print(f"Result: {final_diagnostic}")