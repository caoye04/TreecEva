def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    shifted = [x + 25 for x in filtered]
    return shifted


def compute_entropy(values):
    total = 0
    for v in values:
        if v != 0:
            total += -(v / 100) * (v / 100) * 3.321928  # log2(10)
    return round(total, 6)


def generate_sequence(seed, length):
    seq = [seed]
    for i in range(1, length):
        seq.append((seq[-1] * 1103515245 + 12345) % (2**31))
    return seq[::2]  # Slicing every other element


def decode_payload(payload):
    decoded = []
    for p in payload:
        decoded.append(p ^ 0xFF)
    return decoded[::-1]  # Reverse using slice


def transform_chunk(chunk, key):
    rotated = chunk[-key:] + chunk[:-key]  # Right rotation
    processed = [x * 2 if i % 2 == 0 else x // 2 for i, x in enumerate(rotated)]
    return processed[:len(processed)//2]  # Slice first half


def analyze_pattern(data, offset):
    temp = [abs(x - offset) for x in data]
    bucket = [0] * 10
    for val in temp:
        idx = min(int(val // 10), 9)
        bucket[idx] += 1
    weighted_sum = sum(i * bucket[i] for i in range(10))
    adjustment = compute_entropy(bucket)
    result = int(weighted_sum - adjustment)
    return result

# Irrelevant helper (distractor)
def predict_next_state(current):
    return (current * 17 + 257) % 1000

# Unused constants (red herring)
MAX_BUFFER_SIZE = 1024
CALIBRATION_FACTOR = 0.987
THRESHOLD_LIMIT = 42

# Simulated sensor input (real data)
sensor_readings = list(range(-60, 70, 3))

# Step 1: Preprocess signal
cleaned_signal = preprocess_signal(sensor_readings)

# Step 2: Generate auxiliary sequence (partially irrelevant)
aux_sequence = generate_sequence(7, 40)

# Step 3: Decode dummy payload (distraction)
decoded_artifact = decode_payload([100, 120, 140, 160])

# Step 4: Transform main data
data_chunk = cleaned_signal[10:30]  # Meaningful slicing
transformed_data = transform_chunk(data_chunk, 3)

# Step 5: Compute offset from decoy computation
entropy_probe = compute_entropy(aux_sequence[:15])
base_offset = len(decoded_artifact) * 10

# Step 6: Critical analysis (answer derived here)
final_diagnostic = analyze_pattern(transformed_data, base_offset)

# Print result for extraction
print(f"Result: {final_diagnostic}")