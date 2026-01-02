def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(length):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[i-1] + seq[i-2])
    return seq  # Unused function - red herring


def encode_state(config):
    state = 0
    for i, bit in enumerate(config):
        state |= (bit << i)
    return state


def analyze_pattern(data, limit):
    count = 0
    running_sum = 0.0
    toggle = True
    
    for val in data:
        if val < 0:
            count += 1
            running_sum -= val
        elif val > 0.5:
            running_sum += val ** 2
        else:
            running_sum += val
            
        if count >= limit and toggle:
            running_sum = abs(running_sum) * 1.5
            toggle = False

    checksum = 0
    for i, v in enumerate(data):
        checksum ^= int(v * 100) & i  # Bitwise distraction

    temp_result = running_sum * 1000
    final_score = int(temp_result) + checksum
    
    # Irrelevant transformation chain
    buffer = set(str(final_score))
    if '7' in buffer:
        final_score -= 100
    if len(buffer) % 2 == 0:
        final_score += 50

    return final_score

# Main execution flow
raw_input_data = [-2.1, -1.3, 0.05, 0.65, 0.8, 0.2, -0.45, 1.2]
baseline_offset = sum([i*i for i in range(5)])  # Dead computation

transformed_data = preprocess_signal(raw_input_data)

# Simulate configuration state (unused in logic)
config_flags = [True, False, True, True]
encoded_mode = encode_state([1 if b else 0 for b in config_flags])

threshold = len([x for x in transformed_data if x > 0.3])

intermediate_stats = {
    'avg': sum(transformed_data) / len(transformed_data),
    'peak': max(transformed_data),
    'noise_floor': min(abs(x) for x in transformed_data)
}

# Decoy loop with no impact on result
snapshot = []
for _ in range(3):
    snapshot.append({
        'time': 1000,
        'value': encoded_mode ^ 15
    })

final_diagnostic = analyze_pattern(transformed_data, threshold)

# Extraneous post-processing
if final_diagnostic > 1000:
    final_diagnostic = (final_diagnostic >> 2) + 10

Result: {final_diagnostic}