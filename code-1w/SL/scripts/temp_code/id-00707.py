def preprocess_signal(raw_input):
    amplitude = sum(abs(x) for x in raw_input) / len(raw_input)
    normalized = [x / amplitude for x in raw_input]
    filtered = [x for x in normalized if abs(x) > 0.1]
    return filtered


def encode_sequence(seq):
    encoded = []
    for val in seq:
        if val > 0:
            encoded.append(int((val ** 2) * 100))
        else:
            encoded.append(-int((abs(val) ** 0.5) * 50))
    return encoded


def shift_cipher(text, key):
    # Irrelevant string manipulation function (distractor)
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char.lower()) - ord('a')
            shifted = (shifted + key) % 26
            result += chr(shifted + ord('a'))
        else:
            result += char
    return result


def simulate_feedback_loop(samples):
    # Dead-end simulation with no impact on final result
    state = 1.0
    history = []
    for _ in range(50):
        state = (state * 3.9) * (1 - state)
        history.append(state)
    return history[-1]


def transform_features(data):
    # Complex but partially irrelevant transformation chain
    temp_a = [x * 1.5 for x in data]
    temp_b = [int(x) ^ 7 for x in temp_a if x > 0]  # Bitwise red herring
    temp_c = ''.join(str(bin(x))[2:] for x in temp_b[:3])
    checksum = sum(int(b) for b in temp_c) * 0.1
    adjusted = [x + checksum for x in data]
    return adjusted


def analyze_pattern(seq):
    threshold = 3.5
    count_above = 0
    running_total = 0.0
    
    for i, val in enumerate(seq):
        if i % 2 == 0 and val > threshold:
            count_above += 1
            running_total += val
        elif val < 1.0:
            running_total -= 0.5
            break  # Early termination condition (misleading path)
    
    if count_above == 0:
        return 42  # Decoy return
    
    avg_high = running_total / count_above if count_above else 0
    
    # Core logic disguised among distractions
    modifier = len(seq) % 4
    final_score = avg_high * (modifier + 1)
    
    # Actual answer computation
    return int(final_score) + 5

# Main execution flow
raw_sensor_data = [2.1, -1.3, 4.8, 6.2, -0.5, 3.9, 5.1]

# Irrelevant preprocessing chain
filtered_data = preprocess_signal(raw_sensor_data)
decoded_str = "signal_7x"
encrypted_tag = shift_cipher(decoded_str, 7)

# Distractor: unused complex structure
feedback_state = simulate_feedback_loop(filtered_data)

# Multi-stage transformation with red herrings
encoded_data = encode_sequence(filtered_data)
interim_result = [x for x in encoded_data if x > 0]
transformed_data = transform_features(interim_result)

# Key statement containing the target variable
final_diagnostic = analyze_pattern(transformed_data)

# Output the result as required
print(f"Target result: {final_diagnostic}")