import itertools

def analyze_pattern(seq):
    """Irrelevant analysis function - distractor"""
    return sum(a * b for a, b in zip(seq, seq[1:]))

def filter_outliers(data, threshold=50):
    """Misleading preprocessing that isn't actually used"""
    return [x for x in data if abs(x) < threshold]

def transform_signal(signal_stream):
    processed = []
    temp_accum = 0
    for val in signal_stream:
        temp_accum += val ** 2
        if temp_accum > 100:
            temp_accum = 0
            processed.append(val % 7)
    return processed

def extract_features(dataset):
    # Real path starts here
    features = []
    for item in dataset:
        if item % 3 == 0 and item > 0:
            features.append(item)
    return features[:5]  # Limit to first five valid items

def simulate_propagation(values):
    """Complex-looking but unused simulation"""
    result = 0
    for i, v in enumerate(values):
        result += v * (i + 1) ** 0.5
    return round(result, 3)

def accumulate_phases(input_sequence):
    phase_sum = 0
    multiplier = 1
    for idx, val in enumerate(input_sequence):
        if idx % 2 == 0:
            phase_sum += val * multiplier
            multiplier += 1
        else:
            phase_sum -= val // multiplier
    return phase_sum

def harvest_results(data_chunk):
    base_values = [x * 2 for x in data_chunk]
    shifted = [(x + 5) % 17 for x in base_values]
    mapped = list(itertools.accumulate(shifted, func=lambda a, b: a + b - 2))
    if len(mapped) >= 3:
        mapped[2] = mapped[2] * 2  # Double the third element
    total = sum(mapped)
    adjustment = 0
    for i in range(len(mapped)):
        if mapped[i] > 20:
            adjustment += 1
    return total + adjustment * 3

# Main execution flow
raw_input = [-8, -3, 0, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]

# Irrelevant transformations
analyzed = analyze_pattern(raw_input)
sanitized = filter_outliers(raw_input)
signal_output = transform_signal(raw_input)

# Critical processing chain
extracted_data = extract_features(raw_input)
# The following line is a decoy - appears important but unused later
simulated = simulate_propagation(extracted_data)

phased_total = accumulate_phases(extracted_data)

# Key statement
final_yield = harvest_results(extracted_data)

print(f"Result: {final_yield}")