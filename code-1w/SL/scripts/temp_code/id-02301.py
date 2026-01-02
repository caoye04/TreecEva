import itertools

def analyze_signal_strength(raw_samples):
    # Normalize signal values using min-max scaling
    min_val, max_val = min(raw_samples), max(raw_samples)
    normalized = [(x - min_val) / (max_val - min_val + 1e-9) for x in raw_samples]

    # Apply noise filter: remove values below sensitivity threshold
    sensitivity = 0.1
    filtered = [val for val in normalized if val > sensitivity]

    # Misleading computation: calculate variance but never use it
    mean_val = sum(filtered) / len(filtered)
    variance = sum((x - mean_val) ** 2 for x in filtered) / len(filtered)
    redundant_check = variance > 0.05

    # Simulate packet segmentation based on chunk size
    chunk_size = 3
    segments = list(itertools.batched(filtered, chunk_size))

    # Pad last segment if incomplete
    if segments and len(segments[-1]) < chunk_size:
        segments[-1] += (0.0,) * (chunk_size - len(segments[-1]))

    # Flatten back with string-based marker insertion (dummy operation)
    flattened = []
    for i, seg in enumerate(segments):
        flattened.extend(seg)
        if i % 2 == 0:
            flattened.append(0.0)  # dummy separator that will be removed

    cleaned = [x for x in flattened if x != 0.0]  # remove dummy separators

    return cleaned


def process_signals(data, limit):
    # Compute rolling XOR of three consecutive elements
    shifted_a = data[1:] + [0]
    shifted_b = data[2:] + [0, 0]
    xor_sequence = [a ^ b ^ c for a, b, c in zip(data, shifted_a, shifted_b)]

    # Trim to length and apply magnitude boost
    trimmed = xor_sequence[:len(data)]
    boosted = [x * 1.5 for x in trimmed]

    # Bucketing logic based on thresholds
    categories = []
    for val in boosted:
        if val < 0.5:
            categories.append(1)
        elif val < 1.0:
            categories.append(2)
        else:
            categories.append(3)

    # Red herring: count category transitions (not used)
    transitions = 0
    for i in range(1, len(categories)):
        if categories[i] != categories[i-1]:
            transitions += 1

    # Actual result: weighted sum using tuple unpacking
    weights = [1, 2, 1.5, 2.5, 1]
    extended_weights = (weights * (len(boosted) // len(weights) + 1))[:len(boosted)]
    final_value = sum(w * v for w, v in zip(extended_weights, boosted))

    # Additional unused tracking variables
    avg_weight = sum(extended_weights) / len(extended_weights)
    peak_value = max(boosted)

    return int(final_value)

# Main execution
raw_input = [120, 85, 140, 70, 135, 90, 150, 65, 130]
threshold = 0.15

# Irrelevant preprocessing: reverse and shift (not affecting logic path)
reversed_copy = raw_input[::-1]
shifted_values = [x >> 2 for x in reversed_copy]  # bitwise shift distraction

filtered_data = analyze_signal_strength(raw_input)
final_output = process_signals(filtered_data, threshold)

# Dummy string analysis to incorporate string methods
log_entry = "Signal analysis complete. Output={}".format(final_output)
diagnostic_tags = log_entry.upper().replace(".", "").split()
valid_tags = [tag for tag in diagnostic_tags if "OUTPUT" not in tag]

# Unused lambda function (distractor)
square_if_positive = lambda x: x**2 if x > 0 else 0
side_calc = list(map(square_if_positive, [final_output - 100, final_output + 50]))

print(f"Result: {final_output}")