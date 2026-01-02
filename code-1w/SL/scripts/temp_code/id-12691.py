def preprocess_segment(segment):
    smoothed = [segment[i] + (segment[i-1] + segment[i+1]) / 2 for i in range(1, len(segment)-1)]
    smoothed.insert(0, segment[0])
    smoothed.append(segment[-1])
    return [x * 0.9 for x in smoothed]

# Irrelevant helper - dead code path
def legacy_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data] if max_val else data

def encode_pattern(sequence):
    encoded = 0
    for val in sequence:
        encoded = (encoded << 1) ^ int(abs(val)) % 7
    return encoded

def filter_outliers(stream, limit=3.5):
    mean_val = sum(stream) / len(stream)
    deviances = [abs(x - mean_val) for x in stream]
    cutoff = limit * (sum(deviances) / len(deviances))
    return {i for i, d in enumerate(deviances) if d < cutoff}

# Misleading intermediate computation
aggregation_key = 0
for i in range(8):
    aggregation_key ^= (i * 17) % 19

raw_readings = [12.4, 15.1, 9.8, 10.2, 14.5, 13.3, 11.0, 9.9, 10.1, 12.7]

# Distractor: unused but plausible transformation
weighted_sum = sum(x * (i+1) for i, x in enumerate(raw_readings[:5]))

processed_signal = preprocess_segment(raw_readings)

# Early break red herring
status_flags = []
for val in processed_signal:
    if val > 20.0:
        status_flags.append(3)
        break
    elif val > 15.0:
        status_flags.append(2)
    elif val > 10.0:
        status_flags.append(1)
    else:
        status_flags.append(0)
else:
    status_flags.append(-1)  # Executes since loop doesn't break

# Set operations (required)
valid_indices = set(range(len(processed_signal)))
noise_floor = {i for i, x in enumerate(raw_readings) if x < 10.0}
anomaly_candidates = filter_outliers(raw_readings, limit=2.8)

threshold_set = valid_indices - noise_floor | anomaly_candidates

# Complex multi-step data transformation
compressed_data = []
carry = 0.0
for i, val in enumerate(processed_signal):
    if i % 2 == 0:
        transformed = abs(val) ** 0.5 + carry
        carry = val * 0.1
    else:
        transformed = val - carry
        carry = abs(transformed) * 0.05
    compressed_data.append(round(transformed, 3))

# Decoy function that's defined but not used
def decrypt_payload(data):
    return [x ^ 255 for x in data]

# Critical analysis function with multiple logic steps
def analyze_signal(data, thresholds):
    base_score = 0
    for i, x in enumerate(data):
        if i not in thresholds:
            continue
        if x > 12.0:
            base_score += int(x)
        elif x > 9.5:
            base_score += int(x * 1.5)
        else:
            base_score -= 1
    
    # Additional logic involving set membership and bit manipulation
    encoded_sig = encode_pattern(data)
    adjustment = 0
    for bit_pos in range(4):
        if (encoded_sig >> bit_pos) & 1:
            adjustment += (bit_pos + 1) * 3
    
    # Final fusion
    final_score = base_score + adjustment
    
    # Apply spurious offset (looks important but is part of distraction)
    metadata_offset = len(thresholds) ^ 7
    final_score += metadata_offset
    
    # Key output variable
    final_diagnostic = final_score * 2
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_signal(compressed_data, threshold_set)
print(f"Result: {final_diagnostic}")