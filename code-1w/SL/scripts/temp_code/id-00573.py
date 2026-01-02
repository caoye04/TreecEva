def preprocess_input(raw_data):
    # Irrelevant transformation chain (distractor)
    temp_a = sum(x ** 2 for x in raw_data if x > 0) % 97
    temp_b = ''.join([chr((x + temp_a) % 26 + 97) for x in raw_data[:5]])
    checksum = (temp_a * len(raw_data)) ^ 153

    # Actual relevant preprocessing
    filtered = [x for x in raw_data if x % 2 == 1]  # Keep only odd values
    normalized = [x / 3 for x in filtered]
    return normalized


def transform_signal(x):
    # Bit manipulation red herring
    bits = bin(x)[2:].zfill(8)
    flipped = ''.join('1' if b == '0' else '0' for b in bits)
    decoy_value = int(flipped, 2)

    # Real logic: apply non-linear scaling
    if x < 0:
        return abs(x) ** 0.5
    return x ** 0.5 if x != 0 else 0.0


def analyze_noise_pattern(signal_list):
    # Dead-end analysis with string methods (distraction)
    pattern_str = ''.join(str(int(s * 10) % 10) for s in signal_list[:3])
    if pattern_str.startswith('7'):
        return pattern_str.count('3')
    else:
        return pattern_str.find('5')

    # Unreachable code (red herring)
    return len(pattern_str) * -1


def generate_baseline(count):
    # Unused function — dead code path
    return [i * 0.77 for i in range(count, 0, -1)]


def validate_coherence(data):
    # Distractor: complex validation that isn't used in final result
    if len(data) == 0:
        return False
    coherence_score = 0
    for i in range(1, len(data)):
        coherence_score += abs(data[i] - data[i-1])
    return coherence_score < 50

# Main execution flow
raw_sensor_data = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

# Step 1: Preprocess to extract meaningful subset
processed_signals = preprocess_input(raw_sensor_data)

# Step 2: Apply non-linear transformation to each signal
transformed = []
for val in processed_signals:
    transformed.append(transform_signal(val))

# Step 3: Compute moving average window (partially irrelevant)
window_size = 2
averages = []
for i in range(len(transformed) - window_size + 1):
    avg = sum(transformed[i:i+window_size]) / window_size
    averages.append(avg)

# Step 4: Noise analysis — called but result unused (misleading call)
dummy_diagnostic = analyze_noise_pattern(averages)

# Step 5: Core diagnostic logic (uses original transformed data)
valid_count = 0
for t_val in transformed:
    if t_val > 2.0:
        valid_count += 1

# Step 6: Final computation using modular arithmetic and bit check
core_metric = sum(int(t * 10) for t in transformed) % 89
flag_state = valid_count & 1  # XOR-like flag

# Step 7: Combine into final diagnostic
final_diagnostic = core_metric + (flag_state * 100)

# Output target result
print(f"Result: {final_diagnostic}")