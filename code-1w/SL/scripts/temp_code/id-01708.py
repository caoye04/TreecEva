import itertools

def analyze_sequence(pattern):
    # Irrelevant function - dead code path
    return sum(a * b for a, b in zip(pattern, pattern[1:]))

def preprocess_inputs(raw_values):
    # Distractor: complex-looking but unused preprocessing
    normalized = [x / max(raw_values) for x in raw_values]
    filtered = [x for x in normalized if x > 0.2]
    return [int(x * 100) for x in filtered]

def compute_metric(signal, noise_level=0.05):
    # Real computation starts here
    base = 0
    for i in range(len(signal)):
        if i % 3 == 0:
            base += signal[i] ** 2
        elif i % 4 == 0:
            base -= signal[i]
        else:
            base ^= i  # Bitwise distraction with partial relevance

    # Key transformation
    temp_result = base & 0xFFFF  # Mask to 16 bits

    # Decoy metric calculation (never used)
    decoy = [temp_result >> i for i in range(4)]
    decoy_sum = sum(decoy) ^ 0xABCD

    return temp_result

def generate_baseline(count):
    # Produces baseline values using itertools – relevant
    seq = list(itertools.accumulate(range(count), lambda a, b: (a + b) % 7))
    return [x * 3 + 1 for x in seq]

def evaluate_performance(metrics, reference):
    # Core logic with distractors
    adjustment = 0
    for val in metrics:
        if val > 100:
            adjustment += 1
        elif val < 0:
            adjustment -= 1
        else:
            adjustment += val % 7

    # Irrelevant set operation (looks important)
    unique_refs = set(reference)
    overlaps = len(unique_refs.intersection({3, 10, 21, 63}))
    adjustment *= (overlaps + 1)

    # Actual key step: XOR with fixed pattern derived from reference
    key_shift = sum(reference[i] for i in range(0, len(reference), 3)) % 19
    final_component = 0
    for m in metrics:
        final_component += (m ^ key_shift) % 100

    # Final score built from multiple layers
    intermediate = (adjustment * 17) + final_component
    final_score = intermediate - (key_shift ** 2)

    # Unused but misleading variable
    diagnostic_trace = [
        f'Step{i}: {intermediate - i * 10}' for i in range(3)
    ]

    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data setup
    sensor_readings = [12, 7, 15, 3, 9, 18, 6, 11, 14, 8]
    processed_data = preprocess_inputs(sensor_readings)  # Unused later

    # Generate real metric data
    metric_data = [compute_metric([x+1, x*2, x-3]) for x in sensor_readings]

    # Baseline generation (used in evaluation)
    baseline = generate_baseline(10)

    # Red herring: bitwise checksum on unrelated data
    shadow_value = 0
    for v in sensor_readings:
        shadow_value ^= (v << 2) | (v >> 1)
    shadow_value = shadow_value & 0xFF

    # Critical statement
    final_score = evaluate_performance(metric_data, baseline)

    # Output result
    print(f"Result: {final_score}")