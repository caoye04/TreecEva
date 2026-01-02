import math

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing with red herring operations
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    stats = {'mean': sum(filtered) / len(filtered), 'variance': 0}
    decoy_sum = 0
    for val in filtered:
        decoy_sum += val ** 2
    stats['variance'] = decoy_sum - stats['mean']**2
    return [int(x * 100) for x in filtered]  # Discretize

def generate_mask(length, key=7):
    # Misleading mask generation (not actually used in critical path)
    mask = []
    for i in range(length):
        mask.append((key * i + 3) % 256)
    return mask

def corrupt_data(data, level=0.1):
    # Dead function: never called but looks important
    indices = [i for i in range(len(data)) if i % int(1/level) == 0]
    for i in indices:
        data[i] = data[i] ^ 255
    return data

def shift_cipher(text, shift=3):
    # Distractor: string manipulation unrelated to main logic
    shifted = ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower() else c for c in text)
    reversed_shifted = shifted[::-1]
    return reversed_shifted.upper()

def analyze_pattern(sequence, limit):
    # Core logic buried in noise
    cumulative = 0
    trend_flags = []
    for i, val in enumerate(sequence):
        if i == 0:
            continue
        delta = sequence[i] - sequence[i-1]
        parity_flag = (val & 1) == 1
        magnitude_check = abs(delta) > (limit >> 1)
        # Conditional expression and bitwise mix
        trend_flags.append(1 if parity_flag and magnitude_check else -1)
    
    # Real computation path
    weighted_sum = 0
    for j in range(len(trend_flags)):
        weight = (j + 1) * trend_flags[j]
        weighted_sum += weight * (sequence[j+1] % 7)
    
    # Decoy aggregation (never used)
    anomaly_score = 0
    for x in sequence:
        if x % 5 == 0:
            anomaly_score += math.log(x + 1) * 2.5
    
    # Final result built from correct chain
    adjustment = len([x for x in sequence if x > 50])
    base_result = weighted_sum + adjustment
    
    # Key transformation
    final_value = (base_result ^ 98765) & 0xFFFF  # Bitwise finalize
    return final_value

# Main execution flow
raw_input_data = [120, 85, 150, 43, 200, 75, 180, 90]
config_mode = 'diagnostic'
mode_flag = 1 if config_mode == 'diagnostic' else 0

# Step 1: Preprocess signal
processed_signal = preprocess_signal(raw_input_data)

# Step 2: Generate unused cryptographic mask (red herring)
mask_key = sum(processed_signal) % 100
security_mask = generate_mask(len(processed_signal), mask_key)

# Step 3: Simulate data transformation (relevant)
transformed_data = []
for idx, sample in enumerate(processed_signal):
    rotated = ((sample << 2) & 0xFF) | (sample >> 6)  # Circular left shift
    if idx % 3 == 0:
        rotated = rotated ^ 0x55  # XOR pattern every 3rd
    transformed_data.append(rotated)

# Step 4: Determine adaptive threshold
threshold = 0
for val in transformed_data:
    threshold += (val >> 3) & 7
threshold = max(5, threshold // len(transformed_data))

# Step 5: Analyze final pattern (critical statement)
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Step 6: Print result
print(f"Result: {final_diagnostic}")