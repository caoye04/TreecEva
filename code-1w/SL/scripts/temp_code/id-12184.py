import math

# Simulated sensor array diagnostics with embedded logic chain
def collect_entropy(stream, threshold):
    entropy_values = []
    temp_buffer = []
    cumulative = 0
    count = 0

    for val in stream:
        if val < 0:  # Irrelevant filter (never triggers)
            continue
        if val > threshold:
            temp_buffer.append(val)
            cumulative += val
            count += 1
        else:
            if count > 0:
                mean_val = cumulative / count
                entropy_values.append(round(math.log(mean_val + 1e-5) * -1, 3))
            cumulative = 0
            count = 0

    if count > 0:  # Handle remaining buffer
        mean_val = cumulative / count
        entropy_values.append(round(math.log(mean_val + 1e-5) * -1, 3))

    # Dead code path — never reached due to logic above
    if len(temp_buffer) == 0:
        entropy_values.append(999.999)

    return entropy_values


def shift_cipher(text, offset):
    # Distractor function: character manipulation not directly related
    shifted = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted += chr((ord(char) - base + offset) % 26 + base)
        else:
            shifted += char
    return shifted

# Unused but misleading intermediate calculation
def evaluate_stability(risk_factor, history):
    if risk_factor < 0.5:
        return sum(history) / len(history) > 0.7
    else:
        return False

# Core analysis with set operations and bit manipulation
def analyze_pattern(sequence, flags):
    adjusted = []
    mask = 0b1010  # Bitmask for filtering

    for idx, val in enumerate(sequence):
        if idx % 2 == 0:
            # Apply XOR only on even indices
            transformed = int((val * 100) ^ mask)
            adjusted.append(abs(transformed) % 1000)
        else:
            adjusted.append(int(val * 50))

    # Set-based filtering using relevant and irrelevant criteria
    raw_set = set(adjusted)
    high_values = {x for x in raw_set if x > 300}
    mid_values = {x for x in raw_set if 100 <= x < 300}
    low_values = {x for x in raw_set if x < 100}

    # Decoy operation: symmetric difference that isn't used
    decoy_combination = high_values ^ low_values

    # Actual computation path
    selected = mid_values & {x for x in range(150, 250)}  # Intersection matters

    # Conditional branching based on flag state (simulates system mode)
    if 'ENHANCED' in flags:
        adjustment_factor = 3
    elif 'SAFE' in flags:
        adjustment_factor = 1
    else:
        adjustment_factor = 2  # Default execution path

    # Critical computation step
    base_score = sum(selected) * adjustment_factor

    # Bitwise interference (red herring)
    masked_score = base_score & 0xFFFF  # Masking upper bits
    if masked_score > 10000:
        masked_score = masked_score >> 2  # Right shift if large

    # Final logic gate: inject constant offset based on set size
    if len(high_values) > 2:
        final_offset = 42
    else:
        final_offset = 17  # This will be taken

    result = masked_score + final_offset

    # Unused transformation — distracts from actual output
    if result < 500:
        result = int(math.sqrt(result) * 10)

    return result

# Initialization sequence (simulated sensor data)
data_stream = [12.4, 15.6, 8.2, 18.1, 9.3, 14.7, 11.2]
system_mode = "NORMAL"

calibration_map = {
    'baseline': 10.0,
    'tolerance': 2.5,
    'active': True
}

# Trigger entropy collection
entropy_sequence = collect_entropy(data_stream, threshold=9.0)

# Misleading diagnostic call (no side effects)
stability_log = [0.8, 0.75, 0.82, 0.68]
risk_assessment = evaluate_stability(0.6, stability_log)

# Cipher distraction with irrelevant message
message = "Status: Nominal"
encoded_msg = shift_cipher(message, 13)

# System flags — note 'ENHANCED' is not present
system_flags = {'BOOTED', 'ACTIVE', 'SECURE'}  # Triggers default branch

# Key execution point
final_diagnostic = analyze_pattern(entropy_sequence, system_flags)

# Output result as required
print(f"Target result: {final_diagnostic}")